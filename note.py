my_english_dict = {}

def add_to_dict(key, item, defi=None):
    if(type(key) != dict):
        print("You need to send a dictionary. You sent:", type(key))
    elif(defi == None):
        print("You need to send a word and a definition")
    elif(item in key):
        print(f"{item} is already on the dictionary. Won't add.")
    else:
        my_english_dict[f"{item}"] = defi
        print(f"{item} has been added.")


add_to_dict(my_english_dict, "kimchi", "asd")
print(my_english_dict)
print(my_english_dict["kimchi"])