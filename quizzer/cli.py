
import typer
from rich import print
from rich.table import Table
from quiz_api import fetch_questions
from utils import calculate_score

app = typer.Typer()

@app.command()
def start(
    topic: str = typer.Option("python", help="Quiz topic (e.g., 'science', 'history')"),
    difficulty: str = typer.Option("easy", help="Difficulty: easy/medium/hard")
):
    """Start an interactive quiz."""
    print(f"\n[bold blue]🚀 Starting {topic} quiz ({difficulty} mode)[/bold blue]\n")
    questions = fetch_questions(topic, difficulty)
    score = 0

    for idx, q in enumerate(questions, 1):
        print(f"[bold]{idx}. {q['question']}[/bold]")
        for i, ans in enumerate(q["incorrect_answers"] + [q["correct_answer"]]):
            print(f"  {i+1}. {ans}")

        user_ans = int(input("\nYour answer (number): ")) - 1
        correct_ans = q["incorrect_answers"].index(q["correct_answer"]) if q["correct_answer"] in q["incorrect_answers"] else len(q["incorrect_answers"])
        
        if user_ans == correct_ans:
            score += 1
            print("[green]✓ Correct![/green]")
        else:
            print(f"[red]✗ Wrong! Correct: {q['correct_answer']}[/red]")

    print(f"\n[bold yellow]🏆 Your score: {score}/{len(questions)}[/bold yellow]")

if __name__ == "__main__":
    app()
