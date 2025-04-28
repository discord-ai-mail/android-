import streamlit as st


def main():
    st.title("Download ADT android development tool kit")
    st.write("http://bit.ly/35GUYzF")

    st.title("layout")
    st.write("xml code in activity_main")
    st.code("""
    <RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="20dp"
    tools:context=".MainActivity" >

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:layout_centerInParent="true">

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Student Information"
            android:textAppearance="?android:attr/textAppearanceLarge"
            android:textStyle="bold"
            android:layout_gravity="center" />

        <EditText
            android:id="@+id/editTextName"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Enter Name" />

        <EditText
            android:id="@+id/editTextDno"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Enter D.NO" />

        <EditText
            android:id="@+id/editTextDept"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Enter Department" />

        <EditText
            android:id="@+id/editTextContact"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Enter Contact Number" />

        <Button
            android:id="@+id/buttonOpenActivity2"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="OK"
            android:layout_gravity="center"
            android:layout_marginTop="20dp" />

    </LinearLayout>

</RelativeLayout>""")
    st.write("activity2.xml")
    st.code("""
    <RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="20dp" >
    
    <TextView
        android:id="@+id/textView1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentLeft="true"
        android:layout_alignParentTop="true"
        android:layout_marginTop="32dp"
        android:paddingBottom="10dp"
        android:text="STUDENT INFORMATION"
        android:textAppearance="?android:attr/textAppearanceLarge"
        android:textStyle="bold" />

    <TextView
        android:id="@+id/textViewDno"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignLeft="@+id/textViewName"
        android:layout_below="@+id/textViewName"
        android:text="D.NO:" />

    <TextView
        android:id="@+id/textViewContact"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignRight="@+id/textViewDept"
        android:layout_below="@+id/textViewDno"
        android:text="ContactNO:" />

    <TextView
        android:id="@+id/textViewName"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignRight="@+id/textViewContact"
        android:layout_below="@+id/textView1"
        android:layout_marginTop="18dp"
        android:text="Name:" />

    <TextView
        android:id="@+id/textViewDept"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentLeft="true"
        android:layout_below="@+id/textViewContact"
        android:text="Department:" />

</RelativeLayout>""")
    st.write("activity1.java")
    st.code("""
    package com.example.layout;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class activity1 extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final EditText editTextName = (EditText) findViewById(R.id.editTextName);
        final EditText editTextDno = (EditText) findViewById(R.id.editTextDno);
        final EditText editTextDept = (EditText) findViewById(R.id.editTextDept);
        final EditText editTextContact = (EditText) findViewById(R.id.editTextContact);
        Button buttonOpenActivity2 = (Button) findViewById(R.id.buttonOpenActivity2);

        buttonOpenActivity2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String name = editTextName.getText().toString();
                String dno = editTextDno.getText().toString();
                String department = editTextDept.getText().toString();
                String contact = editTextContact.getText().toString();

                Intent intent = new Intent(activity1.this, activity2.class);
                intent.putExtra("NAME", name);
                intent.putExtra("DNO", dno);
                intent.putExtra("DEPARTMENT", department);
                intent.putExtra("CONTACT", contact);
                startActivity(intent);
            }
        });
    }
}""")
    st.write("activity2.java")
    st.code("""
    package com.example.layout;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class activity2 extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity2);

        TextView textViewName = (TextView) findViewById(R.id.textViewName);
        TextView textViewDno = (TextView) findViewById(R.id.textViewDno);
        TextView textViewDept = (TextView) findViewById(R.id.textViewDept);
        TextView textViewContact = (TextView) findViewById(R.id.textViewContact);

        String name = getIntent().getStringExtra("NAME");
        String dno = getIntent().getStringExtra("DNO");
        String department = getIntent().getStringExtra("DEPARTMENT");
        String contact = getIntent().getStringExtra("CONTACT");

        textViewName.setText("Name:" + name);
        textViewDno.setText("D.NO:" + dno);
        textViewDept.setText("Department:" + department);
        textViewContact.setText("ContactNO:" + contact);
    }
}""")
    st.write("androidmanifist.xml")
    st.code("""
    <?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.layout"
    android:versionCode="1"
    android:versionName="1.0" >

    <uses-sdk
        android:minSdkVersion="8"
        android:targetSdkVersion="18" />

    <application
        android:allowBackup="true"
        android:icon="@drawable/ic_launcher"
        android:label="@string/app_name"
        android:theme="@style/AppTheme" >
        <activity 
            android:name=".activity1"
            
            android:label="@string/app_name" >
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        <activity android:name="com.example.layout.activity2" />
    </application>

</manifest>""")




    st.title("Calculator")
    st.write("xml code")
    st.code("""
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">

    <EditText
        android:id="@+id/editText11"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter first number"
        android:inputType="number" />

    <EditText
        android:id="@+id/editText22"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter second number"
        android:inputType="number" />

    <Button
        android:id="@+id/addButtonn"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Add" />

    <Button
        android:id="@+id/button1"
        android:layout_width="282dp"
        android:layout_height="wrap_content"
        android:text="sub" />

    <EditText
        android:id="@+id/editText33"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:ems="10"
        android:focusable="false"
        android:hint="Result" >

        <requestFocus />
    </EditText>

</LinearLayout>""")

    st.write("mainactivity java code")
    st.code("""
package com.example.calculator;

import android.app.Activity;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends Activity {

    private EditText editText1, editText2, editText3;
    private Button addButton, subbutton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize UI components
        editText1 = (EditText) findViewById(R.id.editText11);
        editText2 = (EditText) findViewById(R.id.editText22);
        editText3 = (EditText) findViewById(R.id.editText33);
        addButton = (Button) findViewById(R.id.addButtonn);
        subbutton = (Button) findViewById(R.id.button1);

        // Set the button's onClickListener
        addButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                calculateSum();
            }
        });
        subbutton.setOnClickListener(new View.OnClickListener(){
        	@Override
        	public void onClick(View v){
        		calculateSub();
        	}
        });
    }

    private void calculateSum() {
        // Get the input values as strings
        String input1 = editText1.getText().toString();
        String input2 = editText2.getText().toString();

        

        // Parse the inputs to integers
        
         int number1 = Integer.parseInt(input1);
         int number2 = Integer.parseInt(input2);

            // Calculate the sum
         int sum = number1 + number2;

            // Display the result in editText3
         editText3.setText(String.valueOf(sum));
        
    }
    
    
    private void calculateSub() {
        // Get the input values as strings
        String input1 = editText1.getText().toString();
        String input2 = editText2.getText().toString();

        

        // Parse the inputs to integers
        
         int number1 = Integer.parseInt(input1);
         int number2 = Integer.parseInt(input2);

            // Calculate the sum
         int sum = number1 - number2;

            // Display the result in editText3
         editText3.setText(String.valueOf(sum));
        
    }
}
""")


    st.title("Business calculator")
    st.write("XML code")
    st.code("""
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">

    <EditText
        android:id="@+id/costPrice"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter Cost Price"
        android:inputType="numberDecimal" />

    <EditText
        android:id="@+id/sellingPrice"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter Selling Price"
        android:inputType="numberDecimal" />

    <Button
        android:id="@+id/btnProfit"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Calculate Profit" />

    <Button
        android:id="@+id/btnLoss"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Calculate Loss" />

    <TextView
        android:id="@+id/result"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Result:"
        android:textSize="16sp"
        android:paddingTop="10dp" />
</LinearLayout>
""")

    st.write("mainActivity java code")

    st.code("""
package com.example.businesscalculator;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize UI components
        final EditText costPrice = (EditText) findViewById(R.id.costPrice);
        final EditText sellingPrice = (EditText) findViewById(R.id.sellingPrice);
        final TextView result = (TextView) findViewById(R.id.result);
        Button btnProfit = (Button) findViewById(R.id.btnProfit);
        Button btnLoss = (Button) findViewById(R.id.btnLoss);

        // Handle Calculate Profit Button
        btnProfit.setOnClickListener(new View.OnClickListener() {
            @SuppressLint("NewApi") @Override
            public void onClick(View v) {
                String cpText = costPrice.getText().toString().trim();
                String spText = sellingPrice.getText().toString().trim();

   

                try {
                    double cp = Double.parseDouble(cpText);
                    double sp = Double.parseDouble(spText);

                    if (sp > cp) {
                        result.setText("Profit: " + (sp - cp));
                    } else {
                        result.setText("No Profit.");
                    }
                } catch (NumberFormatException e) {
                    result.setText("Invalid input. Please enter numeric values.");
                }
            }
        });

        // Handle Calculate Loss Button
        btnLoss.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String cpText = costPrice.getText().toString().trim();
                String spText = sellingPrice.getText().toString().trim();

               

                try {
                    double cp = Double.parseDouble(cpText);
                    double sp = Double.parseDouble(spText);

                    if (cp > sp) {
                        result.setText("Loss: " + (cp - sp));
                    } else {
                        result.setText("No Loss.");
                    }
                } catch (NumberFormatException e) {
                    result.setText("Invalid input. Please enter numeric values.");
                }
            }
        });
    }
}
""")


    st.title("bouncing ball")
    st.write("Xml code")
    st.code("""
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:orientation="vertical" >

    <Button
        android:id="@+id/bounceBallButton"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_centerHorizontal="true"
        android:text="Bounce Ball" />

    <ImageView
        android:id="@+id/bounceBallImage"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_below="@+id/bounceBallButton"
        android:layout_centerHorizontal="true"
        android:background="@drawable/ball_shape" />

</RelativeLayout>
""")



    st.write("Xml code in ball image the file located in under drawable folder file name like(ball_shape.xml)")


    st.code("""
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="oval" >

    <solid android:color="#8c0000" />

    <stroke
        android:width="2dp"
        android:color="#fff" />
    
    <size
        android:height="80dp"
        android:width="80dp" />

</shape>
""")




    st.write("mainActivity java code")

    st.code("""
package com.example.bounc;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.animation.Animation;
import android.view.animation.BounceInterpolator;
import android.view.animation.TranslateAnimation;
import android.view.animation.Animation.AnimationListener;
import android.widget.Button;
import android.widget.ImageView;

public class MainActivity extends Activity {

    private static final String TAG = "AnimationStarter";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button bounceBallButton = (Button) findViewById(R.id.bounceBallButton);
        final ImageView bounceBallImage = (ImageView) findViewById(R.id.bounceBallImage);

        bounceBallButton.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {
                bounceBallImage.clearAnimation();
                TranslateAnimation transAnim = new TranslateAnimation(0, 0, 0,
                        getDisplayHeight()/2);
                transAnim.setStartOffset(500);
                transAnim.setDuration(3000);
                transAnim.setFillAfter(true);
                transAnim.setInterpolator(new BounceInterpolator());
                transAnim.setAnimationListener(new AnimationListener() {

                    @Override
                    public void onAnimationStart(Animation animation) {
                        Log.i(TAG, "Starting button dropdown animation");

                    }

                    @Override
                    public void onAnimationRepeat(Animation animation) {
                        // TODO Auto-generated method stub

                    }

                    @Override
                    public void onAnimationEnd(Animation animation) {
                        Log.i(TAG,
                                "Ending button dropdown animation. Clearing animation and setting layout");
                        bounceBallImage.clearAnimation();
                        final int left = bounceBallImage.getLeft();
                        final int top = bounceBallImage.getTop();
                        final int right = bounceBallImage.getRight();
                        final int bottom = bounceBallImage.getBottom();
                        bounceBallImage.layout(left, top, right, bottom);

                    }
                });
                bounceBallImage.startAnimation(transAnim);
            }
        });

    }

    private int getDisplayHeight() {
        return this.getResources().getDisplayMetrics().heightPixels;
    }
}
""")

    st.markdown("""<center><h1 style="color:red;">color bg change</h1></center>""",unsafe_allow_html=True)
    
    st.write("Xml code")
    st.code("""<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp"
    android:id="@+id/relativelayout1">

    <Button
        android:id="@+id/button1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentLeft="true"
        android:layout_alignParentTop="true"
        android:layout_marginLeft="94dp"
        android:layout_marginTop="87dp"
        android:text="@string/cool" 
        android:onClick="OnClick"/>

    <Button
        android:id="@+id/button2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignRight="@+id/button1"
        android:layout_centerVertical="true"
        android:text="Button" />

</RelativeLayout>

""")

    st.write("change string.xml it's located in res under value folder")


    st.code("""<?xml version="1.0" encoding="utf-8"?>
<resources>

    <string name="app_name">backgroundcolorapp</string>
    <string name="action_settings">Settings</string>
    <string name="hello_world">Hello world!</string>
    
    
    <string name="cool">cool</string>
    
    <color name="cool">#188FcF</color>

</resources>
""")


    st.write("mainactivity java folder")

    st.code("""
package com.example.backgroundcolorapp;

import android.app.Activity;
import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.webkit.WebView.FindListener;
import android.widget.RelativeLayout;
import android.widget.Button;
import java.util.Random;

public class MainActivity extends Activity {

    RelativeLayout r1;
    Button b1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        r1=(RelativeLayout)findViewById(R.id.relativelayout1);
        
        b1=(Button)findViewById(R.id.button1);
        
        b1.setOnClickListener(new OnClickListener()
        {
        	@Override
        	public void onClick(View arg0){
        		r1.setBackgroundResource(R.color.cool);
        	}
        });
        

       
    }
}
""")
    st.write("color code finding website link:https://colorcodefinder.com/")
    st.title("two ball bouncing ball")
    st.write("activity.xml")
    st.code("""<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:orientation="vertical" >

    <Button
        android:id="@+id/bounceBallButton"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_centerHorizontal="true"
        android:text="Bounce Ball" />

    <ImageView
        android:id="@+id/bounceBallImage2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentLeft="true"
        android:layout_below="@+id/bounceBallButton"
        android:layout_marginLeft="42dp"
        android:layout_marginStart="50dp"
        android:layout_marginTop="26dp"
        android:background="@drawable/ball_shape" />

    <ImageView
        android:id="@+id/bounceBallImage1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignTop="@+id/bounceBallImage2"
        android:layout_marginEnd="50dp"
        android:layout_marginLeft="54dp"
        android:layout_toRightOf="@+id/bounceBallImage2"
        android:background="@drawable/ball_shape" />

</RelativeLayout>""")
    st.write("drawable folder with in ball_shape.xml")
    st.code("""<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="oval" >

    <solid android:color="#8c0000" />

    <stroke
        android:width="2dp"
        android:color="#fff" />
    
    <size
        android:height="80dp"
        android:width="80dp" />

</shape>""")
    st.write("ball2")
    st.code("""<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="oval" >

    <solid android:color="#8c0000" />

    <stroke
        android:width="2dp"
        android:color="#fff" />

    <size
        android:height="80dp"
        android:width="80dp" />

</shape>""")
    st.write("java code ")
    st.code("""package com.example.bounc;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.BounceInterpolator;
import android.view.animation.TranslateAnimation;
import android.view.animation.Animation.AnimationListener;
import android.widget.Button;
import android.widget.ImageView;

public class MainActivity extends Activity {

    private static final String TAG = "AnimationStarter";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button bounceBallButton = (Button) findViewById(R.id.bounceBallButton);
        final ImageView bounceBallImage1 = (ImageView) findViewById(R.id.bounceBallImage1);
        final ImageView bounceBallImage2 = (ImageView) findViewById(R.id.bounceBallImage2);

        bounceBallButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                animateBall(bounceBallImage1, 0);  // First ball
                animateBall(bounceBallImage2, 500); // Second ball with delay
            }
        });
    }

    private void animateBall(final ImageView ball, int startOffset) {
        ball.clearAnimation();
        TranslateAnimation transAnim = new TranslateAnimation(0, 0, 0, getDisplayHeight() / 2);
        transAnim.setStartOffset(startOffset);
        transAnim.setDuration(3000);
        transAnim.setFillAfter(true);
        transAnim.setInterpolator(new BounceInterpolator());

        transAnim.setAnimationListener(new AnimationListener() {
            @Override
            public void onAnimationStart(Animation animation) {
                Log.i(TAG, "Starting ball bounce animation");
            }

            @Override
            public void onAnimationRepeat(Animation animation) {}

            @Override
            public void onAnimationEnd(Animation animation) {
                Log.i(TAG, "Ending ball bounce animation.");
                ball.clearAnimation();
                final int left = ball.getLeft();
                final int top = ball.getTop();
                final int right = ball.getRight();
                final int bottom = ball.getBottom();
                ball.layout(left, top, right, bottom);
            }
        });

        ball.startAnimation(transAnim);
    }

    private int getDisplayHeight() {
        return this.getResources().getDisplayMetrics().heightPixels;
    }
}""")
    st.markdown("""<center><h1 style="color:red;">END SEM LAB</h1></center>""",unsafe_allow_html=True)
    st.title("GUI font & Color change ")
    st.write("xml code ")
    st.code("""<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
xmlns:tools="http://schemas.android.com/tools"
android:layout_width="fill_parent"
android:layout_height="fill_parent"
android:orientation="vertical"
>

<TextView
android:id="@+id/textView1"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:text="WELCOME"
android:layout_margin="20sp"
android:gravity="center"
android:textSize="20sp"
android:textStyle="bold"
/>
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
    st.write("mainactivity.java")
    st.code("""package com.example.gui;
import android.app.Activity;
import android.graphics.Typeface;
import android.graphics.Color;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;

import android.app.Activity;
import android.graphics.Typeface;
import android.graphics.Color;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
public class MainActivity extends Activity {
float font = 24;
int i = 1;




protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);
final TextView t1 = (TextView)findViewById(R.id.textView1);
Button b1 = (Button)findViewById(R.id.button1);
b1. setOnClickListener(new View.OnClickListener() {
public void onClick(View view) {
t1.setTextSize(font);
font = font+4;
if(font==40)
font = 20;

}
});
Button b2 = (Button)findViewById(R.id.button2);
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

i = 1;
}
});

}
}""")

    st.title("singup validation")
    st.write("XML code")
    st.code("""<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp">

    <EditText
        android:id="@+id/username"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Username" />

    <EditText
        android:id="@+id/password"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_below="@id/username"
        android:layout_marginTop="16dp"
        android:hint="Password"
        android:inputType="textPassword" />

    <Button
        android:id="@+id/signupButton"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_below="@id/password"
        android:layout_marginTop="16dp"
        android:text="Sign Up" />

    <TextView
        android:id="@+id/errorText"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_below="@id/signupButton"
        android:layout_marginTop="16dp"/>

