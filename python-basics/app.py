from tkinter import * 
def hello():
    print("hello i love being pegged")
root = Tk()
root.geometry("600x600")

frame_one = Frame(root)
frame_one.pack()

button_one = Button(frame_one , text="Say i love being pegged", command = hello)
button_one.pack()

root.mainloop()

