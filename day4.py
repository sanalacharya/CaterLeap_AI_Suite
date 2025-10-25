#step 3 condietionals

# Task 1
# Program to demonstrate simple if-else condition

rating = 9  # Movie rating value
# If the rating is greater than 8, print "Must watch!"
if rating > 8:
    print("Must watch!")
# Otherwise, print "Could be better"
else:
    print("Could be better")

# Step 3 - Task 2
# Program to classify movie rating using if-elif-else

rating = 6  # Example rating

if rating > 8:
    print("Blockbuster Hit!")  # print if rating > 8
elif rating >= 5:
    print("Average") 

    print("Flop")  


# Step 3 - Task 3
# Program to take rating from user and classify the movie

# ex for float datatype
rating = float(input("Enter movie rating (0-10): "))

# Checking rating range
if rating > 8:
    print("Blockbuster Hit!")
elif rating >= 5:
    print("Average Movie")
else:
    print("Flop Show")

# Step 3 - Task 4
# Program to show nested if conditions

age = int(input("Enter your age: "))

if age >= 18:
    # Inner condition executes only if age is 18 or more
    print("You are eligible to watch adult movies.")
    rating = float(input("Enter movie rating: "))

    if rating > 8:
        print("Blockbuster Hit!")
    else:
        print("Average Watch.")
else:
    
    print("You can only watch U/A rated movies.")



# Step 3 - Task 5
# A small Movie Suggestion Bot using conditional statements

# Asking user for movie name and rating
movie = input("Enter your favorite movie: ")
rating = float(input("Enter its rating (0-10): "))

# Conditional logic to categorize movie
if rating > 8:
    print(f"{movie} is a Blockbuster Hit! ")
elif 5 <= rating <= 8:
    print(f"{movie} is an Average entertainer ")
else:
    print(f"{movie} is a Flop. Better luck next time ")
