from tkinter import * 
import webbrowser

def open_smartfit():
	webbrowser.open_new("")
# creer une premiere fenetre 
window = Tk()

# personnaliser cette fenetre
window.title("SmartFit")
window.geometry("720x480")
window.minsize(480, 360)
window.config(background='#020000')

# creer la frame
frame = Frame(window, bg='#020000')

#ajouter un premier texte
label_title = Label(frame, text="Bienvenue sur SmartFit", font=("Arial",  40), bg='#020000', fg='white')
label_title.pack()

# ajouter un second texte 
label_subtitle = Label(frame, text="Votre application de coach sportif", font=("Arial",  25), bg='#020000', fg='white')
label_subtitle.pack()

# ajouter un premier bouton
yt_button = Button(frame, text="Lancez-Vous",font=("Arial",  15), bg='white', fg='#020000', command=open_smartfit)
yt_button.pack(pady=25, fill=X)

# ajouter 
frame.pack(expand=YES)
# afficher 
window.mainloop()