</RelativeLayout>""")
    st.write("main Activity.java code")
    st.code("""package com.example.signup_validation;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

@SuppressLint("DefaultLocale")
public class MainActivity extends Activity {

    private View usernameEditText;
    private View passwordEditText;
    private View errorTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        usernameEditText = findViewById(R.id.username);
        passwordEditText = findViewById(R.id.password);
        errorTextView = findViewById(R.id.errorText);
        View signupButton = findViewById(R.id.signupButton);

        signupButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                @SuppressWarnings("unused")
				String username = ((TextView) usernameEditText).getText().toString();
                String password = ((TextView) passwordEditText).getText().toString();

                if (isValidPassword(password)) {
                    // Proceed with sign-up process
                    Toast.makeText(MainActivity.this, "Sign Up Successful!", Toast.LENGTH_SHORT).show();
                } else {
                    // Display error message
                    ((TextView) errorTextView).setText("Password does not meet the requirements.");
                }
            }
        });

    }

    @SuppressLint("DefaultLocale")
	private boolean isValidPassword(String password) {
        if (password.length() < 8) {
            return false;
        }
        boolean hasUpperCase = !password.equals(password.toLowerCase());
        boolean hasLowerCase = !password.equals(password.toUpperCase());
        boolean hasDigit = !TextUtils.isEmpty(password.replaceAll("[^0-9]", ""));
        boolean hasSpecialChar = !password.matches("[A-Za-z0-9]*");

        return hasUpperCase && hasLowerCase && hasDigit && hasSpecialChar;
    }
}""")
    st.title("graphical line")
    st.write("XML code")
    st.code("""<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
