import requests
import json


def shorten_url(url):
    post_url = 'https://www.googleapis.com/urlshortener/v1/url?key={AIzaSyDQu0-T6fIRKzHhlJWlntp1ZF25AwLz8N4}'
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(post_url, data=json.dumps(payload), headers=headers)
    print r.text

