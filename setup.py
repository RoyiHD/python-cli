from setuptools import find_packages, setup


setup(
    name = "Cli Tutorial",
    description = "Tutorial on writing python cli",
    packages = find_packages(exclude=["*.tests"]),
    include_packages_data = True,
    install_requires = [
        "click==8.1.7"
    ]    
)