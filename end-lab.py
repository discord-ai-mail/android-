import streamlit as st
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

        /* Glow effect for code blocks */
        pre, code {
            background-color: #1E1E1E !important; /* Dark background */
            color: #FFFFFF !important; /* White text */
            padding: 0px !important;
            border-radius: -20px !important;
            font-family: "Segoe UI Semibold", monospace !important;
            transition: box-shadow 0.3s ease-in-out;
        }

        /* Glow effect on hover */
        pre:hover, code:hover {
            box-shadow: 0 0 15px rgba(30, 144, 255, 0.8); /* DodgerBlue glow */
        }

        /* Hide Streamlit footer including 'Created by GitHub' */
        footer {visibility: hidden !important;}
    </style>
"""

# Inject the custom CSS into Streamlit
st.markdown(custom_css, unsafe_allow_html=True)


st.header("Develop an application that uses GUI components")
st.write("main.java")
st.code("""packagecom.example.gui; 
importandroid.os.Bundle; 
importandroid.app.Activity; 
importandroid.graphics.Typeface; 
importandroid.graphics.Color; 
importandroid.view.View; 
importandroid.widget.Button; 
importandroid.widget.TextView; 
 
publicclassMainActivityextends Activity { 
float font = 24; 
inti = 1; 
 protectedvoidonCreate(Bundle savedInstanceState) { 
  super.onCreate(savedInstanceState); 
  setContentView(R.layout.activity_main); 
  finalTextView t1 = (TextView)findViewById(R.id.textView1); 
  Button b1 = (Button)findViewById(R.id.button1); 
  b1.setOnClickListener(newView.OnClickListener() { 
   
    publicvoidonClick(View view) { 
    t1.setTextSize(font); 
    font = font+4; 
    if(font==40) 
     font = 20; 
  } 
  }); 
  Button b2 = (Button)findViewById(R.id.button2); 
  b2.setOnClickListener(newView.OnClickListener() { 
     
   publicvoidonClick(View view) { 
    switch(i) 
    { 
    case 1: 
    t1.setTextColor(Color.parseColor("#0000FF")); 
    break; 
    case 2: 
     t1.setTextColor(Color.parseColor("#00FF00")); 
     break; 
   case 3: 
     t1.setTextColor(Color.parseColor("#FF0000")); 
     break; 
   case 4: 
     t1.setTextColor(Color.parseColor("#800000")); 
     break; 
      
   } 
   i++; 
   if(i==5) 
 i = 1; 
          } 
  }); 
   } 
} 
 
""")
st.write("Xml")
st.code(""" 
<LinearLayoutxmlns:android="http://schemas.android.com/apk/res/android" 
xmlns:tools="http://schemas.android.com/tools" 
android:layout_width="fill_parent" 
android:layout_height="fill_parent" 
android:orientation="vertical" /> 
 
<TextView 
android:id="@+id/textView1" 
android:layout_width="match_parent" 
android:layout_height="wrap_content" 
android:text="WELCOME" 
android:layout_margin="20sp" 
android:gravity="center" 
android:textSize="20sp" 
android:textStyle="bold" /> 
 
<Button 
android:id="@+id/button1" 
android:layout_width="match_parent" 
android:layout_height="wrap_content" 
android:layout_margin="20sp" 
android:gravity="center" 
android:text="Change Font Size" /> 
 
<Button 
android:id="@+id/button2" 
android:layout_width="match_parent" 
android:layout_height="wrap_content" 
android:gravity="center" 
android:layout_margin="20sp" 
android:text="Change Color" /> 
 
