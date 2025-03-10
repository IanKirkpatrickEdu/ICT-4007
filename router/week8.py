################################################################################
# 1. Get warmed up by trying out some of the simple examples from the textbook.
################################################################################

# 8.1 Create a list called years_list, starting with the year of your birth, and each year thereafter until the year of your fifth birthday. For example, if you were born in 1980, the list would be years_list = [1980, 1981, 1982, 1983, 1984, 1985]. If you’re less than five years old and reading this book, I don’t know what to tell you.

birth_year = 1995
years_list = [birth_year + i for i in range(6)]
print("Years: ", years_list)

# 8.2 In which year in years_list was your third birthday? Remember, you were 0 years of age for your first year.

print("My 3rd birthday was in the year: ", years_list[3])

# 8.3 In which year in years_list were you the oldest?

print("The last year in my years_list is: ", years_list[-1])

# 8.4 Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".

things = ["mozzarella", "cinderella", "salmonella"]
print("Things start: ", things)

# 8.5 Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?

things[1] = things[1].title()
print("Things after person change: ", things) # yes it did change (mutable)

# 8.6 Make the cheesy element of things all uppercase and then print the list.

things[0] = things[0].upper()
print("Things after cheesy change: ", things)

# 8.7 Delete the disease element from things, collect your Nobel Prize, and print the list.

del things[-1]
print("Things after removing disease: ", things)

# 8.8 Create a list called surprise with the elements "Groucho", "Chico", and "Harpo".

surprise = ["Groucho", "Chico", "Harpo"]
print("Surprise start: ", surprise)

# 8.9 Lowercase the last element of the surprise list, reverse it, and then capitalize it.

surprise[-1] = surprise[-1].lower()[::-1].title()
print("Surprise updated: ", surprise)

# 7.10 Use a list comprehension to make a list called even of the even numbers in range(10).

even_numbers = [n for n in range(10) if n % 2 == 0]
print("Even Numbers: ", even_numbers)

# 8.11 Let’s create a jump rope rhyme maker. You’ll print a series of two-line rhymes. Start with this program fragment:

start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
    ]
start2 = "Someone better"

# For each tuple (first, second) in rhymes:
for first, second in rhymes:
#    For the first line:
#       Print each string in start1, capitalized and followed by an exclamation point and a space.
    line1_a = "".join([f"{s.title()}! " for s in start1])
#       Print first, also capitalized and followed by an exclamation point.
    line1_b = f"{first.title()}!"
    print(f"{line1_a}{line1_b}")

#    For the second line:
#       Print start2 and a space.
#       Print second and a period.
    line2 = f"{start2} {second}."
    print(line2)

    
################################################################################
# 2. Create a tuple and save it to a variable of your choice and output the values of the tuple to the screen.
################################################################################

fruits = (('Watermelon', '🍉'), ('Lemon', '🍋‍🟩'), ('Apple', '🍎'), ('Banana', '🍌'))
print("Available fruits: ", [f[0] for f in fruits])
print("Available fruit emojis: ", [f[1] for f in fruits])

################################################################################
# 3. Find the data type of your tuple.
################################################################################

print("The type of the fruit tuple is: ", type(fruits))
print("The type of the inner tuples is: ", type(fruits[0]))

################################################################################
# 4. Create a list and save it to a variable of your choice and output the values of the list to the screen.
################################################################################

chess_pieces = ["♛", "♞", "♚", "♔", "♜", "♕", "♘", "♙", "♖", "♝", "♗"]
print("Chess pieces: ", chess_pieces)

################################################################################
# 5. Find the data type of your list.
################################################################################

print("The type of the chess pieces array is: ", type(chess_pieces))
print("The type of the chess pieces themselves is: ", type(chess_pieces[0]))

################################################################################
# 6. Compare your two variables to see if they are equal to each other.
#      well im assuming that I was supposed to make the same thing so
################################################################################

fruit_tuple = ('🍉', '🍋‍🟩', '🍎', '🍌')
fruit_list = ['🍉', '🍋‍🟩', '🍎', '🍌']
print("Are they equal? -> ", fruit_tuple == fruit_list)
print("Are all values equal? -> ", len(fruit_tuple) == len(fruit_list) and all(a == b for a, b in zip(fruit_tuple, fruit_list)))

################################################################################
# 7. Iterate through your list and output the results to the screen.
################################################################################

for piece in chess_pieces:
    print("Chess Piece: ", piece)

################################################################################
# 8. Use the list() function to convert your tuple to a list and then also output the items to the screen as a list.
################################################################################

for fruit in list(fruits):
    print(f"Fruit {fruit[0]} has an emoji {fruit[1]}")
