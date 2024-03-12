import tkinter as tk

class MainWindow:
    def __init__(self, master):
        master.title("Police Database")
        master.geometry("1000x500")
        master.configure(bg="yellow")

        # Fő frame inicializálása
        main_frame = tk.Frame(master, bg="cyan")
        main_frame.pack(expand=True, fill="both")

        # Adatbázis felirat középre igazítása a képernyő tetején
        main_label = tk.Label(main_frame, text="adatbázis", font=("Comic Sans MS", 18), bg="yellow", fg="red")
        main_label.pack(side="top", pady=20)

        # További kód...

window = tk.Tk()
main = MainWindow(window)
window.mainloop()