xmlns:tools="http://schemas.android.com/tools"
android:layout_width="match_parent"
android:layout_height="match_parent"
>

<ImageView
android:id="@+id/imageView1"
android:layout_width="wrap_content"
android:layout_height="match_parent"
android:layout_alignParentLeft="true"
android:layout_alignParentRight="true"
android:layout_alignParentTop="true"
android:src="@drawable/ic_launcher" />
</RelativeLayout>""")
    st.write("MainActivity.java code")
    st.code("""package com.example.graphical;

import android.app.Activity;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.os.Bundle;
import android.view.Display;
import android.view.MotionEvent;
import android.view.View;
import android.view.View.OnTouchListener;
import android.widget.ImageView;
public class MainActivity extends Activity implements OnTouchListener {
private ImageView imageView;

private Bitmap bitmap;
private Canvas canvas;
private Paint paint;
private float downx = 0, downy = 0, upx = 0, upy = 0;
public void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);
imageView = (ImageView) this.findViewById(R.id.imageView1);
Display currentDisplay = getWindowManager().getDefaultDisplay();
@SuppressWarnings("deprecation")
float dw = currentDisplay.getWidth();
@SuppressWarnings("deprecation")
float dh = currentDisplay.getHeight();
bitmap = Bitmap.createBitmap((int) dw, (int) dh, Bitmap.Config.ARGB_8888);
canvas = new Canvas(bitmap);
paint = new Paint();
paint.setColor(Color.BLUE);
imageView.setImageBitmap(bitmap);
imageView.setOnTouchListener(this);
}
public boolean onTouch(View v, MotionEvent event) {
int action = event.getAction();
switch (action) {
case MotionEvent.ACTION_DOWN:
downx = event.getX();
downy = event.getY();
break;
case MotionEvent.ACTION_MOVE:
break;
case MotionEvent.ACTION_UP:
upx = event.getX();
upy = event.getY();
canvas.drawLine(downx, downy, upx, upy, paint);
imageView.invalidate();
break;
case MotionEvent.ACTION_CANCEL:
break;
default:
break;
}
return true;
}
}""")
    st.title("intern print std details in other page ")
    st.write("Actvity1.xml")
    st.code("""<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="20dp"
    tools:context=".MainActivity" >

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:layout_centerInParent="true">

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Student Information"
            android:textAppearance="?android:attr/textAppearanceLarge"
            android:textStyle="bold"
            android:layout_gravity="center" />

        <EditText
            android:id="@+id/editTextName"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Enter Name" />

        <EditText
            android:id="@+id/editTextDno"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Enter D.NO" />

        <EditText
            android:id="@+id/editTextDept"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Enter Department" />

        <EditText
            android:id="@+id/editTextContact"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Enter Contact Number" />

        <Button
            android:id="@+id/buttonOpenActivity2"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="OK"
            android:layout_gravity="center"
            android:layout_marginTop="20dp" />

    </LinearLayout>

