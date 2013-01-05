{
	'variables': {
		'default_configuration': 'Debug',     
    },
	'targets': [
	{
		'target_name': 'mylib',
			'type': 'static_library',
			'defines': [
			  'PLATFORM="<(OS)"',
			],
			'include_dirs': [
				'..',
			],
			'sources': [
				'mylib.cc',
				'mylib.h',
			],
	},
	{
		'target_name': 'main',
			'type': 'executable',
			'include_dirs': [
				'..',
			],
		   'cflags': [
		       # Don't warn about printf format problems.
		       # This is off by default in gcc but on in Ubuntu's gcc(!).
		    ],
			'sources': [
				'main.cc',
			],
		    'dependencies': [
			     'mylib',
			 ],
	},
  ],
}
