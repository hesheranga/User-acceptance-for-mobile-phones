from turtle import right
import customtkinter as ctk
import tkinter as tk
from tkinter import StringVar, filedialog
from docxtpl import DocxTemplate
import datetime
import os


# window 
window = ctk.CTk()
window.title('User Acceptance')
window.geometry('410x500')

frame1 = ctk.CTkFrame(master=window, width=410, height=300)
frame1.pack()
frame2 = ctk.CTkFrame(master=window, width=410, height=200)
frame2.pack()

def generate():
    date_info=datetime.datetime.now().strftime("%Y-%m-%d")
    name_get=name.get()
    name_info=name_get.strip()
    epf_info=epf.get()
    designation_info=designation.get()

    mobile_info=mobile.get()
    mobile_check_info=mobile_check_var.get()
    if mobile_check_info == "1":
        print_mobile="0" + mobile_info
    else:
        print_mobile="-"

    model_info=model.get()
    imei_info=imei.get()
    remark_info=remark.get()

    phone_check_var_info=phone_check_var.get()
    if phone_check_var_info == "1":
        print_phone="X"
    else:
        print_phone="-"

    battery_check_var_info=battery_check_var.get()
    if battery_check_var_info == "1":
        print_battery="X"
    else:
        print_battery="-"

    charger_check_var_info=charger_check_var.get()
    if charger_check_var_info == "1":
        print_charger="X"
    else:
        print_charger="-"

    data_cable_check_var_info=data_cable_check_var.get()
    if data_cable_check_var_info == "1":
        print_data_cable="X"
    else:
        print_data_cable="-"

    sim_check_var_info=sim_check_var.get()
    if sim_check_var_info == "1":
        print_sim="X"
    else:
        print_sim="-"

    hands_free_check_var_info=hands_free_check_var.get()
    if hands_free_check_var_info == "1":
        print_hands_free="X"
    else:
        print_hands_free="-"

 # Get the absolute path of the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the template file
    template_path = os.path.join(script_dir, "template.docx")

# Load the template using the absolute path
    doc = DocxTemplate(template_path)

    context=({"date": date_info,
            "name_info": name_info,
            "epf_info": epf_info,
            "designation_info": designation_info,
            "model_info": model_info,
            "imei_info": imei_info,
            "remark_info": remark_info,
            "print_mobile": print_mobile,
            "print_phone": print_phone,
            "print_battery": print_battery,
            "print_charger": print_charger,
            "print_data_cable": print_data_cable,
            "print_sim": print_sim,
            "print_hands_free": print_hands_free})
    doc.render(context)
    doc_name = epf_info + "_" + date_info + ".docx"
    doc.save(os.path.join(script_dir, doc_name))

    print(name_info," ",epf_info," ",designation_info," ",model_info," ",imei_info," ",remark_info," ",print_mobile)
    print(print_phone," ",print_battery," ",print_charger," ",print_data_cable ," ",print_sim," ", print_hands_free)

def clear_all():
    name.set("")
    epf.set("")
    designation.set("")
    mobile.set("")
    model.set("")
    imei.set("")
    remark.set("")

def clear_user():
    name.set("")
    epf.set("")
    designation.set("")
    mobile.set("")
    imei.set("")


name_lable = ctk.CTkLabel(master = frame1, text="Name", justify="right")
name_lable.grid(row = 0, column = 0, pady=8)

name=StringVar()
name_entry = ctk.CTkEntry(master = frame1, textvariable=name, width=230)
name_entry.grid(row = 0, column = 1)

epf_lable = ctk.CTkLabel(master = frame1, text="EPF")
epf_lable.grid(row = 1, column = 0, pady=8 )

epf=StringVar()
epf_entry = ctk.CTkEntry(master = frame1, textvariable=epf, width=230)
epf_entry.grid(row = 1, column = 1)

