import random
import tkinter
from tkinter import *


global player
global comp

options =["r","p","s"]
comp = random.choice(options)

root = Tk()
root.title("Rock-Paper-Scissors")
root.geometry("500x600")
root["bg"] = "orange"


Label(root,text="GAME",font = ("roboto",30),bg="orange").place(x=180,y=20)
Label(root,bg="orange",text="-----------------------------------------------------------------------------------------------------------------------",font = ("roboto")).place(x=0,y=70)



comp = random.choice(options)


def rock():
     global player
     player = "r"
def paper():
     global player
     player = "p"
def scissors():
     global player
     player = "s"

def fun():
      global var
      global bar
      if player == "r":
           var = "Rock"
      elif player == "p":
           var = "Paper"
      else:
           var ="Scissors"
      if comp == "r":
           bar = "Rock"
      elif comp == "p":
           bar = "Paper"
      else:
           bar ="Scissors"    

      if player == comp:
       Label(root,bg="orange",text=f"You choose     :{var} \nComp choose :{bar}",font=("arial",16)).place(x=140,y=310)

       Label(root,bg="orange",text="__ Tie __",font =("bold",17)).place(x=186,y=405)
       
      else:
       if (player == "r"):
         if comp == "p":
                 Label(root,bg="orange",text=f"You choose    :{var} \nComp choose :{bar}",font=("arial",16)).place(x=140,y=310)

                 Label(root,bg="orange",text="__ Comp Wins __",font =("bold",17)).place(x=178,y=405)

          
         else:
          Label(root,bg="orange",text=f"You choose  :{var} \nComp choose :{bar}",font=("arial",16)).place(x=140,y=310)

          Label(root,bg="orange",text="__ Player Won __",font =("bold",17)).place(x=178,y=405)
          

       elif (player=="p"):
        if(comp=="s"):
                 Label(root,bg="orange",text=f"You choose   :{var} \nComp choose :{bar}",font=("arial",16)).place(x=140,y=310)

                 Label(root,bg="orange",text="__ Comp Wins __",font =("bold",17)).place(x=178,y=405)

         
          
        else:
                    Label(root,bg="orange",text=f"You choose     :{var} \nComp choose :{bar}",font=("arial",16)).place(x=140,y=310)

                    Label(root,bg="orange",text="__ Player Won __",font =("bold",17)).place(x=178,y=405)

                                                 
          
       elif(player=="s"):
        if(comp=="r"):
                Label(root,bg="orange",text=f"You choose     :{var} \nComp choose :{bar}",font=("arial",16)).place(x=140,y=310)

                Label(root,bg="orange",text="__ Comp Wins __",font =("bold",17)).place(x=178,y=405)

          
          
        else:
                    Label(root,bg="orange",text=f"You choose     :{var}\nComp choose :{bar}",font=("arial",16)).place(x=140,y=310)

                    Label(root,bg="orange",text="__ Player Won __",font =("bold",17)).place(x=178,y=405)

          








Label(root,text ="Choose any one the the following",bg="orange",font=("",15)).place(x=75,y=100)

b1 =Button(root,text="Rock",font=("",12),fg="#fff",bg="#5A4D41",width=9,bd =3,command=rock).place(x=55,y=150)
b2 =Button(root,text="Paper",font=("",12),width=9,fg="#fff",bg="#FFD700",bd =3,command=paper).place(x=205,y=150)
b3 =Button(root,text="Scissors",font=("",12),width=9,fg="#fff",bg="#454545",bd =3,command=scissors).place(x=355,y=150)

b4 = Button(root, text = "Confirm",font=("",12),fg="#fff",bg="blue",bd =3,command = fun).place(x=215,y=230)








Button(root,text= "Exit ->",fg="#fff",bg="green",width=5,height=1,font=("",10),bd =3,command=root.destroy).place(x=220,y=500)



root.mainloop()





