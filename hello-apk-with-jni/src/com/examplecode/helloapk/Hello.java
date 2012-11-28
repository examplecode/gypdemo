package com.examplecode.helloapk;

public class Hello {

	 public void sayHello() {
		System.out.println(nativeStringFromJNI());
	}
	public native String  nativeStringFromJNI();
}
