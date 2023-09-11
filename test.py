import urllib.request
page = urllib.request.urlopen("https://kculture.kgames.fr/?join=JntqshknU")
print(page.read())