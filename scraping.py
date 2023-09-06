import requests
try:
    url = "http://glwec.in/glamz"
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
    response = requests.get(url,headers=headers)
    print(response.text)
except ConnectionError:
    print("EEEEEEEEEEEEEE")
