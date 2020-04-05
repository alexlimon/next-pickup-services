import requests
import json
from urllib.error import HTTPError

session = requests.Session()

session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
session.headers['Accept'] = "*/*"
session.headers['Accept-Encoding'] = "gzip, deflate, br"
session.headers['Connection'] = "keep-alive"
session.headers['Content-Type'] = "application/json"

def get(url):
    response = session.get(url)
    
    return json.loads(response.content)

def post(url, payload):
    response = session.post(url, payload)

    if(not response.ok):
        raise HTTPError(url, response.status_code, response.content, response.headers, None)

    return json.loads(response.content)

