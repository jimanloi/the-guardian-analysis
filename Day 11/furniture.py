from multiprocessing.pool import worker


class Furniture:
    def __init__(self, materials: list[str], number_leg:int, height:float, width: float, depth:float, price):
        self.materials = materials
        self.number_leg = number_leg
        self.height = height
        self.width = width
        self.depth = depth
        self.name = None
        self.price = price
        self.color = None

    def get_size(self):
        return (f"{self.height}cm x {self.width}cm x {self.depth}cm")

    def get_surface(self):
        return self.height*self.width+self.width*self.depth+self.height*self.depth

    def get_volume(self):
        return self.height*self.width*self.depth

    def get_materials(self):
        return (" and ".join(self.materials))

    def get_price_tag(self):
        return (f"{self.name} {self.price}")

    def sample_message(self):
        return (f"The {self.name} is made of {self.get_materials()}. The size is {self.get_size()}. Each item costs {self.price}€.")

    def fits_into(self, another_furniture):
        if not isinstance(another_furniture, Furniture):
            raise TypeError
        if  self.height > another_furniture.height or self.width > another_furniture.width or self.depth > another_furniture.depth:
            return self.name+" does not fit into "+another_furniture.name+"."
        else:
            return  self.name+" fits into "+another_furniture.name+"."


class Table(Furniture):
    def __init__(self, materials, number_leg, height, width, depth, price):
        super().__init__(materials, number_leg, height, width, depth, price)
        self.name = "table"

class IkeaTable(Furniture):
    def __init__(self, color):
        super().__init__(['wood'], 4, 40, 40, 40,24.99)
        self.name = "IKEA Lack Side Table"

class Wardrobe(Furniture):
    def __init__(self, materials, number_leg, height, width, depth, number_door=2, price=0.0 ):
        super().__init__(materials, number_leg, height, width, depth, price)
        self.number_door = number_door
        self.name = "wardrobe"

class Stool(Furniture):
    def __init__(self, materials, number_leg, height, width, depth, price):
        super().__init__(materials, number_leg, height, width, depth, price)
        self.name = "stool"

if __name__ == "__main__":
    table1 = Table(["wood"], 4, 45.0, 30.0, 20.0,55.99)
    table1.name = "ABC table"
    print("table 1 size : " + table1.get_size())
    print(f"Materials of table 1 : {table1.get_materials()}")

    wardrobe1 = Wardrobe(["wood","metal"],4,85.0,60.0,35.0, 4, 80.0)
    wardrobe1.name = "big wardrobe XXL"
    print("wardrobe 1 size : "+wardrobe1.get_size())
    print(f"wardrobe 1 surface : {wardrobe1.get_surface()}cm\u00B2")
    print(f"wardrobe 1 volume : {wardrobe1.get_volume()}cm\u00B3")
    print(f"Materials of wardrobe 1 : {wardrobe1.get_materials()}")

    ikeatable1 = IkeaTable("black")
    print(ikeatable1.get_price_tag(),"€")

    print(table1.sample_message())

    print(table1.fits_into(wardrobe1))
    print(ikeatable1.fits_into(table1))