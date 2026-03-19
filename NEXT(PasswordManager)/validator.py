import re
import string
import tkinter.messagebox

def data_validation_name(data, data_name):
    if len(data) > 0 and len(data) < 14:
        if not re.search(r"\d", data):
            if not any(char in string.punctuation for char in data):
                return True
            else:
                tkinter.messagebox.showerror("ValueError", f"{data_name} entry can't contain punctuation.")
        else:
            tkinter.messagebox.showerror("ValueError", f"{data_name} entry can't contain digits.")    
    else:
        tkinter.messagebox.showerror("Length Error", f"The length of the {data_name} entry is to long or to short.")

def password_validation_name(data):
    if len(data) >= 6 and len(data) < 24:
        return True
    else:
        tkinter.messagebox.showerror("LengtError", "Password must be between 6 and 24 characters")