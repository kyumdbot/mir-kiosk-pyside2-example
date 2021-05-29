import setuptools
from distutils.core import setup
import sys,os

setup(
    name = 'mir-kiosk-pyside2-example',
    version = '0.1.0',
    description = 'Mir-kiosk PySide2 example',
    license='private',
    author = 'hex',
    packages = ['src'],
    package_data={'src': ['description.txt']
                 },
    classifiers = [
        'Operating System :: POSIX ::Linux'],
    python_requires='>=3.6, <4',
    entry_points = {
        'console_scripts': [
            'mir-kiosk-pyside2-example=src.app:main']
            },
)
