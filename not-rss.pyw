import tkinter as tk

class Gui(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)

dict_txt = {
	'title': 'Not RSS',
}

def txt(s):
	return dict_txt.get(s)

if __name__ == '__main__':
	root = tk.Tk()
	root.title(txt('title'))
	root.geometry("300x500+500+50")
	app = Gui(master=root)
	app.mainloop()
