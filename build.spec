# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['dependency_unified.py'],
             pathex=['C:\\Users\\dd-jy\\pythonProject\\fosslight_dependency\\unified_script'],
             binaries=[('third_party\\askalono\\askalono.exe', 'third_party\\askalono')],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='fosslight_dependency',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
