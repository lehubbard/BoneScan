import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Bonescan",
    version="0.1",
    author="Lucas Hubbard",
    author_email="lhubbar9@emich.edu",
    description="A vulnerability scanner for the BeagleBoard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/melvinofida/BoneScan",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Linux",
    ],
    install_requires=['spur', 'requests', 'signal'],

    python_requires='>=3.6',
)
