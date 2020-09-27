import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="frnz",
    version="0.0.1",
    author="Alex Franz",
    author_email="a@frnz.io",
    description="A small python package for data science.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alfranz/frnz-sample",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pandas>=1.1.1",
    ],
    tests_require=["pytest>=6.1.0"],
)