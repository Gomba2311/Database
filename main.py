import tkinter as tk

window = tk.Tk()

window.title("Police Database")
window.geometry("1000x500")

label = tk.Label(window, text="adatbázis", font=("Comic Sans MS", 18))
label.pack(padx=20, pady=20)


entry = tk.Entry(window, width="30", font=("Comic Sans MS", 12))
entry.pack()

rabok = ["peter", "jozsef", "elek"]

def write():
    nothuman = True
    human = False
    for i in range(len(rabok)):
        if rabok[i] == entry.get():
            print(rabok[i])
            nothuman = False
            human = True
        elif rabok[i] != entry.get():
            nothuman = True
        if i == len(rabok) - 1 and nothuman and not human:
            print('nem létező személy')

button = tk.Button(window, text="enter", font=('Arial', 15), command = write)
button.pack()

window.mainloop()
