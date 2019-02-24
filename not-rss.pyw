import tkinter as tk

class Gui(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.read_data = self.read_file()
		# maybe spawn loading here?
		self.render_elements()
		
	def render_elements(self):
		self.entry_add = tk.Entry()
		self.btn_add = tk.Button(text='Add Site', command=self.add_site)
		self.entry_add.pack()
		self.btn_add.pack()

		self.label_all = tk.Label(text='All Sites')
		self.list_all = tk.Listbox()
		self.label_all.pack()
		self.list_all.pack()

		self.label_up = tk.Label(text='Updated Sites')
		self.list_up = tk.Listbox()
		self.label_up.pack()
		self.list_up.pack()

		self.btn_check = tk.Button(text='Check Now')
		self.btn_check.pack()

	def read_file(self):
		# if doesn't exist create empty file with instructions
		return 'read site list here'

	def add_site(self):
		self.read_data += entry_add.get()
		# then save back


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
