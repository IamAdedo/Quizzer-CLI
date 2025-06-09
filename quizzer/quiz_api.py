import requests

def fetch_questions(topic: str, difficulty: str, amount: int = 5):
    """Fetch questions from OpenTDB API."""
    categories = {
        "python": 18,  # Programming category
        "science": 17,
        "history": 23
    }
    url = f"https://opentdb.com/api.php?amount={amount}&category={categories.get(topic, 18)}&difficulty={difficulty}"
    response = requests.get(url)
    return response.json().get("results", [])
