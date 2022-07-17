import tkinter as tk
from tkinter import COMMAND, FLAT, Frame, Text, ttk
import hashit

# --- constants ---

RICKROLL = "We\'re no strangers to love\nYou know the rules and so do I (do I)\nA full commitment\'s what I\'m thinking of\nYou wouldn\'t get this from any other guy\nI just wanna tell you how I\'m feeling\nGotta make you understand\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nWe\'ve known each other for so long\nYour heart\'s been aching, but you\'re too shy to say it (say it)\nInside, we both know what\'s been going on (going on)\nWe know the game and we\'re gonna play it\nAnd if you ask me how I\'m feeling\nDont tell me you\'re too blind to see\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nWe\'ve known each other for so long\nYour heart\'s been aching, but you\'re too shy to say it (to say it)\nInside, we both know what\'s been going on (going on)\nWe know the game and we\'re gonna play it\nI just wanna tell you how I\'m feeling\nGotta make you understand\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\
\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you"

# title bar colors
TITLE_FOREGROUND = "orange"
TITLE_BACKGROUND = "#222"
TITLE_BACKGROUND_HOVER = "#222"

BUTTON_FOREGROUND = "orange"
BUTTON_BACKGROUND = TITLE_BACKGROUND
BUTTON_FOREGROUND_HOVER = BUTTON_FOREGROUND
BUTTON_BACKGROUND_HOVER = 'orange'

# window colors
WINDOW_BACKGROUND = "#333"
WINDOW_FOREGROUND = "orange"

# --- classes --- 

class MyButton(tk.Button):

    def __init__(self, master, text='x', command=None, **kwargs):
        super().__init__(master, bd=0,  padx=5, pady=2, 
                         fg=BUTTON_FOREGROUND, 
                         bg=BUTTON_BACKGROUND,
                         activebackground=BUTTON_BACKGROUND_HOVER,
                         activeforeground=BUTTON_FOREGROUND_HOVER, 
                         highlightthickness=0, 
                         text=text,
                         command=command)

        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)

    def on_enter(self, event):
        self['bg'] = BUTTON_BACKGROUND_HOVER

    def on_leave(self, event):
        self['bg'] = BUTTON_BACKGROUND

class MyTitleBar(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, relief='flat', bd=1, 
                         bg=TITLE_BACKGROUND,
                         highlightcolor=TITLE_BACKGROUND, 
                         highlightthickness=0)

        self.title_label = tk.Label(self, 
                                    bg=TITLE_BACKGROUND, 
                                    fg=TITLE_FOREGROUND)
                                    
        self.set_title("#ify")

        self.close_button = MyButton(self, text='x', command=master.destroy)
        self.other_button = MyButton(self, text='?', command=self.on_other)
                         
        self.pack(expand=True, fill='x')
        self.title_label.pack(side='left')
        self.close_button.pack(side='right')
        self.other_button.pack(side='right')

        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<ButtonRelease-1>", self.on_release)
        self.bind("<B1-Motion>", self.on_move)
        
    def set_title(self, title):
        self.title = title
        self.title_label['text'] = title
        
    def on_press(self, event):
        self.xwin = event.x
        self.ywin = event.y
        self.set_title("#ify")
        self['bg'] = '#222'
        self.title_label['bg'] = TITLE_BACKGROUND_HOVER

    def on_release(self, event):
        self.set_title("#ify")
        self['bg'] = TITLE_BACKGROUND
        self.title_label['bg'] = TITLE_BACKGROUND
        
    def on_move(self, event):
        x = event.x_root - self.xwin
        y = event.y_root - self.ywin
        self.master.geometry(f'+{x}+{y}')
        
    def on_other(self):
        hashedresultbox.config(state='normal')
        hashedresultbox.delete("1.0", "end")
        hashedresultbox.insert("1.0",'#ify v0.1\n(file hashing in next version)\nhttps://github.com/BXL909\n \n'+RICKROLL)
        hashedresultbox.config(state='disabled')


