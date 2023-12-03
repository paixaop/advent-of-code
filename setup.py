from setuptools import setup, find_packages

setup(
    name="advent-of-code-solutions",
    version="0.1",
    description="Pedro Paixao's solutions for https://adventofcode.com/",
    url="https://github.com/paixaop/advent-of-code-myusername",
    author="Pedro Paixao",
    author_email="paixaop@gmail.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    install_requires=[
        "advent-of-code-data >= 2.0.1",
        # list your other requirements here, for example:
        # "numpy", "parse", "networkx",
    ],
    packages=find_packages(),
    entry_points={
        "adventofcode.user": ["paixaop = mysolutions:solve"],
    },
)
