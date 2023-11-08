from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.13'
DESCRIPTION = 'LamaForge Encrypted Password Manager'
LONG_DESCRIPTION = 'A package that allows you to store encrypted data locally.'

# Setting up
setup(
    name="LFPWM",
    version=VERSION,
    author="LamaForge (Jadon Lama)",
    author_email="<lamaforgecode@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['sqlite3', 'bcrypt'],
    keywords=['python', 'encryption', 'data', 'password manager', 'user auth'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
