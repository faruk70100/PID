import serial.tools.list_ports
import tkinter as tk

seri = serial.Serial("COM1", 9600)#seri adında COM1 pinine 9600 baundrate ile arduino senkron olaacak şekilde ayarlandı

def ProSend():
    seri.write(("Kp:"+ent1.get()).encode('ascii'))#bu değişkeni encode fonk ile ascii türünden com1 üzerinden gönderildi
    print(ent1.get())

def IntSend():
    seri.write(("Ki:"+ent2.get()).encode('ascii'))#bu değişkeni encode fonk ile ascii türünden com1 üzerinden gönderildi

def DerSend():
    seri.write(("Kd:"+ent3.get()).encode('ascii'))#bu değişkeni encode fonk ile ascii türünden com1 üzerinden gönderildi

wind = tk.Tk()#çalışacak pencere oluşturuldu
wind.title("led yakma")#pencere başlığı oluşturuldu
wind.geometry('500x500')#pencerenin genişliği belirlendi
e1 = tk.Label(text="Kp değeri gir", font="Arial 12 bold")#kp değeri girileceği yer belirtildi
e1.pack()
ent1 = tk.Entry(width=50)#kp değerlerini yazılacağı alanlar
ent1.pack()
e2 = tk.Label(text="Ki değeri gir", font="Arial 12 bold")#ki değeri girileceği yer belirtildi
e2.pack()
ent2 = tk.Entry(width=50)#ki değerlerini yazılacağı alanlar
ent2.pack()
e3 = tk.Label(text="Kd değeri gir", font="Arial 12 bold")#kd değeri girileceği yer belirtildi
e3.pack()
ent3 = tk.Entry(width=50)#kd değerlerini yazılacağı alanlar
ent3.pack()
b1 = tk.Button(text="Kp gönder", bg="black", fg="white",
               font="Arial 12 bold", command=ProSend) #yazılan değerleri gönderme işlemini başlatan buton
b1.pack()
b2 = tk.Button(text="Ki gönder", bg="black", fg="white",
               font="Arial 12 bold", command=IntSend)
b2.pack()
b3 = tk.Button(text="Kd gönder", bg="black", fg="white",
               font="Arial 12 bold", command=DerSend)
b3.pack()
wind.mainloop()
