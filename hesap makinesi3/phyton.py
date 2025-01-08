import tkinter as tk

# Hesaplama işlevini tanımlayalım
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Pencereyi oluştur
root = tk.Tk()
root.title("Python Hesap Makinesi")

# Ekran alanını oluştur
entry = tk.Entry(root, width=25, borderwidth=5, font=("Arial", 14), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Butonlar
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Butonlara işlev ekleyelim
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), command=button_equal)
    elif text == 'C':
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), command=button_clear)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda value=text: button_click(value))
    button.grid(row=row, column=col, padx=5, pady=5)

# Pencereyi çalıştır
root.mainloop()