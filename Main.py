import requests

r = requests.get('http://www.google.com')

print(r.text)


bgg = requests.get('https://www.boardgamegeek.com/xmlapi2/')
