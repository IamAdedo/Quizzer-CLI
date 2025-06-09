from setuptools import setup, find_packages  # Updated import

setup(
    name="quizzer-cli",
    version="0.1",
    packages=find_packages(),  # Automatically discover packages
    install_requires=["typer>=0.9.0", "rich>=13.0", "requests>=2.31.0"],
    entry_points={"console_scripts": ["quizzer-cli=quizzer.cli:app"]},
    include_package_data=True,  # For JSON files
)
