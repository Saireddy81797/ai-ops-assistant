from tools.github_tool import search_repositories
from tools.weather_tool import get_current_weather


def execute_plan(plan: dict):
    results = []

    for step in plan.get("steps", []):
        tool = step.get("tool")
        action = step.get("action")
        parameters = step.get("parameters", {})

        if tool == "github" and action == "search_repos":
            query = parameters.get("query", "")
            limit = parameters.get("limit", 5)
            output = search_repositories(query, limit)
            results.append({
                "tool": "github",
                "output": output
            })

        elif tool == "weather" and action == "get_weather":
            city = parameters.get("city")
            output = get_current_weather(city)
            results.append({
                "tool": "weather",
                "output": output
            })

        else:
            results.append({
                "tool": tool,
                "error": "Unknown tool or action"
            })

    return results
