package com.examplecode.helloapk;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;
import com.examplecode.helloapk.R;

public class HelloApkActivity extends Activity {
	static {
		System.loadLibrary("hellojni");
	}
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        TextView text = (TextView) findViewById(R.id.label);
        Hello hello = new Hello();
        text.setText(hello.nativeStringFromJNI());
    }
}
