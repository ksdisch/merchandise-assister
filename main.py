# TODO: Make list of all our products
beer_dict = {
    "Stone": {
        "Location": "California",
        "Products We Carry": ["IPA; 6pk btls", "Variety Pack; 12pk cans"],

    },

    "Brewery": {
        "Location": "",
        "Products We Carry": [],
        
    },
}



# TODO: Create a new store to track
# Binny's as example

# TODO: Create dictionaries for products of the store that are in coolers, on warm shelves, stacks, display, in backstock, etc.
#   Track the amount of each product in each location 
cooler_products = {"IPA; 6pk btls": 3, }
warm_shelf_products = {"IPA; 6pk btls": 2, "Variety Pack; 12pk cans": 3}
stacked_products = {}
backstock_products = {}

# Dictionary to track store stock and other information
new_store = {
    "Coolers": cooler_products,
    "Warm Shelves": warm_shelf_products,
    "Stacks": stacked_products,
    "Backstock": backstock_products
}
# print(new_store.items())

# TODO: Show/report the amount of each product in each location 
for key, value in new_store.items():
    print(key, '->', value)
    location = value
    for key, value in location.items():
        print (key, '->', value)
    # print(item.)

# TODO: Write function to increment or decrement a given product based on user input



# TODO: 


# TODO: 


# TODO: 



# TODO: 


# TODO: 


# TODO: 
