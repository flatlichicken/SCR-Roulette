import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import time
import random

# Create the main application window
root = tk.Tk()
root.title("SCR Roulette")
root.geometry("400x400")
root.resizable(False, False)


def next():
    # 1. This checks: "Have I made the page variable yet?"
    if not hasattr(next, "page"):
        next.page = 1  # This ONLY runs the very first time you click
        
    
    
    # 2. Now, everywhere you had "page", change it to "next.page"
    if next.page == 1:
        Page1.pack_forget()
        Page2.pack(fill="both", expand=True)
        next.page = 2
        print(next.page)
        
    elif next.page == 2: # Use 'elif' so it doesn't skip pages instantly
        Page2.pack_forget()
        Page3.pack(fill="both", expand=True)
        next.page = 3
        print(next.page)

    elif next.page == 3:
        Page3.pack_forget()
        Page4.pack(fill="both", expand=True)
        next.page = 4
        print(next.page)

    elif next.page == 4:
        Page4.pack_forget()
        Page5.pack(fill="both", expand=True)
        next.page = 5
        print(next.page)

    elif next.page == 5:
        Page5.pack_forget()
        Page1.pack(fill="both", expand=True)
        next.page = 1 
        print(next.page)

def back():
    # 1. This checks: "Have I made the page variable yet?"
    if not hasattr(next, "page"):
        next.page = 1  # This ONLY runs the very first time you click
        
    
    
    # 2. Now, everywhere you had "page", change it to "next.page"
    if next.page == 1:
        Page1.pack_forget()
        Page5.pack(fill="both", expand=True)
        next.page = 5
        print(next.page)
        
    elif next.page == 2: # Use 'elif' so it doesn't skip pages instantly
        Page2.pack_forget()
        Page1.pack(fill="both", expand=True)
        next.page = 1
        print(next.page)

    elif next.page == 3:
        Page3.pack_forget()
        Page2.pack(fill="both", expand=True)
        next.page = 2
        print(next.page)

    elif next.page == 4:
        Page4.pack_forget()
        Page3.pack(fill="both", expand=True)
        next.page = 3
        print(next.page)

    elif next.page == 5:
        Page5.pack_forget()
        Page4.pack(fill="both", expand=True)
        next.page = 4 
        print(next.page)        
        
# selector buttons
buttonpannel = tk.Frame(root, height=25, width=400)
buttonpannel.pack(side= 'bottom')

next_button = tk.Button(buttonpannel, text=" > ", command=next)
next_button.pack(side= 'right')

back_button = tk.Button(buttonpannel, text=" < ", command=back)
back_button.pack(side= 'left')


Page1 = tk.Frame(root, height=400, width=400)
Page2 = tk.Frame(root, height=400, width=400)
Page3 = tk.Frame(root, height=400, width=400)
Page4 = tk.Frame(root, height=400, width=400)
Page5 = tk.Frame(root, height=400, width=400)
Page1.pack(fill="both", expand=True)


# Connect Trains

# --- Variables ---
ct1 = tk.IntVar(value=0)
ct2 = tk.IntVar(value=0)
ct3 = tk.IntVar(value=0)
ct4 = tk.IntVar(value=0)
ct5 = tk.IntVar(value=0)
ct6 = tk.IntVar(value=0)
ct7 = tk.IntVar(value=0)
ct8 = tk.IntVar(value=0)
ct9 = tk.IntVar(value=0)
ct10 = tk.IntVar(value=0)
ct11 = tk.IntVar(value=0)
ct12 = tk.IntVar(value=0)
ct13 = tk.IntVar(value=0)
ct14 = tk.IntVar(value=0)
ct15 = tk.IntVar(value=0)
ct16 = tk.IntVar(value=0)
ct17 = tk.IntVar(value=0)
ct18 = tk.IntVar(value=0)
ct19 = tk.IntVar(value=0)
ct20 = tk.IntVar(value=0)
ct21 = tk.IntVar(value=0)
ct22 = tk.IntVar(value=0)
ct23 = tk.IntVar(value=0)
ct24 = tk.IntVar(value=0)
ct25 = tk.IntVar(value=0)
ct26 = tk.IntVar(value=0)
ct27 = tk.IntVar(value=0)
ct28 = tk.IntVar(value=0)
ct29 = tk.IntVar(value=0)
ct30 = tk.IntVar(value=0)
ct31 = tk.IntVar(value=0)