# --- functions ---

def hashbuttonpressed(a,b):
    algo_valid = 'n'
    for algorithm in algos_available:
        if algorithm == b:
            algo_valid = 'y'
    if algo_valid != 'y':
        hashedresultbox.config(state='normal')
        hashedresultbox.delete("1.0", "end")
        hashedresultbox.insert("1.0",'There is no spoon')
        hashedresultbox.config(state='disabled')
    else:
        hashedresult = hashit.hash_it(a,b)
        hashedresultbox.config(state='normal')
        hashedresultbox.delete("1.0", "end")
        hashedresultbox.insert("1.0",hashedresult[0])
        hashedresultbox.config(state='disabled')
        print (hashedresult)

def callbackfunc(event):
    hashtext.focus()
    combo.selection_clear()

def copytextbox():
    root.clipboard_clear()
    root.clipboard_append(hashedresultbox.get(1.0,'end'))
    root.update()
    copiedlabel = tk.Label(root, text='Copied to clipboard',background='#333', fg='orange')
    copiedlabel.place(width=120,x=140, y=100)
    root.after(3000, copiedlabel.destroy)    

# --- main ---

root = tk.Tk()

root.overrideredirect(True)
root.geometry('400x200+200+200')
title_bar = MyTitleBar(root) 
window = tk.Canvas(root, bg=WINDOW_BACKGROUND, highlightthickness=0)

# dummy button behind text box to give border to text box and put orange lines on the window (must be a better way to do this!)
btndummy1 = tk.Button(relief=FLAT, text='', background='#888')
btndummy1.place(width=382, height=60,x=9,y=33)
btndummy2 = tk.Button(relief=FLAT, text='', background='orange')
btndummy2.place(width=400, height=1,x=0,y=23)
btndummy3 = tk.Button(relief=FLAT, text='', background='orange')
btndummy3.place(width=400, height=1,x=0,y=199)
btndummy4 = tk.Button(relief=FLAT, text='', background='orange')
btndummy4.place(width=400, height=1,x=0,y=0)
btndummy5 = tk.Button(relief=FLAT, text='', background='orange')
btndummy5.place(width=1, height=200,x=0,y=0)
btndummy6 = tk.Button(relief=FLAT, text='', background='orange')
btndummy6.place(width=1, height=200,x=399,y=0)

# text box
hashtext = tk.Text(root, undo=True, height = 3,background='#222',fg='#eee',border=0,padx=5,pady=5, insertbackground='#eee')
hashtext.place( width=380, x=10, y=34)
hashtext.focus_set()

# combobox
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "#222", background= "#222", foreground="orange",darkcolor="#222",lightcolor="#222" )
combo = ttk.Combobox(root, width= 25,)
combo.set("sha256")
cache=list()
algos_available = ['sha3_224', 'sha3_384', 'sha512', 'sha3_256', 'sha3_512', 'sha256', 'sha1', 'sha224', 'md5', 'blake2b', 'blake2s', 'sha384']
algos_available.sort()
for algorithm in algos_available:
    cache.append(algorithm)
combo['values'] = cache
combo.place( width=100, x=10, y=100)
combo.bind("<<ComboboxSelected>>",callbackfunc)

# button
btn = tk.Button(relief=FLAT, text='#ify', command=lambda: hashbuttonpressed(hashtext.get("1.0", "end - 1 chars"),combo.get()),background='orange')
btn.place(width=70, height=18,x=320,y=100)

# text box
hashedresultbox = tk.Text(root, undo=True, height = 3,background='#333',fg='#eee',border=0,padx=5,pady=5,cursor="hand2")
hashedresultbox.place(width=390,x=6,y=128)
hashedresultbox.insert("1.0", " ")
hashedresultbox.config(state='disabled')
hashedresultbox.bind("<Button-1>", lambda e:copytextbox())

# pack the widgets
window.pack(expand=True, fill='both')

root.mainloop()
