import json
# importing json

numbers = "NIschal"
f = open("numbers.json", "w")

json.dump(numbers,f)  # adds the data into the jason file
f.close()
print("data has been outputed")

f = open ("numbers.json", "r")
username = json.load(f) # reads the data from the file
print(username)