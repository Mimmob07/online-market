from tkinter import *
import ast

f = open("/Users/mimmo/black_market/orders.txt", "r")
contents = f.read()
f.close()
things = ast.literal_eval(contents)
secondthing = [things, "test"]
root = Tk()
f = Frame(root).pack()
l = Listbox(root, height=20, width=30)
b = Button(root, text = "delete selection", command = lambda: delete(l, l.curselection()))
b.pack()
l.pack()

for i, j in things.items():
    oneitem = i + ":" + j
    l.insert(END, oneitem)

def delete(listbox, index: int):
    global things
    item = listbox.get(index)
    key = item.split(":")[0]
    del things[key]
    listbox.delete(index)
    f = open("/Users/mimmo/black_market/orders.txt", "w")
    f.write(str(things))
    f.close()

root.mainloop()