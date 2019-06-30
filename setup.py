from setuptools import setup


def readme():
    with open("readme.md") as f:
        return f.read()


setup(
    name = "file-unzipper",
    version = "0.1.0",
    description = "File unzipping made easy",
    url = "https://github.com/M69k65y/file-unzipper",
    author = "M69k65y",
    license = "MIT",
    packages = ["file_unzipper"],
    zip_safe = False,
    install_requires = [
        "pillow",
        "python-magic"
    ],
    classifiers = [
        "Intended Audience :: Developers"
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    keywords = "python unzipping unzipper zipfile zip",
    long_description = readme(),
    long_description_content_type = "text/markdown"
)