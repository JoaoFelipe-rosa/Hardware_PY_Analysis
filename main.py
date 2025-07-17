import customtkinter as ctk


# Configs
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("analise de hardware")
app.geometry("500x500")
app.grid_columnconfigure(0, weight=1)

label = "AQUI VAI QUALQUER COISA"

# functionalities
def buttonResponse():
    print("Button Was Pressed")

def checkBoxResponse(checkbox_widget, checkbox):
        if checkbox_widget.get() == 1:
            print(f"Checked {checkbox}")
        else:
            print(f"Unchecked {checkbox}")



button = ctk.CTkButton(app, text="Click Me", command=buttonResponse)
button.pack(padx=20, pady=20)
button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

checkbox_1 = ctk.CTkCheckBox(app, text="checkbox 1")
checkbox_1.configure(command=lambda: checkBoxResponse(checkbox_1, "Checkbox 1"))
checkbox_1.grid(row=3, column=3, padx=20, pady=(0, 20), sticky="w")




label_1 = ctk.CTkLabel(app, text=label, fg_color="transparent")
label_1.grid(row=2, column=0, padx=20, pady=(0, 20) , columnspan=2)







app.mainloop()