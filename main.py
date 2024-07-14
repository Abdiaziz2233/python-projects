# import threading
# import time

# def eat_breakfast():
#     time.sleep(3)
#     print("Finished eating breakfast")

# def drink_coffee():
#     time.sleep(4)
#     print("Finished drinking coffee")

# def study():
#     time.sleep(5)
#     print("Finished studying")

# def timer():
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print("Logged in for", count, " seconds")

# # Create threads for each task
# x = threading.Thread(target=eat_breakfast)
# y = threading.Thread(target=drink_coffee)
# z = threading.Thread(target=study)

# # Start threads
# x.start()
# y.start()
# z.start()

# # Join threads to wait for completion
# x.join()
# y.join()
# z.join()

# # Ask user if they wish to exit

# x =threading.Thread(target=timer)
# x.start()
# answer = input("Do you wish to exit the program? ")

# # Implement further logic based on user input (not specified in your original code)
# import time
# from multiprocessing import Process, cpu_count

# def counter(num):
#     count = 0
#     while count < num:
#         count += 1

# def main():
#     start_time = time.perf_counter()
#     print("Number of CPUs:", cpu_count())
    
#     processes = []
#     num_processes = 4  # Adjust this number as needed
    
#     for _ in range(num_processes):
#         p = Process(target=counter, args=(1250000000,))
#         processes.append(p)
#         p.start()

#     for p in processes:
#         p.join()

#     end_time = time.perf_counter()
#     print("Finished in", end_time - start_time, "seconds")

# if __name__ == "__main__":







# #     main()
# from tkinter import *

# # Create the main window












# from tkinter import *

# # Create the main window







# from tkinter import *

# # Create the main window
# window = Tk()
# window.geometry("420x420")  # Set window size
# window.title("Zizo's First Personal Programming")  # Set window title
# window.config(background='#62f5e1')  # Set background color

# # Set window icon
# icon = PhotoImage(file="Apple.png")
# window.iconphoto(True, icon)

# # Load an image
# photo = PhotoImage(file='Apple.png')

# # Create a label widget with text, image, and other properties
# label = Label(window,
#               text="Hello, World!",
#               font=('Arial', 40, 'bold'),
#               fg='#00ff00',
#               bg='black',
#               relief=RAISED,
#               bd=10,
#               padx=20,
#               pady=20,
#               compound='top',  # 'compound' should be a string ('top' in this case)
#               image=photo)

# # Pack the label widget into the window with some padding
# label.pack(pady=50)
# window.mainloop()







# from tkinter import *
# import tkinter as tk

# count = 0



# def click():
#     print()
#     global count
#     count += 1
#     print(count)

# # Create the main window
# window = Tk()

# # # Load image
# # photo = PhotoImage(file="photo.jpg")


# button = tk.Button(window,
#                    text="Click me!",
#                    command=click,
#                    font=("Comic Sans MS", 30),
#                    fg="#00ff00",        
#                    bg="black",          
#                    activeforeground="#00ff00",  
#                    activebackground="black",     
#                    state=ACTIVE,  
#                 #    image=photo,
#                    compound="bottom")



# window.mainloop()







# creating entrybox



# from tkinter import *

# def submit():
#     username = entry.get()
#     print("hello SALAT HASSAN GURE", username)

# def delete():
#     entry.delete(0, END)

# def backspace():
#     current_text = entry.get()
#     entry.delete(len(current_text)-1, END)

# window = Tk()

# entry = Entry(window, font=("arial", 50), fg="green", bg="black")
# entry.pack(side=LEFT)

# submit_button = Button(window, text="Submit", command=submit)
# submit_button.pack(side=RIGHT)

# delete_button = Button(window, text="Delete", command=delete)
# delete_button.pack(side=RIGHT)

# backspace_button = Button(window, text="Backspace", command=backspace)
# backspace_button.pack(side=RIGHT)

# window.mainloop()







# # creating checkedbox

# from tkinter import *


# def display():
#     if x.get() == 1:
#         print("You agree")
#     else:
#         print("You disagree")

