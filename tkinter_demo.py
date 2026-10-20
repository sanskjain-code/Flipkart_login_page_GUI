from tkinter import *                    #GUI library
from PIL import ImageTk,Image            #Library to add image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = pass_input.get()

    if email == 'rani@gmail.com' and password == '1997':
        messagebox.showinfo('Yayy!','Login Successful')
    else:
        messagebox.showerror('Error','Invalid Password')
root = Tk()                              #Obj
root.title("Login Page")                 #title at link
root.iconbitmap('shopping_logo.ico')              #Icon

#root.minsize(500,500)
#root.maxsize(700,700)

root.geometry('400x600')                       #Structure : LXB
root.configure(background='#0096DC')         #Bacground colour   (config==confgiure)

img = Image.open('flipkart_logo.png')          #PNG file ko open karta hai aur ek Image object banata hai.
resized_img = img.resize((100,100))            #Resizing it
img = ImageTk.PhotoImage(resized_img)          #Pillow Image ko Tkinter-compatible format me convert karta hai.

img_label = Label(root,image=img)              #root : window & image=img show krega
img_label.pack(pady=(10,10))                   #Pack show krne me madad krta h + pady="padding k liye"

text_label = Label(root,text='Flipkart',fg='white',bg='#0096DC')                 #fg=foreground & bg=background
text_label.pack()                                                                  #Pack used to show label
text_label.config(font=('verdana',24))         #text, color, font, background, image, etc  --> configure also

email_label = Label(root,text='Enter your email : ',fg='white',bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))

email_input = Entry(root,width=50)             #Entry : Block for entries
email_input.pack(ipady=5,pady=(1,10))          #ipady : height

pass_label = Label(root,text='Enter your password : ',fg='white',bg='#0096DC')
pass_label.pack(pady=(20,5))
pass_label.config(font=('verdana',12))

pass_input = Entry(root,width=50)              #Entry : Block for entries
pass_input.pack(ipady=5,pady=(1,10))  

login_btn = Button(root,text='Login Now',fg='black',bg='white',width=20,height=3,command=handle_login)
login_btn.pack(pady=(60,20))                   #Creating Button
login_btn.config(font=('verdana',12))
root.mainloop()                                #Button click, mouse move, key press, window resize, close button press.