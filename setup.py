from setuptools import setup, find_packages


VERSION = "1.0.2"
DESCRIPTION = "LamaForge Encrypted Password Manager"
LONG_DESCRIPTION = "A package that allows you to store encrypted data locally."

# Setting up
setup(
    name="LFPWM",
    version=VERSION,
    author="LamaForge (Jadon Lama)",
    author_email="<lamaforgecode@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["bcrypt"],
    keywords=["python", "encryption", "data", "password manager", "user auth"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
