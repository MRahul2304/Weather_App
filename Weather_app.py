from tkinter import*
from tkinter import ttk
import requests


def dataget():

    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=d02413acddc678cecfb11417c4c2f096").json()
    weather_label1.config(text=data["weather"][0]["main"])
    weather_discription1.config(text = data["weather"][0]["description"])
    tem_label1.config(text = str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text = data["main"]["pressure"])


win = Tk()
win.title("My Weather")
win.config(bg="light blue")
win.geometry("720x720")

name_label = Label(win,text = "Weather", font = ("Lexend",40, "bold") )
name_label.place(x = 120, y = 70, height = 70, width = 550)

city_name = StringVar()
list_name = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Delhi",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jammu and Kashmir",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]

com = ttk.Combobox(win, values = list_name , font = ("Lexend",30, "bold"), textvariable = city_name)
com.place(x = 120, y = 160, height = 70, width = 550)

weather_label = Label(win,text = "Weather Climate", font = ("Lexend", 15, "bold") )
weather_label.place(x = 130, y = 330, height = 40, width = 220)

weather_label1 = Label(win,text = "", font = ("Lexend", 15, "bold") )
weather_label1.place(x = 380, y = 330, height = 40, width = 220)

weather_discription = Label(win,text = "Weather Discription", font = ("Lexend", 15, "bold") )
weather_discription.place(x = 130, y = 380, height = 40, width = 220)

weather_discription1 = Label(win,text = "", font = ("Lexend", 15, "bold") )
weather_discription1.place(x = 380, y = 380, height = 40, width = 220)


tem_label = Label(win,text = "Temprature", font = ("Lexend", 15, "bold") )
tem_label.place(x = 130, y = 430, height = 40, width = 220)

tem_label1 = Label(win,text = "", font = ("Lexend", 15, "bold") )
tem_label1.place(x = 380, y = 430, height = 40, width = 220)


per_label = Label(win,text = "Pressur", font = ("Lexend", 15, "bold") )
per_label.place(x = 130, y = 480, height = 40, width = 220)

per_label1 = Label(win,text = "", font = ("Lexend", 15, "bold") )
per_label1.place(x = 380, y = 480, height = 40, width = 220)

done_button = Button(win,text = "DONE", font = ("Lexend",20, "bold"), command = dataget)
done_button.place(x = 300, y = 260, height = 40, width = 200)


win.mainloop()
