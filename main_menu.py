from Products.Shoes.formals import Formals
from Products.Shoes.joggers import Joggers
from product import Product


joggersObj = Joggers(1, "white", 35, "NB", "Running")
formalsObj = Formals(3, "Red", 45, "Jordans", "Basketball")

joggersObj.AddJoggers(1, "white", 35, "NB", "Running")
joggersObj.AddJoggers(2, "yellow", 31, "Nike", "gym")
formalsObj.AddFormals(3, "Red", 45, "Jordans", "Basketball")
formalsObj.AddFormals(4, "Black", 41, "Yeezys", "Party-wear")

for product in formalsObj.products:
    print(product)