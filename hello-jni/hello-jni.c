/*
 * =====================================================================================
 *
 *       Filename:  hello.c
 *
 *    Description:  演示增加一个模块到chromium中
 *
 *        Version:  1.0
 *        Created:  2012年11月19日 16时12分11秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdlib.h>
#include "hello-jni.h"
#include <jni/Hello_jni.h>

void say_hello_by_jni() 
{
	printf("Hello World!");
}



