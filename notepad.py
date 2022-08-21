# SIMPLE NOTEPAD
# CRED : armz2002

# add library
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile

# create base gui
win = Tk()
win.maxsize(800,450)
win.minsize(800,450)
win.title("NOTEPAD");

# create text filed for write in notepad
t = Text(win, width=800, height=450 , fg="black" , font=('B nazanin', 17 , 'bold'))
t.pack(expand = tk.YES, fill = tk.BOTH, side = tk.LEFT)

# option in help menu for more info
def aboutme():
	winn = Tk()
	winn.maxsize(350,200)
	winn.minsize(350,200)
	winn.title("ABOUT ME");
	message ='''hello and welcome

i am amirreza mehdizdeh 
i hope enjoy to this simple notepad
this application created by python tkinter

instagram : armz_coded
telegram : AmirM5092
	'''
	text_box = Text(winn,height=12,width=45)
	text_box.pack(expand=True)
	text_box.insert('end', message)
	text_box.config(state='disabled')

	winn.mainloop()

# option in file menu for clear text filed for new text filed
def new_notepad():
	if not t.edit_modified():
		t.delete("1.0",END)
	else:
		savefile()
		t.delete("1.0",END)
	t.edit_modified(0)

# option in file menu for save user written
def savefile():
	try:
		path = filedialog.asksaveasfile(filetypes = (("Text files" , "*.txt"),("All files" , "*.*"))).name 
		win.title('note pad - ' +path)
	except:
		return
	with open(path,'w') as f:
		f.write(t.get('1.0',END))

# option in file menu for exit in app and select 2 choses
def exit():
	winnn = Tk()
	winnn.maxsize(300,75)
	winnn.minsize(300,75)
	winnn.title("EXIT")
	def savefile_exit():
		try:
			path = filedialog.asksaveasfile(filetypes = (("Text files" , "*.txt"),("All files" , "*.*"))).name 
			win.title('note pad - ' +path)
		except:
			return
		with open(path,'w') as f:
			f.write(t.get('1.0',END))
		winnn.destroy()
		win.destroy()
	b1 = Button(winnn, text="cancel" ,padx=20,pady=10 , fg = "black" , command=winnn.destroy).place(x=50,y=15)
	b2 = Button(winnn, text="save" ,padx=20,pady=10 , fg = "black" , command=savefile_exit).place(x=175,y=15)
	winnn.mainloop()

# option of file menu for open in brower
def openfile():
	if not t.edit_modified():
		try:
			path = filedialog.askopenfile(filetypes = (("Text files" , "*.txt") , ("All files" , "*.*"))).name
			win.title('notepad - ' +path)
			with open(path,'r') as f:
				cont = f.read()
				t.delete('1.0' , END)
				t.insert('1.0' , cont)
				t.edit_modified(0)
		except:
			pass 
	else:
		savefile()
		t.edit_modified(0)
		openfile()
	
# create a menubar
menubar = Menu(win)
win.config(menu=menubar)

# create a menu
file_menu = Menu(menubar , tearoff=0)
file_menuu = Menu(menubar , tearoff=0)
file_menuuu = Menu(menubar , tearoff=0)
file_menu.add_command(label='New' , command=new_notepad)
file_menu.add_separator()
file_menu.add_command(label='Open',command=openfile)
file_menu.add_separator()
file_menu.add_command(label='Save',command=lambda : savefile())
file_menu.add_separator()
file_menu.add_command(label='Exit',command=exit)
# add header of menu name is File
menubar.add_cascade(label="File",menu=file_menu)
file_menuuu.add_command(label='Find')
menubar.add_cascade(label="Edit",menu=file_menuuu)
file_menuu.add_command(label='About Me' , command=aboutme)
menubar.add_cascade(label="Help",menu=file_menuu)

# run gui
win.mainloop()