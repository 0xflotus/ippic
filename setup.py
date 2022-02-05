import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="ippic",
    version="0.0.1",
    description="Create an image from an IP address",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/0xflotus/ippic",
    author="0xflotus",
    author_email="0xflotus+pypi@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["ippic"],
    include_package_data=True,
    install_requires=["argparse", "netaddr", "Pillow"],
    tests_require=["pytest"],
    entry_points={"console_scripts": ["ippic=ippic.__main__:main"]},
)
