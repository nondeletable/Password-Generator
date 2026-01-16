# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['password_gen\\ui\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('password_gen/assets/fonts', 'password_gen/assets/fonts'), ('password_gen/assets/images', 'password_gen/assets/images')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='PasswordGenerator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version='C:\\Users\\ADMINI~1\\AppData\\Local\\Temp\\6f4cabe4-8a9a-4757-ad1a-de4209df00e3',
    icon=['password_gen\\assets\\images\\password_icon.ico'],
)