labelconnect = tk.Label(Page1, text="Connect Trains")
labelconnect.pack(pady=5)

Dconnect_trains_frame = tk.Frame(Page1)
Dconnect_trains_frame.pack(pady=10)
Dconnect_trains_frame.place(x=10, y=50) 


# Diesel Checkboxes

c1 = tk.Checkbutton(Dconnect_trains_frame, text='Class 68', variable=ct1, onvalue=1, offvalue=0)
c1.pack(anchor='w')

c2 = tk.Checkbutton(Dconnect_trains_frame, text='Class 156', variable=ct2, onvalue=1, offvalue=0)
c2.pack(anchor='w')

c3 = tk.Checkbutton(Dconnect_trains_frame, text='Class 156 (Double)', variable=ct3, onvalue=1, offvalue=0)
c3.pack(anchor='w')

c4 = tk.Checkbutton(Dconnect_trains_frame, text='Class 158/0', variable=ct4, onvalue=1, offvalue=0)
c4.pack(anchor='w')

c5 = tk.Checkbutton(Dconnect_trains_frame, text='Class 158/9', variable=ct5, onvalue=1, offvalue=0)
c5.pack(anchor='w')

c6 = tk.Checkbutton(Dconnect_trains_frame, text='Class 158/9 (Double)', variable=ct6, onvalue=1, offvalue=0)
c6.pack(anchor='w')

c7 = tk.Checkbutton(Dconnect_trains_frame, text='Class 168', variable=ct7, onvalue=1, offvalue=0)
c7.pack(anchor='w')

c8 = tk.Checkbutton(Dconnect_trains_frame, text='Class 170/2', variable=ct8, onvalue=1, offvalue=0)
c8.pack(anchor='w')

c9 = tk.Checkbutton(Dconnect_trains_frame, text='Class 170/4', variable=ct9, onvalue=1, offvalue=0)
c9.pack(anchor='w')

c10 = tk.Checkbutton(Dconnect_trains_frame, text='Class 170/2 (Double)', variable=ct10, onvalue=1, offvalue=0)
c10.pack(anchor='w')

c11 = tk.Checkbutton(Dconnect_trains_frame, text='Class 185', variable=ct11, onvalue=1, offvalue=0)
c11.pack(anchor='w')

c12 = tk.Checkbutton(Dconnect_trains_frame, text='Class 195', variable=ct12, onvalue=1, offvalue=0)
c12.pack(anchor='w')


Econnect_trains_frame = tk.Frame(Page1)
Econnect_trains_frame.pack(pady=5)
Econnect_trains_frame.place(x=150, y=50)

# Electric Checkboxes

c13 = tk.Checkbutton(Econnect_trains_frame, text='Class 321', variable=ct13, onvalue=1, offvalue=0)
c13.pack(anchor='w')

c14 = tk.Checkbutton(Econnect_trains_frame, text='Class 331/0', variable=ct14, onvalue=1, offvalue=0)
c14.pack(anchor='w')

c15 = tk.Checkbutton(Econnect_trains_frame, text='Class 331/1', variable=ct15, onvalue=1, offvalue=0)
c15.pack(anchor='w')

c16 = tk.Checkbutton(Econnect_trains_frame, text='Class 333', variable=ct16, onvalue=1, offvalue=0)
c16.pack(anchor='w')

c17 = tk.Checkbutton(Econnect_trains_frame, text='Class 350/1', variable=ct17, onvalue=1, offvalue=0)
c17.pack(anchor='w')

c18 = tk.Checkbutton(Econnect_trains_frame, text='Class 350/2', variable=ct18, onvalue=1, offvalue=0)
c18.pack(anchor='w')

c19 = tk.Checkbutton(Econnect_trains_frame, text='Class 350/2 (Double)', variable=ct19, onvalue=1, offvalue=0)
c19.pack(anchor='w')

c20 = tk.Checkbutton(Econnect_trains_frame, text='Class 357', variable=ct20, onvalue=1, offvalue=0)
c20.pack(anchor='w')

c21 = tk.Checkbutton(Econnect_trains_frame, text='Class 360', variable=ct21, onvalue=1, offvalue=0)
c21.pack(anchor='w')

