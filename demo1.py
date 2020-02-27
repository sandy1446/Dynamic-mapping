from tkinter import *
import numpy as np
import time
z=[]
from boundry import y as z
global center
center=[]
def eqn(center):
    global res
    #print("\n",x[0],y[0],x[1],y[1])
    a=int(center[0][3][1])-int(center[0][3][0])
    b=int(center[0][2][0])-int(center[0][2][1])
    c=(int(center[0][2][0])*(int(center[0][3][0])-int(center[0][3][1]))-int(center[0][3][0])*(int(center[0][2][0])-int(center[0][2][1])))
    #print(x[0],y[0])
    res=a*int(center[0][0])+b*int(center[0][1])+c
    print(res)
    #print("\n",x1,y1)
    #print("\n",a,b,c)
    #print("\n",res)     
x1=20
y1=30
my_window = Tk()
my_canvas = Canvas(my_window,width=400,height=400,background='black')
my_canvas.grid(row=0,column=0)
i=0
j=1
k=0
s=0
u=0
while (k<4):
    center.append([x1,y1,z[i],z[j]])
    print(center)
    print(type(center))
    t=eqn(center)
    my_canvas.create_line(z[i][0],z[i][1],z[j][0],z[j][1],fill='white')
    if res<0:
        print("in at",i)
        u+=1
        my_canvas.create_line(x1,y1,x1+1,y1+1,fill='white')
    else:
        print("out at",i)
        s+=1
        my_canvas.create_line(x1,y1,x1+1,y1+1,fill='red')
    i+=1
    j+=1
    k+=1
    if j==4:
        j=0
    if i==4:
        i=0
    if k==4:
        break
   # print("\n",s)
    time.sleep(0.5)
    center.clear()
if s==4 or u==4:
    print("inside the boundry")
else:
    print("outside the boundry")
my_window.mainloop()
