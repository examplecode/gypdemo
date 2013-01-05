/*
 * =====================================================================================
 *
 *       Filename:  mylib.cc
 *
 *    Description:  my lib demo
 *
 *        Version:  1.0
 *        Created:  2013/01/02 20时26分40秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdio.h>
#include "mylib.h"

void say_hello()  {

#ifdef  PLATFORM
	printf(">>>>>>>>> Hello MyLib on %s !>>>>>>>>>>>\n",PLATFORM);
#else      /* -----  not PLATFORM  ----- */
	printf(">>>>>>>>> Hello MyLib  >>>>>>>>>>>\n");
#endif     /* -----  not PLATFORM  ----- */
}

