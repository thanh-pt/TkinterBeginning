import tkinter as tk
from AppComponent import ListView, HackerrankItem
from DataManager import DataManager


class AppMain:
    def __init__(self):
        self.root = tk.Tk()
        self.listView = ListView(self.root)

        self.listView.pack(fill='both', expand=True)
        self.listView.model = ['blue', 'yellow', 'red']
        self.listView.item = HackerrankItem

        self.button = tk.Button(self.root, text='Reload', command=self.btnClick).pack()

        self.dataManager = DataManager()

        self.root.mainloop()

    def btnClick(self):
        self.dataManager.loadJsonFile()
        self.listView.model = self.dataManager.data
        self.listView.reload()
        totalScore = 0
        for item in self.dataManager.data:
            totalScore += int(item.Score)
        print("Total scores: " + str(totalScore))


