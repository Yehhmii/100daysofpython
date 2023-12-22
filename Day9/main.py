#Dictionary and Nesting in python

python_dictionary = {
    "key": "value",
    "new_item": "new item value or text",
    "Bug": "An error in aprogram that prevents the program from running as expected.",
}

# To retrive items from a dictionary 
python_dictionary["key"]

# Adding new items to a dictionary
python_dictionary["added"] = "This is the new item added to our dictionary." 

# creating an empty dictionary 
new_emptyDic = {}

# editing an item in a python dictionary
python_dictionary["new_item"] = "This item will be changed to what is here"

# Loop through a dictionary 
for key in python_dictionary:
    print(key) # which will get us only the key name
    print(python_dictionary[key]) # which then gets us the value 



# ============================================================================
# Nesting in python 
states = {
    "Edo": "Benin",
    "Aduja": "FCT",
}

# Nesting a list in a dictionary 
states_traved = {
    "Edo": ["Ring-Road", "Round", "Iguweben"],
    "Abuja": ["Kurudu", "Jabi", "Gwarinpa"],
}

# Nesting dictionay in dictionary 
states_traved_andtime = {
    "Edo": {"cities": ["Ring-Road", "Round", "Iguweben"], "number_visited": 3},
    "Abuja": {"cities_visited": ["Kurudu", "Jabi", "Gwarinpa"], "number": 43}
}

# Nesting dictionary  in a list
traved = [
    {
        "state": "Edo", 
        "cities": ["Ring-Road", "Round", "Iguweben"], 
        "number": 3
    },
    {
        "state": "Abuja", 
        "cities": ["Kurudu", "Jabi", "Gwarinpa"], 
        "number": 43
    },
]