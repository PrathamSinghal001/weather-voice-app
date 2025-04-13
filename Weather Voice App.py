# import modules 
import tkinter as tk #--> GUI module
import requests #--> API requests get module
from tkinter import PhotoImage #--> GUI with image 
import pyttsx3 # --> python engine talk
import threading # --> fast process from pyttsx3
import sys # --> system controlling module
import tkinter.messagebox as tmsg # --> it's important for used a messagebox in python tkinter 


# STRUCTURE1 --> main window, frame, size, configuration, icon, heading label
root = tk.Tk()
root.geometry("1300x250")
root.config(bg="#1A1D23")

frame = tk.Frame(root, height=200, width=200, bg="white", relief="solid")
frame.grid(row=0, column=0, sticky="nsew", padx=600, pady=20)

frame1 = tk.Frame(root, bg="snow")
frame1.grid()
# frame.pack()

# Load the PNG image
icon = PhotoImage(file="D:\\OneDrive\\python projects files\\Project Items\\weather\\wthr.png") 
# Set the window icon
root.iconphoto(False, icon)

# main_head = tk.Label(root, text="Weather GUI", font="cursive 20 bold", bg="white", fg='black')
# main_head.grid(columnspan=165)

heading = tk.Label(frame, text="Welcome to Weather GUI App", font="lucida 15 bold", bg="yellow", fg="red")
heading.grid(columnspan=20, row=0)


# pyttsx3 module working
engine = pyttsx3.init() # --> get all function from pyttsx3 init() function 

# setProperty --> get 2 value --> (name, value)
engine.setProperty('rate', 200) # set rate property --> rate means the speed of saying 
engine.setProperty('volume', 1500) # set volume property 


# pyttsx3 module working
def title(text):
    engine.say(text) # saying function --> define what saying by engine 
    engine.runAndWait() # define for start engine and stop the engine 


# threading module work
def button_clicked():
    text = "welcome to  Weather GUI App" # saying string or line or command
    thread = threading.Thread(target=title, args=(text, )) # --> threading module --> target function 
    thread.start() # --> start threading
button_clicked()


# STRUCTURE2 --> weather function nd other some functions

# url = https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m

# api_url = "https://api.open-meteo.com/v1/forecast?"


def weather_talk():
    lat = lat_entry.get()
    long = long_entry.get()
    
    # Construct the full URL with dynamic parameters
    # url = f"{api_url}latitude={lat}&longitude={long}&current_weather={current}&current_units={current_units}"
    
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,wind_speed_10m"
    
    # Send the request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # pure_data = data["object"]
        temperature = data["current"]["temperature_2m"]
        wind_speed = data["current"]["wind_speed_10m"]
        
        pure_data = f"Temperature : {temperature}°C\nwind speed : {wind_speed}Km/h"
    
    else:
        pure_data = f"Sorry, failed to retrieve data, {response.status_code}" 
      
    # lable point for frame defining
    tk.Label(frame1, text="Output : ", font="verdana 15 italic").grid(row=6, column=0)
    
    # data variable
    output = tk.Label(frame1, text=pure_data, font="Helvetica 15 underline", fg="Black", bg="Seashell")
    output.grid(columnspan=20, row=6, column=3)
    print(pure_data)
    
    def saying():
        # pyttsx3 module working
        engine.say(pure_data) # saying function --> define what saying by engine 
        engine.runAndWait() # define for start engine and stop the engine 
    
    # threading module work
    def button_clicked():
        thread = threading.Thread(target=saying) # --> threading module --> target function 
        thread.start() # --> start threading
    button_clicked()


def quit(event):
    root.destroy()
    # sys.exit()
    # root.quit()
    
    
# STRUCTURE3 --> entry, labels, buttons
# label points as a placeholder
lat_label = tk.Label(frame, text="Enter Latitude : ", font="calibari")
lat_label.grid(row=1, column=0, padx=0, pady=1)
long_label = tk.Label(frame, text="Enter Longitude : ", font="calibari")
long_label.grid(row=2, column=0, padx=0, pady=1)

# entry points
lat_entry = tk.Entry(frame, text="Latitude", font="calibari 12", textvariable=tk.DoubleVar())
lat_entry.grid(row=1, column=2)
long_entry = tk.Entry(frame, text="Latitude", font="calibari 12", textvariable=tk.DoubleVar())
long_entry.grid(row=2, column=2)

# button points
btn_show = tk.Button(frame, text="Show Weather", font="lucida 10 bold", command=weather_talk)
btn_show.grid(row=4, column=0, pady=3, padx=0)
btn_exit = tk.Button(frame, text="Exit", font="lucida 10 bold", command=exit)
btn_exit.grid(row=4, column=3, padx=3, pady=3)
btn_exit.bind("<Button-1>", quit)


# frame config
frame.grid_rowconfigure(10, weight=1)
frame.grid_columnconfigure(10, weight=1)
root.mainloop()

