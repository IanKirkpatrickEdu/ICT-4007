################################################################################
# 1. Get warmed up by trying out some of the simple examples from the textbook.
################################################################################

# 8.1 Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.
e2f = {
  "dog": "chien",
  "cat": "chat",
  "walrus": "morse",
}
print(e2f)

# 8.2 Using your three-word dictionary e2f, print the French word for walrus.

print(f"The french word for walrus is: {e2f.get("walrus")}")

# 8.3 Make a French-to-English dictionary called f2e from e2f. Use the items method.

f2e = {v: k for k, v in e2f.items()}
print(f2e)

# 8.4 Print the English equivalent of the French word chien.

print(f"The english equavelent to chien is: {f2e.get("chien")}")

# 8.5 Print the set of English words from e2f.

print(f"the english words in e2f are: {e2f.keys()}")

# 8.6 Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.

life = {
  "animals": {
    "cats": ["Henri", "Grumpy", "Lucy"],
    "octopi": {}, 
    "emus": {}, 
  },
  "plants": {}, 
  "other": {}, 
}

# 8.7 Print the top-level keys of life.

print(f"Top level keys of life: {life.keys()}")

# 8.8 Print the keys for life['animals'].

print(f"Top keys of life.animals: {life.get("animals", {}).keys()}")

# 8.9 Print the values for life['animals']['cats'].

print(f"life.animals.cats array is: {life.get("animals", {}).get("cats", None)}")

# 8.10 Use a dictionary comprehension to create the dictionary squares. Use range(10) to return the keys, and use the square of each key as its value.

squares = {x: x**2 for x in range(10)}
print(f"Squares(10): {squares}")

# 8.11 Use a set comprehension to create the set odd from the odd numbers in range(10).

odd = {x for x in range(10) if x % 2 != 0}
print(f"Odd(10): {squares}")

# 8.12 Use a generator comprehension to return the string 'Got ' and a number for the numbers in range(10). Iterate through this by using a for loop.

got_numbers = ('Got ' + str(x) for x in range(10))
for item in got_numbers:
    print(item)


# 8.13 Use zip() to make a dictionary from the key tuple ('optimist', 'pessimist', 'troll') and the values tuple ('The glass is half full', 'The glass is half empty', 'How did you get a glass?').

key_tuple = ('optimist', 'pessimist', 'troll')
value_tuple = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')

glass_dict = dict(zip(key_tuple, value_tuple))
print(glass_dict)

# 8.14 Use zip() to make a dictionary called movies that pairs these lists: titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane'] and plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']

titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']

movies = dict(zip(titles, plots))
print("Movies: ", movies)

################################################################################
# 2. Create a dictionary of your own using { }
################################################################################

my_dict = {}

################################################################################
# 3. Populate your dictionary with some personal information that is important to your daily routine at home.
################################################################################

my_dict["wake_up_time"] = "08:00 AM"
my_dict["morning_exercise"] = None
my_dict["breakfast"] = "Eggs with hot sauce"
my_dict["work_start"] = "9:00 AM"
my_dict["work_end"] = "5:00 PM"
my_dict["evening_activities"] = {
    "monday": "video games with the bois",
    "tuesday": "D&D at Copper Kettle",
    "wednesday": "school discussions are due",
    "thursday": "relaxation with tv or video games",
    "friday": "movie night with the meyers",
    "saturday": None,
    "sunday": "school assignments are due",
}
my_dict["bedtime"] = "1:00 AM"

################################################################################
# 4. Print the values of your dictionary to the screen.
################################################################################

print(f"My Dict: {my_dict}")

################################################################################
# 5. Create another dictionary using dict( ) consisting of professional information that is important to your daily routine, process, or project at work or school.
################################################################################

my_other_dict = {
    "school": {
        "databases": ["Oracle", "Microsoft SQL Server"],
        "backend": ["Python"],
        "frontend": ["JavaScript"]
    },
    "work": {
        "databases": ["PostgreSQL", "MongoDB", "Redis", "Elasticsearch", "DynamoDB"],
        "backend": ["Python", "GoLang"],
        "frontend": ["TypeScript"]
    }
}

################################################################################
# 6. Oops! You made a mistake and you didn’t even know it. Change one of your values to something else by its key.
################################################################################

my_other_dict.get("work", {}).get("backend", []).append("Java")

################################################################################
# 7. Grab an item by key and then also by get( ) and display it to the screen.
################################################################################

print(f"Backend languages at work (by keys): {my_other_dict["work"]["backend"]}")
print(f"Backend languages at work (by get()): {my_other_dict.get("work", {}).get("backend", [])}")

################################################################################
# 8. Get all keys with keys() and display it on the screen.
################################################################################

print(f"My Other Dict Keys: {my_other_dict.keys()}")
