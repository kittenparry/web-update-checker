import tkinter as tk
import os

DICT_CONSTS = {
	'site_names': 'site_names.txt',
	'saved_sites': 'saved_sites/',
}
DICT_TXT = {
	'title': 'Not RSS',
}

def txt(s):
	return DICT_TXT.get(s)

def const(s):
	return DICT_CONSTS.get(s)


class Gui(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.read_data, self.read_all = self.read_file()
		# maybe spawn loading here?
		self.render_elements()
		self.render_sites()
	
	def reload(self):
		self.render_sites()
		
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

	def render_sites(self):
		self.list_all.delete(0, 'end')
		for x, site in enumerate(self.read_data):
			self.list_all.insert(x, site)

	def read_file(self):
		if os.path.isfile(const('site_names')):
			temp = open(const('site_names')).read().split('\n')
			sites = []
			for line in temp:
				if not line.startswith('#') and line != '':
					sites.append(line)
			return sites, temp
		else:
			with open(const('site_names'), 'w') as f:
				f.write('# Paste website names one per line\n')
				return self.read_file()
	
	def write_file(self):
		with open(const('site_names'), 'w') as f:
			f.write('\n'.join(self.read_all))

	def add_site(self):
		entry = self.entry_add.get()
		if not entry.startswith('#') and entry != '':
			self.read_all.append(entry)
			self.read_data.append(entry)
			self.write_file()
			self.reload()
		else:
			print('empty or comment')


if __name__ == '__main__':
	root = tk.Tk()
	root.title(txt('title'))
	root.geometry("300x500+500+50")
	app = Gui(master=root)
	app.mainloop()
