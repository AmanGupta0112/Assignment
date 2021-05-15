import requests as r
url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"

word = input("Enter the Word : ")

new_url = url + word.lower()

re = r.get(new_url).json()

try:
    pos = re[0]['meanings'][0]['partOfSpeech']
    defi = re[0]['meanings'][0]['definitions'][0]['definition']
    new_str = f"{word}.{pos}. {defi}"    
except:
    new_str = "No Definition Found."
 
print(new_str)
        


