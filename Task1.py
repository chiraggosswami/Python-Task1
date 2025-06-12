import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# === CONFIG ===
API_KEY = '7c0b4b80624c90c18088078ad437590e'  
CITY = 'Pune'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# === FETCH DATA ===
response = requests.get(URL)
data = response.json()

# === PARSE TEMPERATURE AND TIMESTAMP ===
timestamps = []
temperatures = []

for entry in data['list']:
    time = datetime.strptime(entry['dt_txt'], "%Y-%m-%d %H:%M:%S")
    temp = entry['main']['temp']
    timestamps.append(time)
    temperatures.append(temp)

# === PLOT ===
plt.figure(figsize=(12, 6))
sns.lineplot(x=timestamps, y=temperatures, marker='o', color='orange')
plt.title(f"5-Day Weather Forecast for {CITY}", fontsize=16)
plt.xlabel("Date and Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()