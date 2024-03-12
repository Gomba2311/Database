import tkinter as tk
import json as js
#        _____________________________
# ++!++ |main window creating in class| ++!++
class MainWindow:
    def __init__(self, master):

        # --|--master generate--|--
        master.title("Police Database")
        master.geometry("1000x500")
        master.configure(bg="yellow")

        self.mast = master
        # --|--main area--|--
        main_frame = tk.Frame(master, bg="yellow")
        # @@
        main_label = tk.Label(main_frame, text="Adatbázis", font=("Comic Sans MS", 20), bg="yellow", fg="red")
        main_label.pack()
        # @@
        main_frame.grid(row=1, column=2)

        # --|--search area--|--
        search_frame = tk.Frame(master, bg="yellow")
        # @@
        search_label = tk.Label(search_frame, text="search", bg="yellow", width="30", font=("Comic Sans MS", 18), fg="red")
        search_label.pack()
        self.search_entry = tk.Entry(search_frame, width="30", font=("Comic Sans MS", 12))
        self.search_entry.pack()

        search_button = tk.Button(search_frame, text="enter", command=self.search, font=('Arial', 15), bg="lightgreen")
        search_button.pack()
        # @@
        search_frame.grid(row=2, column=1)

        # --|--create area--|--
        create_frame = tk.Frame(master)
        # @@
        create_label = tk.Label(create_frame, text="Create", font=("Comic Sans MS", 18), bg="yellow", fg="red")
        create_label.pack()
        create_button = tk.Button(create_frame, text="Create", command=self.create, font=('Arial', 15), bg="lightgreen")
        create_button.pack()
        # @@
        create_frame.grid(row=2, column=3)

        # --|--load trying--|--
        try:
            with open("Assets/persons.txt") as pl:
                self.személyek = js.load(pl)
        except:
            pass
        self.peron = None

    # --|-- search definiton--|--
    def search(self):
        nothuman = True
        human = False
        try:
            for i in range(len(self.személyek)):
                if self.személyek[i] == self.search_entry.get():
                    self.peron = i
                    FailedLabel = tk.Label(self.mast, text=self.személyek[i], font=("Georga", 20), bg="yellow", fg="green")
                    FailedLabel.grid(row=5, padx=350, column=1)
                    nothuman = False
                    human = True
                elif self.személyek[i] != self.search_entry.get():
                    nothuman = True
                if i == len(self.személyek) - 1 and nothuman and not human:
                    FailedLabel = tk.Label(self.mast, text="Nem létező személy!", font=("Georga", 20), bg="yellow", fg="red")
                    FailedLabel.grid(row=5, padx=350, column=1)
        except:
            FailedLabel = tk.Label(self.mast, text="Hiányzó Adat!", font=("Georga", 18), bg="yellow", fg="red")
            FailedLabel.grid(row=3, column=2)

    def create(self):
        pass




window = tk.Tk()

main = MainWindow(window)


window.mainloop()
