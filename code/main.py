import tkinter as tk
from tkinter import ttk
import numpy as np
from code import Code
import pandas as pd


def model_name(event):
    selected_item = brand_combo.get() 
    if selected_item != ' ':
        model_combo['values'] = tuple(Code.model(selected_item))
    else:
        pass

def prediction():
    input = pd.DataFrame({
    "Car Brand"     : [brand_combo.get()],  # String
    "Model"         : [model_combo.get()],  # String
    "Price"         : [0],  # int
    "Model Year"    : [int(year_spinbox.get())],  # int
    "Location"      : [location_combo.get()],  # String
    "Fuel"          : [fuel_combo.get()],  # String
    "Driven (Kms)"  : [int(driven_spinbox.get())],  # int
    "Gear"          : [gear_combo.get()],  # String
    "Ownership"     : [int(owners_spinbox.get())],  # int
    })

    predict_text.config(state='normal')
    predict_text.insert('1.0',Code.predict(input))
    predict_text.config(state='disabled')



window = tk.Tk()
window.title('Car Price predictor')

frame = tk.Frame(window)
frame.pack()

input_frame = tk.LabelFrame(frame, text='Car details', padx=20, pady=20)
input_frame.pack()

brand = ttk.Label(input_frame, text='Brand')
brand.grid(row=0, column=0)
brand_combo = ttk.Combobox(input_frame, values=Code.brand())
brand_combo.grid(row=1, column=0)
brand_combo.bind("<<ComboboxSelected>>", model_name)


model = ttk.Label(input_frame, text='Model')
model.grid(row=0, column=1)
vals=[]
model_combo = ttk.Combobox(input_frame, values=vals)
model_combo.grid(row=1, column=1)

year = ttk.Label(input_frame, text='Year')
year.grid(row=0, column=2)
year_spinbox = ttk.Spinbox(input_frame, values=tuple(np.arange(2007,2021)))
year_spinbox.grid(row=1, column=2)



location = ttk.Label(input_frame, text='Location')
location.grid(row=0, column=3)
location_combo = ttk.Combobox(input_frame, values=Code.location())
location_combo.grid(row=1, column=3)


fuel = ttk.Label(input_frame, text='Fuel Type')
fuel.grid(row=2, column=0)
fuel_combo = ttk.Combobox(input_frame, values=Code.fuel())
fuel_combo.grid(row=3, column=0)

driven = ttk.Label(input_frame, text='Kms Driven')
driven.grid(row=2, column=1)
driven_spinbox = ttk.Spinbox(input_frame, values=tuple(np.arange(0,300000,10000)))
driven_spinbox.grid(row=3, column=1)

owners = ttk.Label(input_frame, text='Owners')
owners.grid(row=2, column=2)
owners_spinbox = ttk.Spinbox(input_frame, values=tuple(np.arange(1,6)))
owners_spinbox.grid(row=3, column=2)

gear = ttk.Label(input_frame, text='Gear Type')
gear.grid(row=2, column=3)
gear_combo = ttk.Combobox(input_frame, values=Code.gear())
gear_combo.grid(row=3, column=3)

for widget in input_frame.winfo_children():
    widget.grid(padx=5, pady=2)

'''Executables'''
exec_frame = tk.LabelFrame(frame, text='Executable', padx=20, pady=20)
exec_frame.pack()

predict_button = ttk.Button(exec_frame, text='Predict', command=prediction)
predict_button.grid(padx=5, pady=3)

predict_text = tk.Text(exec_frame, height=1, width=25)
predict_text.grid(padx=5, pady=3)
predict_text.config(state='disabled', bg='#dddddd')

window.mainloop()