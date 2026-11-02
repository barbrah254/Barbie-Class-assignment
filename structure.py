# List data structure
# mutable/ changable
# has indexed


products=["Bread","milk","sugar","blue band"]
print( f"My products {products}")

products[0]="cake"
print(f"My products {products}")

products.pop()
print(f"My products {products}")




# used on item that dont change

# location[]


# set data structure
# removes duplicates
mystock={"hp","lenovo","dell","hp"}
print(mystock)


dictionary data structure
customer={
    "name":"Barbra",
    "age": 24,
    "city":"Nairobi",
    "profession":"student",
}
print (f"name: {customer['name']}")

store product and their prices
shop={
    "bread":130,
    "milk":100,
    "sugar":200,
    "blue band":120
}
for product ,price in shop.items():
    print(product,"cost ksh", price)
          print ("milk costs ksh", shop["milk"])
    imagine you are building a school system that calculate the average mark of  a student

 marks=[76,83,67,90,79]
total=0
for mark in marks:
    total=total+mark
average=total/len(marks)
print("Total Marks :{total}")
print("Average Marks :{average}")

 create a complex
# calculate using inputput output and loops
