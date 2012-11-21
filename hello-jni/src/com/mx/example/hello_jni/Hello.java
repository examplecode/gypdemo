package com.mx.example.hello_jni;

@JNINamespace("hello")
public class Hello {

	public void sayHello() {
		System.out.println(nativeSayHelloFromJni());
	}


	private native String nativeSayHelloFromJni();
	
	@CalledByNative
	public void useJavaPrint(String string) 
	{
		System.out.println("========== string from jni: + " +string + "================");
	}
}
