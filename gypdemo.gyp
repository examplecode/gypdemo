# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
	#在此定义一些变量
    'var_name': 'vaule',
  },
  'targets': [
    {
      'target_name': 'gypdemo',
      'type': 'none',
      'dependencies': [
		#增加依赖
	  'hello/hello.gyp:hello',
	  'hello-jni/hello-jni.gyp:hello_jni',
	  'hello-apk/hello-apk.gyp:hello_apk',
	  #'hello-jar/hello-jar.gyp:hello_jar',	
      ],
    },
  ],
}
