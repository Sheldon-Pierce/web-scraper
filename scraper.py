import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/History_of_Spain"

req = requests.get(url)

markup = req.text

soup = BeautifulSoup(markup, 'html.parser')


def get_citations_needed_count(url_string):
    count = 0
    for citations in soup.find_all('span'):
        if "citation needed" in citations:
            count += 1
    print(count)


def get_citations_needed_report(url_string):
    for citations in soup.find_all('li'):
        if "citation needed" in citations.text:
            print(citations.text)


if __name__ == '__main__':
    get_citations_needed_count(url)
    get_citations_needed_report(url)
