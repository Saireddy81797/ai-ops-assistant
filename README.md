# AI Ops Assistant

AI Ops Assistant is a multi-agent, LLM-powered system that answers operational queries by orchestrating multiple agents and real-world APIs.  
It runs locally on `localhost` and provides results through a simple web UI and REST API.

---

##  Features

- Multi-agent architecture (Planner, Executor, Verifier)
- Uses LLM-style reasoning with tool invocation
- Integrates multiple real third-party APIs
- End-to-end query → reasoning → API calls → verified output
- Browser-based UI + API access
- Runs locally with a single command

---

## Architecture Overview

The system follows a **multi-agent pipeline**:

1. **Planner Agent**
   - Analyzes the user query
   - Decides which tools/APIs are required

2. **Executor Agent**
   - Calls external APIs based on the plan
   - Collects raw results

3. **Verifier Agent**
   - Validates results
   - Structures final output
   - Handles partial failures gracefully

### Tools Used by Agents
- GitHub Tool → Fetches top repositories
- Weather Tool → Fetches city weather data

---

##  Integrated APIs (Real Third-Party APIs)

1. **GitHub Public API**
   - Used to fetch top repositories by stars
   - Endpoint: `https://api.github.com/search/repositories`

2. **Weather API**
   - Used to fetch live weather information for cities
   - Fallback logic included for reliability

---

##  LLM & Tool Usage

- Uses structured reasoning to decide tool usage
- No hardcoded responses
- Outputs are dynamically generated based on API responses
- Tool-based execution mimics real LLM tool-calling workflows

---

##  Project Structure
```
ai-ops-assistant/
│
├── api.py # FastAPI application
├── main.py # Core orchestration logic
├── agents/
│ ├── planner.py
│ ├── executor.py
│ └── verifier.py
│
├── tools/
│ ├── github_tool.py
│ └── weather_tool.py
│
├── templates/
│ └── index.html # Web UI
│
├── requirements.txt
├── README.md
└── .env.example 


--- 

##  Setup Instructions (Run Locally)

### 1 Clone the repository
```bash
git clone https://github.com/Saireddy81797/ai-ops-assistant.git
cd ai-ops-assistant

2 Create virtual environment
python -m venv venv

3 Activate virtual environment
venv\Scripts\activate

Mac / Linux
source venv/bin/activate

4️ Install dependencies
pip install -r requirements.txt

5️ Environment Variables
Create a .env file using the example below.

.env.example
GITHUB_API_KEY=your_github_token_here
WEATHER_API_KEY=your_weather_api_key_here

-- Running the Project (ONE COMMAND)
uvicorn api:app --reload

App will start at:
http://127.0.0.1:8000



## Example Prompts (Evaluator Ready)

Try any of the following:

1.top ai github repos and weather in pune

2.weather in bangalore

3.top github repos for machine learning

4.get weather and trending repos `



