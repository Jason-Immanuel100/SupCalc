from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk 
from customtkinter import CTkImage  
from math import *
import re

root = Tk()
root.title("SupCalc")

app_width = 1000
app_height = 900

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - app_width / 2)
center_y = int(screen_height / 2 - app_height / 2)

root.geometry(f'{app_width}x{app_height}+{center_x}+{center_y}')
root.configure(bg="#ffffff")

title_label = ctk.CTkLabel(root, text="SUPCALC", font=("Frutiger", 50, "bold"), bg_color="#ffffff")
title_label.pack(padx=20, pady=30)

light_image = Image.open("Assets/nhs-royal-surrey-logo.png")
dark_image = Image.open("Assets/nhs-royal-surrey-logo.png")

image_tk = ctk.CTkImage(light_image=light_image, dark_image=dark_image, size=(232.5, 160))

nhs_logo_label = ctk.CTkLabel(root, image=image_tk, bg_color="#ffffff", text="")
nhs_logo_label.place(x=16.9, y=11.9)

entry_box_x_1 = 320
entry_box_x_2 = 740

row_1_y = 190
row_2_y = 250
row_3_y = 310
row_4_y = 370
row_5_y = 430
row_6_y = 490

patient_firstname_label = ctk.CTkLabel(root, text="Patient First Name:", font=("Frutiger", 21), bg_color="#ffffff")
patient_firstname_label.place(x=120, y=row_1_y)

patient_firstname_entry = ctk.CTkEntry(root, font=("Frutiger", 21), bg_color="#ffffff", border_color="#0072CE")
patient_firstname_entry.place(x=entry_box_x_1, y=row_1_y)

patient_surname_label = ctk.CTkLabel(root, text="Patient Surname:", font=("Frutiger", 21), bg_color="#ffffff")
patient_surname_label.place(x=550, y=190)

patient_surname_entry = ctk.CTkEntry(root, font=("Frutiger", 21), bg_color="#ffffff", border_color="#0072CE")
patient_surname_entry.place(x=entry_box_x_2, y=row_1_y)

date_of_birth_label = ctk.CTkLabel(root, text="Date of Birth:", font=("Frutiger", 21), bg_color="#ffffff")
date_of_birth_label.place(x=174, y=row_2_y)

dob_entry = ctk.CTkEntry(root, font=("Frutiger", 21), bg_color="#ffffff", border_color="#0072CE")
dob_entry.place(x=entry_box_x_1, y=row_2_y)

hospital_number_label = ctk.CTkLabel(root, text="Hospital Number:", font=("Frutiger", 21), bg_color="#ffffff")
hospital_number_label.place(x=549, y=row_2_y)

hospital_number_entry = ctk.CTkEntry(root, font=("Frutiger", 21), bg_color="#ffffff", border_color="#0072CE")
hospital_number_entry.place(x=entry_box_x_2, y=row_2_y)

prescription_label = ctk.CTkLabel(root, text="Prescription Name:", font=("Frutiger", 21), bg_color="#ffffff")
prescription_label.place(x=120, y=row_3_y)

prescription_entry = ctk.CTkEntry(root, font=("Frutiger", 21), bg_color="#ffffff", border_color="#0072CE")
prescription_entry.place(x=entry_box_x_1, y=row_3_y)

number_of_fractions_var = StringVar()
prescribed_dose_var = StringVar()
dose_per_fraction_var = StringVar()

prescribed_dose_label = ctk.CTkLabel(root, text="Prescribed Dose:", font=("Frutiger", 21), bg_color="#ffffff")
prescribed_dose_label.place(x=550, y=row_3_y)

prescribed_dose_entry = ctk.CTkEntry(root, font=("Frutiger", 21), bg_color="#ffffff", border_color="#0072CE", textvariable=prescribed_dose_var)
prescribed_dose_entry.place(x=entry_box_x_2, y=row_3_y)

number_of_fractions_label = ctk.CTkLabel(root, text="Number of Fractions:", font=("Frutiger", 21), bg_color="#ffffff")
number_of_fractions_label.place(x=100, y=row_4_y)

number_of_fractions_entry = ctk.CTkEntry(root, font=("Frutiger", 21), bg_color="#ffffff", border_color="#0072CE", textvariable=number_of_fractions_var)
number_of_fractions_entry.place(x=entry_box_x_1, y=row_4_y)

dose_per_fraction_label = ctk.CTkLabel(root, text="Dose per Fraction:", font=("Frutiger", 21), bg_color="#ffffff")
dose_per_fraction_label.place(x=540, y=row_4_y)

dose_per_fraction_output = ctk.CTkLabel(root, font=("Frutiger", 21), bg_color="#ffffff", textvariable=dose_per_fraction_var)
dose_per_fraction_output.place(x=entry_box_x_2, y=row_4_y)

