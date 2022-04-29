from setuptools import setup

VERSION = "1.1.0"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="awsutils",
    version=VERSION,
    description="Tiny module to allow some AWS tasks over some other scripts for AWS",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="aws utils",
    url="https://github.com/danilocgsilva/AWSUtils",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["awsutils"],
    include_package_data=True
)

