#!/usr/bin/env python3

import setuptools

with open("README.md",'r') as f:
    long_description = f.read()

setuptools.setup(
        name="dango",
        version="0.1.0",
        author="gsobell",
        author_email="@gsobell",
        description="a terminal based Go board written in python",
        # long_description=long_description,
        # long_description_content_type="text/markdown",
        url='https://github.com/gsobell/dango',
        packages=setuptools.find_packages(),
        # py_modules=['dango'],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GPL License",
            "Operating System :: OS Independent",
            ],
        python_requires='>=3',
    )
