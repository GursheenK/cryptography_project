from email.mime import text
import tkinter
from tkinter import ttk
from tkinter import font
import customtkinter
from vigenere import *
from vigenerecryptanalysis import *

def validate_field(entryField):
    if len(entryField.get())==0:
        entryField.configure(placeholder_text='Field cannot be empty!',placeholder_text_color='#fe5963')
        return False
    else: 
        return True

def encrypt():
    plain_text=entryText.get()
    key=entryKey.get()
    if validate_field(entryText) & validate_field(entryKey):
        enc=encrypt_words(plain_text,key)
        entryResult.configure(textvariable=tkinter.StringVar(value=enc))

def decrypt():
    cipher_text=entryText.get()
    key=entryKey.get()
    if validate_field(entryText) & validate_field(entryKey):
        dec=decrypt_words(cipher_text,key)
        entryResult.configure(textvariable=tkinter.StringVar(value=dec))

def cryptanalysis():
    cipher_text=entryText1.get()
    if validate_field(entryText1):
        possible_decodes,best_sol=hackVigenere(cipher_text)
        pd=''
        for i in possible_decodes:
            pd+='\n'+i
        entryPD.configure(textvariable=tkinter.StringVar(value=pd))
        entryBS.configure(textvariable=tkinter.StringVar(value=best_sol))

def clear():
    entryResult.configure(state='normal')
    entryText.delete(0,tkinter.END)
    entryKey.delete(0,tkinter.END)
    entryResult.delete(0,tkinter.END)
    entryText.configure(placeholder_text='text',placeholder_text_color='gray')
    entryKey.configure(placeholder_text='key',placeholder_text_color='gray')
    entryResult.configure(placeholder_text='result',placeholder_text_color='gray')
    entryResult.configure(state='disabled')
    
def clear2():
    entryText1.delete(0,tkinter.END)

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, 

root_tk = customtkinter.CTk()
root_tk.title('Cryptography Project')
root_tk.geometry('900x900') # create CTk window like you do with the Tk window
tabControl = ttk.Notebook(root_tk)
style = ttk.Style()
BG_COLOUR='#1a1a1a'
style.theme_create(
    "name", parent="alt", settings = {
        ".": {"configure": {"background": BG_COLOUR,
                            "foreground": "silver",
                            "relief": "flat"}},
        "TLabel": {"configure": {"foreground": "white","padding": 30,"font": ("Calibri", 50)}},
        "TNotebook": {"configure": {"tabmargins": [0, 10, 10, 0]}
                        },
        "TNotebook.Tab": {
            "configure": {"relief" : "flat",
                            "bordercolor" : BG_COLOUR,
                            "darkcolor" : BG_COLOUR,
                            "lightcolor" : BG_COLOUR,
                            "padding": [10, 1], "background": BG_COLOUR
                            },
            "map": {"background": [("selected", BG_COLOUR)],
                    "expand": [("selected", [1, 1, 1, 0])]}
        }
    })

style.theme_use("name")

tab1 = customtkinter.CTkFrame(master=tabControl,corner_radius=0)
tab2 = customtkinter.CTkFrame(master=tabControl,corner_radius=0)
tabControl.add(tab1, text='  Vigenere Cipher     ',)
tabControl.add(tab2, text='  Cryptanalysis of Vigenere    ')
tabControl.pack(expand=1, fill="both")  #configure "tabs" background color

frame = customtkinter.CTkFrame(master=tab1,corner_radius=10)
frame.pack(padx=5, pady=20)

text_var = tkinter.StringVar(value="Text")
labelText = customtkinter.CTkLabel(master=frame,textvariable=text_var,text_font=('Calibri',14),width=120,height=25,anchor="w")
labelText.grid(row=0,column=0,padx=20,pady=20)

entryText = customtkinter.CTkEntry(master=frame,placeholder_text="text",text_font=('Calibri',14),width=280,height=50,border_width=1,corner_radius=8)
entryText.grid(row=0,column=1,columnspan=2,padx=20,pady=20)

