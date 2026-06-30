[app]
title = Rezistivite PRO
package.name = rezistivite
package.domain = com.defineci
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3, kivy==2.3.0
orientation = portrait
fullscreen = 1
android.permissions = BLUETOOTH, BLUETOOTH_ADMIN, ACCESS_FINE_LOCATION, WRITE_EXTERNAL_STORAGE
android.api = 33
android.ndk = 25b
android.minapi = 21
android.archs = arm64-v8a
p4a.bootstrap = sdl2
log_level = 2
warn_on_root = 1

[buildozer]
log_level = 2
warn_on_root = 1
