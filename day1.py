#variable = A container for a value (str, int, float ,boolean)

#string
Movie_title="Kantara_Chapter1"
print(f"Movie Title is {Movie_title}")

#integer
tickets=3
price=300
print(f"{Movie_title} movies price for {tickets} tickets is {price*tickets}")

#float
tickets=3
price=350.75
print(f"{Movie_title} movies price for {tickets} tickets is {price*tickets}")

#Boolean
rating=9
is_blockbuster=rating >8
print(is_blockbuster)
price=300
is_expensive=price > 500
print(is_expensive)

#Movie Calculator
movie =input("Enter Movie Name: ") #string 
avl_tikt=5 #int
tickets=int(input("Enter the numbers of tickets u want: ")) #float
if tickets > avl_tikt: #if condition
    print(f"sorry !! that much tickets are not available now only {avl_tikt} are available")
else:
    price=float(input("enter the price for a ticket: "))
    print(f"the total price for {tickets} tickets to {movie} is {tickets*price}")