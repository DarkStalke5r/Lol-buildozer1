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
# Синхронизируем python3 и hostpython3, чтобы p4a не качал недопустимую версию 3.14
requirements = python3==3.11.0, hostpython3==3.11.0, kivy

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# permissions = INTERNET

# (list) List of service to declare
# services = Name:service.py

# (list) Architectural target
android.archs = arm64-v8a

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

# (str) Extra arguments to pass to python-for-android
# Принудительно задаем версию hostpython для тулчейна
p4a.extra_args = --hostpython=3.11.0

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = error, 1 = info)
warn_on_root = 1
