
import csv
from typing import List, Dict

def load_questions_from_csv(filepath: str) -> List[Dict]:
    """Load questions from CSV (format: question,correct,option1,option2,...)."""
    questions = []
    with open(filepath) as f:
        reader = csv.reader(f)
        for row in reader:
            questions.append({
                "question": row[0],
                "correct_answer": row[1],
                "incorrect_answers": row[2:]
            })
    return questions
