import tkinter as tk

class Gui(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.render_elements()
		
	def render_elements(self):
		self.add_text = tk.Entry()
		self.add_btn = tk.Button(text='Add Site')
		self.add_text.pack()
		self.add_btn.pack()

		self.all_label = tk.Label(text='All Sites')
		self.all_list = tk.Listbox()
		self.all_list.insert(1, "stuff")
		self.all_list.insert(2, "more stuff")
		self.all_label.pack()
		self.all_list.pack()

		self.updated_label = tk.Label(text='Updated Sites')
		self.updated_list = tk.Listbox()
		self.updated_list.insert(1, 'that good never updated site')
		self.updated_list.insert(2, 'mediocre at best updated site')
		self.updated_label.pack()
		self.updated_list.pack()

		self.check_now_btn = tk.Button(text='Check Now')
		self.check_now_btn.pack()

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
