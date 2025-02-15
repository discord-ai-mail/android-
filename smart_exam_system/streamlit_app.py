import streamlit as st
import sqlite3

custom_css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Figtree:wght@600&display=swap');

        html, body, [class*="st-"] {
            font-family: 'Figtree', sans-serif;
        }

        /* Change font for headers */
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Figtree', sans-serif !important;
            font-weight: 600 !important;
        }

        /* Adjust header sizes */
        h1 { font-size: 36px !important; }
        h2 { font-size: 30px !important; }
        h3 { font-size: 24px !important; }
    </style>
"""

# Inject the custom CSS into Streamlit
st.markdown(custom_css, unsafe_allow_html=True)


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

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS marks (
            student_id TEXT NOT NULL,
            class TEXT,
            course_name TEXT,
            marks INTEGER
        )
    ''')

    conn.commit()
    conn.close()

# Authenticate user
def authenticate_user(username, password, role):
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
        return True
    return False

# Login Page
def login():
    st.subheader("🔑 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["student", "staff"])

    if st.button("Login"):
        if authenticate_user(username, password, role):
            st.rerun()
        else:
            st.error("❌ Invalid credentials!")

# Logout
def logout():
    st.session_state.clear()
    st.rerun()

# Dashboard for staff
def staff_dashboard():
    st.sidebar.title("📌 Staff Dashboard")
    menu = st.sidebar.radio("Select an option", ["📌 Add/Edit Questions", "🚪 Logout"])

    if menu == "📌 Add/Edit Questions":
        add_questions()
    elif menu == "🚪 Logout":
        logout()

# Staff: Set & Edit Questions
def add_questions():
    st.subheader("✏️ Set or Edit Questions")

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

    st.write(f"📌 Editing: {course_name} - {class_name}")

    # Form to add new questions
    with st.form("add_question_form"):
        question = st.text_area("Enter New Question")
        option1 = st.text_input("Option 1")
        option2 = st.text_input("Option 2")
        option3 = st.text_input("Option 3")
        option4 = st.text_input("Option 4")
        correct_option = st.selectbox("Correct Answer", [option1, option2, option3, option4])

        submit = st.form_submit_button("Add Question")
        if submit:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO question_setter (course_name, class, question, option1, option2, option3, option4, correct_option) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (course_name, class_name, question, option1, option2, option3, option4, correct_option))
            conn.commit()
            conn.close()
            st.success("✅ Question Added Successfully!")
            st.rerun()

# Student Dashboard
def student_dashboard():
    st.sidebar.title("🎓 Student Dashboard")
    menu = st.sidebar.radio("Select an option", ["📝 Take Exam", "🚪 Logout"])
    if menu == "📝 Take Exam":
        take_exam()
    elif menu == "🚪 Logout":
        logout()

# Student: Take Exam
def take_exam():
    st.subheader("📝 Take Exam")

    student_id = st.session_state.get("student_id")
    if not student_id:
        st.error("❌ You need to log in first.")
        return

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Fetch available courses
    cursor.execute("SELECT DISTINCT course_name FROM question_setter")
    courses = cursor.fetchall()
    if not courses:
        st.warning("No exams available.")
        conn.close()
        return

    selected_course = st.selectbox("Select Course", [c[0] for c in courses])

    # Fetch questions for the selected course
    cursor.execute("SELECT id, question, option1, option2, option3, option4 FROM question_setter WHERE course_name = ?", (selected_course,))
    questions = cursor.fetchall()
    conn.close()

    if not questions:
        st.warning(f"No questions available for {selected_course}.")
        return

    # Display questions
    student_answers = {}
    for q in questions:
        if len(q) != 6:  # Ensuring data integrity
            st.error(f"Invalid question format: {q}")
            return

        q_id, q_text, a, b, c, d = q
        student_answers[q_id] = st.radio(q_text, [a, b, c, d], key=f"ans_{q_id}")

    # Submit button
    if st.button("Submit Exam"):
        correct_answers = sum(1 for q_id, answer in student_answers.items() if answer == "correct")
        total_marks = correct_answers * 5
        st.success(f"🎉 Exam Submitted! You scored: {total_marks}")


# Main function
def main():
    st.title("🎓 Smart Exam Management System")
    
    if "logged_in" not in st.session_state:
        login()
    elif st.session_state["role"] == "staff":
        staff_dashboard()
    else:
        student_dashboard()

if __name__ == "__main__":
    init_db()
    main()