c22 = tk.Checkbutton(Econnect_trains_frame, text='Class 365', variable=ct22, onvalue=1, offvalue=0)
c22.pack(anchor='w')

c23 = tk.Checkbutton(Econnect_trains_frame, text='Class 377', variable=ct23, onvalue=1, offvalue=0)
c23.pack(anchor='w')


E2connect_trains_frame = tk.Frame(Page1)
E2connect_trains_frame.pack(pady=5)
E2connect_trains_frame.place(x=290, y=50)

c24 = tk.Checkbutton(E2connect_trains_frame, text='Class 380/0', variable=ct24, onvalue=1, offvalue=0)
c24.pack(anchor='w')

c25 = tk.Checkbutton(E2connect_trains_frame, text='Class 380/1', variable=ct25, onvalue=1, offvalue=0)
c25.pack(anchor='w')

c26 = tk.Checkbutton(E2connect_trains_frame, text='Class 385/0', variable=ct26, onvalue=1, offvalue=0)
c26.pack(anchor='w')

c27 = tk.Checkbutton(E2connect_trains_frame, text='Class 385/1', variable=ct27, onvalue=1, offvalue=0)
c27.pack(anchor='w')

c28 = tk.Checkbutton(E2connect_trains_frame, text='Class 700', variable=ct28, onvalue=1, offvalue=0)
c28.pack(anchor='w')

c29 = tk.Checkbutton(E2connect_trains_frame, text='Class 707', variable=ct29, onvalue=1, offvalue=0)
c29.pack(anchor='w')

c30 = tk.Checkbutton(E2connect_trains_frame, text='Class 720', variable=ct30, onvalue=1, offvalue=0)
c30.pack(anchor='w')

c31 = tk.Checkbutton(E2connect_trains_frame, text='Class 730/1', variable=ct31, onvalue=1, offvalue=0)
c31.pack(anchor='w')


# Metro Trains

# --- Variables ---
mt1 = tk.IntVar(value=0)
mt2 = tk.IntVar(value=0)
mt3 = tk.IntVar(value=0)
mt4 = tk.IntVar(value=0)
mt5 = tk.IntVar(value=0)
mt6 = tk.IntVar(value=0)
mt7 = tk.IntVar(value=0)
mt8 = tk.IntVar(value=0)
mt9 = tk.IntVar(value=0)

labelmetro = tk.Label(Page2, text="Metro Trains")
labelmetro.pack(pady=5)

# Checkboxes

metro_trains_frame = tk.Frame(Page2)
metro_trains_frame.place(x=150, y=50)


m1 = tk.Checkbutton(metro_trains_frame, text='Class 398', variable=mt1, onvalue=1, offvalue=0)
m1.pack(anchor='w')

m2 = tk.Checkbutton(metro_trains_frame, text='Class 398 (Double)', variable=mt2, onvalue=1, offvalue=0)
m2.pack(anchor='w')

m3 = tk.Checkbutton(metro_trains_frame, text='Class 555', variable=mt3, onvalue=1, offvalue=0)
m3.pack(anchor='w')

m4 = tk.Checkbutton(metro_trains_frame, text='Class 555 (Double)', variable=mt4, onvalue=1, offvalue=0)
m4.pack(anchor='w')

m5 = tk.Checkbutton(metro_trains_frame, text='Class 717', variable=mt5, onvalue=1, offvalue=0)
m5.pack(anchor='w')

m6 = tk.Checkbutton(metro_trains_frame, text='Class 756/0', variable=mt6, onvalue=1, offvalue=0)
m6.pack(anchor='w')

m7 = tk.Checkbutton(metro_trains_frame, text='Class 756/1', variable=mt7, onvalue=1, offvalue=0)
m7.pack(anchor='w')

m8 = tk.Checkbutton(metro_trains_frame, text='Class 777', variable=mt8, onvalue=1, offvalue=0)
m8.pack(anchor='w')

m9 = tk.Checkbutton(metro_trains_frame, text='Class 777 (Double)', variable=mt9, onvalue=1, offvalue=0)
m9.pack(anchor='w')


# Waterline Trains

# --- Variables ---
wt1 = tk.IntVar(value=0)
wt2 = tk.IntVar(value=0)
wt3 = tk.IntVar(value=0)
wt4 = tk.IntVar(value=0)
wt5 = tk.IntVar(value=0)
wt6 = tk.IntVar(value=0)
wt7 = tk.IntVar(value=0)
wt8 = tk.IntVar(value=0)
wt9 = tk.IntVar(value=0)
wt10 = tk.IntVar(value=0)
wt11 = tk.IntVar(value=0)
wt12 = tk.IntVar(value=0)

