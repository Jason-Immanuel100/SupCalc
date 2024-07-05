# Import necessary libraries
from tkinter import Tk  # Tkinter module for creating GUI applications
import customtkinter as ctk # CustomTkinter for modern and customizable GUI components
from PIL import Image, ImageTk  # PIL (Python Imaging Library) for image processing tasks
from customtkinter import CTkImage  # CustomTkinter's image widget for displaying images
from tkinter import StringVar # StringVar from Tkinter for creating variable wrappers
from tkinter import messagebox # Tkinter's messagebox module for displaying alerts
import math
import re
# Initialize the main application window
root = Tk()
root.title("SupCalc")

app_width = 720
app_height = 580

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

image_tk = ctk.CTkImage(light_image=light_image, dark_image=dark_image, size=(160, 116))

# Use the converted image with CTkLabel
nhs_logo_label = ctk.CTkLabel(root, image=image_tk, bg_color="#ffffff", text="")
nhs_logo_label.place(x=15, y=5.2)

patient_firstname_label = ctk.CTkLabel(root, text="Patient First Name:", font=("Frutiger", 18), bg_color="#ffffff")
patient_firstname_label.place(x=15, y=144)

patient_firstname_entry = ctk.CTkEntry(root, font=("Frutiger", 18), bg_color="#ffffff", border_color="#0072CE")
patient_firstname_entry.place(x=186, y=144)

patient_surname_label = ctk.CTkLabel(root, text="Patient Surname:", font=("Frutiger", 18), bg_color="#ffffff")
patient_surname_label.place(x=374, y=144)

patient_surname_entry = ctk.CTkEntry(root, font=("Frutiger", 18), bg_color="#ffffff", border_color="#0072CE")
patient_surname_entry.place(x=523.3, y=144)

date_of_birth_label = ctk.CTkLabel(root, text="Date of Birth:", font=("Frutiger", 18), bg_color="#ffffff")
date_of_birth_label.place(x=60.6, y=189)

dob_entry = ctk.CTkEntry(root, font=("Frutiger", 18), bg_color="#ffffff", border_color="#0072CE")
dob_entry.place(x=186, y=189)

hospital_number_label = ctk.CTkLabel(root, text="Hospital Number:", font=("Frutiger", 18), bg_color="#ffffff")
hospital_number_label.place(x=370, y=189)

hospital_number_entry = ctk.CTkEntry(root, font=("Frutiger", 18), bg_color="#ffffff", border_color="#0072CE")
hospital_number_entry.place(x=523.3, y=189)

prescription_label = ctk.CTkLabel(root, text="Prescription Name:", font=("Frutiger", 18), bg_color="#ffffff")
prescription_label.place(x=15.8, y=234)

prescription_entry = ctk.CTkEntry(root, font=("Frutiger", 18), bg_color="#ffffff", border_color="#0072CE")
prescription_entry.place(x=186, y=234)

number_of_fractions_var = StringVar()
prescribed_dose_var = StringVar()
dose_per_fraction_var = StringVar()

prescribed_dose_label = ctk.CTkLabel(root, text="Prescribed Dose:", font=("Frutiger", 18), bg_color="#ffffff")
prescribed_dose_label.place(x=374, y=234)

prescribed_dose_entry = ctk.CTkEntry(root, font=("Frutiger", 18), bg_color="#ffffff", border_color="#0072CE", textvariable=prescribed_dose_var)
prescribed_dose_entry.place(x=523.3, y=234)

number_of_fractions_label = ctk.CTkLabel(root, text="Number of Fractions:", font=("Frutiger", 18), bg_color="#ffffff")
number_of_fractions_label.place(x=0, y=279)

number_of_fractions_entry = ctk.CTkEntry(root, font=("Frutiger", 18), bg_color="#ffffff", border_color="#0072CE", textvariable=number_of_fractions_var)
number_of_fractions_entry.place(x=186, y=279)

field_shape_label = ctk.CTkLabel(root, text="Field Shape:", font=("Frutiger", 18), bg_color="#ffffff")
field_shape_label.place(x=70, y=324)

shape_list = ["Square", "Circle", "Elipse", "Rectangle"]

field_shape_drop_down = ctk.CTkComboBox(root, values=shape_list, border_color="#0072CE", font=("Frutiger", 18), button_color="#005EB8")
field_shape_drop_down.place(x=186, y=324)

dose_per_fraction_label = ctk.CTkLabel(root, text="Dose per Fraction:", font=("Frutiger", 18), bg_color="#ffffff")
dose_per_fraction_label.place(x=364, y=279)

def validate_entry_content(event):
    entry_widget = event.widget
    text = entry_widget.get()
    new_text = ''.join(filter(str.isalpha, text))
    if text != new_text:
        entry_widget.delete(0, "end")  # Remove current text
        entry_widget.insert(0, new_text)  # Insert validated text

