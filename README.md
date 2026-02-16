# 📍 RouteWise: AI Trip Planner & Weather Guide

**RouteWise** is an AI-powered travel companion that transforms a simple destination query into a fully optimized, weather-aware itinerary. By combining Large Language Models (LLMs) with real-time routing and meteorological data, RouteWise ensures your journey is not just fast, but safe and comfortable.

## ✨ Key Features

* **Smart Routing:** Calculates the most efficient paths based on your travel preferences.
* **Live Weather Integration:** Monitors conditions along your specific route to suggest the best departure times.
* **Tailored Rest Stops:** Suggests ideal breaks based on driving duration and local amenities.
* **RAG-Powered Intelligence:** Uses Retrieval-Augmented Generation to provide contextually aware travel advice.
* **Stress-Free Scheduling:** Balances drive time with safety buffers for road conditions.

---

## 🏗️ Project Structure

The project is designed with a modular approach to separate the "brain" from the "tools":

| File | Description |
| --- | --- |
| `main.py` | The core logic. Handles LLM configuration, API orchestration, and the main agent loop. |
| `tools.py` | The engine room. Contains functions for RAG implementation, routing APIs, and weather forecasting. |

---

## 🚀 Getting Started

### Prerequisites

* Python 3.12.x
* An API Key for your chosen LLM (e.g., OpenAI, Anthropic, or Google Gemini) https://platform.claude.com/dashboard
* API Keys for mapping https://openrouteservice.org/ and Weather (e.g., OpenWeatherMap) https://www.weatherapi.com/

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/milindparitshinde/RouteWise-AI-Trip-Planner-Weather-Guide.git
cd RouteWise-AI-Trip-Planner-Weather-Guide

```


2. **Install dependencies:**
```bash
pip install -r requirements.txt
# if requirements.txt file exists
```


3. **Set up environment variables:**
Create a `.env` file in the root directory:
```env
LLM_API_KEY=your_key_here
WEATHER_API_KEY=your_key_here
MAPS_API_KEY=your_key_here

```



---

## 🛠️ How It Works

### 1. The Brain (`main.py`)

This file initializes the LLM and defines the system prompt. It acts as the **Agent** that decides which tools to call based on your natural language input (e.g., *"I want to drive from NYC to DC tomorrow morning, avoid heavy rain, and stop for coffee."*).

### 2. The Tools (`tools.py`)

This file houses the specialized functions that the AI uses to interact with the real world:

* **Routing Tool:** Fetches coordinates and road data.
* **Weather Tool:** Retrieves forecasts for specific waypoints and times.
* **RAG System:** Pulls from travel guides or safety documentation to provide better recommendations.

---

## 📝 Example Usage

```python
# Run the main application
python main.py #windows
python3 main.py #mac / linux

```

**Sample Prompt:**

> "Plan a 5-hour road trip to the mountains. I want to avoid the snow expected this afternoon and find a scenic spot for lunch."

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for new tools (like EV charging station finders or hotel integrations), feel free to fork the repo and submit a PR.

---

**Would you like me to help you write the specific `requirements.txt` file or create a sample "System Prompt" for your `main.py`?**
