import streamlit as st
hide_github_elements = """
<style>
    #GithubIcon, .viewerBadge_container__1QSob, .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137, .viewerBadge_text__1JaDK {
        display: none;
    }
</style>
"""
st.markdown(hide_github_elements, unsafe_allow_html=True)

st.write("calculator")
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


st.write("business calculator")
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


st.write("bouncing ball")
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


st.write("color bg change")
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

st.write("Layout XMl")
st.code("""         
<LinearLayout 
 xmlns:android="http://schemas.android.com/apk/res/android" 
 android:layout_width="match_parent" 
 android:layout_height="match_parent" 
 android:orientation="vertical"> 
 <RelativeLayout 
 android:layout_width="match_parent" 
 android:layout_height="200dp" 
 android:background="#FFC107"> 
 <TextView 
 android:layout_width="wrap_content" 
 android:layout_height="wrap_content" 
 android:text="RelativeLayout" 
 android:layout_centerInParent="true" /> 
 </RelativeLayout> 
 <FrameLayout 
 android:layout_width="match_parent" 
 android:layout_height="200dp" 
 android:background="#03A9F4"> 
 <TextView 
 android:layout_width="wrap_content" 
 android:layout_height="wrap_content" 
 android:text="FrameLayout" 
 android:layout_gravity="center" />
</FrameLayout> 
</LinearLayout>"""
        st.write("Main_activity.java")
        st.code("""package com.example.layouts;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

 @Override

 protected void onCreate(Bundle savedInstanceState) {

 super.onCreate(savedInstanceState);

 setContentView(R.layout.layout1);

 }

}"""