# Assuming patient_firstname_entry and patient_surname_entry are already created as CTkEntry widgets
patient_firstname_entry.bind("<KeyRelease>", validate_entry_content)
patient_surname_entry.bind("<KeyRelease>", validate_entry_content)

def validate_nhs_number(nhs_number):
    cleaned_nhs_number = nhs_number.replace(" ", "")
    if len(cleaned_nhs_number) != 10 or not cleaned_nhs_number.isdigit():
        return False
    digits = [int(digit) for digit in cleaned_nhs_number]
    digits_reversed = digits[::-1]
    sum_of_products = sum(weight * digit for weight, digit in enumerate(digits_reversed[1:], 2))
    remainder = sum_of_products % 11
    check_digit = (11 - remainder) % 11
    return check_digit == digits_reversed[0]

# Step 2: Define a function to be called when the entry loses focus or a button is pressed
def on_validate_nhs_number():
    nhs_number = hospital_number_entry.get()
    if validate_nhs_number(nhs_number):
        print("NHS number is valid.")
    else:
        print("NHS number is invalid.")
        messagebox.showerror("Invalid NHS Number", "The NHS number is invalid. Please enter a valid NHS number.")
        
hospital_number_entry.bind("<FocusOut>", lambda event: on_validate_nhs_number())

def validate_numeric_entry(event):
    entry_widget = event.widget
    text = entry_widget.get()
    # Allow only digits and a single decimal point
    new_text = ''.join([char for char in text if char.isdigit() or char == "."])
    # Remove extra decimal points if present
    if new_text.count('.') > 1:
        new_text = new_text.replace(".", "", new_text.count('.') - 1)
    if text != new_text:
        entry_widget.delete(0, "end")  # Remove current text
        entry_widget.insert(0, new_text)  # Insert validated text

# Assuming prescribed_dose_entry and number_of_fractions_entry are already created as CTkEntry widgets
prescribed_dose_entry.bind("<KeyRelease>", validate_numeric_entry)
number_of_fractions_entry.bind("<KeyRelease>", validate_numeric_entry)

def validate_dob_format(event):
    # Regular expression to match the dd/mm/yyyy format
    pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/\d{4}$"
    dob = dob_entry.get()
    
    # Check if the input matches the pattern
    if re.match(pattern, dob) or dob == "":
        # If it matches, or the entry is empty (allowing deletion), do nothing
        pass
    else:
        # If it doesn't match, show an error and clear the input
        messagebox.showerror("Invalid Date", "Date must be in dd/mm/yyyy format")
        dob_entry.delete(0, "end")

# Bind the validation function to the dob_entry widget
dob_entry.bind("<FocusOut>", validate_dob_format)

def add_unit_gy(event):
    # Get the current value from the entry widget
    current_value = prescribed_dose_var.get()
    # Check if the value does not end with 'Gy'
    if not current_value.strip().endswith("Gy"):
        # Append 'Gy' to the value
        new_value = current_value + " Gy"
        # Update the StringVar with the new value
        prescribed_dose_var.set(new_value)

# Bind the FocusOut event to the prescribed_dose_entry widget
prescribed_dose_entry.bind("<FocusOut>", add_unit_gy)

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

def get_values():
    patient_surname = patient_surname_entry.get()
    patient_firstname = patient_firstname_entry.get()
    prescription = prescription_entry.get()
    dob = dob_entry.get()
    prescribed_dose = prescribed_dose_entry.get()
    number_of_fractions = number_of_fractions_entry.get()
    field_shape = field_shape_drop_down.get()
    hospital_number = hospital_number_entry.get()

    print(f"Patient Surname: {patient_surname}")
    print(f"Patient First Name: {patient_firstname}")
    print(f"Prescription Name: {prescription}")
    print(f"Date of Birth: {dob}")
    print(f"Prescribed Dose: {prescribed_dose}")
    print(f"Number of Fractions: {number_of_fractions}")
    print(f"Field Size: {field_shape}")
    print(f"Hospital Number: {hospital_number}")

dose_per_fraction_output = ctk.CTkLabel(root, font=("Frutiger", 18), bg_color="#ffffff", textvariable=dose_per_fraction_var)
dose_per_fraction_output.place(x=523.3, y=279)


enter_button = ctk.CTkButton(root, text="Calculate", fg_color="#005EB8", text_color="#ffffff", font=("Frutiger", 18), command=lambda: [get_values(), open_result_window()])
enter_button.pack(side='bottom', anchor='s', pady=50)

def open_result_window():
    result_window = ctk.CTkToplevel(root, title="Results", width=500, height=500, bg_color="#ffffff")
    result_window.geometry(f'+{center_x}+{center_y}')

root.mainloop()