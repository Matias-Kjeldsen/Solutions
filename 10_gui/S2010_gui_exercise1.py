"""
Opgave "GUI step 1":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2010.png

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""
import tkinter as tk

padx = 32
pady = 12

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")

frame_1 = tk.LabelFrame(main_window, text="Container")
frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

# Create a button
button_1 = tk.Button(frame_1, text="Create")
button_1.grid(row=2, column=1, padx=padx, pady=pady)

# Create a label
label_1 = tk.Label(frame_1, text="Id")
label_1.grid(row=0, column=1, padx=padx, pady=pady)

# Create an entry
entry_1 = tk.Entry(frame_1, width=5, justify="right")
entry_1.grid(row=1, column=1, padx=padx, pady=pady)
entry_1.insert(0, " ")


if __name__ == "__main__":
    main_window.mainloop()