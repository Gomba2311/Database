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
        main_label = tk.Label(main_frame, text="  Adatbázis  ", font=("Comic Sans MS", 20), bg="yellow", fg="red")
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
        self.create_hiv_entry = tk.Entry(create_frame, width="30", font=("Comic Sans MS", 12))
        self.create_name_entry = tk.Entry(create_frame, width="30", font=("Comic Sans MS", 12))
        self.create_age_entry = tk.Entry(create_frame, width="30", font=("Comic Sans MS", 12))
        self.create_gender_entry = tk.Entry(create_frame, width="30", font=("Comic Sans MS", 12))
        # -- packing --
        self.create_hiv_entry.pack()
        self.create_name_entry.pack()
        self.create_age_entry.pack()
        self.create_gender_entry.pack()
        # -------------
        create_button = tk.Button(create_frame, text="Create", command=self.create, font=('Arial', 15), bg="lightgreen")
        create_button.pack()
        # @@
        create_frame.grid(row=2, column=3)

        # --|--load trying--|--
        try:
            with open("Assets/hivatkozasok.txt") as pl:
                self.hiv = js.load(pl)
        except:
            self.hiv = []
        self.peron = None
        try:
            with open("Assets/szemelyek.txt") as nl:
                self.nevek = js.load(pl)
        except:
            self.nevek = []

    # --|-- search definiton--|--
    def search(self):
        nothuman = True
        human = False
        try:
            for i in range(len(self.hiv)):
                if self.hiv[i] == self.search_entry.get():
                    self.peron = i
                    FailedLabel = tk.Label(self.mast, text=self.nevek[i], font=("Georga", 20), bg="yellow", fg="green")
                    FailedLabel.grid(row=5, column=1)
                    nothuman = False
                    human = True
                elif self.hiv[i] != self.search_entry.get():
                    nothuman = True
                if i == len(self.hiv) - 1 and nothuman and not human:
                    FailedLabel = tk.Label(self.mast, text="Nem létező személy!", font=("Georga", 20), bg="yellow", fg="red")
                    FailedLabel.grid(row=5, padx=350, column=1)
        except:
            FailedLabel = tk.Label(self.mast, text="Hiányzó Adat!", font=("Georga", 18), bg="yellow", fg="red")
            FailedLabel.grid(row=3, column=2)
    def new_member(self, nev, kor, gend):
        nmn = nev
        nma = kor
        nmg = gend
        nmp = {nmn, nma, nmg}
        self.nevek.append(nmp)

    def create(self):
        self.hiv.append(self.create_hiv_entry.get())
        self.new_member(self.create_name_entry.get, self.create_age_entry.get, self.create_gender_entry.get)



window = tk.Tk()

main = MainWindow(window)


window.mainloop()