</RelativeLayout>""")
    st.write("Activity2.xml")
    st.code("""<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="20dp" >
    
    <TextView
        android:id="@+id/textView1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentLeft="true"
        android:layout_alignParentTop="true"
        android:layout_marginTop="32dp"
        android:paddingBottom="10dp"
        android:text="STUDENT INFORMATION"
        android:textAppearance="?android:attr/textAppearanceLarge"
        android:textStyle="bold" />

    <TextView
        android:id="@+id/textViewDno"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignLeft="@+id/textViewName"
        android:layout_below="@+id/textViewName"
        android:text="D.NO:" />

    <TextView
        android:id="@+id/textViewContact"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignRight="@+id/textViewDept"
        android:layout_below="@+id/textViewDno"
        android:text="ContactNO:" />

    <TextView
        android:id="@+id/textViewDept"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentLeft="true"
        android:layout_below="@+id/textViewContact"
        android:text="Department:" />

    <TextView
        android:id="@+id/textViewName"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignRight="@+id/textViewContact"
        android:layout_below="@+id/textView1"
        android:text="Name:" />

</RelativeLayout>""")
    st.write("main1.java")
    st.code("""package com.example.layout;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class activity1 extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final EditText editTextName = (EditText) findViewById(R.id.editTextName);
        final EditText editTextDno = (EditText) findViewById(R.id.editTextDno);
        final EditText editTextDept = (EditText) findViewById(R.id.editTextDept);
        final EditText editTextContact = (EditText) findViewById(R.id.editTextContact);
        Button buttonOpenActivity2 = (Button) findViewById(R.id.buttonOpenActivity2);

        buttonOpenActivity2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String name = editTextName.getText().toString();
                String dno = editTextDno.getText().toString();
                String department = editTextDept.getText().toString();
                String contact = editTextContact.getText().toString();

                Intent intent = new Intent(activity1.this, activity2.class);
                intent.putExtra("NAME", name);
                intent.putExtra("DNO", dno);
                intent.putExtra("DEPARTMENT", department);
                intent.putExtra("CONTACT", contact);
                startActivity(intent);
            }
        });
    }
}""")
    st.write("main2.java")
    st.code("""package com.example.layout;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class activity2 extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity2);

        TextView textViewName = (TextView) findViewById(R.id.textViewName);
        TextView textViewDno = (TextView) findViewById(R.id.textViewDno);
        TextView textViewDept = (TextView) findViewById(R.id.textViewDept);
        TextView textViewContact = (TextView) findViewById(R.id.textViewContact);

        String name = getIntent().getStringExtra("NAME");
        String dno = getIntent().getStringExtra("DNO");
        String department = getIntent().getStringExtra("DEPARTMENT");
        String contact = getIntent().getStringExtra("CONTACT");

        textViewName.setText("Name:" + name);
        textViewDno.setText("D.NO:" + dno);
        textViewDept.setText("Department:" + department);
        textViewContact.setText("ContactNO:" + contact);
    }
}""")
    st.title("Send SMS")
    st.write("XML code")
    st.code("""<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp">

    <EditText
        android:id="@+id/phoneNumber"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter phone number (e.g., 5556)"
        android:inputType="phone" />

    <EditText
        android:id="@+id/message"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_below="@id/phoneNumber"
        android:layout_marginTop="16dp"
        android:hint="Enter message"
        android:inputType="textMultiLine" />

    <Button
        android:id="@+id/sendButton"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_below="@id/message"
        android:layout_marginTop="16dp"
        android:text="Send SMS" />

