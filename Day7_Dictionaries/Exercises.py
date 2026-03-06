# create a dictionary with your name, age, and city and print it out
my_info =  {"name": "Tsion", "age": 22, "city": "Adiss Ababa"}
print(my_info)
#acess the value of age and print it out
print(my_info["age"])
# add a new key-value pair for ur favorite color and print the updated dictionary
my_info["favorite_color"]= "blue"
print(my_info)
# update the value of favorite color with ur new favorite color and print out the updated dictionary
my_info["favorite_color"] = "pink"
print(my_info)
# remove a key from input
my_info.pop(input("enter a key to remove"))
print(my_info)
# loop through your dictionary and print all keys and values.
for key, value in my_info.items():
    print(key, "->", value)
# create a dictionary with 3 students and their scores and print all students who score above 85
scores = {
    "Abel": 80,
    "Hana": 90,
    "Meron": 85
}
found_above_85 = False

for student, score in scores.items():
    if score > 85:
        print(f"{student}: {score}")
        found_above_85 = True

if not found_above_85:
    print("no one scored above 85")

#create a dictionary with 3 subjects and their scores then print out the total marks
marks = {
    "math": 80,
    "physics": 75,
    "programming": 90
}

total = sum([score for score in marks.values()])
print(f"Total marks: {total}")