text_var = tkinter.StringVar(value="Key")
labelKey= customtkinter.CTkLabel(master=frame,textvariable=text_var,text_font=('Calibri',14),width=120,height=50,anchor="w")
labelKey.grid(row=1,column=0,padx=20,pady=20)

entryKey = customtkinter.CTkEntry(master=frame,placeholder_text="key",text_font=('Calibri',14),width=280,height=50,border_width=1,corner_radius=8)
entryKey.grid(row=1,column=1,columnspan=2,padx=20,pady=20)

text_var = tkinter.StringVar(value="Result")
labelResult = customtkinter.CTkLabel(master=frame,textvariable=text_var,text_font=('Calibri',14),width=120,height=25,anchor="w")
labelResult.grid(row=2,column=0,padx=20,pady=20)

entryResult = customtkinter.CTkEntry(master=frame,placeholder_text="result",text_font=('Calibri',14),state='disabled',width=280,height=50,border_width=1,corner_radius=8)
entryResult.grid(row=2,column=1,columnspan=2,padx=20,pady=20)

buttonEncrypt = customtkinter.CTkButton(master=frame,width=120,height=32,text_font=('Calibri',14),border_width=0,corner_radius=8,text="Encrypt",command=encrypt)
buttonEncrypt.grid(row=3,column=0,padx=20,pady=20)

buttonDecrypt = customtkinter.CTkButton(master=frame,width=120,height=32,text_font=('Calibri',14),border_width=0,corner_radius=8,text="Decrypt",command=decrypt)
buttonDecrypt.grid(row=3,column=1,padx=20,pady=20)

buttonClear = customtkinter.CTkButton(master=frame,width=120,height=32,text_font=('Calibri',14),border_width=0,corner_radius=8,text="Clear",command=clear)
buttonClear.grid(row=3,column=2,padx=20,pady=20)

frame2 = customtkinter.CTkFrame(master=tab2,corner_radius=10)
frame2.pack(padx=10, pady=20)

text_var = tkinter.StringVar(value="Cipher Text")
labelText1 = customtkinter.CTkLabel(master=frame2,textvariable=text_var,text_font=('Calibri',14),width=140,height=25,anchor="w")
labelText1.grid(row=0,column=0,padx=20,pady=20)

entryText1= customtkinter.CTkEntry(master=frame2,placeholder_text="text",text_font=('Calibri',14),width=600,height=50,border_width=1,corner_radius=8)
entryText1.grid(row=0,column=1,columnspan=2,padx=20,pady=20)

text_var = tkinter.StringVar(value="Possible Decodes")
labelText1 = customtkinter.CTkLabel(master=frame2,textvariable=text_var,text_font=('Calibri',14),width=140,height=25,anchor="w")
labelText1.grid(row=1,column=0,padx=20,pady=20)

text_var = tkinter.StringVar(value=" ")
entryPD = customtkinter.CTkLabel(master=frame2,textvariable=text_var,text_font=('Calibri',14),width=600,height=25)
entryPD.grid(row=1,column=1,columnspan=2,padx=20,pady=20)

text_var = tkinter.StringVar(value="Best Solution")
labelText1 = customtkinter.CTkLabel(master=frame2,textvariable=text_var,text_font=('Calibri',14),width=140,height=25,anchor="w")
labelText1.grid(row=2,column=0,padx=20,pady=20)

text_var = tkinter.StringVar(value=" ")
entryBS = customtkinter.CTkLabel(master=frame2,textvariable=text_var,text_font=('Calibri',14),width=600,height=25)
entryBS.grid(row=2,column=1,columnspan=2,padx=20,pady=20)


buttonCryptanalysis = customtkinter.CTkButton(master=frame2,width=270,height=32,text_font=('Calibri',14),border_width=0,corner_radius=8,text="Cryptanalysis",command=cryptanalysis)
buttonCryptanalysis.grid(row=3,column=1,padx=10,pady=20)
buttonClear = customtkinter.CTkButton(master=frame2,width=270,height=32,text_font=('Calibri',14),border_width=0,corner_radius=8,text="Clear",command=clear2)
buttonClear.grid(row=3,column=2,padx=10,pady=20)

root_tk.mainloop()
