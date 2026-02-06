def create_plan(user_input: str):
    """
    Mock Planner Agent
    Converts user intent into structured execution plan
    """

    user_input_lower = user_input.lower()

    steps = []

    if "github" in user_input_lower or "repository" in user_input_lower:
        steps.append({
            "tool": "github",
            "action": "search_repos",
            "parameters": {
                "query": "python",
                "limit": 5
            }
        })

    if "weather" in user_input_lower:
        steps.append({
            "tool": "weather",
            "action": "get_weather",
            "parameters": {
                "city": "Pune"
            }
        })

    return {"steps": steps}
