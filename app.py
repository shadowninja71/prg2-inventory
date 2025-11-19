class inventory:
    def __init__(self):
        self.contents = []

    def add_item(self, item):
        self.contents.append(item)

    def add_block(self, block):
        self.contents.append(block)
    
    def get_contents(self):
        return self.contents
    
class item:
    def __init__(self, name, weight, durability, damage):
        self.name = name
        self.weight = weight
        self.durability = durability
        self.damage = damage

    def use(self):
        print("you use " + self.name)


class block:
    def __init__(self, name, weight, hardness):
        self.name = name
        self.weight = weight
        self.hardness = hardness

    def interact(self):
        print("you interact with " + self.name)
    
if __name__ == "__main__":
    inventory = inventory()
    inventory.add_item(item("sword", 10, 120, 25))
    inventory.add_item(item("shield", 15, 105, 0))
    inventory.add_item(item("bow", 8, 80, 15))
    inventory.add_item(item("dagger", 5, 60, 10))
    inventory.add_block(block("stone", 20, 150))
    inventory.add_block(block("wood", 10, 50))
    inventory.add_block(block("glass", 5, 30))
    inventory.add_block(block("sand", 8, 20))
    for obj in inventory.get_contents():
        if isinstance(obj, item):
            print(f"Name: {obj.name}, Weight: {obj.weight}, Durability: {obj.durability}, Damage: {obj.damage}")
        elif isinstance(obj, block):
            print(f"Name: {obj.name}, Weight: {obj.weight}, Hardness: {obj.hardness}")