</RelativeLayout>""")
    st.write("mainActivity.java code")
    st.code("""package com.example.sms;

import android.app.Activity;
import android.app.PendingIntent;
import android.content.Intent;
import android.os.Bundle;
import android.telephony.SmsManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends Activity {
    EditText phoneNumber;
    EditText message;
    Button sendButton;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        phoneNumber = (EditText) findViewById(R.id.phoneNumber);
        message = (EditText) findViewById(R.id.message);
        sendButton = (Button) findViewById(R.id.sendButton);

        sendButton.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                sendSMSMessage();
            }
        });
    }

    protected void sendSMSMessage() {
        String phoneNo = phoneNumber.getText().toString();
        String smsMessage = message.getText().toString();

        try {
            SmsManager smsManager = SmsManager.getDefault();
            smsManager.sendTextMessage(phoneNo, null, smsMessage, null, null);
            Toast.makeText(getApplicationContext(), "SMS sent.", Toast.LENGTH_LONG).show();
        } catch (Exception e) {
            Toast.makeText(getApplicationContext(), "SMS failed, please try again.", Toast.LENGTH_LONG).show();
            e.printStackTrace();
        }
    }
}""")
    st.write("Androidmanifest.XML file")
    st.write("NOTE: only change the modified code")
    st.code("""<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.sms"
    android:versionCode="1"
    android:versionName="1.0" >

    <uses-sdk
        android:minSdkVersion="8"
        android:targetSdkVersion="18" />
	<uses-permission android:name="android.permission.SEND_SMS" />
    <application
        android:allowBackup="true"
        android:icon="@drawable/ic_launcher"
        android:label="@string/app_name"
        
        android:supportsRtl="true"
        android:theme="@style/AppTheme" >
        <activity
            android:name="com.example.sms.MainActivity"
            android:label="@string/app_name" >
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>""")
    st.write("when you run the sms application you must run the two emulator")
    st.write("once you application is working to enter the port number in second emulator number example:'5558' and enter message")
    st.image("sms.png")
    st.write("port number is show in the top of the emulator app")
    st.image("sms2.png")

    
    st.title("DIFFERENT MENUES")
    st.write("activity_home.xml")
    st.code("""<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <TextView
        android:id="@+id/homeTextView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Home Page"
        android:layout_centerInParent="true"/>
