from requests import get  # to make GET request
from datetime import datetime as dt

URL = "http://dblp.org/search/publ/api?q=author:%s:&format=bib"


def download(url, file_name):
    with open(file_name, "wb") as fout:
        response = get(url)
        fout.write(response.content)


def process(name):
    slug = ''.join(list(filter(str.isalnum, name.strip()))).lower()
    now = dt.now().strftime("%Y-%m-%d")
    fname = f"{slug}-{now}.bib"
    download(URL % name, fname)
    print(f"Wrote {fname}")


def main():

    from sys import argv

    if len(argv) < 2:
        exit("Usage: dblpbib Firstname [Middlename] Lastname")
    process(" ".join(argv[1:]))

if __name__ == "__main__":
    main()
