import requests
import json


def get_lists(payload):
    api_key = get_api_key()
    payload['api-key'] = api_key
    url = 'https://api.nytimes.com/svc/books/v3/lists.json'
    response = requests.get(url, params=payload)
    return response.text


def get_api_key():
    with open('api.key') as f:
        return f.readline()


def show_books():
    api_result = get_lists({'list': 'e-book-fiction'})
    data = json.loads(api_result)
    status = data.get('status', {})
    print(status)
    # results = data.get('results', {})
    # for book in results:
    #     book_details = book.get('book_details', {})
    #     print(book_details.get('title'), {})


show_books()
