from setuptools import setup
setup(
    version="0.0.2",
    name="dblpbib",
    packages=["dblpbib"],
    description="Download all bibtex references for provided author",
    author="PG Drange",
    author_email="Pal.Drange@uib.no",
    entry_points = {
        'console_scripts': [
            'dblpbib = dblpbib:main',
        ],
    },
    install_requires=["requests"],
)
