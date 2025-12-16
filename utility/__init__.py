"""
Educational utility package for reusable tools.

This package provides business logic modules for common educational tasks
like grade calculation and rubric export. All modules are cross-platform
compatible (Windows/Linux) and include comprehensive type hints and docstrings.
"""

__version__ = "0.1.0"

from utility.core.grade_calculator import calculate_grade, score_to_percentage
from utility.core.rubric_exporter import RubricExporter, RubricCriterion

__all__ = [
    "calculate_grade",
    "score_to_percentage",
    "RubricExporter",
    "RubricCriterion",
]
