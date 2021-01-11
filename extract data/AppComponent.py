import tkinter as tk


class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def on_top(self):
        self.canvas.yview_moveto(0)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * (int(event.delta / 120)), "units")


class BaseItem(tk.Frame):
    def __init__(self, container, data, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(width=100, height=200)
        self.configure(bg=data)


class HackerrankItem(tk.Frame):
    def __init__(self, container, data, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(width=300, height=60)
        self.name = tk.Label(self, text=data.Name).place(x=10, y=5)
        self.score = tk.Label(self, text="Score:" + data.Score).place(x=10, y=30)


class ListView(ScrollableFrame):
    def __init__(self, container, *args, **kwargs):
        super(ListView, self).__init__(container, *args, **kwargs)
        self.model = []
        self.item = BaseItem

    def reload(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        for data in self.model:
            item = self.item(self.scrollable_frame, data).pack()
