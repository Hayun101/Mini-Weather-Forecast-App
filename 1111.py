from tkinter.ttk import Label

import requests
import tkinter

window = tkinter.Tk()
window.title("Weather App")
window.geometry("500x250")

url = input("Enter your url:")
response = requests.get(url)
print(response.json())
name = response.json()["location"]["name"]
country = response.json()["location"]["country"]
temp_c = response.json()["current"]["temp_c"]
temp_f =response.json()["current"]["temp_f"]
weather =response.json()["current"]["condition"]["text"]
label1 = Label(text="Location:",font=("Arial",15))
label1.place(x=0, y=60)
label2 = Label(text=name+", "+country,font=("Arial",15))
label2.place(x=120, y=60)
label3 = Label(text="Temp.(C):",font=("Arial",15))
label3.place(x=0, y=90)
label4 = Label(text=temp_c,font=("Arial",15))
label4.place(x=120, y=90)
label5 = Label(text="Temp.(F):",font=("Arial",15))
label5.place(x=0, y=120)
label6 = Label(text=temp_f,font=("Arial",15))
label6.place(x=120, y=120)
label7 = Label(text="Weather:",font=("Arial",15))
label7.place(x=0, y=150)
label8 = Label(text=weather,font=("Arial",15))
label8.place(x=120, y=150)
label9 = Label(text="Short Weather İnformation",font=("Arial",15))
label9.pack()
window.mainloop()