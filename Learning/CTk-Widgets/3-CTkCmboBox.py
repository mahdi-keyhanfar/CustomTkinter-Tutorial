import customtkinter as ctk # ==> For import CustomTkinter and make a object from it (ctk)

root = ctk.CTk()
root.title("mahdi-keyhanfar")
root.geometry("400x300")

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

#!  CTkComboBox
combobox = ctk.CTkComboBox(root,
                            values=["option 1", "option 2"],
                            command=combobox_callback)

combobox.set("option 2")

combobox.pack(pady=20) #==> pady=top and bottom ---- padx=left and right

root.mainloop()

# For Learn More Arguments Of Button Read README.md in Repositories Main Page




