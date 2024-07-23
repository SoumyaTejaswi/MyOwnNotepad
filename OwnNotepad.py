import tkinter as tk #libraries imported
from tkinter.filedialog import askopenfilename,asksaveasfilename #filedialog:one of the functions of tkinter.

def saving_file():
    file_location=asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text files","*.txt"),["All files","*.*"]]
    )
    if not file_location: #if no file found at file location. if what then what to do
        return
    with open(file_location,"w") as file_output:
        text=text_edit.get(1.0,tk.END)
        file_output.write(text)
    root.title(f"MY OWN NOTEPAD-{file_location}")
def opening_file():
    file_location=askopenfilename(
        filetypes=[("Text files","*.txt"),("All files","*.*")]
    )
    if not file_location:
        return
    text_edit.delete(1.0,tk.END)
    with open(file_location,"r") as file_input:
        text=file_input.read()
        text_edit.insert(tk.END,text)
    root.title(f"MY OWN NOTEPAD-{file_location}")

root=tk.Tk() #tk:tkinter lib Tk():tkinter function is basicalley used to make a tkinter function.
root.title("My Own Notepad") #for giving title which is stored in root
root.rowconfigure(0,minsize=800) #row value given using rowconfigure 0 is the denotion for row and 1200 is the row.
root.columnconfigure(1,minsize=800)#coloumn value 1 and size 1200

text_edit=tk.Text(root) #text_edit=variable name.tk=tkinter lib Text()=Function which I have in the tkinter lib  and root referring to the table where our edited text will be stored.
text_edit.grid(row=0,column=1,sticky="nsew") #sticky parameter is used to make proper alignments and bringing the buttons to the very top

frame_button=tk.Frame(root,relief=tk.RAISED,bd=3)#making buttons .Typed of button :Raised which is saved in root where tkinter lib is stored.
frame_button.grid(row=0,column=0,sticky="ns")

open_button=tk.Button(frame_button,text="OPEN FILE",command=opening_file) #POSITION?
open_button.grid(row=0,column=0,padx=5,pady=5)

button_save=tk.Button(frame_button,text="SAVE AS",command=saving_file)
button_save.grid(row=1,column=0,padx=5)


root.mainloop() #whenever a program is written using tkinter lib we add the mainloop function at the last to close the loop.
