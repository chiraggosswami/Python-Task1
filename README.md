# Python Task1
Company: CodTech IT Solutions
Name: Chirag Goswami
Intern Id: CT06DF670
Domain: Python Programming
Duration: 4 weeks
Mentor: NEELA SANTOSH
#Result: ![Image](https://github.com/user-attachments/assets/065e7660-5b3f-42ef-965c-6c291d3d6ffa)

Description:

### **Overview**

This Python script fetches a 5-day weather forecast for a specific city (in this case, **Pune**) using the **OpenWeatherMap API**. It processes the returned data to extract temperature readings and corresponding timestamps, and then visualizes this information using **Seaborn** and **Matplotlib**, two popular libraries for data visualization in Python.

The script is structured into clear sections:

1. **Imports**
2. **Configuration**
3. **Data Fetching**
4. **Data Parsing**
5. **Data Visualization**

Let’s explore each section in detail.

---

## **1. Imports**

```python
import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
```

### **Explanation:**

* **`requests`**: This library is used for making HTTP requests. Here, it is used to call the weather API and retrieve JSON data.
* **`matplotlib.pyplot`**: Commonly imported as `plt`, this module from the `matplotlib` library is used for creating static, interactive, and animated plots.
* **`seaborn`**: A statistical data visualization library built on top of matplotlib. It provides a high-level interface for drawing attractive graphs. In this script, it's used to plot the line graph with improved aesthetics.
* **`datetime`**: Python's built-in module for working with date and time. It’s used to convert string timestamps from the API into `datetime` objects for plotting.

---

## **2. Configuration**

```python
API_KEY = '7c0b4b80624c90c18088078ad437590e'  
CITY = 'Pune'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'
```

### **Explanation:**

* **`API_KEY`**: A string representing your personal access key for OpenWeatherMap API. This key is required to authenticate and authorize the API request.
* **`CITY`**: The name of the city for which the forecast will be fetched. In this case, it is hardcoded as `'Pune'`.
* **`URL`**: This is the complete API endpoint assembled using an f-string. It includes the city, API key, and units (`metric`, which returns temperatures in Celsius).

### **Why Configuration Matters:**

This section allows flexibility. If you want to fetch weather data for a different city, you only need to change the `CITY` variable. Also, the use of f-strings ensures that the URL is easy to read and update.

---

## **3. Data Fetching**

```python
response = requests.get(URL)
data = response.json()
```

### **Explanation:**

* `requests.get(URL)`: Sends a GET request to the OpenWeatherMap API endpoint and fetches the forecast data.
* `response.json()`: Converts the API response (which is in JSON format) into a Python dictionary, enabling structured data access.

### **What the API Returns:**

The 5-day forecast API returns weather predictions in 3-hour intervals. This means there are 8 data points per day, and about 40 entries in total.

---

## **4. Data Parsing**

```python
timestamps = []
temperatures = []

for entry in data['list']:
    time = datetime.strptime(entry['dt_txt'], "%Y-%m-%d %H:%M:%S")
    temp = entry['main']['temp']
    timestamps.append(time)
    temperatures.append(temp)
```

### **Explanation:**

* `data['list']`: This is the main body of the forecast data. It's a list of dictionaries, each representing weather data for a specific 3-hour time interval.
* `entry['dt_txt']`: This field contains the date and time of the forecast in a string format (`YYYY-MM-DD HH:MM:SS`).
* `datetime.strptime(...)`: Converts the string timestamp into a Python `datetime` object, which is crucial for accurate plotting on the x-axis.
* `entry['main']['temp']`: Extracts the temperature (in °C due to the `units=metric` parameter) from each entry.
* `timestamps.append(time)` and `temperatures.append(temp)`: Collect these values into their respective lists for plotting.

### **Why Parsing Is Necessary:**

APIs often return data in a nested format. Before you can visualize or analyze it, you need to extract and convert it into a usable structure. Here, lists of timestamps and temperatures are created so that each temperature corresponds to a point in time.

---

## **5. Data Visualization**

```python
plt.figure(figsize=(12, 6))
sns.lineplot(x=timestamps, y=temperatures, marker='o', color='orange')
plt.title(f"5-Day Weather Forecast for {CITY}", fontsize=16)
plt.xlabel("Date and Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
```

### **Explanation:**

* **`plt.figure(figsize=(12, 6))`**: Sets the size of the entire plot. A wider figure allows more space for densely packed x-axis labels.
* **`sns.lineplot(...)`**: Plots the data with a line graph using Seaborn. Each temperature reading is marked with a circle (`marker='o'`), and the color of the line is orange.
* **`plt.title(...)`**: Sets the title of the chart dynamically using the city name.
* **`plt.xlabel()` / `plt.ylabel()`**: Label the x- and y-axes for clarity.
* **`plt.xticks(rotation=45)`**: Rotates the x-axis labels by 45 degrees to prevent overlap, especially since timestamps are long strings.
* **`plt.tight_layout()`**: Adjusts subplot parameters for better layout and prevents clipping.
* **`plt.grid(True)`**: Adds a background grid to improve readability.
* **`plt.show()`**: Renders the plot.

---

## **Purpose and Use Cases**

This script provides a quick way to visualize short-term weather forecasts, which is useful for:

* **Weather monitoring**: For individuals or businesses that need to plan based on upcoming weather.
* **Learning projects**: For Python beginners who want hands-on experience with APIs, JSON parsing, and data visualization.
* **Dashboards**: Can be adapted into a larger web or desktop application to provide live weather updates.

---

## **Potential Improvements and Enhancements**

1. **Error Handling**:

   * If the API key is invalid or the city name is wrong, the script will currently crash. Adding error checks would make it more robust.

   ```python
   if response.status_code != 200:
       print("Error fetching data:", response.json())
       exit()
   ```

2. **Dynamic User Input**:

   * Replace the hardcoded `CITY` variable with `input()` to make it interactive.

3. **Data Smoothing or Aggregation**:

   * Show daily averages instead of raw 3-hour data for a cleaner chart.

4. **Multiple Parameters**:

   * Plot humidity, wind speed, or weather conditions alongside temperature.

5. **Save Plot**:

   * Use `plt.savefig('forecast.png')` to save the chart as an image.

---

## **Conclusion**

This script is a compact but powerful demonstration of real-world Python usage. It fetches external data from an API, processes JSON, handles date and time conversions, and produces meaningful visualizations. It's an excellent example for anyone learning how to combine web data with data visualization libraries to create insightful tools.

By breaking down tasks—configuration, data fetching, parsing, and visualization—this code achieves a clean and functional workflow that can be expanded into larger projects with ease.
