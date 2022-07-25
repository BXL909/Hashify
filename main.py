import tkinter as tk
from tkinter import COMMAND, FLAT, Frame, Text, ttk
from tkinter import filedialog as fd
import hashlib

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

fileloc = ""

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
        #hide any label that might exist from previous hashes
        hashinfolabel = tk.Label(root, text="",background='#333', fg='orange',anchor="w",justify="left")
        hashinfolabel.place(width=380,x=10, y=158)           

        hashedresultbox.config(state='normal')
        hashedresultbox.delete("1.0", "end")
        hashedresultbox.insert("1.0",'#ify v1.0\nhttps://github.com/BXL909\n \n'+RICKROLL)
        hashedresultbox.config(state='disabled')


# --- functions ---

def is_it_in_tuple(tuple, thing_to_search):
    for each_hash in tuple:
        if each_hash == thing_to_search:
            return True
    return False 

def hash_it(thing_to_be_hashed,type_of_hash_wanted):
    import hashlib

    #validate type_of_hash_wanted
    if is_it_in_tuple(hashlib.algorithms_available, type_of_hash_wanted):
        #convert to bytes
        byte_encoded_thing_to_be_hashed = thing_to_be_hashed.encode()
        #construct the function name e.g hashlib.sha256(thingtobehashed) and call it. This is to avoid a massive IF statement.. 
        # e.g if sha256 then hashlib.sha256(blah). if sha384 then hashlib.sha384blahblah, etc.
        hashed_result = eval("hashlib." + type_of_hash_wanted)(byte_encoded_thing_to_be_hashed)
        #construct a list to return to the calling code
        hashed_list = [str(hashed_result.hexdigest()), str(hashed_result.digest_size), str(hashed_result.block_size)]
        return hashed_list
    else:
        print ("Invalid selection")

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
        hashedresult = hash_it(a,b)
        hashedresultbox.config(state='normal')
        hashedresultbox.delete("1.0", "end")
        hashedresultbox.insert("1.0",hashedresult[0])
        hashedresultbox.config(state='disabled')
        stringforlabel = b+" hash for input '" + a + "'"
        if len(stringforlabel) > 60:
            formattedstringforlabel = (stringforlabel[:60]+'...')
        else:
            formattedstringforlabel = stringforlabel
        #remove new lines from the string (purely for displaying)
        hashinfolabel = tk.Label(root, text=formattedstringforlabel.replace('\n', ''),background='#333', fg='orange',anchor="w",justify="left")
        hashinfolabel.place(width=380,x=10, y=158)        
        
def hashfile(type_of_hash_wanted,stringtohash):
    algo_valid = 'n'
    for algorithm in algos_available:
        if algorithm == combo.get():
            algo_valid = 'y'
    if algo_valid != 'y':
        hashedresultbox.config(state='normal')
        hashedresultbox.delete("1.0", "end")
        hashedresultbox.insert("1.0",'There is no spoon')
        hashedresultbox.config(state='disabled')
    else:
        if stringtohash == "":
            hashinfolabel = tk.Label(root, text="You need to select a file first",background='#333', fg='orange',anchor="w",justify="left")
            hashinfolabel.place(width=380,x=10, y=158)                
        else:
            filename = stringtohash
            h = eval("hashlib." + type_of_hash_wanted + "()")
            with open(filename, 'rb') as file:
                while True:
                    # Reading is buffered, so we can read smaller chunks.
                    chunk = file.read(h.block_size)
                    if not chunk:
                        break
                    h.update(chunk)
            hashedresultbox.config(state='normal')
            hashedresultbox.delete("1.0", "end")
            hashedresultbox.insert("1.0",h.hexdigest())
            hashedresultbox.config(state='disabled')
            stringforlabel = type_of_hash_wanted + " hash for file " + filename
            if len(stringforlabel) > 60:
                formattedstringforlabel = (stringforlabel[:60]+'...')
            else:
                formattedstringforlabel = stringforlabel
            #remove new lines from the string (purely for displaying)
            hashinfolabel = tk.Label(root, text=formattedstringforlabel.replace('\n', ''),background='#333', fg='orange',anchor="w",justify="left")
            hashinfolabel.place(width=380,x=10, y=158)           

def callbackfunc(event):
    hashtext.focus()
    combo.selection_clear()

