from tkinter import *

root=Tk()
root.title("LABO")
root.geometry('400x500')
root.resizable(width=False,height=False)

#menu and submenu
main_menu=Menu(root)

file_menu=Menu(root)
#add commands to the submenu
file_menu.add_command(label='New..')
file_menu.add_command(label='Save As ..')
file_menu.add_command(label='Exit')

main_menu.add_cascade(label='File',menu=file_menu)

#add the rest of the menu options to the main menu
main_menu.add_command(label='Edit')
main_menu.add_command(label='Quit')
root.config(menu=main_menu)

#conversation window
chatWindow=Text(root, bd=1, bg="black",  width="50", height="8", font=("Arial", 23), foreground="#00ffff")
chatWindow.place(x=6,y=6,height=385,width=370)

#text area window
messageWindow = Text(root, bd=0, bg="black",width="30", height="4", font=("Arial", 23), foreground="#00ffff")
messageWindow.place(x=128, y=400, height=88, width=260)

scrollbar=Scrollbar(root,command=chatWindow.yview,cursor='star')
scrollbar.place(x=375,y=5,height=385)

#submit button
button=Button(root, text="Send",  width="12", height=5,
                    bd=0, bg="#0080ff", activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12))

button.place(x=6,y=400,height=88)

root.mainloop()