# # Create the main Tkinter window
# window = Tk()

# x = IntVar()


# check_button = Checkbutton(window, 
#                            text="I agree to something", 
#                            variable=x, 
#                            onvalue=1, 
#                            offvalue=0, 
#                            command=display,
#                            font=("Arial", 20),
#                            fg="#00ff00",
#                            bg="black",
#                            activeforeground="#00ff00",
#                            activebackground="black",
#                            padx=25,
#                            pady=10   
#                            )

# # Pack the Checkbutton widget into the window
# check_button.pack()

# # Start the Tkinter event loop
# window.mainloop()










# import tkinter as tk
# from tkinter import Label, Radiobutton, PhotoImage

# window = tk.Tk()
# window.title("Pizza Image Example")

# food = ['pizza', 'hamburger', 'hotdog']

# pizzaImage = PhotoImage(file="")
# hamburgerImage = PhotoImage(file="")
# hotdogImage = PhotoImage(file="")

# foodImages = [pizzaImage, hamburgerImage, hotdogImage]

# x = tk.IntVar()

# for index in range(len(food)):
#     radiobutton = Radiobutton(window,
#                               text=food[index],
#                               variable=x,
#                               value=index,
#                               compound=tk.LEFT,
#                               padx=25,
#                               font=("impact", 20),
#                               image=foodImages[index])

#     radiobutton.pack(anchor=tk.W)

# window.pizzaImage = pizzaImage
# window.hamburgerImage = hamburgerImage
# window.hotdogImage = hotdogImage

# window.mainloop()













# from tkinter import *

# def submit():
#     print("Temperature is: " + str(scale.get()) + " degrees Celsius")

# window = Tk()

# window.title("Temperature Converter")

# scale = Scale(window, 
#               from_=0,
#               to=100, 
#               length=600,
#             #   showvalue=0, 
#               resolution=5, 
#               tickinterval=10,
#               troughcolor="#69FAFF",
#               fg="#FF1C00",
#               bg="#111111",
        
#               orient=VERTICAL)
# scale.pack(pady=20)
# scale.set(((scale["from"] - scale["to"]) / 2) + scale["to"])


# coldImage =PhotoImage(file="")
# coldlabel =Label(image =coldImage)
# coldlabel.pack()

# button = Button(window, text="Submit", command=submit)
# button.pack()

# window.mainloop()





















# creating box hotel menu

# from tkinter import *

# def submit():
#     selected_indices = listbox.curselection()
#     if selected_indices:
#         selected_items = [listbox.get(index) for index in selected_indices]
#         print(f"You ordered: {', '.join(selected_items)}")
#     else:
#         print("Please select an item from the list.")

# def add():
#     new_item = entry.get().strip()
#     if new_item: 
#         listbox.insert(END, new_item)
#         listbox.config(height=listbox.size()) 
#         entry.delete(0, END) 
#     else:
#         print("Please enter an item to add.")

# def delete():
#     selected_indices = listbox.curselection()
#     if selected_indices:
#         for index in reversed(selected_indices):  # Delete items from last to first
#             listbox.delete(index)
#         listbox.config(height=listbox.size())
#     else:
#         print("Please select an item to delete.")

# def clear():
#     listbox.delete(0, END)
#     listbox.config(height=listbox.size())

# def exit_program():
#     window.destroy()

# window = Tk()

# listbox = Listbox(window, 
#                 bg="#f7ffde", 
#                 font=("constantia", 35),
#                 width=12, 
#                 selectmode=MULTIPLE)
# listbox.pack()

# initial_items = ["Pizza", 
#                  "Garlic bread", 
#                  "pasta", "Hotdog", "Hamburger",
#                  "Rice saldato", "Ugali sukuma", 
#                  "Caybacayn", "Tea","Juice","[]"]
# for item in initial_items:
#     listbox.insert(END, item)

# entry = Entry(window)
# entry.pack()

# commands = [
#     ("Submit", submit),
#     ("Add", add),
#     ("Delete", delete),
#     ("Clear", clear),
#     ("Exit", exit_program)
# ]