def copytextbox():
    root.clipboard_clear()
    root.clipboard_append(hashedresultbox.get(1.0,'end'))
    root.update()
    copiedlabel = tk.Label(root, text='Copied to clipboard',background='#333', fg='orange')
    copiedlabel.place(width=114,x=110, y=130)
    root.after(3000, copiedlabel.destroy)    

def openfile():
    filename = fd.askopenfilename()
    global fileloc
    fileloc = filename
    if len(filename) > 38:
        filenamefordisplay = (filename[:38]+'...')
    else:
        filenamefordisplay = filename
    filelocationlabel = tk.Label(root, text=filenamefordisplay,background='#333', fg='#eee',anchor="w",justify="left")
    filelocationlabel.place(width=280,x=41, y=34)   
    
    


# --- main ---

root = tk.Tk()

root.overrideredirect(True)
root.geometry('400x240+200+200')
title_bar = MyTitleBar(root) 
window = tk.Canvas(root, bg=WINDOW_BACKGROUND, highlightthickness=0)

# dummy button behind text box to give border to text box and put orange lines on the window (must be a better way to do this!)
btndummy1 = tk.Button(relief=FLAT, text='', background='#888')
btndummy1.place(width=382, height=60,x=9,y=61)
btndummy2 = tk.Button(relief=FLAT, text='', background='orange')
btndummy2.place(width=400, height=1,x=0,y=23)
btndummy3 = tk.Button(relief=FLAT, text='', background='orange')
btndummy3.place(width=400, height=1,x=0,y=239)
btndummy4 = tk.Button(relief=FLAT, text='', background='orange')
btndummy4.place(width=400, height=1,x=0,y=0)
btndummy5 = tk.Button(relief=FLAT, text='', background='orange')
btndummy5.place(width=1, height=250,x=0,y=0)
btndummy6 = tk.Button(relief=FLAT, text='', background='orange')
btndummy6.place(width=1, height=250,x=399,y=0)

# text box
hashtext = tk.Text(root, undo=True, height = 3,background='#222',fg='#eee',border=0,padx=5,pady=5, insertbackground='#eee')
hashtext.place( width=380, x=10, y=62)
hashtext.focus_set()

# combobox
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "#222", background= "#222", foreground="orange",darkcolor="#222",lightcolor="#222" )
combo = ttk.Combobox(root, width= 70,)
combo.set("sha256")
cache=list()
algos_available = ['sha3_224', 'sha3_384', 'sha512', 'sha3_256', 'sha3_512', 'sha256', 'sha1', 'sha224', 'md5', 'blake2b', 'blake2s', 'sha384']
algos_available.sort()
for algorithm in algos_available:
    cache.append(algorithm)
combo['values'] = cache
combo.place( width=70, x=10, y=130)
combo.bind("<<ComboboxSelected>>",callbackfunc)

# open file button
btnopenfile = tk.Button(relief=FLAT, text='open', command=lambda: openfile(),background='orange')
btnopenfile.place(width=60, height=18,x=330,y=34)

# hash input button
btn = tk.Button(relief=FLAT, text='#ify text', command=lambda: hashbuttonpressed(hashtext.get("1.0", "end - 1 chars"),combo.get()),background='orange')
btn.place(width=60, height=18,x=330,y=130)

# hash file button
btnhashfile = tk.Button(relief=FLAT, text='#ify file', command=lambda: hashfile(combo.get(),fileloc),background='orange')
btnhashfile.place(width=60, height=18,x=260,y=130)

# text box
hashedresultbox = tk.Text(root, undo=True, height = 3,background='#333',fg='#eee',border=0,padx=5,pady=5,cursor="hand2")
hashedresultbox.place(width=390,x=6,y=174)
hashedresultbox.insert("1.0", " ")
hashedresultbox.config(state='disabled')
hashedresultbox.bind("<Button-1>", lambda e:copytextbox())

#label 
fileinfolabel = tk.Label(root, text="File: ",background='#333', fg='orange',anchor="w",justify="left")
fileinfolabel.place(width=40,x=10, y=34)           

#label
filelocationlabel = tk.Label(root, text="No file selected.",background='#333', fg='#eee',anchor="w",justify="left")
filelocationlabel.place(width=280,x=41, y=34)           

# pack the widgets
window.pack(expand=True, fill='both')

root.mainloop()