</LinearLayout>""")

st.header("Application to design a Visiting Card")
st.write("xml")
st.code("""<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginStart="17dp"
        android:layout_marginTop="17dp"
        android:text="SJCIT"
        android:textSize="38sp" />

    <ImageView
        android:id="@+id/imageView"
        android:layout_width="231dp"
        android:layout_height="174dp"
        android:layout_alignParentEnd="true"
        android:layout_marginEnd="14dp"
        android:layout_marginTop="17dp"
        app:srcCompat="@drawable/logo" />

    <View
        android:id="@+id/view"
        android:layout_width="match_parent"
        android:layout_height="4dp"
        android:layout_below="@id/imageView"
        android:layout_marginTop="20dp"
        android:background="#4444" />

    <TextView
        android:id="@+id/textView2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_below="@id/view"
        android:layout_centerHorizontal="true"
        android:layout_marginTop="20dp"
        android:text="Amar Akbar Anthony"
        android:textSize="30sp"
        android:textStyle="bold" />

    <TextView
        android:id="@+id/textView3"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_below="@id/textView2"
        android:layout_centerHorizontal="true"
        android:layout_marginTop="10dp"
        android:text="Assistant Professor-ISE"
        android:textSize="25sp" />

    <TextView
        android:id="@+id/textView4"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_below="@id/textView3"
        android:layout_centerHorizontal="true"
        android:layout_marginTop="10dp"
        android:text="Ph No: 9988776655"
        android:textSize="20sp" />

    <TextView
        android:id="@+id/textView5"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_below="@id/textView4"
        android:layout_centerHorizontal="true"
        android:layout_marginTop="10dp"
        android:text="PB No. 20, BB Road, Chickballapur-562 101"
        android:textSize="20sp" />

    <TextView
        android:id="@+id/textView6"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_below="@id/textView5"
        android:layout_centerHorizontal="true"
        android:layout_marginTop="10dp"
        android:text="Email: amarakbaranthony@sjcit.ac.in"
        android:textSize="20sp" />
</RelativeLayout>""")
st.write("main.java")
st.code("""import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity { 
    @Override
    protected void onCreate(Bundle savedInstanceState) { 
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    } 
}
""")

st.header("Create a SIGN Up activity with Username and Password")
st.write("SignUpActivity.java")
st.code("""import.AppCompatActivity; 
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.util.regex.Pattern;

