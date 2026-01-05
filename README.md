# 🌤️ Intelligent Weather Chatbot Webhook

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-green)
![API](https://img.shields.io/badge/API-OpenWeatherMap-orange)

## 📌 Project Overview
This project serves as a **Backend Fulfillment Webhook** for an intelligent chatbot (designed for platforms like **Dialogflow**). It processes natural language requests for weather updates, resolves geolocation data, and fetches real-time meteorological information.

It acts as the "brain" connecting the user interface (Chatbot) to external data services (OpenWeatherMap).

## 🛠️ Tech Stack
* **Framework:** Flask (Python)
* **Geolocation:** Geopy (Nominatim API)
* **Data Source:** OpenWeatherMap API
* **Integration:** JSON Webhook for Dialogflow

## ⚙️ How It Works
1.  **Input:** The chatbot sends a JSON payload containing the city name (extracted via NLP) to this Flask server.
2.  **Processing:**
    * The server uses `Geopy` to convert the city name into Latitude/Longitude coordinates.
    * It requests weather data for those coordinates from the OpenWeatherMap API.
3.  **Output:** It formats a natural language response (e.g., *"The weather in London is mainly Cloudy..."*) and sends it back to the chatbot for the user.

## 🚀 How to Run Locally

1.  **Clone the repository**
    ```bash
    git clone https://github.com/KSAahil/weather-chatbot-webhook.git
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Server**
    ```bash
    python src/app.py
    ```

## 📂 Directory Structure
```text
├── src/
│   └── app.py           # Main application logic
├── requirements.txt     # Dependencies

└── README.md            # Documentation
