import cv2
import numpy as np
from tkinter import *
import csv
def resmiklasordenal(dosyaadi):
    resim = cv2.imread(yol.get()%dosyaadi)
    return resim
ad=0
def resimayar():
    i=1
    a = np.array(["label"])
    for i in range(784):
        a = np.append(a, "pixel%s" % i)
    with open(csvadi.get(), 'a') as f:
        writer = csv.writer(f)
        writer.writerow(a)
    for i in range(int(adet.get())):
        klasordenalinmisresim=0
        if i%2==0:
            ad=8
        else:
            ad=1
        i = i + 1
        string='%s.jpg'%i
        klasordenalinmisresim=resmiklasordenal(string)
        boyutlandirilmisresim=cv2.resize(klasordenalinmisresim,(28,28))
        boyutlandirilmisresim=boyutlandirilmisresim.flatten()
        boyutlandirilmisresim=np.hstack((ad,boyutlandirilmisresim))
        print(i+1)
        with open(csvadi.get(), 'a') as f:
            writer = csv.writer(f)
            writer.writerow(boyutlandirilmisresim)

#GUI oluşturma
root=Tk()
root.geometry("300x200")

#Fotoğrafları diziye dönüştürme bölümü
yol=StringVar()
adet=StringVar()
csvadi=StringVar()
root.title("Dönüştürme")
dosyayolutxt=Label(root,text='Dosya Yolu :').place(x=10,y=20)
boxyol=Entry(root,text='%s',textvariable=yol).place(x=100,y=20)
örn=Label(root,text='../%s').place(x=230,y=20)
dosyaadettxt=Label(root,text='Dosya Adedi :').place(x=10,y=50)
boxadet=Entry(root,text='%s',textvariable=adet).place(x=100,y=50)
csvadettxt=Label(root,text='CSV Adı :').place(x=10,y=80)
csvboxadet=Entry(root,text='%s',textvariable=csvadi).place(x=100,y=80)
donusturbutton=Button(root,text='Dönüştür',command=resimayar).place(x=100,y=110)
root.mainloop()