public class SignUpActivity extends AppCompatActivity {
    EditText emailEditText, passwordEditText;
    Button signUpBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signup);

        emailEditText = findViewById(R.id.emailEditText);
        passwordEditText = findViewById(R.id.passwordEditText);
        signUpBtn = findViewById(R.id.signUpBtn);

        signUpBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String email = emailEditText.getText().toString().trim();
                String password = passwordEditText.getText().toString().trim();

                if (!isValidPassword(password)) {
                    Toast.makeText(SignUpActivity.this, "Password doesn't match rules", Toast.LENGTH_SHORT).show();
                    return;
                }
                
                Intent intent = new Intent(SignUpActivity.this, LoginActivity.class);
                intent.putExtra("email", email);
                intent.putExtra("password", password);
                startActivity(intent);
            }
        });
    }

    private boolean isValidPassword(String password) {
        if (password.length() < 8) {
            return false;
        }

        Pattern lowerCase = Pattern.compile(".*[a-z].*");
        Pattern upperCase = Pattern.compile(".*[A-Z].*");
        Pattern number = Pattern.compile(".*[0-9].*");
        Pattern specialCharacter = Pattern.compile(".*[^a-zA-Z0-9].*");

        return lowerCase.matcher(password).find() &&
               upperCase.matcher(password).find() &&
               number.matcher(password).find() &&
               specialCharacter.matcher(password).find();
    }
}""")
st.write("LoginActivity.java")
st.code("""import android.os.Bundle;
import android.content.Intent;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class LoginActivity extends AppCompatActivity {
    EditText emailEditText, passwordEditText;
    Button loginBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        emailEditText = findViewById(R.id.emailEditText);
        passwordEditText = findViewById(R.id.passwordEditText);
        loginBtn = findViewById(R.id.loginBtn);

        String registeredEmail = getIntent().getStringExtra("email");
        String registeredPassword = getIntent().getStringExtra("password");

        loginBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String email = emailEditText.getText().toString().trim();
                String password = passwordEditText.getText().toString().trim();

                if (registeredEmail != null && registeredPassword != null &&
                        registeredEmail.equals(email) && registeredPassword.equals(password)) {
                    Intent intent = new Intent(LoginActivity.this, LoginSuccessActivity.class);
                    startActivity(intent);
                } else {
                    Toast.makeText(LoginActivity.this, "Invalid Credentials", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}""")
st.write("LoginSuccessActivity.java ")
st.code("""import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;

public class LoginSuccessActivity extends AppCompatActivity { 
    @Override 
    protected void onCreate(Bundle savedInstanceState) { 
        super.onCreate(savedInstanceState); 
        setContentView(R.layout.activity_login_success); 
    } 
}
""")
st.header("create page using Intent and one Button and pass the Values")
st.write("Main Activity Java File")
st.code("""package com.example.transferofdata;
import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.Menu;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
public class MainActivity extends Activity 
{
@Override
protected void onCreate(Bundle savedInstanceState) 
{
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);
final EditText et=(EditText)findViewById(R.id.editText1);
final EditText et1=(EditText)findViewById(R.id.editText2);
Button send=(Button)findViewById(R.id.button1);
send.setOnClickListener(new OnClickListener()
{
@Override
public void onClick(View arg0)
{
String s=et.getText().toString();
String s1=et1.getText().toString();
Intent it=new Intent(MainActivity.this,Second.class);
it.putExtra("uname", s);
it.putExtra("pwd", s1);

startActivity(it);

}

});

}

@Override

public boolean onCreateOptionsMenu(Menu menu) 

{

getMenuInflater().inflate(R.menu.main, menu);

return true;

}

}
""")
st.write("SecondActivity.java")

st.code("""package com.example.transferofdata;

import android.os.Bundle;

import android.app.Activity;

import android.view.Menu;

import android.widget.TextView;

public class Second extends Activity 

{

@Override

protected void onCreate(Bundle savedInstanceState) 

{

super.onCreate(savedInstanceState);

setContentView(R.layout.activity_second);

TextView tv=(TextView)findViewById(R.id.textView1);

TextView tv1=(TextView)findViewById(R.id.textView2);

tv.setText(getIntent().getExtras().getString("uname"));

tv1.setText(getIntent().getExtras().getString("pwd"));

}

@Override

public boolean onCreateOptionsMenu(Menu menu) 
{
getMenuInflater().inflate(R.menu.second, menu);

return true;

}

}""")
st.write("main.xml")
st.code("""<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"

xmlns:tools="http://schemas.android.com/tools"

android:layout_width="match_parent"

android:layout_height="match_parent"

android:paddingBottom="@dimen/activity_vertical_margin"

android:paddingLeft="@dimen/activity_horizontal_margin"

android:paddingRight="@dimen/activity_horizontal_margin"

android:paddingTop="@dimen/activity_vertical_margin"

tools:context=".MainActivity" >

<Button

android:id="@+id/button1"

android:layout_width="wrap_content"

android:layout_height="wrap_content"

android:layout_alignParentLeft="true"

android:layout_alignParentTop="true"

android:layout_marginLeft="78dp"

android:layout_marginTop="154dp"

android:text="send" />

<EditText

android:id="@+id/editText1"

android:layout_width="wrap_content"

android:layout_height="wrap_content"

android:layout_alignParentTop="true"

android:layout_alignRight="@+id/button1"

android:layout_marginTop="18dp"

android:ems="10" ><requestFocus /></EditText>

<EditText

android:id="@+id/editText2"
android:layout_width="wrap_content"

android:layout_height="wrap_content"

android:layout_alignRight="@+id/button1"

android:layout_below="@+id/editText1"

android:layout_marginTop="37dp"

android:ems="10"

android:inputType="textPassword" /></RelativeLayout>""")
st.write("secondactivity.xml")
st.code("""<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"

xmlns:tools="http://schemas.android.com/tools"

android:layout_width="match_parent"

android:layout_height="match_parent"

android:paddingBottom="@dimen/activity_vertical_margin"

android:paddingLeft="@dimen/activity_horizontal_margin"

android:paddingRight="@dimen/activity_horizontal_margin"

android:paddingTop="@dimen/activity_vertical_margin"

tools:context=".Second" >

<TextView

android:id="@+id/textView1"

android:layout_width="wrap_content"

android:layout_height="wrap_content"

android:layout_alignParentLeft="true"

android:layout_alignParentTop="true"

android:layout_marginLeft="42dp"

android:layout_marginTop="70dp"

android:text="uname" />

<TextView

android:id="@+id/textView2"

android:layout_width="wrap_content"

android:layout_height="wrap_content"

android:layout_alignLeft="@+id/textView1"

android:layout_below="@+id/textView1"

android:layout_marginLeft="15dp"
 android:layout_marginTop="37dp"

android:text="password" />

</RelativeLayout>""")
st.header("android application Send SMS using Intent")
st.write("java")
st.code("""package com.example.sms;

import android.os.Bundle;

import android.app.Activity;

import android.telephony.gsm.SmsManager;

import android.view.Menu;

import android.view.View;

import android.view.View.OnClickListener;

import android.widget.Button;

public class MainActivity extends Activity 

{

@Override

protected void onCreate(Bundle savedInstanceState

{

super.onCreate(savedInstanceState);

setContentView(R.layout.activity_main);

Button bt=(Button)findViewById(R.id.button1);

bt.setOnClickListener(new OnClickListener() 

{

@Override

public void onClick(View v) 
{

// TODO Auto-generated method stub

SmsManager sms=SmsManager.getDefault();

sms.sendTextMessage("5554", null, "hai", null, null);

}

});

}
public boolean onCreateOptionsMenu(Menu menu) 

{

// Inflate the menu; this adds items to the action bar if it is present.

getMenuInflater().inflate(R.menu.main, menu);

return true;

}

}""")
st.write("xml")
st.code("""<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"

xmlns:tools="http://schemas.android.com/tools"

android:layout_width="match_parent"

android:layout_height="match_parent"

android:paddingBottom="@dimen/activity_vertical_margin"

android:paddingLeft="@dimen/activity_horizontal_margin"

android:paddingRight="@dimen/activity_horizontal_margin"

android:paddingTop="@dimen/activity_vertical_margin"

tools:context=".MainActivity" >

<Button

android:id="@+id/button1"

android:layout_width="wrap_content"

android:layout_height="wrap_content"

android:layout_alignParentLeft="true"

android:layout_alignParentTop="true"

android:layout_marginLeft="54dp"

android:layout_marginTop="166dp"

android:text="send" />

</RelativeLayout>""")
st.header("Background Color change")
st.write("Xml code")
st.code("""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
 android:layout_width="fill_parent"
 android:layout_height="fill_parent"
 android:orientation="vertical">
<LinearLayout
 android:id="@+id/linearLayout1"
 android:layout_width="match_parent"
 android:layout_height="match_parent"
 android:orientation="vertical">
<Button
 android:id="@+id/button1"
 android:layout_width="wrap_content"
 android:layout_height="wrap_content"
android:text="CYAN"/>
<Button
 android:id="@+id/button2"
 android:layout_width="wrap_content"
 android:layout_height="wrap_content"
android:text="BLUE" />
<Button
 android:id="@+id/button3"
 android:layout_width="wrap_content"
 android:layout_height="wrap_content"
android:text="YELLOW" />
</LinearLayout>
</LinearLayout>
""")
st.write("java")
st.code("""package bgcolor.com;
import android.app.Activity;
import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.LinearLayout;
import bgcolor.com.R;
public class BgcolorActivity extends Activity {
LinearLayout l1;

public void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
 setContentView(R.layout.main);
l1=(LinearLayout)findViewById(R.id.linearLayout1);
 handleclick hc=new handleclick();
 findViewById(R.id.button1).setOnClickListener(hc);
 findViewById(R.id.button2).setOnClickListener(hc);
 findViewById(R.id.button3).setOnClickListener(hc);
 }
public class handleclick implements OnClickListener{
public void onClick(View args0){
if(args0.getId()==R.id.button1)
l1.setBackgroundColor(Color.CYAN);
else if(args0.getId()==R.id.button2)
l1.setBackgroundColor(Color.BLUE);
else if(args0.getId()==R.id.button3)
l1.setBackgroundColor(Color.YELLOW);
else
l1.setBackgroundColor(Color.TRANSPARENT);
}
 }
}
""")
st.header("Fond and Color change")
st.write("xml")
st.code("""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:baselineAligned="false"
    android:orientation="vertical" >

    <TextView
        android:id="@+id/textView1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_margin="20sp"
        android:gravity="center"
        android:text="WELCOME"
        android:textSize="20sp" />


    <Button
        android:id="@+id/button1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_margin="20sp"
        android:gravity="center"
        android:text="Change fond size" />
    
    <Button
        android:id="@+id/button2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_margin="20sp"
        android:gravity="center"
        android:text="Change Color" />

</LinearLayout>

""")
st.write("java")
st.code("""package com.display;

import android.app.Activity;
import android.os.Bundle;
import android.graphics.Typeface;
import android.graphics.Color;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class FondAndColorChangeActivity extends Activity {
	float font=24;
	int i=1;
  
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
    
    final TextView t1=(TextView)findViewById(R.id.textView1);
    Button b1=(Button)findViewById(R.id.button1);
    b1.setOnClickListener(new View.OnClickListener(){
    	public void onClick(View view){
    		t1.setTextSize(font);
    		font=font+4;
    		if(font==40)
    			font=20;
    	}
    });
    Button b2=(Button)findViewById(R.id.button2);
    b2.setOnClickListener(new View.OnClickListener() {
		
		public void onClick(View view) {
		switch(i)
		{
		case 1:
			t1.setTextColor(Color.parseColor("#0000FF"));
			break;
			
		case 2:
			t1.setTextColor(Color.parseColor("#00FF00"));
			break;
			
		case 3:
			t1.setTextColor(Color.parseColor("#FF0000"));
			break;
			
		case 4:
			t1.setTextColor(Color.parseColor("#800000"));
			break;
		}
		i++;
		if(i==5)
			i=1;
		}
	});
    
    }
}
""")
st.header("Sjctni Admission")
st.write("java")
st.code("""Sjctni.java
package com.example.sjctnimenu;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button homeButton = findViewById(R.id.btnHome);
        Button coursesButton = findViewById(R.id.btnCourses);
        Button admissionsButton = findViewById(R.id.btnAdmissions);
        Button contactButton = findViewById(R.id.btnContact);

        homeButton.setOnClickListener(view -> openPage(HomeActivity.class));
        coursesButton.setOnClickListener(view -> openPage(CoursesActivity.class));
        admissionsButton.setOnClickListener(view -> openPage(AdmissionsActivity.class));
        contactButton.setOnClickListener(view -> openPage(ContactActivity.class));
    }

    private void openPage(Class<?> activityClass) {
        Intent intent = new Intent(this, activityClass);
        startActivity(intent);
    }
}