labelwaterline = tk.Label(Page3, text="Waterline Trains")
labelwaterline.pack(pady=5)

# Checkboxes

waterline_trains_frame = tk.Frame(Page3)
waterline_trains_frame.place(x=150, y=50)

w1 = tk.Checkbutton(waterline_trains_frame, text='Class 143', variable=wt1, onvalue=1, offvalue=0)
w1.pack(anchor='w')

w2 = tk.Checkbutton(waterline_trains_frame, text='Class 143 (Double)', variable=wt2, onvalue=1, offvalue=0)
w2.pack(anchor='w')

w3 = tk.Checkbutton(waterline_trains_frame, text='Class 165', variable=wt3, onvalue=1, offvalue=0)
w3.pack(anchor='w')

w4 = tk.Checkbutton(waterline_trains_frame, text='Class 165 (Double)', variable=wt4, onvalue=1, offvalue=0)
w4.pack(anchor='w')

w5 = tk.Checkbutton(waterline_trains_frame, text='Class 166', variable=wt5, onvalue=1, offvalue=0)
w5.pack(anchor='w')

w6 = tk.Checkbutton(waterline_trains_frame, text='Class 171', variable=wt6, onvalue=1, offvalue=0)
w6.pack(anchor='w')

w7 = tk.Checkbutton(waterline_trains_frame, text='Class 195/0', variable=wt7, onvalue=1, offvalue=0)
w7.pack(anchor='w')

w8 = tk.Checkbutton(waterline_trains_frame, text='Class 195/1', variable=wt8, onvalue=1, offvalue=0)
w8.pack(anchor='w')

w9 = tk.Checkbutton(waterline_trains_frame, text='Class 313', variable=wt9, onvalue=1, offvalue=0)
w9.pack(anchor='w')

w10 = tk.Checkbutton(waterline_trains_frame, text='Class 319', variable=wt10, onvalue=1, offvalue=0)
w10.pack(anchor='w')

w11 = tk.Checkbutton(waterline_trains_frame, text='Class 379', variable=wt11, onvalue=1, offvalue=0)
w11.pack(anchor='w')

w12 = tk.Checkbutton(waterline_trains_frame, text='Class 730/0', variable=wt12, onvalue=1, offvalue=0)
w12.pack(anchor='w')

# Express Trains

# --- Variables ---
et1 = tk.IntVar(value=0)
et2 = tk.IntVar(value=0)
et3 = tk.IntVar(value=0)
et4 = tk.IntVar(value=0)
et5 = tk.IntVar(value=0)
et6 = tk.IntVar(value=0)
et7 = tk.IntVar(value=0)
et8 = tk.IntVar(value=0)
et9 = tk.IntVar(value=0)
et10 = tk.IntVar(value=0)
et11 = tk.IntVar(value=0)
et12 = tk.IntVar(value=0)
et13 = tk.IntVar(value=0)
et14 = tk.IntVar(value=0)
et15 = tk.IntVar(value=0)
et16 = tk.IntVar(value=0)
et17 = tk.IntVar(value=0)
et18 = tk.IntVar(value=0)
et19 = tk.IntVar(value=0)
et20 = tk.IntVar(value=0)
et21 = tk.IntVar(value=0)
et22 = tk.IntVar(value=0)
et22 = tk.IntVar(value=0)
et23 = tk.IntVar(value=0)
et24 = tk.IntVar(value=0)

label = tk.Label(Page4, text="Express Trains")
label.pack(pady=5)

# Checkboxes

express_trains_frame = tk.Frame(Page4)
express_trains_frame.place(x=30, y=50)

e1 = tk.Checkbutton(express_trains_frame, text='Class 43 HST', variable=et1, onvalue=1, offvalue=0)
e1.pack(anchor='w')

e2 = tk.Checkbutton(express_trains_frame, text='Class 43 HST (5 Car)', variable=et2, onvalue=1, offvalue=0)
e2.pack(anchor='w')

e3 = tk.Checkbutton(express_trains_frame, text='Class 43 HST (Buffer)', variable=et3, onvalue=1, offvalue=0)
w3.pack(anchor='w')

