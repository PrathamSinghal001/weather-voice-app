<h1 align="center">🌤️ Weather Voice App</h1>
<p align="center">
  A sleek Python desktop application that gives you real-time weather updates with a voice assistant.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue?logo=python">
  <img src="https://img.shields.io/badge/GUI-Tkinter-yellow?logo=windowsterminal">
  <img src="https://img.shields.io/badge/Speech-pyttsx3-orange?logo=soundcloud">
  <img src="https://img.shields.io/badge/API-Open--Meteo-green?logo=cloud">
</p>

---

## 🚀 Features

- ✅ Fetch real-time **temperature** and **wind speed** using latitude and longitude.
- 🗣️ Get audio feedback with built-in **text-to-speech**.
- 🎨 User-friendly **Tkinter GUI** interface.
- ⚡ Smooth performance with **threading** for speech execution.
- 🌐 Uses the free and reliable **Open-Meteo API**.

---

## 🧰 Tech Stack

| Purpose              | Tool / Library    |
|----------------------|-------------------|
| GUI                  | `tkinter`         |
| Weather API Calls    | `requests`        |
| Text-to-Speech       | `pyttsx3`         |
| Multithreading       | `threading`       |
| System Controls      | `sys`             |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/PrathamSinghal001/weather-voice-app.git
cd weather-voice-app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
Note - Make sure Python 3.6+ is installed on your machine.

### 3. Run the app
```bash
python "Weather Voice App.py"
```
Note - Note: The icon image path in the script (PhotoImage(file="...")) must be updated to a valid image on your machine.

---

## 🌐 API Used
Open-Meteo — A free weather API for non-commercial use.
(https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m)

---

## 🧠 How It Works
1. Enter Latitude and Longitude in the input fields.
2. Click Show Weather to fetch current temperature and wind speed.
3. The output is displayed on screen and read aloud using the speech engine.
4. Click Exit to close the application.

---

## 📄 License
This project is licensed under the MIT License.

---

## 🙋‍♂️ Author
Made with ❤️ by Pratham Singhal
📫 prathamsinghal0011@gmail.com
