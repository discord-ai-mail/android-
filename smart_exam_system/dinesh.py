import streamlit as st
import sqlite3

# Initialize Database
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            class TEXT NOT NULL,
            staff TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS question_setter (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            class TEXT NOT NULL,
            question TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL,
            correct_option TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Logout function
def logout():
    st.session_state.clear()
    st.rerun()

# Staff Dashboard
def staff_dashboard():
    st.sidebar.title("📌 Staff Dashboard")
    menu = st.sidebar.radio("Select an option", ["📌 Add/Edit Questions", "🚪 Logout"])

    if menu == "📌 Add/Edit Questions":
        add_questions()
    elif menu == "🚪 Logout":
        logout()

# Staff: Add & Edit Questions
def add_questions():
    st.subheader("✏️ Add or Edit Questions")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT course_name, class FROM courses")
    courses = cursor.fetchall()
    conn.close()

    if not courses:
        st.warning("No courses available.")
        return

    course_class_mapping = {f"{course} ({class_name})": (course, class_name) for course, class_name in courses}
    selected_course = st.selectbox("Select Course & Class", list(course_class_mapping.keys()))
    course_name, class_name = course_class_mapping[selected_course]

    st.write(f"📌 Managing Questions for: {course_name} - {class_name}")

    # Load existing questions
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, question, option1, option2, option3, option4, correct_option FROM question_setter WHERE course_name = ? AND class = ?", (course_name, class_name))
    questions = cursor.fetchall()
    conn.close()

    # Display existing questions
    for q in questions:
        q_id, q_text, op1, op2, op3, op4, correct_option = q
        st.write(f"**{q_text}**")
        st.write(f"A) {op1} | B) {op2} | C) {op3} | D) {op4}")

        if st.button("📝 Edit", key=f"edit_{q_id}"):
            with st.form(key=f"edit_form_{q_id}"):
                new_question = st.text_area("Edit Question", q_text, key=f"edit_question_{q_id}")
                new_op1 = st.text_input("Option 1", op1, key=f"edit_op1_{q_id}")
                new_op2 = st.text_input("Option 2", op2, key=f"edit_op2_{q_id}")
                new_op3 = st.text_input("Option 3", op3, key=f"edit_op3_{q_id}")
                new_op4 = st.text_input("Option 4", op4, key=f"edit_op4_{q_id}")

                new_correct_option = st.selectbox("Correct Answer", [new_op1, new_op2, new_op3, new_op4], 
                                                  index=[new_op1, new_op2, new_op3, new_op4].index(correct_option), 
                                                  key=f"edit_correct_{q_id}")

                submit = st.form_submit_button("Save Changes")

                if submit:
                    conn = sqlite3.connect("database.db")
                    cursor = conn.cursor()
                    cursor.execute("UPDATE question_setter SET question=?, option1=?, option2=?, option3=?, option4=?, correct_option=? WHERE id=?",
                                   (new_question, new_op1, new_op2, new_op3, new_op4, new_correct_option, q_id))
                    conn.commit()
                    conn.close()
                    st.success("✅ Question updated successfully!")
                    st.rerun()

    # Form to add a new question
    with st.form("add_question_form"):
        st.subheader("➕ Add a New Question")
        new_question = st.text_area("Enter Question")
        new_option1 = st.text_input("Option 1")
        new_option2 = st.text_input("Option 2")
        new_option3 = st.text_input("Option 3")
        new_option4 = st.text_input("Option 4")
        new_correct_option = st.selectbox("Correct Answer", [new_option1, new_option2, new_option3, new_option4])

        submit_new = st.form_submit_button("Add Question")
        if submit_new:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO question_setter (course_name, class, question, option1, option2, option3, option4, correct_option) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (course_name, class_name, new_question, new_option1, new_option2, new_option3, new_option4, new_correct_option))
            conn.commit()
            conn.close()
            st.success("✅ Question Added Successfully!")
            st.rerun()

# Main Function
def main():
    st.title("🎓 Smart Exam Management System")

    if "username" not in st.session_state:
        st.subheader("🔑 Login Required")
        st.text_input("Username", key="username")
        st.text_input("Password", type="password", key="password")
        role = st.selectbox("Role", ["student", "staff"], key="role")

        if st.button("Login"):
            username = st.session_state.username
            password = st.session_state.password

            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM users WHERE username = ? AND password = ? AND role = ?", 
                           (username, password, role))
            user = cursor.fetchone()
            conn.close()

            if user:
                st.session_state["username"] = username
                st.session_state["role"] = role
                st.session_state["student_id"] = user[0]
                st.session_state["logged_in"] = True
                st.rerun()
            else:
                st.error("❌ Invalid credentials!")

    elif st.session_state["role"] == "staff":
        staff_dashboard()
    else:
        st.sidebar.title("🎓 Student Dashboard")
        menu = st.sidebar.radio("Select an option", ["📝 Take Exam", "🚪 Logout"])
        if menu == "📝 Take Exam":
            st.subheader("📝 Exam Functionality (Placeholder)")
        elif menu == "🚪 Logout":
            logout()

if __name__ == "__main__":
    init_db()
    main()
          
