#dictionnary and set = non ordonné, unlike str/list

users = {"sylvain": "azerty", "john": "0000"}

users["sylvain"] = "AZERTY"         #met à jour la valeur de la clé "sylvain"

users["alice"] = "1234"                #créer la paire "alice": "1234"

print(users)

for user in users:                  #user = key
    print(user)                     #print only keys

values = [2,4,6]
for index, value in enumerate(values, start=1):             #by default start = 0
    print(f"indice: {index}, value : {value}")

for value in users.values():            # or   values = list(users.values)
    print(value)
for key in users.keys():     #same as    keys = list(users)
    print(key)

for key, value in users.items():
    print(f"key : {key}, value: {value}" )

users.setdefault("joe")             #add key without value
print(users)

#find a value if it exists
print(users.get("jean", "A"))               #jean is not in the dictionnary -> it prints "A"
print(users.get("sylvain", "A"))            #sylvain is in the dictionnary -> it prints its value