e4 = tk.Checkbutton(express_trains_frame, text='Class 43 HST (7 Car)', variable=et4, onvalue=1, offvalue=0)
e4.pack(anchor='w')

e5 = tk.Checkbutton(express_trains_frame, text='Class 43 HST (8 Car - Buffer)', variable=et5, onvalue=1, offvalue=0)
e5.pack(anchor='w')

e6 = tk.Checkbutton(express_trains_frame, text='Class 43 HST (9 Car)', variable=et6, onvalue=1, offvalue=0)
e6.pack(anchor='w')

e7 = tk.Checkbutton(express_trains_frame, text='Class 91 (7 Car)', variable=et7, onvalue=1, offvalue=0)
e7.pack(anchor='w')

e8 = tk.Checkbutton(express_trains_frame, text='Class 91 (9 Car)', variable=et8, onvalue=1, offvalue=0)
e8.pack(anchor='w')

e9 = tk.Checkbutton(express_trains_frame, text='Class 180', variable=et9, onvalue=1, offvalue=0)
e9.pack(anchor='w')

e10 = tk.Checkbutton(express_trains_frame, text='Class 180 (Double)', variable=et10, onvalue=1, offvalue=0)
e10.pack(anchor='w')

e11 = tk.Checkbutton(express_trains_frame, text='Class 220', variable=et11, onvalue=1, offvalue=0)
e11.pack(anchor='w')

e12 = tk.Checkbutton(express_trains_frame, text='Class 220 (Double)', variable=et12, onvalue=1, offvalue=0)
e12.pack(anchor='w')

# Checkboxes 2

express2_trains_frame = tk.Frame(Page4)
express2_trains_frame.place(x=220, y=50)

e13 = tk.Checkbutton(express2_trains_frame, text='Class 221', variable=et13, onvalue=1, offvalue=0)
e13.pack(anchor='w')

e14 = tk.Checkbutton(express2_trains_frame, text='Class 221 (Double)', variable=et14, onvalue=1, offvalue=0)
e14.pack(anchor='w')

e15 = tk.Checkbutton(express2_trains_frame, text='Class 390 (9 Car)', variable=et15, onvalue=1, offvalue=0)
e15.pack(anchor='w')

e16 = tk.Checkbutton(express2_trains_frame, text='Class 390 (11 Car)', variable=et16, onvalue=1, offvalue=0)
e16.pack(anchor='w')

e17 = tk.Checkbutton(express2_trains_frame, text='Class 397/0', variable=et17, onvalue=1, offvalue=0)
e17.pack(anchor='w')

e18 = tk.Checkbutton(express2_trains_frame, text='Class 397/0 (Double)', variable=et18, onvalue=1, offvalue=0)
e18.pack(anchor='w')

e19 = tk.Checkbutton(express2_trains_frame, text='Class 800/1', variable=et19, onvalue=1, offvalue=0)
e19.pack(anchor='w')

e20 = tk.Checkbutton(express2_trains_frame, text='Class 800/2', variable=et20, onvalue=1, offvalue=0)
e20.pack(anchor='w')

e21 = tk.Checkbutton(express2_trains_frame, text='Class 800/2 (Double)', variable=et21, onvalue=1, offvalue=0)
e21.pack(anchor='w')

e22 = tk.Checkbutton(express2_trains_frame, text='Class 801/1', variable=et22, onvalue=1, offvalue=0)
e22.pack(anchor='w')

e23 = tk.Checkbutton(express2_trains_frame, text='Class 801/2', variable=et23, onvalue=1, offvalue=0)
e23.pack(anchor='w')

e24 = tk.Checkbutton(express2_trains_frame, text='Class 801/1 (Double)', variable=et24, onvalue=1, offvalue=0)
e24.pack(anchor='w')


# Airlink Trains
label = tk.Label(Page5, text="Airlink Trains")
label.pack(pady=5)

      


