import tkinter as tk
from tkinter import ttk


class ControlForm(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("Control Form")

        # Using pack geometry manager
        label_pack = ttk.Label(self, text="Using Pack:")
        label_pack.pack()
        button_pack = ttk.Button(self, text="Button using Pack")
        button_pack.pack()

        # Using grid geometry manager
        label_grid = ttk.Label(self, text="Using Grid:")
        label_grid.grid(row=1, column=0)
        button_grid = ttk.Button(self, text="Button using Grid")
        button_grid.grid(row=1, column=1)

        # Using place geometry manager
        label_place = ttk.Label(self, text="Using Place:")
        label_place.place(x=20, y=60)
        button_place = ttk.Button(self, text="Button using Place")
        button_place.place(x=20, y=80)

        # Using pack inside a frame
        frame_pack = ttk.Frame(self)
        frame_pack.place(x=150, y=20)
        label_frame = ttk.Label(frame_pack, text="Inside Frame - Pack:")
        label_frame.pack()
        button_frame = ttk.Button(frame_pack, text="Button inside Frame using Pack")
        button_frame.pack()

        # Using grid inside a frame
        frame_grid = ttk.Frame(self)
        frame_grid.place(x=150, y=100)
        label_frame_grid = ttk.Label(frame_grid, text="Inside Frame - Grid:")
        label_frame_grid.grid(row=0, column=0)
        button_frame_grid = ttk.Button(frame_grid, text="Button inside Frame using Grid")
        button_frame_grid.grid(row=0, column=1)


if __name__ == "_main_":
    app = ControlForm()
    app.mainloop()