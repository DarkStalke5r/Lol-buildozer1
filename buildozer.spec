[app]
title = BuildozerTest
package.name = buildozertest
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Явно задаем hostpython3 той же версии, чтобы p4a не качал 3.14
requirements = python3==3.11.0, hostpython3==3.11.0, kivy

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.accept_sdk_license = True

# Фиксируем версию python-for-android на стабильном релизе
p4a.version = v2024.01.21