Designation_lable = ctk.CTkLabel(master = frame1, text="Designation")
Designation_lable.grid(row = 2, column = 0, pady=8 )

designation=StringVar()
Designation_entry = ctk.CTkEntry(master = frame1, textvariable=designation, width=230)
Designation_entry.grid(row = 2, column = 1)

Mobile_lable = ctk.CTkLabel(master = frame1, text="Mobile")
Mobile_lable.grid(row = 3, column = 0, pady=8 )

mobile=StringVar()
Mobile_entry = ctk.CTkEntry(master = frame1, textvariable=mobile, width=230)
Mobile_entry.grid(row = 3, column = 1)

mobile_check_var = ctk.StringVar(value="1")
mobile_check = ctk.CTkCheckBox(master = frame1, text="", variable=mobile_check_var, onvalue="1", offvalue="0")
mobile_check.grid(row = 3, column = 2, padx=20)

phone_lable = ctk.CTkLabel(master = frame1, text="Phone Model")
phone_lable.grid(row = 4, column = 0, pady=8)

model=StringVar()
model_entry = ctk.CTkEntry(master = frame1, textvariable=model, width=230)
model_entry.grid(row = 4, column = 1)

imei_lable = ctk.CTkLabel(master = frame1, text="IMEI")
imei_lable.grid(row = 5, column = 0, pady=8)

imei=StringVar()
imei_entry = ctk.CTkEntry(master = frame1, textvariable=imei, width=230)
imei_entry.grid(row = 5, column = 1)

remark_lable = ctk.CTkLabel(master = frame1, text="Remark")
remark_lable.grid(row = 6, column = 0, pady=8)

remark=StringVar()
remark_entry = ctk.CTkEntry(master = frame1, textvariable=remark, width=230)
remark_entry.grid(row = 6, column = 1)

phone_check_var = ctk.StringVar(value="1")
phone_check = ctk.CTkCheckBox(master = frame2, text="Phone", variable=phone_check_var, onvalue="1", offvalue="0")
phone_check.grid(row = 7, column = 0, padx=20, pady=20)

battery_check_var = ctk.StringVar(value="0")
battery_check = ctk.CTkCheckBox(master = frame2, text="Battery", variable=battery_check_var, onvalue="1", offvalue="0")
battery_check.grid(row = 7, column = 1, padx=20, pady=20)

charger_check_var = ctk.StringVar(value="0")
charger_check = ctk.CTkCheckBox(master = frame2, text="Charger", variable=charger_check_var, onvalue="1", offvalue="0")
charger_check.grid(row = 7, column = 2, padx=20)

data_cable_check_var = ctk.StringVar(value="0")
data_cable_check = ctk.CTkCheckBox(master = frame2, text="Data Cable", variable=data_cable_check_var, onvalue="1", offvalue="0")
data_cable_check.grid(row = 8, column = 0, padx=20)

sim_check_var = ctk.StringVar(value="0")
sim_check = ctk.CTkCheckBox(master = frame2, text="SIM", variable=sim_check_var, onvalue="1", offvalue="0")
sim_check.grid(row = 8, column = 1, padx=20, pady=20)

hands_free_check_var = ctk.StringVar(value="0")
hands_free_check = ctk.CTkCheckBox(master = frame2, text="Hands Free", variable=hands_free_check_var, onvalue="1", offvalue="0")
hands_free_check.grid(row = 8, column = 2, padx=20)

clear_all_button = ctk.CTkButton(master = frame2, text="Clear all", command=clear_all, width=100)
clear_all_button.grid(row = 9, column = 0, pady=20)

clear_user_button = ctk.CTkButton(master = frame2, text="Clear user", command=clear_user, width=100)
clear_user_button.grid(row = 9, column = 1, pady=20)

generate_button = ctk.CTkButton(master = frame2, text="Generate", command=generate, width=100)
generate_button.grid(row = 9, column = 2, pady=20)
# run
window.mainloop()