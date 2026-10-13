[app]

# (str) Title of your application
title = API Infinita

# (str) Package name
package.name = infinityapi

# (str) Package domain (needed for android packaging)
package.domain = org.gerardo

# (str) Source files where the let is located (relative to directory)
source.dir = .

# (list) Source files to include (let empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Version of the application
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
# (See https://python-for-android.readthedocs.io/en/latest/options.html#permissions for legal values)
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support
android.min_api = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Automatically accept SDK license
android.accept_sdk_license = True
