
customers = [
            {
                "name": "Alice",
                "pets": [],
                "cash": 1000
            },
            {
                "name": "Bob",
                "pets": [],
                "cash": 50
            },
            {
                "name": "Jack",
                "pets": [],
                "cash": 100
            }
        ]

new_pet = {
            "name": "Bors the Younger",
            "pet_type": "cat",
            "breed": "Cornish Rex",
            "price": 100
        }

cc_pet_shop = {
            "pets": [
                {
                    "name": "Sir Percy",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "King Bagdemagus",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "Sir Lancelot",
                    "pet_type": "dog",
                    "breed": "Pomsky",
                    "price": 1000,
                },
                {
                    "name": "Arthur",
                    "pet_type": "dog",
                    "breed": "Husky",
                    "price": 900,
                },
                {
                    "name": "Tristan",
                    "pet_type": "cat",
                    "breed": "Basset Hound",
                    "price": 800,
                },
                {
                    "name": "Merlin",
                    "pet_type": "cat",
                    "breed": "Egyptian Mau",
                    "price": 1500,
                }
            ],
            "admin": {
                "total_cash": 1000,
                "pets_sold": 0,
            },
            "name": "Camelot of Pets"
        }

# def get_pets_by_breed(pet_shop, breed):
#     found = []

#     for pet in pet_shop["pets"]:
        
#         if pet["breed"] == breed:
#             found.append(pet)
        
#     print(found)
#     print(len(found))

# get_pets_by_breed(cc_pet_shop, "British Shorthair")




# list = [1, 2, 3, 2]
# found = []
# for num in list:
#     if num == 2:
#         found.append(num)

# print(found)
# print(len(found))
def get_customer_pet_count(customers1):

    pet_count = 0

    for customer in customers1:
        pet_count += len(customers["pets"])

    return pet_count

    

def add_pet_to_customer(new_pet1, customers1):
    pet_count = 0

    for customer in customers1:
        customer["pets"].append(new_pet1)
        print(len(customer["pets"]))
        pet_count += len(customer["pets"])
    
    print(pet_count)
    # print(customers1)

add_pet_to_customer(new_pet, customers)

# add_pet_to_customer(new_pet, customers)


    
# def get_customer_index_by_name(customer_name, customers1):

    

# # print(get_customer_index_by_name("Bob", customers))
   