field_shape_label = ctk.CTkLabel(root, text="Field Shape:", font=("Frutiger", 21), bg_color="#ffffff")
field_shape_label.place(x=178.5, y=row_5_y)

shape_list = ["Square", "Circle", "Ellipse", "Rectangle"]

width_var = StringVar()
length_var = StringVar()
equivalent_shape_var = StringVar()

field_shape_drop_down = ctk.CTkComboBox(root, values=shape_list, border_color="#0072CE", font=("Frutiger", 21), button_color="#005EB8")
field_shape_drop_down.place(x=entry_box_x_1, y=row_5_y)

width_label = ctk.CTkLabel(root, text="Width:", font=("Frutiger", 21), bg_color="#ffffff")
width_label.place(x=550, y=row_5_y)

width_entry = ctk.CTkEntry(root, font=("Frutiger", 21), bg_color="#ffffff", border_color="#0072CE", width=80, textvariable=width_var)
width_entry.place(x=620, y=row_5_y)

length_label = ctk.CTkLabel(root, text="Length:", font=("Frutiger", 21), bg_color="#ffffff")
length_label.place(x=720, y=row_5_y)

length_entry = ctk.CTkEntry(root, font=("Frutiger", 18), bg_color="#ffffff", border_color="#0072CE", width=80, textvariable=length_var)
length_entry.place(x=800, y=row_5_y)

equivalent_shape_label = ctk.CTkLabel(root, text="Eq.Square/Circle Diameter:", font=("Frutiger", 21), bg_color="#ffffff")
equivalent_shape_label.place(x=200, y=row_6_y)

equivalent_shape_output = ctk.CTkLabel(root, font=("Frutiger", 21), bg_color="#ffffff", textvariable=equivalent_shape_var)
equivalent_shape_output.place(x=500, y=row_6_y)

def calculate_equivalent_shape(*args):
    selected_shape = field_shape_drop_down.get()
    try:
        if selected_shape == "Square":
            width = float(width_entry.get())
            equivalent_shape_var.set(f"{width:.3f}")
        elif selected_shape == "Circle":
            diameter = float(width_entry.get())
            equivalent_shape_var.set(f"{diameter:.3f}")
        elif selected_shape == "Ellipse":
            a = float(width_entry.get())
            b = float(length_entry.get())
            equivalent_diameter = sqrt(a * b)
            equivalent_shape_var.set(f"{equivalent_diameter:.3f}")
        elif selected_shape == "Rectangle":
            a = float(width_entry.get())
            b = float(length_entry.get())
            equivalent_diameter = sqrt(a * b)
            equivalent_shape_var.set(f"{equivalent_diameter:.3f}")
    except ValueError:
        equivalent_shape_var.set("Invalid input")

field_shape_drop_down.bind("<<ComboboxSelected>>", calculate_equivalent_shape)
width_entry.bind("<KeyRelease>", calculate_equivalent_shape)
length_entry.bind("<KeyRelease>", calculate_equivalent_shape)

def calculate_dose_per_fraction(*args):
    try:
        # Extract the numeric part from the prescribed_dose_entry, removing "Gy" if present
        prescribed_dose_str = prescribed_dose_entry.get().replace("Gy", "").strip()
        prescribed_dose = float(prescribed_dose_str)
        
        number_of_fractions_str = number_of_fractions_entry.get().strip()
        number_of_fractions = float(number_of_fractions_str)
        
        dose_per_fraction = prescribed_dose / number_of_fractions
        dose_per_fraction_var.set(f"{dose_per_fraction:.3f} Gy")  # Set the calculated value with formatting and append "Gy"
    except ValueError:
        dose_per_fraction_var.set("")  # Clear the value if there is an error in conversion

prescribed_dose_entry.bind("<KeyRelease>", calculate_dose_per_fraction)
number_of_fractions_entry.bind("<KeyRelease>", calculate_dose_per_fraction)

def sync_dimensions(*args):
    selected_shape = field_shape_drop_down.get()
    if selected_shape in ["Circle", "Square"]:
        if width_entry.get() != length_entry.get():
            if args and args[0] == 'width':
                length_entry.delete(0, "end")
                length_entry.insert(0, width_entry.get())
            else:
                width_entry.delete(0, "end")
                width_entry.insert(0, length_entry.get())

# Bind the sync_dimensions function to changes in the shape selection, width, and length entries
field_shape_drop_down.bind("<<ComboboxSelected>>", lambda event: sync_dimensions())
width_entry.bind("<KeyRelease>", lambda event: sync_dimensions('width'))
length_entry.bind("<KeyRelease>", lambda event: sync_dimensions('length'))

root.mainloop()