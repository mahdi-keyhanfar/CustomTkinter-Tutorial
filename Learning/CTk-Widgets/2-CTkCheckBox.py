import customtkinter as ctk # ==> For import CustomTkinter and make a object from it (ctk)

root = ctk.CTk()
root.title("mahdi-keyhanfar")
root.geometry("400x300")

def checkbox_event():
    print("CheckBox Toggled, Current Value:", checkbox_var.get())

#!  CTkCheckBox
checkbox_var = ctk.StringVar(value = "on") # ==> Save On Value In String Variable
checkbox = ctk.CTkCheckBox(root,
                          text = "this is check box", # ==> Title Of CheckBox
                          command = checkbox_event, # ==> Connect Def To CheckBox
                          variable = checkbox_var, # ==> The Value Of CheckBox When App Run
                          onvalue = "on", # ==> The Return Value Of CheckBox When CheckBox Is On
                          offvalue = "off") # ==> The Return Value Of CheckBox When CheckBox Is Off

checkbox.pack(pady = 20) #==> pady=top and bottom ---- padx=left and right

root.mainloop()

# For Learn More Arguments Of Button Read README.md in Repositories Main Page