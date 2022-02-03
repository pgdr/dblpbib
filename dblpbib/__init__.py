import sys
from requests import get  # to make GET request
from datetime import datetime as dt

URL_B = "http://dblp.org/search/publ/api?"
URL_Q = "q=author:{author}:&format={extension}&h={hits}&f={first}"
URL = URL_B + URL_Q
DEBUG = False


def _get_url(author=None, extension="bib", hits=100, first=0):
    if not author:
        raise ValueError("Provide author")
    return URL.format(
        author=author, extension=extension, hits=hits, first=first
    )


def download(author, file_name):
    first = 0
    hits = 100
    with open(file_name, "wb") as fout:
        while first < 3000:  # HARD UPPER LIMIT to save dblp
            url = _get_url(author=author, first=first, hits=hits)
            if DEBUG:
                print(f"wget {url}")
            response = get(url)
            first += hits
            if response.status_code == 200 and response.content:
                fout.write(response.content)
            else:
                break


def process(name):
    slug = "".join(list(filter(str.isalnum, name.strip()))).lower()
    now = dt.now().strftime("%Y-%m-%d")
    fname = f"{slug}-{now}.bib"
    download(name, fname)
    print(f"Wrote {fname}")


def _exit_with_usage(code=1):
    print("Usage: dblpbib Firstname [Middlename] Lastname")
    sys.exit(code)


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        _exit_with_usage(code=0)
    if len(sys.argv) < 2:
        _exit_with_usage()
    process(" ".join(sys.argv[1:]))


if __name__ == "__main__":
    main()
