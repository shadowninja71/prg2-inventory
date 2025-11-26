import tkinter
from tkinter import *
from app import inventory, item
inventory = inventory()

main = tkinter.Tk()

inputbox = tkinter.Entry(main)

inputweight = tkinter.Entry(main)

inputdurability = tkinter.Entry(main)

inputdamage = tkinter.Entry(main)

inputbox.grid(pady = 20, row=1)
inputweight.grid(pady = 20, row=3)
inputdurability.grid(pady = 20, row=5)
inputdamage.grid(pady = 20, row=7)

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

button.grid(pady = 20)

textbox = tkinter.Text(main, height = 10, width = 50)

textbox.grid(pady = 20)

Label(main, text='Name of item').grid(row=0)
Label(main, text='weight of item').grid(row=2)
Label(main, text='durability of item').grid(row=4)
Label(main, text='damage of item').grid(row=6)


main.mainloop()