</RelativeLayout>""")
    st.write("activity_main.xml")
    st.code("""<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <TextView
        android:id="@+id/mainTextView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Main Page"
        android:layout_centerInParent="true"/>
</RelativeLayout>""")
    st.write("activity_content.xml")
    st.code("""<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <TextView
        android:id="@+id/contentTextView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Content Page"
        android:layout_centerInParent="true"/>
</RelativeLayout>""")
    st.write("HomeActivity.java")
    st.code("""package com.example.menu_app;
import android.app.Activity;
import android.os.Bundle;


public class HomeActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
    }
}""")
    st.write("MainActivity.java")
    st.code("""package com.example.menu_app;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;


public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.main_menu, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();

        if (id == R.id.action_home) {
            Intent intent = new Intent(this, HomeActivity.class);
            startActivity(intent);
            return true;
        } else if (id == R.id.action_content) {
            Intent intent = new Intent(this, ContentActivity.class);
            startActivity(intent);
            return true;
        } else if (id == R.id.action_exit) {
            Intent intent = new Intent(Intent.ACTION_MAIN);
            intent.addCategory(Intent.CATEGORY_HOME);
            intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
            startActivity(intent);
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}""")
    st.write("ContentActivity.java")
    st.code("""package com.example.menu_app;

import android.app.Activity;
import android.os.Bundle;


public class ContentActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_content);
    }
}""")
    st.write("Create a file named main_menu.xml in the res/menu directory")
    st.code("""<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item
        android:id="@+id/action_home"
        android:title="Home" />
    <item
        android:id="@+id/action_content"
        android:title="Content" />
    <item
        android:id="@+id/action_exit"
        android:title="Exit" />
</menu>""")
    st.write("AndroidManifest.xml")
    st.code("""<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.yourapp">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.YourApp">
        <activity android:name=".HomeActivity"></activity>
        <activity android:name=".ContentActivity"></activity>
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>""")


    st.image("menu.png")




    
