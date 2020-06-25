import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-HareeshpkgVersion", # Replace with your own username
    version="0.0.1",
    author="hareesh",
    author_email="hareesh787878@gmail.com",
    description="A small example package and uploading into the test pypi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hareesh77/hareesh77",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)