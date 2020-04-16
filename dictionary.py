import json
from difflib import get_close_matches
data=json.load(open('original.json'))

def translate(word):
    word=word.lower()
    if(word in data):
        return(data[word])
    elif(word.title() in data):
        return(data[word.title()])
    elif(word.upper() in data):
        return(data[word.upper()])
    elif(len(get_close_matches(word,data))>0):
        print("Did you mean %s"%get_close_matches(word,data.keys())[0])
        x=input("Enter y for YES and n for NO")
        if(x=='y'):
            return(data[get_close_matches(word,data.keys())[0]])
        else:
            return("You enter wrong word")
    else:
        return("Enter wrong word bro")

word=input()
result=translate(word)
if(type(result)==list):
    for i in result:
        print(i)
else:
    print(result)
