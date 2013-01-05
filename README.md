# chromium gyp 构建系统的一些演示示例 #

## 说明 ##

1. hello 使用gyp生成一个最简单的程序
2. hello-jar  构建一个.jar 的包
3. hello-jni 生成jni注册头文件
4. hello-apk 构建一个apk包
5. hello-apk-with-jni 构建一个使用jni模块的apk

## 使用方法: ##


在chromium/src/build/all_android.gyp "dependencies" 字段中中增加下面一句话

	'../gypdemo/gypdemo.gyp:gypdemo',
	

使用编译目标

1. 生成makefile
	cd chromium/src/
	. build/android/envsetup.sh
	android_gyp

2. 编译生成目标
	make hello



## 通用的GYP使用方法 ##

mylib-gyp 示范不依赖chromium构建环境，只使用gyp构建 (确认gyp命令已经在你的环境变量中生效)

	cd mylib-gyp
	gyp mylib.gyp --depth=./ -fmake
	make main


