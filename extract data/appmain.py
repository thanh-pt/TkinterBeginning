import tkinter as tk
from AppComponent import ListView, TargetItem


class AppMain:
    def __init__(self):
        self.root = tk.Tk()
        self.listView = ListView(self.root)

        self.listView.pack(fill='both', expand=True)
        self.listView.model = ['blue', 'yellow', 'red']
        self.listView.item = TargetItem

        self.button = tk.Button(self.root, text='Reload', command=self.btnClick).pack()

        self.root.mainloop()

    def btnClick(self):
        self.listView.reload()


