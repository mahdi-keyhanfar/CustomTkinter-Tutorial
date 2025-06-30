import customtkinter as ctk # ==> For import CustomTkinter and make a object from it (ctk)

root = ctk.CTk()
root.title("mahdi-keyhanfar")
root.geometry("400x300")

def combobox_callback(choice): # ==> For Save Selected Option Of CombiBox
    print("combobox dropdown clicked:", choice) # ==> For Print Selected Option Of ComboBox

#!  CTkComboBox
combobox = ctk.CTkComboBox(root,
                            values=["option 1", "option 2"], # ==> Values Of ComboBox
                            command=combobox_callback) # ==> Connect Def To ComboBox

combobox.set("option 2") # ==> Select a default Value Or Option For ComboBox

combobox.pack(pady=20) #==> pady=top and bottom ---- padx=left and right

root.mainloop()

# For Learn More Arguments Of Button Read README.md in Repositories Main Page
