# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
setup(
    name='math-utils',
    version='0.1.0',
    packages=find_packages(where = "src"),
    package_dir={"": "src"},
    install_requires=[],
    description='A collection of mathematical utilities',
    author='Pavel Pikuza',
    author_email='pavlo.pikuza@gmail.com',
    url='https://github.com/pavel-pikuza/math-utils',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