// HomeActivity.java
package com.example.sjctnimenu;

import android.app.Activity;
import android.os.Bundle;

public class HomeActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
    }
}

// CoursesActivity.java
package com.example.sjctnimenu;

import android.app.Activity;
import android.os.Bundle;

public class CoursesActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_courses);
    }
}

// AdmissionsActivity.java
package com.example.sjctnimenu;

import android.app.Activity;
import android.os.Bundle;

public class AdmissionsActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_admissions);
    }
}

// ContactActivity.java
package com.example.sjctnimenu;

import android.app.Activity;
import android.os.Bundle;

public class ContactActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_contact);
    }
}""")
st.write("Xml")
st.code("""Home Page (activity_home.xml)
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    android:orientation="vertical">
    <TextView android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Welcome to SJCTNI" />
</LinearLayout>
Courses Page (activity_courses.xml)
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    android:orientation="vertical">
    <TextView android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Courses Offered: B.Sc, B.A, B.Com, M.Sc, M.A, M.Com" />
</LinearLayout>

Admissions Page (activity_admissions.xml)
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    android:orientation="vertical">
    <TextView android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Admission Open! Apply at sjctni.edu/admissions" />
</LinearLayout>
Contact Page (activity_contact.xml)
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    android:orientation="vertical">
    <TextView android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Contact: 123-456-7890 | Email: info@sjctni.edu" />
</LinearLayout>""")