# for text, command in commands:
#     button = Button(window, text=text, command=command)
#     button.pack()

# window.mainloop()









# creating messagebox 





# from tkinter import *
# from tkinter import messagebox

# def click():
#     answer = messagebox.askyesno(title="Yes or No", message="Do you like to code?")
#     if answer:
#         print("I like to code too!")
#     elif answer is False:
#         print("Do you like watching people doing code?")
#     else:
#         print("You have dodged the question.")

# window = Tk()
# window.title("Message Box Example")

# # Create a button to trigger the message box
# button = Button(window, text='Click me', command=click)
# button.pack(pady=20)

# # Start the Tkinter main loop
# window.mainloop()









# creating colorchooser


# from tkinter import *
# from tkinter import colorchooser

# def click():
#     color = colorchooser.askcolor()
#     if color[1]:
#         colorHex = color[1]
#         print("Selected color:", colorHex)
#         window.config(bg=colorHex)  # Update window background color
#     else:
#         print("No color selected.")

# window = Tk()
# window.geometry("420x420")

# button = Button(window, text="Click me!", command=click)
# button.pack()

# window.mainloop()









# creating inputs 


# from tkinter import *

# def submit():
#     text_input = text.get("1.0", END)
#     print("Input:", text_input)

# window = Tk()
# window.geometry("400x300")
# window.title("Text Input Example")

# text = Text(window, height=10, width=40)
# text.config(font=("Ink Free", 12), bg='light yellow',fg='purple')  # Configure font and background color
# text.pack()

# button = Button(window, text="Submit", command=submit)
# button.pack(pady=10)

# window.mainloop()










# from tkinter import *
# from tkinter import filedialog
# import os

# def openfile():
#     filepath = filedialog.askopenfilename(initialdir="hello")
#     if filepath:
#         # Extract file title (filename) and file type (extension)
#         filename = os.path.basename(filepath)
#         file_extension = os.path.splitext(filename)[1]
        
#         file = open(filepath, "r")
#         file_contents = file.read()
#         file.close()
        
#         # Print file title and file type
#         print("File Title:", filename)
#         print("File Type:", file_extension)
#         print("File Contents:")
#         print(file_contents)

# window = Tk()
# button = Button(window, text="Open", command=openfile)
# button.pack()

# window.mainloop()









# from tkinter import *
# from tkinter import filedialog

# def savefile():
#     filename = filedialog.asksaveasfilename(
#         defaultextension=".txt",
#         filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
#     )

#     if filename == "":
#         return

#     file = open(filename, 'w')
#     filetext = text.get(1.0, END)
#     file.write(filetext)
#     file.close()

# # Create the main window
# window = Tk()
# window.title("Text Editor")

# # Create a Text widget for input
# text = Text(window)
# text.pack()

# # Create a button to trigger the savefile function
# button = Button(window, text="Save", command=savefile)
# button.pack()

# # Start the tkinter main loop
# window.mainloop()













# # all in one files 



# from tkinter import *

# def new_file():
#     print("New file has been created")

# def open_file():
#     print("File has been opened")

# def save_file():
#     print("File has been saved")

# def copy():
#     print("Copy operation")

# def cut():
#     print("Cut operation")

# def paste():
#     print("Paste operation")

# window = Tk()
# window.title("Simple Text Editor")

# menubar = Menu(window)



# # File menu
# filemenu = Menu(menubar, tearoff=0,font=("MV boli",15))
# filemenu.add_command(label='New', command=new_file)
# filemenu.add_command(label='Open', command=open_file)
# filemenu.add_command(label='Save', command=save_file)
# filemenu.add_separator()
# filemenu.add_command(label='Exit', command=window.quit)
# menubar.add_cascade(label='File', menu=filemenu)




# # Edit menu
# editmenu = Menu(menubar, tearoff=0,font=("MV boli",15))
# editmenu.add_command(label='Copy', command=copy)
# editmenu.add_command(label='Cut', command=cut)
# editmenu.add_command(label='Paste', command=paste)
# menubar.add_cascade(label='Edit', menu=editmenu)



