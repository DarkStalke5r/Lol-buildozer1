[app]

# (str) Title of your application
title = BuildozerTest

# (str) Package name
package.name = buildozertest

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (e.g. 0.0.1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions (раскомментируйте, если приложению нужен интернет)
# android.permissions = INTERNET

# (int) Target Android API (стандарт для современных устройств)
android.api = 33

# (int) Minimum API supported (API 24 = Android 7.0)
android.minapi = 24

# (list) Architectural target
android.archs = arm64-v8a

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = error, 1 = info)
warn_on_root = 1
