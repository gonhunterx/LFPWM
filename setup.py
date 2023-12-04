from setuptools import setup, find_packages


from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")


VERSION = "1.0.6"
DESCRIPTION = "LamaForge Encrypted Password Manager"
# LONG_DESCRIPTION = ""

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
    install_requires=["bcrypt", "cryptography"],
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
