from setuptools import setup, find_packages

with open("requirements.txt") as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name="FindAtcoderRival",
    version="0.0.1",
    description="find just right rival for you in Atcoder",
    author="popper2710",
    packages=find_packages(),
    install_requires=install_requirements,
    entri_points={
        "far=src.cli:main",
    }
)
