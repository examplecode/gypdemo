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
      'target_name': 'hello',
      'type': 'shared_library',
      'defines!': ['CONTENT_IMPLEMENTATION'],
      'dependencies': [
		#增加依赖
      ],
      'include_dirs': [
        '..',
      ],
      'sources': [
        'hello.c',
        'hello.h',
      ],
    },
  ],
}
