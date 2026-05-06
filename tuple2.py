Dictionary_Name={} #symbol method
print(Dictionary_Name)
print(type(Dictionary_Name))
Dictionary_Name=dict()#dict constructor method
print(Dictionary_Name)
print(type(Dictionary_Name))
phone_book={
                'ramya':'1234568790',
                'sathish':'9325698789',
                'prudhvi':'6326598752'
           }
print ("phone number:",phone_book['ramya'])
print ("phone number:",phone_book['sathish'])
phone_book=dict(
                ramya='1234568790',
                sathish='9325698789',
                prudhvi='6326598752'
           )
print ("phone number:",phone_book['ramya'])
print ("phone number:",phone_book['sathish'])
words = {}
words["Hello"] = "Bonjour"
words["Yes"] = "Oui"
words["No"] = "Non"
words["Bye"] = "Au Revoir"
print(words)
for key in words:  
         print(key," is :",words[key])
print("Keys are:",phone_book.keys())
print("Keys are:",words.keys())
print("Values are:",phone_book.values())
print("Values are:",words.values())
print( "tuples are:",phone_book.items())
print ("value:",phone_book.get('ramya'))
print ("value:",phone_book.pop('ramya'))
print(phone_book)
copy_phone_book=phone_book.copy()
print(copy_phone_book)
for key, value in phone_book.items():
    print(f"{key}: {value}")
