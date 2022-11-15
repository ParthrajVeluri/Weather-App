import tkinter as tk 
from tkinter import font
import requests

#Apikey 75d0fb6a379541588b8a93f9647266d7

def format_response(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]["description"]
        temparature = weather["main"]["temp"]

        final_str = 'City: %s \nConditions: %s \nTemparature (°C): %s' % (name,description,temparature)
    except: 
        final_str = "There was a problem recieving that information"
    return final_str

    

def getWeather(city):
    weather_key = "75d0fb6a379541588b8a93f9647266d7"
    url = "https://api.openweathermap.org/data/2.5/weather"
    param = {'APPID' : weather_key, 'q': city, 'units' : 'metric'}
    response = requests.get(url, params = param)
    weather = response.json()

    label['text'] = format_response(weather)

HEIGHT = 500
WIDTH = 600

#NOTE: Pack places widgets in vertical and horizontal boxes, where as place puts widgets in a 2d grid using
#x and y coordinates

root = tk.Tk() #Tk() is a function which creates a little window 

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH) #Creates a rectangular area for putting things in
canvas.pack() #Inputs the canvas into the parent window (root)

background_image = tk.PhotoImage(file = 'landscape.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

frame = tk.Frame(root, bg="#80c1ff", bd = 5) #A container to put other things inside, frames always fit inside cavases
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n') 
#rel = relative. Using this the dimensions are adjusted depending on the size of the window

button = tk.Button(frame, text = "GO", font = 40, command= lambda: getWeather(entry.get())) #Creates a button with frame as its parent window
button.place(relx = 0.7, relheight = 1, relwidth = 0.3)

entry = tk.Entry(frame, font = 40)
entry.place(relwidth = 0.65, relheight = 1)

lower_frame = tk.Frame(root, bg ="#80c1ff", bd = 10)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor ='n')

label = tk.Label(lower_frame, bg ="white", font=("Courier", 18))
label.place(relwidth = 1, relheight = 1)

root.mainloop() #mainloop() actually runs the little window and is the start of the application