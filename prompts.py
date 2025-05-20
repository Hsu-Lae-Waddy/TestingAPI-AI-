def generate_prompt(destination: str, days: str) -> str:
    return f"""
You are a helpful travel assistant. A user is planning a trip to {destination} for {days}.
Give a bullet point list of important things they should bring for the trip, considering:
- weather
- location type (e.g., city, mountain, temple)
- local customs (if relevant)
- duration of the trip

Return only the list in plain English.
"""
