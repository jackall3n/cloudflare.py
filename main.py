import cloudscraper
from flask import Flask, request
app = Flask(__name__)


def get(url):
    scraper = cloudscraper.create_scraper()
    return scraper.get(url).text


@app.route('/')
def hello():
    url = request.args.get('url')

    if not url:
        return ''

    return get(url)
