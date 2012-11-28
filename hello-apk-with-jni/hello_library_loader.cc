/*
 * =====================================================================================
 *
 *       Filename:  hello_library_loader.cc
 *
 *    Description:  for test
 *
 *        Version:  1.0
 *        Created:  11/26/2012 04:55:41 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include "base/logging.h"
#include "base/android/jni_registrar.h"
#include "base/android/jni_android.h"
#include "base/android/jni_string.h"
#include <jni/Hello_jni.h>
// This is called by the VM when the shared library is first loaded.
 JNI_EXPORT jint JNI_OnLoad(JavaVM* vm, void* reserved) {
	ALOG(3,"this is log test");

	JNIEnv* env = NULL;
	jint ret = vm->AttachCurrentThread(&env, NULL);
	if(ret == -1) {
		ALOG(3,"can't attache current thread");
		return -1;
	} else {
		ALOG(3,"register native function");
		RegisterNativesImpl(env);
	}


	return JNI_VERSION_1_4;
 }
static jstring StringFromJNI(JNIEnv* env, jobject obj) {
	jclass cls = env->FindClass("java/lang/String");
//	jclass cls1 = (*env)->FindClass(env, "java/lang/String");
    return env->NewStringUTF("Hello from JNI !");
}
