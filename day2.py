#Lists and dictioneries
#Lists!!!
#Task1

# Creating a list of Indian movies
indian_movies = ["Kanthara 2", "RRR", "KGF"]
print(f"My movie list:, {indian_movies}")

#Task2
# Accessing the second movie
print(f"Second movie:, {indian_movies[1]}")

# Add a new movie to the list
indian_movies.append("Lucifer")
print("After adding new movie:", indian_movies)

# Remove the first movie
indian_movies.remove("Kanthara 2")
print("After removing first movie:", indian_movies)

#Task3

print("\nList of Indian movies:")
for movie in indian_movies:
    print(movie)


