'''
A program that store this book information

Title , Author
Year , ISBN

User can:
view all entries,
update,
add,
delete,
search,
close


'''
from tkinter import *
import backend


def get_selected_row(event):
	try:
	    global selected_tuple
	    index=list1.curselection()[0]
	    selected_tuple=list1.get(index)
	    e1.delete(0,END)
	    e1.insert(END,selected_tuple[1])
	    e2.delete(0,END)
	    e2.insert(END,selected_tuple[2])
	    e3.delete(0,END)
	    e3.insert(END,selected_tuple[3])
	    e4.delete(0,END)
	    e4.insert(END,selected_tuple[4])
	except IndexError:
		pass

	
def search_command():
	list1.delete(0,END)
	for row in backend.search(author_text.get(),title_text.get(),year_text.get(),ISBN_text.get()):
		list1.insert(END, row)


def view_command():
	list1.delete(0,END)
	for row in backend.view():
		list1.insert(END, row)

def entry_command():
	backend.insert(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get())
	list1.delete(0,END)
	list1.insert(END , (title_text.get(),author_text.get(),year_text.get(),ISBN_text.get()))

def delete_command():
	backend.delete(selected_tuple[0])
	view_command()

def update_command():
	backend.update(selected_tuple[0],author_text.get(),title_text.get(),year_text.get(),ISBN_text.get())

window = Tk()

window.wm_title("Book Store")

#labels
l1 =Label(window ,text='Title').grid(row='0',column='0')
l1 =Label(window ,text='Year').grid(row='1',column='0')
l1 =Label(window ,text='Author').grid(row='0',column='2')
l1 =Label(window ,text='ISBN').grid(row='1',column='2')

#textboxs
title_text = StringVar()
e1 =Entry(window ,textvariable = title_text)
e1.grid(row='0',column='1')
author_text = StringVar()
e2 =Entry(window ,textvariable = author_text)
e2.grid(row='0',column='3')
year_text = StringVar()
e3 =Entry(window ,textvariable = year_text)
e3.grid(row='1',column='1')
ISBN_text = StringVar()
e4 =Entry(window ,textvariable = ISBN_text)
e4.grid(row='1',column='3')

#buttons
b1 =Button(window ,text='View all',width='12',command=view_command).grid(row='2',column='3')
b2 =Button(window ,text='Search Entry',width='12',command=search_command).grid(row='3',column='3')
b3 =Button(window ,text='Add Entry',width='12',command=entry_command).grid(row='4',column='3')
b4 =Button(window ,text='Update',width='12',command=update_command).grid(row='5',column='3')
b5 =Button(window ,text='Delete',width='12' ,command=delete_command).grid(row='6',column='3')
b6 =Button(window ,text='Close',width='12',command=window.destroy).grid(row='7',column='3')


list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

window.mainloop()
