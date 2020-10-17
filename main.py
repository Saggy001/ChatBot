from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pyttsx3 as pt

engine=pt.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#speaking
def speak(query):
    engine.say(query)
    engine.runAndWait()

bot = ChatBot("my bot")
trainer=ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

window=Tk()
window.title('CHATBOT')
window.resizable(0,0)
window.geometry('500x545')

def reponse():
    question=entry.get()
    answer=bot.get_response(question)
    txt.insert(END,"\nyou : " + question)
    speak(answer)
    txt.insert(END,"\nbot : "  + str(answer))
    entry.delete(0,END)
    txt.yview(END)

canvas=Canvas(window,bg='light green')
canvas.pack(expand=YES,fill=BOTH)

lb=Label(canvas,text='C\nH\nA\nT',font=('cooper black',30),bg='light green',fg='blue')
lb.place(x=50,y=10)
lb1=Label(canvas,text='B\nO\nT',font=('cooper black',30),fg='blue',bg='light green')
lb1.place(x=400,y=30)
im=PhotoImage(file='chatr.png')
pic=PhotoImage(file='mic2.png')
canvas.create_image(140,5,anchor=NW,image=im)
txt=Listbox(canvas,bg='powder blue',width=52,height=9,fg='blue',font=40)
txt.place(x=8,y=230)
scr=Scrollbar(canvas,orient=VERTICAL,command=txt.yview)
txt.configure(yscrollcommand=scr.set)
scr.place(x=480,y=230,height=175)
fr=Frame(canvas,bg='pink',height=125,width=485)
fr.place(x=8,y=410)

entry=Entry(canvas,bd=9,bg='white',text='Enter Message',fg='black',font='-size 10',width=65)
entry.place(x=13,y=420)

btn1=Button(canvas,text='Clear',bd=4,bg='red',activeforeground='black',activebackground='white',command=lambda:entry.delete(0,END),padx=30,pady=5)
btn1.place(x=180,y=480)

btn=Button(canvas,image=pic,bd=4,bg='green',activeforeground='white',activebackground='red',command=lambda: reponse(),padx=0,pady=10,)
btn.place(x=300,y=479)

# press enter button

def action(event):
    btn.invoke()

window.bind('<Return>',action)

window.mainloop()



