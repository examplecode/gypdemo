# This file is generated by gyp; do not edit.

TOOLSET := target
TARGET := hello_jni_header
### Generated for rule _home_chengkai_develop_chromium_src_sample_hello_jni_hello_jni_gyp_hello_jni_header_target_generate_jni_headers:
rule__home_chengkai_develop_chromium_src_sample_hello_jni_hello_jni_gyp_hello_jni_header_target_generate_jni_headers_outputs :=

### Finished generating for rule: _home_chengkai_develop_chromium_src_sample_hello_jni_hello_jni_gyp_hello_jni_header_target_generate_jni_headers

### Finished generating for all rules

### Rules for final target.
# Build our special outputs first.
$(obj).target/sample/hello-jni/hello_jni_header.stamp: | $(rule__home_chengkai_develop_chromium_src_sample_hello_jni_hello_jni_gyp_hello_jni_header_target_generate_jni_headers_outputs)

# Preserve order dependency of special output on deps.
$(rule__home_chengkai_develop_chromium_src_sample_hello_jni_hello_jni_gyp_hello_jni_header_target_generate_jni_headers_outputs): | 

$(obj).target/sample/hello-jni/hello_jni_header.stamp: TOOLSET := $(TOOLSET)
$(obj).target/sample/hello-jni/hello_jni_header.stamp:  FORCE_DO_CMD
	$(call do_cmd,touch)

all_deps += $(obj).target/sample/hello-jni/hello_jni_header.stamp
# Add target alias
.PHONY: hello_jni_header
hello_jni_header: $(obj).target/sample/hello-jni/hello_jni_header.stamp

# Add target alias to "all" target.
.PHONY: all
all: hello_jni_header

