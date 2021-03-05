import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(w):
    w=w.lower()     # lowercases all characters.
    if w in data:   #simply checks if input key is present or not returns its value.
        return data[w]
    elif w.title() in data: #for proper noun cases eg Delhi,Texas
        return data[w.title()]  
    elif w.upper() in data: #for acronyms cases eg USA,NASA, NATO
        return data[w.upper()]       
    elif len(get_close_matches(w,data.keys())) > 0:  #recommends the best match.
        yn=input("Did you mean %s instead? Enter Y if yes , or N if no: " % get_close_matches(w, data.keys())[0] )
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word dosen't exist. Please double check it."    

word =input("Enter a word : ")

output=translate(word) #formating output
if type(output)==list:
    for item in output:
        print(item)
else:    
    print(output)