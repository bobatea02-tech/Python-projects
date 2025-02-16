import tkinter as tk
from tkinter import messagebox

# Create a window
root = tk.Tk()
root.config(bg='white')
root.title('Unit Converter')
root.geometry('450x450')

def unit_conversion():
    conversion_factors = {  
        'm_to_ft': 3.28084,  
        'ft_to_m': 0.3048,  
        'km_to_mi': 0.621371,  
        'mi_to_km': 1.60934,  
        'cm_to_in': 0.393701,  
        'in_to_cm': 2.54,
        'm_to_km': 0.001,
        'km_to_m': 1000,
        'cm_to_m': 0.01,
        'm_to_cm': 100,
        'in_to_ft': 0.0833333,
        'ft_to_in': 12,
        'cm_to_ft': 0.0328084,
        'ft_to_cm': 30.48,
        'mi_to_ft': 5280,
        'ft_to_mi': 0.000189394,
        'mi_to_m': 1609.34
        }  
    
    if lbl_entry.get() == '':
        messagebox.showwarning('Error', 'Please enter a value!')
        return
    
    try:
        user_input = float(lbl_entry.get())
    except ValueError:
        messagebox.showwarning('Error', 'Please enter a valid numeric value!')
        return
    
    from_unit = lbl_entry_from.get()
    to_unit = lbl_entry_to.get()
    
    key = f"{from_unit}_to_{to_unit}"
    
    if key in conversion_factors and user_input >= 0:
        result =  user_input * conversion_factors[key]
        messagebox.showinfo('Result', f'{user_input} {from_unit} to {to_unit} is {result} {to_unit}')
        add_to_history(result, from_unit, to_unit, user_input)  # Call the history function
    elif user_input < 0:
        messagebox.showwarning('Error', 'Please enter a positive value!')
    else:
        messagebox.showwarning('Error', 'Conversion not mentioned!')
        
    lbl_entry.delete(0, tk.END)
    lbl_entry_from.delete(0, tk.END)    
    lbl_entry_to.delete(0, tk.END)

def add_to_history(result, from_unit, to_unit, user_input):  
    lbl_listbox.insert(tk.END, f'{user_input} {from_unit} to {to_unit} is {result} {to_unit}')

# Title Label
lbl_title = tk.Label(root, text='UNIT CONVERTER', bg='white', fg='blue', font=('Arial', 20))
lbl_title.pack()

# Value Input
lbl_value = tk.Label(root, text='Enter the value to convert:', bg='white', fg='green', font=('Arial', 12))
lbl_value.pack()
lbl_entry = tk.Entry(root, width=10, bg='white')
lbl_entry.pack()

# From Unit
lbl_from = tk.Label(root, text='Enter the unit to convert from (m, ft, km, mi, cm, in):', bg='white', fg='green', font=('Arial', 12))
lbl_from.pack()
lbl_entry_from = tk.Entry(root, width=10, bg='white')
lbl_entry_from.pack()

# To Unit
lbl_to = tk.Label(root, text='Enter the unit to convert into (m, ft, km, mi, cm, in):', bg='white', fg='green', font=('Arial', 12))
lbl_to.pack()
lbl_entry_to = tk.Entry(root, width=10, bg='white')
lbl_entry_to.pack()

# Convert Button
lbl_enter_button = tk.Button(root, text='Convert', bg='white', command=unit_conversion, font=('Arial', 12), fg='green')
lbl_enter_button.pack()

# History Section
lbl_history = tk.Label(root, text='History:', bg='white', fg='red', font=('Arial', 12))
lbl_history.pack()

history_frame = tk.Frame(root, bg='white')
history_frame.pack()

lbl_listbox = tk.Listbox(history_frame, width=50, height=10, bg='white')
lbl_listbox.pack(fill=tk.BOTH, expand=True,side=tk.LEFT)

# Scrollbar
lbl_scrollbar = tk.Scrollbar(history_frame, orient='vertical')
lbl_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Attach Scrollbar to Listbox
lbl_listbox.config(yscrollcommand=lbl_scrollbar.set)
lbl_scrollbar.config(command=lbl_listbox.yview)

root.mainloop()
