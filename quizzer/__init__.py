"""Top-level package for Quizzer-CLI."""

__version__ = "0.1.0"
__author__ = "Your Name <your.email@example.com>"
__description__ = "A command-line quiz game powered by Open Trivia DB"

# Import key modules to make them available when importing the package
from .cli import app  # noqa: F401
from .quiz_api import fetch_questions  # noqa: F401
from .utils import calculate_score  # noqa: F401

# Initialize package logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
