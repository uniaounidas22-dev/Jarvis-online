[app]
title = JARVIS V6 ONLINE
package.name = jarvisonline
package.domain = com.junior.jarvisonline
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 6.0
requirements = python3,kivy==2.3.0,requests,urllib3,certifi,charset-normalizer,idna
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,MICROPHONE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreements = True
p4a.bootstrap = sdl2
