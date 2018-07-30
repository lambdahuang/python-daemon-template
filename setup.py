import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

    setuptools.setup(
            name="python-daemon",
            version="0.0.1",
            author="Neo Huang",
            author_email="",
            description="A template for python daemon",
            long_description=long_description,
            long_description_content_type="text/markdown",
            url="https://github.com/lambdahuang/",
            packages=setuptools.find_packages(),
            classifiers=(
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
                ),
            )
