import pytest
from quizzer.quiz_api import fetch_questions
from quizzer.utils import calculate_score

def test_fetch_questions():
    """Test API question fetching."""
    questions = fetch_questions("python", "easy", amount=2)
    assert len(questions) == 2
    assert "question" in questions[0]

def test_score_calculation():
    """Test score feedback logic."""
    assert calculate_score(5, 5) == "🎯 Perfect!"
    assert calculate_score(7, 10) == "🔥 Great job!"
    assert calculate_score(2, 10) == "💪 Keep practicing!"