# # Display the menu
# window.config(menu=menubar)
# window.mainloop()








# from tkinter import *

# window =Tk()

# frame = Frame(window,bg='pink',bd=5,relief=SUNKEN)
# frame.place(x=100,y=100)
# button = Button(frame, text="w",font=("consolas",25),width=3).pack(side=TOP)
# button = Button(frame, text="A",font=("consolas",25),width=3).pack(side=LEFT)
# button = Button(frame, text="S",font=("consolas",25),width=3).pack(side=LEFT)
# button = Button(frame, text="D",font=("consolas",25),width=3).pack(side=LEFT)

# window.mainloop()   






# creating window 
# from tkinter import *

# def create_window():
#     new_window = Toplevel()
# window = Tk()

# Button(window, text="Creacting new window", command=create_window).pack()


# window.mainloop()

# from tkinter import *
# from tkinter import ttk

# # Create main window
# window = Tk()
# window.title("Tab Example")

# # Create a notebook (tabs container)
# notebook = ttk.Notebook(window)

# # Create tabs (Frames inside the notebook)
# tab1 = Frame(notebook)
# tab2 = Frame(notebook)

# # Add tabs to the notebook with respective labels
# notebook.add(tab1, text="Tab 1")
# notebook.add(tab2, text="Tab 2")

# # Add content to Tab 1
# Label(tab1, text="Hello, this is Tab 1", width=50, height=25).pack()

# # Add content to Tab 2
# Label(tab2, text="Goodbye, this is Tab 2", width=50, height=25).pack()

# # Pack the notebook (this will show the tabs and their content)
# notebook.pack(expand=True, fill="both")

# # Start the tkinter main loop
# window.mainloop()



# grid

# import tkinter as tk

# window = tk.Tk()

# titleLabel = tk.Label(window, text="Enter your info", font=("Arial", 25))
# titleLabel.grid(row=0, column=0, columnspan=2)

# # First Name widgets
# firstNameLabel = tk.Label(window, text="First Name:", width=20, bg='red')
# firstNameLabel.grid(row=1, column=0)
# firstNameEntry = tk.Entry(window)
# firstNameEntry.grid(row=1, column=1)

# # Last Name widgets
# lastNameLabel = tk.Label(window, text="Last Name:", bg='green')
# lastNameLabel.grid(row=2, column=0)
# lastNameEntry = tk.Entry(window)
# lastNameEntry.grid(row=2, column=1)

# # Email widgets
# emailLabel = tk.Label(window, text="Email:", width=30, bg='blue')
# emailLabel.grid(row=3, column=0)
# emailEntry = tk.Entry(window)
# emailEntry.grid(row=3, column=1)

# # Submit button
# submitButton = tk.Button(window, text="Submit")
# submitButton.grid(row=4, column=0, columnspan=2)

# window.mainloop()


from tkinter import *
from tkinter.ttk import Progressbar

def start():
    total_gb = 5
    downloaded_gb = 0
    
    def update_progress():
        nonlocal downloaded_gb
        if downloaded_gb < total_gb:
            downloaded_gb += 0.1  # Simulate downloading 0.1 GB per iteration (adjust as needed)
            progress = downloaded_gb * 100 / total_gb
            bar['value'] = progress
            label.config(text=f"{progress:.1f}%")
            task_label.config(text=f"Downloading {downloaded_gb:.1f} GB / {total_gb} GB")
            # Schedule the next update in 500 milliseconds
            window.after(500, update_progress)
        else:
            # Reset progress bar and labels after completion
            bar['value'] = 0
            label.config(text="0.0%")
            task_label.config(text="Downloading...")
            downloaded_gb = 0
    
    # Start the progress update process
    update_progress()

window = Tk()

bar = Progressbar(window, 
                orient="horizontal",
                length=200, 
                mode='determinate')
bar.pack(pady=10)

label = Label(window, text="0.0%")
label.pack()

task_label = Label(window, text="Downloading...")
task_label.pack()

button = Button(window, text="Download Game", command=start)
button.pack(pady=10)

window.mainloop()









































                   

 








