import requests
import re

inp = open("links.txt", "r")
out = open('email_addresses.txt', 'w')

links = inp.read().replace("\n", " ")

for link in links:

url = "http://larstheyeti.tumblr.com/"
data = requests.get(url).text