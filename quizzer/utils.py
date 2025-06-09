def calculate_score(correct: int, total: int) -> str:
    """Format score with emoji feedback."""
    if correct == total:
        return "🎯 Perfect!"
    elif correct / total >= 0.7:
        return "🔥 Great job!"
    else:
        return "💪 Keep practicing!"