def ListTrains(): 
    
    trainlist = []

    if ct1.get() == 1:
     trainlist.append('Class 68')

    if ct2.get() == 1:
     trainlist.append('Class 156') 

    if ct3.get() == 1:
     trainlist.append('Class 156 (Double)')

    if ct4.get() == 1:
     trainlist.append('Class 158/0')

    if ct5.get() == 1:
     trainlist.append('Class 158/9')

    if ct6.get() == 1:
     trainlist.append('Class 158/9 (Double)') 

    if ct7.get() == 1:
     trainlist.append('Class 168')

    if ct8.get() == 1:
     trainlist.append('Class 170/2')  

    if ct9.get() == 1:
     trainlist.append('Class 170/4')

    if ct10.get() == 1:
     trainlist.append('Class 170/2 (Double)') 

    if ct11.get() == 1:
     trainlist.append('Class 185')

    if ct12.get() == 1:
     trainlist.append('Class 195')

    if ct13.get() == 1:
     trainlist.append('Class 321')

    if ct14.get() == 1:
     trainlist.append('Class 331/0')

    if ct15.get() == 1:
     trainlist.append('Class 331/1')  

    if ct16.get() == 1:
     trainlist.append('Class 333')  

    if ct17.get() == 1:
     trainlist.append('Class 350/1')

    if ct18.get() == 1:
     trainlist.append('Class 350/2')

    if ct19.get() == 1:
     trainlist.append('Class 350/2 (Double)') 

    if ct20.get() == 1:
     trainlist.append('Class 357')
     
    if ct21.get() == 1:
     trainlist.append('Class 360')

    if ct22.get() == 1:
     trainlist.append('Class 365')

    if ct23.get() == 1:
     trainlist.append('Class 377')

    if ct24.get() == 1:
     trainlist.append('Class 380/0')

    if ct25.get() == 1:
     trainlist.append('Class 380/1')

    if ct26.get() == 1:
     trainlist.append('Class 385/0')

    if ct27.get() == 1:
     trainlist.append('Class 385/1')

    if ct28.get() == 1:
     trainlist.append('Class 700')

    if ct29.get() == 1:
     trainlist.append('Class 707')

    if ct30.get() == 1:
     trainlist.append('Class 720')

    if ct31.get() == 1:
     trainlist.append('Class 730/1') 


    if mt1.get() == 1:
     trainlist.append('Class 398')

    if mt2.get() == 1:
     trainlist.append('Class 398 (Double)') 

    if mt3.get() == 1:
     trainlist.append('Class 555')

    if mt4.get() == 1:
     trainlist.append('Class 555 (Double)')

    if mt5.get() == 1:
     trainlist.append('Class 717')

    if mt6.get() == 1:
     trainlist.append('Class 756/0') 

    if mt7.get() == 1:
     trainlist.append('Class 756/1')

    if mt8.get() == 1:
     trainlist.append('Class 777')  

    if mt9.get() == 1:
     trainlist.append('Class 777 (Double)') 


    if wt1.get() == 1:
     trainlist.append('Class 143')

    if wt2.get() == 1:
     trainlist.append('Class 143 (Double)') 

    if wt3.get() == 1:
     trainlist.append('Class 165')

    if wt4.get() == 1:
     trainlist.append('Class 165 (Double)')

    if wt5.get() == 1:
     trainlist.append('Class 166')

    if wt6.get() == 1:
     trainlist.append('Class 171') 

    if wt7.get() == 1:
     trainlist.append('Class 195/0')

    if wt8.get() == 1:
     trainlist.append('Class 195/1')  

    if wt9.get() == 1:
     trainlist.append('Class 313')

    if wt10.get() == 1:
     trainlist.append('Class 319') 

    if wt11.get() == 1:
     trainlist.append('Class 373')

    if wt12.get() == 1:
     trainlist.append('Class 730/0')     
    
    print(trainlist)
    
    Page1.pack_forget()
    Page2.pack_forget()
    Page3.pack_forget()
    Page4.pack_forget()
    Page5.pack_forget()
    buttonpannel.pack_forget()
    

    if trainlist:
        # Only try to pick a random item if the list is not empty
        randomtrain = random.choice(trainlist)
        print(f"The randomly selected train is: {randomtrain}")
        resultlabel = tk.Label(root, text=f"Your Random Train is the {randomtrain}!")
        resultlabel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        return randomtrain # Optional: return the value for use elsewhere
    else:

        resultlabel = tk.Label(root, text="No Trains Selected!")
        resultlabel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        # Handle the case where no trains were selected
        print("Error: The train list is empty because no options were selected.")


Random_button = tk.Button(buttonpannel, text=" Randomize ", command=ListTrains)
Random_button.pack(side= 'right')



root.mainloop()

