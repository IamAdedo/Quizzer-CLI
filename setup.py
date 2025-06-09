from setuptools import setup

setup(
    name="quizzer-cli",
    version="0.1",
    packages=["quizzer"],
    install_requires=["typer", "rich", "requests"],
    entry_points={"console_scripts": ["quizzer-cli=quizzer.cli:app"]},
)
