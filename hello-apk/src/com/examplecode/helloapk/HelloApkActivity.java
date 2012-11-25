package com.examplecode.helloapk;

import android.app.Activity;
import android.os.Bundle;
import com.examplecode.hellojar.Hello;

public class HelloApkActivity extends Activity {
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
		Hello hello = new Hello();
		System.out.println(hello.saveHello());
    }
}
