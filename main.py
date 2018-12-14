from tkinter import*
from connection import connection
from start import start

try:
	conn = connection()
	cur = conn.get_cursor()
except:
	print("Connecting to server failed")
	exit(1)

root = Tk()
background_color = "white"

startpage = start(root, background_color, cur)
startpage.place_all()

root.configure(background=background_color)
root.geometry('800x600')
root.mainloop()
