import urllib.request

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = urllib.request.urlopen(word_site)
txt = response.read().decode()
WORDS = txt.splitlines()

with open("./standard-words", "w") as file:
    file.writelines(txt)
