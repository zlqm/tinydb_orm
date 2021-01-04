import setuptools

with open('README.rst') as f:
    long_description = f.read()


setuptools.setup(
    name='tinydb_orm',
    version='1.0.0',
    author='Abraham',
    author_email='abraham.liu@hotmail.com',
    description='Orm support for tinydb',
    install_requires=['tinydb'],
    long_description=long_description,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
