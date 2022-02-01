from setuptools import setup
setup(
    version="0.0.1",
    name="dblpbib",
    packages=["dblpbib"],
    descriptiong="get a bib file",
    author="PG Drange",
    author_email="Pal.Drange@uib.no",
    entry_points = {
        'console_scripts': [
            'dblpbib = dblpbib:main',
        ],
    },
    install_requires=["requests"],
)
