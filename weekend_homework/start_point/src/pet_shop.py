# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash
    return pet_shop["admin"]["total_cash"]

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pets_sold):
    pet_shop["admin"]["pets_sold"] += pets_sold
    return pet_shop["admin"]["pets_sold"]


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    found = []
    

    for pet in pet_shop["pets"]:

        if pet["breed"] == breed:
             found.append(pet)
    



    return found
    

def find_pet_by_name(pet_shop, pet_name):


    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet


def remove_pet_by_name(pet_shop, pet_name):

    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)

    return pet_shop["pets"]


def add_pet_to_stock(pet_shop, new_pet):

    pet_shop["pets"].append(new_pet)
    return len(pet_shop["pets"])




def get_customer_cash(customer):

    return customer["cash"]

     
        

def remove_customer_cash(customer, cost):
    
    customer["cash"] -= cost
    return customer["cash"]


        



def get_customer_pet_count(customer):
    pet_count = 0

    
    pet_count += len(customer["pets"])

    return pet_count




def add_pet_to_customer(customer, new_pet):
    
    customer["pets"].append(new_pet)
    # return len(customers["pets"])

    # return pet_count
    
    get_customer_pet_count(customer)

def customer_can_afford_pet(customer, new_pet):
    
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False




def sell_pet_to_customer(pet_shop, pet_name, customer):
    pets_sold = 1
    cost = 900


    
    find_pet_by_name(pet_shop, pet_name)
    add_pet_to_customer(customer, pet_name)
    get_customer_pet_count(customer)
    increase_pets_sold(pet_shop, pets_sold)
    get_pets_sold(pet_shop)
    remove_customer_cash(customer, cost)
    get_customer_cash(customer)
    add_or_remove_cash(pet_shop, cost)
    get_total_cash(pet_shop)







