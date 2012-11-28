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
      'target_name': 'hello_apk_with_jni',
      'type': 'none',
	  'variables': {
		  'package_name': 'hello_apk_with_jni',
		  'apk_name': 'ApkjniDemo',
		  'java_in_dir': '../hello-apk-with-jni/',
		  'resource_dir': 'res',
          'native_libs_paths': ['<(SHARED_LIB_DIR)/libhellojni.so'],
	  },
	  'includes': ['../../build/java_apk.gypi'],

    },
    {
      'target_name': 'libhellojni',
      'type': 'shared_library',
	  'link_settings': {
        'libraries': [
          '-llog',  # ANativeWindow
        ],
      },
	  'dependencies': [
         'hello_jni_headers',
       ],
      'include_dirs': [
        '../..',
        '<(SHARED_INTERMEDIATE_DIR)/hello_apk_with_jni',
      ],
      'sources': [
        'hello_library_loader.cc',
      ],
    },
  	{
    'target_name': 'hello_jni_headers',
    'type': 'none',
    'sources': [
      'src/com/examplecode/helloapk/Hello.java',
    ],
    'variables': {
      'jni_gen_dir': 'hello_apk_with_jni',
    },
    'includes': [ '../../build/jni_generator.gypi' ],
  	},
  ],
}
