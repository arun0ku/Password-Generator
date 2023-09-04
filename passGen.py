import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import string
import random
from PIL import Image
import pyperclip

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():
    win = ctk.CTk()
    app = PassGen(win)
    win.mainloop()

class PassGen:
    def __init__(self, root):
        self.root = root
        self.root.title('Password Generator')
        self.root.resizable(0, 0)
        self.root.config(background='black')
        self.frame = ctk.CTkFrame(self.root, width=350, height=400, fg_color='black').pack()

        self.img = ctk.CTkImage(Image.open('imge\\copy_img.jpg').resize((55, 53)))
        ctk.CTkButton(self.root, image=self.img, width=0, border_width=0, text='', bg_color='black', fg_color='black', hover_color='black', command=self.copy1).place(x=280, y=55)

        self.result = tk.StringVar(value='Password')
        ctk.CTkEntry(self.root,textvariable=self.result,width=200,height=35,font=('Microsoft Yahei',18),bg_color='black',border_width=0,justify='right',placeholder_text='Password').place(x=75, y=50)

        self.vr1 = ctk.IntVar()
        self.vr2 = ctk.IntVar()
        self.vr3 = ctk.IntVar()

        ctk.CTkCheckBox(self.root, text=' ALPHBATES',variable=self.vr1, bg_color='black',font=('Microsoft Yahei',18),hover_color=('black'),onvalue=1,offvalue=0).place(x=85, y=120)
        ctk.CTkCheckBox(self.root, text=' Number',variable=self.vr2, bg_color='black',font=('Microsoft Yahei',18),hover_color='black',onvalue=1,offvalue=0).place(x=85, y=160)
        ctk.CTkCheckBox(self.root, text=' Special Characters',variable=self.vr3, bg_color='black',font=('Microsoft Yahei',18),hover_color='black',onvalue=1,offvalue=0).place(x=85, y=200)

        ctk.CTkLabel(self.root,text='Password Length:- ',font=('Microsoft Yahei',18),bg_color='black').place(x=75, y=250)
        self.pass_len = tk.StringVar()
        ctk.CTkEntry(self.root,width=50,justify='center',textvariable=self.pass_len,font=('Microsoft Yahei',16,'bold'),bg_color='black',placeholder_text='0',fg_color='black').place(x=245, y=248)

        ctk.CTkButton(self.root,text='Generate Password',corner_radius=50,bg_color='black',width=200,height=35, command=self.Generate).place(x=75, y=310)

    def Generate(self):

        if str(self.pass_len.get()) > '0':


            if self.vr1.get() == 0 and self.vr2.get() == 0 and self.vr3.get() == 0:
                messagebox.showinfo('Password Generator', 'You have to choose at least two option',parent=self.root)
            elif self.vr1.get() == 1 and self.vr2.get() != 1 and self.vr3.get() != 1:
                messagebox.showinfo('Password Generator', 'You have to choose at least two option', parent=self.root)
            elif self.vr1.get() != 1 and self.vr2.get() == 1 and self.vr3.get() != 1:
                messagebox.showinfo('Password Generator', 'You have to choose at least two option', parent=self.root)
            elif self.vr1.get() != 1 and self.vr2.get() != 1 and self.vr3.get() == 1:
                messagebox.showinfo('Password Generator', 'You have to choose at least two option', parent=self.root)
            else:
                password_length = int(self.pass_len.get())

                if self.vr1.get() == 1 and self.vr2.get() == 1 and self.vr3.get() == 1:
                    characters = string.ascii_letters + string.digits + string.punctuation
                    password = ''.join(random.choice(characters) for _ in range(password_length))
                    self.result.set(password)
                else:
                    if self.vr1.get() and self.vr2.get() == 1:
                        characters = string.ascii_letters + string.digits
                        password = ''.join(random.choice(characters) for _ in range(password_length))
                        self.result.set(password)

                    if self.vr1.get() and self.vr3.get() == 1:
                        characters = string.ascii_letters + string.punctuation
                        password = ''.join(random.choice(characters) for _ in range(password_length))
                        self.result.set(password)

                    if self.vr2.get() and self.vr3.get() == 1:
                        characters = string.digits + string.punctuation
                        password = ''.join(random.choice(characters) for _ in range(password_length))
                        self.result.set(password)
        elif str(self.pass_len.get()) == '':
            messagebox.showinfo('Password Generator', 'please enter the Password Length in the given Box!')
        else:
            messagebox.showerror('Password Generator','Password Length must be greater than 0!')

    def copy1(self):
        if self.result.get() == '':
            messagebox.showerror('Copy','The Password is not generated')
        else:
            self.random_password = self.result.get()
            pyperclip.copy(self.random_password)
            messagebox.showinfo('Copy Password', f'Your password is Copied:-- \n\n=> {self.random_password}',parent=self.root)

if __name__ == '__main__':
    main()

