[app]
title = Snake Python
package.name = snakepython
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy
orientation = portrait
fullscreen = 1

# ABI dan API Target
android.archs = armeabi-v7a,arm64-v8a,x86,x86_64
android.api = 34
android.minapi = 21
android.ndk = 25b
android.sdk = 34
android.ndk_path = .buildozer/android/platform/android-ndk-r25b

[buildozer]
log_level = 2
warn_on_root = 1
