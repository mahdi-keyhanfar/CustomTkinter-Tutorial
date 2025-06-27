import customtkinter as ctk # ==> For import CustomTkinter and make a object from it (ctk)

root = ctk.CTk()
root.title("mahdi-keyhanfar")
root.geometry("400x300")

def btn_click():
    print("Button Clicked !")

#!  CTkButton
button = ctk.CTkButton(root,
                        text = "Button1", # ==> Button Name
                        command = btn_click) # ==> Connect Def To Button
button.pack() # ==> show button

root.mainloop()

# For Learn More Arguments Of Button Read README.md in Repositories Main Page