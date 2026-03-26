import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import tkinter.messagebox
from logic import Manager

#Application windows
class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        #logic Seperation
        self.manager = Manager()

        #Windwos parameters.
        self.title("Password Manager")
        self.minsize(800, 400)
        self.default_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
        self.iconbitmap(self.manager.cwd() + r"\content\pass.ico")
        
        #Frame Creation.
        #Top frame.
        self.frame_top = tk.Frame(self, bg="#0D1117")
        self.frame_top.pack(side="top", fill="both", expand=False)
        self.frame_top.columnconfigure((0,3), weight=1)
        self.frame_top.rowconfigure(0, weight=1)

        #Middle Frame.
        self.frame_middle = tk.Frame(self, bg="#161B22")
        self.frame_middle.pack(side="top", fill="x", expand=False)
        self.frame_middle.columnconfigure(2, weight=1)
        self.frame_middle.rowconfigure((0), weight=1)

        #Bottom frame.
        self.frame_bottom = tk.Frame(self, bg="#161B22")
        self.frame_bottom.pack(side="bottom", fill="both", expand=True)
        self.frame_bottom.columnconfigure(0, weight=1)
        self.frame_bottom.rowconfigure(0, weight=1)

        #initiate treeview.
        self.tree = self.create_tree()

        #Labels.
        self.company_label = create_labels(
                                        parent=self.frame_top,
                                        font=self.default_font,
                                        text="Company",
                                        padx=11,
                                        pady=2,
                                        row=0,
                                        column=0,
                                        gridpadx=5,
                                        gridpady=5,
                                        sticky="es",
                                        columnspan=1,
                                        )
        self.firstname_label = create_labels(
                                        parent=self.frame_top,
                                        font=self.default_font,
                                        text="First name",
                                        padx=5,
                                        pady=2,
                                        row=1,
                                        column=0,
                                        gridpadx=5,
                                        gridpady=5,
                                        sticky="e",
                                        columnspan=1,
                                        )
        self.lastname_label = create_labels(
                                        parent=self.frame_top,
                                        font=self.default_font,
                                        text="Last name",
                                        padx=6,
                                        pady=2,
                                        row=2,
                                        column=0,
                                        gridpadx=5,
                                        gridpady=5,
                                        sticky="e",
                                        columnspan=1,
                                        )
        self.password_label = create_labels(
                                        parent=self.frame_top,
                                        font=self.default_font,
                                        text="Password",
                                        padx=8,
                                        pady=2,
                                        row=3,
                                        column=0,
                                        gridpadx=5,
                                        gridpady=5,
                                        sticky="ne",
                                        columnspan=1,
                                        )

        self.search_label = create_labels(
                                        parent=self.frame_middle,
                                        font=self.default_font,
                                        text="Search",
                                        padx=0,
                                        pady=0,
                                        row=0,
                                        column=0,
                                        gridpadx=0,
                                        gridpady=0,
                                        sticky="w",
                                        columnspan=1,
                                        )
        
        #Buttons.
        self.save_button = create_buttons(
                                        parent=self.frame_top,
                                        font=self.default_font,
                                        text="Save",
                                        padx=0,
                                        pady=0,
                                        row=4,
                                        column=0,
                                        gridpadx=0,
                                        sticky="ne",
                                        command=self.on_click_save_button,
                                        )
        self.delete_button = create_buttons(
                                        parent=self.frame_top,
                                        font=self.default_font,
                                        text="Delete",
                                        padx=0,
                                        pady=0,
                                        row=4,
                                        column=1,
                                        gridpadx=0,
                                        sticky="",
                                        command=self.on_click_delete,
                                        )
        self.generator_button = create_buttons(
                                        parent=self.frame_top,
                                        font=self.default_font,
                                        text="Generate",
                                        padx=0,
                                        pady=0,
                                        row=3,
                                        column=2,
                                        gridpadx=7,
                                        sticky="e",
                                        command=self.on_click_password
                                        )
        
        #Entry.
        self.company_entry = create_entry(
                                        parent=self.frame_top,
                                        font=self.default_font,
                                        row=0,
                                        column=1,
                                        gridpadx=5,
                                        gridpady=5,
                                        sticky="ws",
                                        columnspan=1,
                                        )
        self.firstname_entry = create_entry(
                                        parent=self.frame_top,
                                        font=self.default_font,
                                        row=1,
                                        column=1,
                                        gridpadx=5,
                                        gridpady=5,
                                        sticky="w",
                                        columnspan=1,
                                        )        
        self.lastname_entry = create_entry(
                                        parent=self.frame_top,
                                        font=self.default_font,
                                        row=2,
                                        column=1,
                                        gridpadx=5,
                                        gridpady=5,
                                        sticky="w",
                                        columnspan=1,
                                        )
        self.password_entry = create_entry(
                                        parent=self.frame_top,
                                        font=self.default_font,
                                        row=3,
                                        column=1,
                                        gridpadx=5,
                                        gridpady=5,
                                        sticky="nw",
                                        columnspan=1,
                                        )
        self.search_entry = create_entry(
                                        parent=self.frame_middle,
                                        font=self.default_font,
                                        row=0,
                                        column=1,
                                        gridpadx=0,
                                        gridpady=0,
                                        sticky="ew",
                                        columnspan=2,
                                        )

    #Create treeview.
    def create_tree(self):
        style = ttk.Style(self)
        self.tree = ttk.Treeview(self.frame_bottom)
        self.tree.grid(row=0, column=0, rowspan=1, columnspan= 1, sticky="nesw")
        self.tree["columns"] = ("1", "2", "3", "4", "5")
        self.tree["show"] = "headings"

        style.theme_use("clam")
        style.configure("Treeview", background="#161B22", fieldbackground="#161B22", foreground="#39FF14")
        style.configure("Treeview.Heading",
                        background="#161B22",
                        foreground="#39FF14",
                        relief="flat")
        style.map("Treeview.Heading", background=[("active", "#2EA043")])

        self.tree.column("1", width=1, anchor="center")
        self.tree.column("2", width=90, anchor="center")
        self.tree.column("3", width=90, anchor="center")
        self.tree.column("4", width=90, anchor="center")
        self.tree.column("5", width=90, anchor="center")

        self.tree.heading("1", text="Id")
        self.tree.heading("2", text ="Company")
        self.tree.heading("3", text ="Firstname")
        self.tree.heading("4", text ="Lastname")
        self.tree.heading("5", text ="Password")

        self.data_insert_treeview() #Insert data into treeview.
        return self.tree
    
    #insert data into treeview.
    def data_insert_treeview(self):
        data = self.manager.database_data()
        for row in data:
            self.tree.insert("", "end", iid=None, values=(row[0], row[1], row[2], row[3], row[4]))
    
    #Generate password.
    def on_click_password(self):
        self.password_entry.config(state="normal")
        self.password_entry.delete(0, "end")
        self.password_entry.insert("end", f"{self.manager.password()}")
         
    #Update Treeview.
    def treeview_update(self):        
        for every_item in self.tree.get_children():
            self.tree.delete(every_item)
        self.data_insert_treeview()

    #Get the entry data from the fields and strip the white space.
    def get_entry_data(self):
        company = self.company_entry.get().strip()
        firstname = self.firstname_entry.get().strip()
        lastname = self.lastname_entry.get().strip()
        password = self.password_entry.get().strip()
        return company, firstname, lastname, password
    
    #Delete the entry data.
    def delete_entry_data(self):
        self.company_entry.delete(0, "end")
        self.firstname_entry.delete(0, "end")
        self.lastname_entry.delete(0, "end")
        self.password_entry.delete(0, "end")

    #Copy password entry.
    def copy_password(self):
        self.clipboard_clear()
        self.clipboard_append(self.password_entry.get())
        self.update()

    #delete item in treeview and updates the treeview.
    def on_click_delete(self):
        selection = self.tree.selection()
        for selection_iid in selection:
            selection_details = self.tree.item(selection_iid)
            iid, company, firstname, lastname, password = selection_details.get("values")
            if self.manager.delete_data(iid, company, firstname, lastname, password):
                continue
        self.treeview_update()
            
    #Saves entrys on button press.
    def on_click_save_button(self):
        company, firstname, lastname, password = self.get_entry_data()
        validation = self.manager.data_validation(company, firstname, lastname, password)
        if validation:
            self.treeview_update()
            self.copy_password()
            self.delete_entry_data()
        else:
            tkinter.messagebox.showerror("Entry Error", "Please check your entrys.\nThey can't contain digits or punctuation.")

#Button creation.
def create_buttons(parent, font,text, padx, pady, row, column, gridpadx, sticky, command):
    button = tk.Button(
                    parent,
                    text=text,
                    font=font,
                    padx=padx,
                    pady=pady,
                    bg="#2EA043",
                    fg="#39FF14",
                    command=command               
                    )
    button.grid(row=row, column=column, padx=gridpadx ,sticky=sticky)
    return button

#Entry creation.
def create_entry(parent, font, row, column, gridpadx, gridpady, sticky, columnspan):
    entry = tk.Entry(
            parent,
            font=font,
            bg="#161B22",
            fg="#39FF14",
            )
    entry.grid(row=row, column=column, padx=gridpadx, pady=gridpady, sticky=sticky ,columnspan=columnspan)
    return entry

#Label creation.
def create_labels(parent, font, text, padx, pady, row, column, gridpadx, gridpady, sticky, columnspan):

    label = tk.Label(
                                parent,
                                text=text,
                                font=font,
                                padx=padx,
                                pady=pady,
                                bg="#0D1117",
                                fg="#39FF14",
                                )
    label.grid(row=row, column=column, padx=gridpadx, pady=gridpady ,sticky=sticky, columnspan=columnspan)
    return label

if __name__ == "__main__":
    ...