import tkinter
from app import inventory, item
inventory = inventory()

main = tkinter.Tk()

label = tkinter.Label(main, text = "Hello World")

label.pack()

inputbox = tkinter.Entry(main)

inputweight = tkinter.Entry(main)

inputdurability = tkinter.Entry(main)

inputdamage = tkinter.Entry(main)

inputbox.pack(pady = 20)
inputweight.pack(pady = 20)
inputdurability.pack(pady = 20)
inputdamage.pack(pady = 20)

def log(event = None):
     for item in inventory.get_contents():
        textbox.insert(tkinter.END, item.name + str(item.weight) + str(item.durability) + str(item.damage) + "\n")

def createadd(event = None):
    itemname = inputbox.get()
    itemweight = inputweight.get()
    itemdurability = inputdurability.get()
    itemdamage = inputdamage.get()
    inventory.add_item(item(itemname, int(itemweight), int(itemdurability), int(itemdamage)))
    log()

button = tkinter.Button(main, text = "create an item", command = createadd)

button.pack(pady = 20)

textbox = tkinter.Text(main, height = 10, width = 50)

textbox.pack(pady = 20)

main.mainloop()