import customtkinter as ctk # ==> For import CustomTkinter and make a object from it (ctk)

root = ctk.CTk()
root.title("mahdi-keyhanfar")
root.geometry("400x300")

label = ctk.CTkLabel(root, text="CTkLabel",
                    fg_color="#f00")
label.pack(pady = 20) #==> pady=top and bottom ---- padx=left and right
root.mainloop()

# For Learn More Arguments Of Button Read README.md in Repositories Main Page