# GRANDFATHER
class Product:
    def __init__(self, unit_num, color, name, count):
        self.unit_num = unit_num
        self.color = color
        self.name = name
        self.count = count

    # not sure if this should be here on in cart.py
    def UpdateCount(self, item, quantityBought):
        if quantityBought <= item.count:
            item.count = item.count - quantityBought
            print(f"The updated count for {item.name} is {item.count}")
        else:
            print("Cannot exceed stock limit")
    # place checks here for item count
    def AddToCart(self, item, quantityBought):
        pass
         
# FATHER
class Shoes(Product):
    shoes = [] 
    def __init__(self, unit_num, color, showSize,name,count):
        super().__init__(unit_num, color, name,count)
        self.showSize = showSize
        Shoes.shoes.append(self) 
# CHILDREN       
class Formals(Shoes):
   
    def __init__(self, unit_num, color, showSize, name, count):
        super().__init__(unit_num, color, showSize,name,count)
        
class Joggers(Shoes):
    def __init__(self, unit_num, color, showSize, name, suited_env, count):
        super().__init__(unit_num, color, showSize,name, count)
        self.suited_env = suited_env

class Sneakers(Shoes):
    def __init__(self, unit_num, color, showSize, name, count):
        super().__init__(unit_num, color, showSize,name,count)


# FATHER
class Jewelry(Product):
    jewelry = []
    def __init__(self, unit_num, color, name, material, weight,count):
        super().__init__(unit_num, color, name,count)
        self.material = material
        self.weight = weight
        Jewelry.jewelry.append(self)
# CHILDREN     
class Bracelet(Jewelry):
    def __init__(self, unit_num, color, name, material, weight, wrist_size, count):
        super().__init__(unit_num, color, name, material, weight,count)
        self.wrist_size = wrist_size

class Earings(Jewelry):
    def __init__(self, unit_num, color, name, material, weight, earing_length, count):
        super().__init__(unit_num, color, name, material, weight, count)
        self.earing_length = earing_length

class Necklace(Jewelry):
    def __init__(self, unit_num, color, name, material, weight, neck_size,count):
        super().__init__(unit_num, color, name, material, weight, count)
        self.neck_size = neck_size


# FATHER
class Clothes(Product):
    clothes = []
    def __init__(self, unit_num, color, name, count):
        super().__init__(unit_num, color, name, count)
        Clothes.clothes.append(self)
# CHILDREN     
class Pants(Clothes):
    def __init__(self, unit_num, color, name, waist, pant_length,count):
        super().__init__(unit_num, color, name, count)
        self.waist = waist
        self.pant_length = pant_length

class Shirts(Clothes):
    def __init__(self, unit_num, color, name, size,count ):
        super().__init__(unit_num, color, name, count)
        self.size = size

class Hoodies(Clothes):
    def __init__(self, unit_num, color, name, size, count):
        super().__init__(unit_num, color, name, count)
        self.size = size






# Creating instances and adding to the all_products list
Joggers(1, "Red", 45, "Nike", "Basketball",10)
Joggers(2, "Yellow", 42, "Adidas", "Running",10)

Sneakers(3, "Black", 40.6, "Jordans",10)
Sneakers(4, "Brown", 41.5, "Yeezeys",10)

Earings(1, "White", "low hanging", "Gold", 1.5, 2,10)
Necklace(2, "Gold", "high hanging", "Silver", 2.5,22.5,10)
Bracelet(3, "Gold", "Round ", "Daimond", 1.5, 8,10)






for jewelry in Jewelry.jewelry:
    print(vars(jewelry))
    