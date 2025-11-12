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
    def __init__(self, name, weight, durability, reach, damage, speed):
        self.name = name
        self.weight = weight
        self.durability = durability
        self.reach = reach
        self.damage = damage
        self.speed = speed

    def use(self):
        print("you use " + self.name)


class block:
    def __init__(self, name, weight, hardness, burnable, gravity, transparent):
        self.name = name
        self.weight = weight
        self.hardness = hardness
        self.burnable = burnable
        self.gravity = gravity
        self.transparent = transparent

    def interact(self):
        print("you interact with " + self.name)
    
if __name__ == "__main__":
    inventory = inventory()
    inventory.add_item(item("sword", 10, 120, 5, 25, 1.2))
    inventory.add_item(item("shield", 15, 105, 0, 0, 0.8))
    inventory.add_item(item("bow", 8, 80, 15, 15, 1.5))
    inventory.add_item(item("dagger", 5, 60, 3, 10, 2.0))
    inventory.add_block(block("stone", 20, 150, False, False, False))
    inventory.add_block(block("wood", 10, 50, True, False, False))
    inventory.add_block(block("glass", 5, 30, False, False, True))
    inventory.add_block(block("sand", 8, 20, False, True, False))
    for item in inventory.get_contents():
        print(f"Item: {item.name}, Weight: {item.weight}, Durability: {item.durability}, Reach: {item.reach}, Damage: {item.damage}, Speed: {item.speed}")
    for block in inventory.get_contents():
        print(f"Block: {block.name}, Weight: {block.weight}, Hardness: {block.hardness}, Burnable: {block.burnable}, Gravity: {block.gravity}, Transparent: {block.transparent}")