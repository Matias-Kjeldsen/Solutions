""" Opgave "GUI step 2":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2020.png

Genbrug din kode fra "GUI step 1".

GUI-strukturen bør være som følger:
    main window
        labelframe
            frame
                labels and entries
            frame
                buttons

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""
import tkinter as tk

padx = 5
pady = 5

main_window = tk.Tk()
main_window.title('my first GUI')

frame_1 = tk.LabelFrame(main_window, text="Container")
frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

frame_1 = tk.Frame(main_window)
frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

label_1 = tk.Label(frame_1, text="Id")
label_1.grid(row=0, column=1, padx=padx, pady=pady)

label_2 = tk.Label(frame_1, text="Weight")
label_2.grid(row=0, column=2, padx=padx, pady=pady)

label_3 = tk.Label(frame_1, text="Destination")
label_3.grid(row=0, column=3, padx=padx, pady=pady)

label_4 = tk.Label(frame_1, text="Weather")
label_4.grid(row=0, column=4, padx=padx, pady=pady)

entry_1 = tk.Entry(frame_1, width=4, justify="right")
entry_1.grid(row=1, column=1, padx=padx, pady=pady)
entry_1.insert(0, " ")

entry_1 = tk.Entry(frame_1, width=8, justify="right")
entry_1.grid(row=1, column=2, padx=padx, pady=pady)
entry_1.insert(0, " ")

entry_1 = tk.Entry(frame_1, width=20, justify="right")
entry_1.grid(row=1, column=3, padx=padx, pady=pady)
entry_1.insert(0, " ")

entry_1 = tk.Entry(frame_1, width=14, justify="right")
entry_1.grid(row=1, column=4, padx=padx, pady=pady)
entry_1.insert(0, " ")

frame_1 = tk.Frame(main_window)
frame_1.grid(row=2, column=0, padx=padx, pady=pady, sticky=tk.N)

button_1 = tk.Button(frame_1, text="Create")
button_1.grid(row=2, column=1, padx=padx, pady=pady)

button_2 = tk.Button(frame_1, text="Update")
button_2.grid(row=2, column=2, padx=padx, pady=pady)

button_3 = tk.Button(frame_1, text="Delete")
button_3.grid(row=2, column=3, padx=padx, pady=pady)

button_4 = tk.Button(frame_1, text="Clear Entry Boxes")
button_4.grid(row=2, column=4, padx=padx, pady=pady)

if __name__ == "__main__":
    main_window.mainloop()
