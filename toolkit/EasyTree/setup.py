from distutils.core import setup
import py2exe

# usage: python setup.py py2exe

options = {"py2exe":{"compressed": 1,
                    "optimize": 2,
                    "bundle_files": 2
                    }}

setup(windows=['EasyTree.py'],
    #options=options,
    zipfile=None)
