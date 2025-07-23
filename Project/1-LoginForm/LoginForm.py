import customtkinter as ctk

root = ctk.CTk(fg_color="#2d3250")
root.title("Money Saver | Login")
root.geometry("400x300")

#! lable
title_lable = ctk.CTkLabel(root,
                           text="Welcome To Money Saver! ",
                           font=("roboto",25,"bold"),
                           text_color="#fff")
title_lable.pack(pady=20)

user_lable = ctk.CTkLabel(root,
                           text="Enter Your Username: ",
                           font=("Vazir Thin",15),
                           text_color="#fff")
user_lable.pack(pady=5)
user_entry = ctk.CTkEntry (root,
                           placeholder_text="Username:",
                           fg_color="#676f9d",
                           text_color="#f9b17a",
                           placeholder_text_color="#f9b17a",
                           width=300) 
user_entry.pack(pady = 5)

pasword_lable = ctk.CTkLabel(root,
                           text="Enter Your Password: ",
                           font=("Vazir Thin",15),
                           text_color="#fff",)
pasword_lable.pack(pady=5)

pasword_entry= ctk.CTkEntry (root,
                           placeholder_text="Password:",
                           fg_color="#676f9d",
                           text_color="#f9b17a",
                           placeholder_text_color="#f9b17a",
                           width=300)
pasword_entry.pack(pady = 5)

botton = ctk.CTkButton (root,
                        text="Login",
                        text_color="#000000",
                        fg_color="#f9b17a",
                        hover_color="#ffcda7")
botton.pack(pady=20)

root.mainloop()