from tkinter import *
import time
import numpy
n=int(input('no of boxes = '))
m=0
center=[]
l=ans='y'
path='/Users/DELL/Desktop/New folder (2)/boundry.txt'
fin=open(path,'w')
my_window = Tk()
my_canvas = Canvas(my_window,width=400,height=400,background='white')
my_canvas.grid(row=0,column=0)
while ans=='y':
    y=[]
    x=[]
    i=0
    while (i<4):
        print('enter the coordinate of vertices')
        print(i)
        x.append([input('enter x['+str(i)+']'),input('enter y['+str(i)+']')])
        i=i+1
    i=0
    while i<4:
        #print(x[i])
        y.append(x[i])
        i=i+1
        time.sleep(.2)
    center.append(y)
    i=0
    j=1
    k=0
    print (center)
    while m<n:
        while k<4:
            #print (center[0][0][0])
            #print (center[0][0][1])
            #print (center[0][1][0])
            #print (center[0][1][1])
            #print (center[0][2][0])
            #print (center[0][2][1])
            #print (center[0][3][0])
            #print (center[0][3][1])
            #my_canvas.create_line(center[m][k][0],center[m][k][1],center[m][j][0],center[m][j][1],fill='red')
            j+=1
            k+=1
            if j==4:
                j=0
            if k==4:
                break
        m+=1
        if m==n:
                break
    ans=input('do you want ot continue')
    if ans=='n':
        break
m=0
j=1
while m<n:
     k=0
     while k<4:
         print(center[m][k][0])
         print(center[m][k][1])
         print(center[m][j][0])
         print(center[m][j][1])
         my_canvas.create_line(center[m][k][0],center[m][k][1],center[m][j][0],center[m][j][1],fill='red')
         #my_canvas.create_line(center[m][k][0],center[m][k][1],center[m][j][0],center[m][j][1],fill='green')
         k+=1
         j+=1
         if j==4:
             j=0
         if k==4:
             break
     m+=1
     print(m)
fin.write(str(center))
print(center)
fin.close()
