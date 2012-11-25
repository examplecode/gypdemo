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
      'target_name': 'hello_apk',
      'type': 'none',
      'dependencies': [
	  '../hello-jar/hello-jar.gyp:hello_jar',	
	  ],
	  'variables': {
		  'package_name': 'hello_apk',
		  'apk_name': 'ApkDemo',
		  'java_in_dir': '../hello-apk/',
		  'resource_dir': 'res',
	  },
	  'includes': ['../../build/java_apk.gypi'],

    },
  ],
}
