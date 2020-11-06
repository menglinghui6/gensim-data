import requests
obj = requests.get('http://api.conceptnet.io/c/en').json()

print(obj)