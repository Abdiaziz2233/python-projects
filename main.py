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

# Set window icon
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
# Start the main event loop







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







# from tkinter import *


# def display():
#     if x.get() == 1:
#         print("You agree")
#     else:
#         print("You disagree")

# # Create the main Tkinter window
# window = Tk()

# # Initialize an IntVar to hold the state of the Checkbutton
# x = IntVar()

# # Create a Checkbutton widget
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
#                            padx=25,  # Horizontal padding around the text
#                            pady=10   # Vertical padding around the text
#                            )

# # Pack the Checkbutton widget into the window
# check_button.pack()

# # Start the Tkinter event loop
# window.mainloop()










import tkinter as tk
from tkinter import Label, Radiobutton, PhotoImage

window = tk.Tk()
window.title("Pizza Image Example")

food = ['pizza', 'hamburger', 'hotdog']

pizzaImage = PhotoImage(file="")
hamburgerImage = PhotoImage(file="")
hotdogImage = PhotoImage(file="")

foodImages = [pizzaImage, hamburgerImage, hotdogImage]

x = tk.IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x,
                              value=index,
                              compound=tk.LEFT,
                              padx=25,
                              font=("impact", 20),
                              image=foodImages[index])

    radiobutton.pack(anchor=tk.W)

window.pizzaImage = pizzaImage
window.hamburgerImage = hamburgerImage
window.hotdogImage = hotdogImage

window.mainloop()









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

# listbox = Listbox(window, bg="#f7ffde", font=("constantia", 35), width=12, selectmode=MULTIPLE)
# listbox.pack()

# initial_items = ["pizza", "garlic bread", "pasta", "ugali", "hamburger","rice saldato", "ugali sukuma", "caybacayn", "",]
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


                   

 








