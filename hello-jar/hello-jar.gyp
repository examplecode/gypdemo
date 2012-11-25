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
      'target_name': 'hello_jar',
      'type': 'none',
      'variables': {
        'package_name': 'hello_jar',
        'java_in_dir': '../hello-jar',
      },
      'includes': ['../../build/java.gypi'],
    },
  ],
}
