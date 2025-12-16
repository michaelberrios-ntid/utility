"""
Grade calculation utilities for educational purposes.

This module provides functions to convert scores to percentages and
letter grades. All functions are pure and stateless, making them
easy to test and integrate into other applications.
"""

from typing import Optional


def score_to_percentage(score: float, max_score: float) -> float:
    """
    Convert a raw score to a percentage.

    Args:
        score: The points earned by the student (0 or positive).
        max_score: The maximum possible points (must be positive).

    Returns:
        The percentage as a float (0.0 to 100.0).

    Raises:
        ValueError: If max_score is zero or negative, or if score is negative.

    Examples:
        >>> score_to_percentage(85, 100)
        85.0
        >>> score_to_percentage(42.5, 50)
        85.0
    """
    if max_score <= 0:
        raise ValueError("max_score must be positive")
    if score < 0:
        raise ValueError("score cannot be negative")
    
    return (score / max_score) * 100.0


def calculate_grade(
    percentage: float,
    scale: Optional[dict[float, str]] = None
) -> str:
    """
    Convert a percentage to a letter grade.

    Args:
        percentage: The percentage score (0.0 to 100.0).
        scale: Optional custom grading scale as a dict mapping minimum
               percentages to letter grades. Defaults to a standard scale:
               90+ = A, 80-89 = B, 70-79 = C, 60-69 = D, <60 = F.

    Returns:
        The letter grade as a string.

    Raises:
        ValueError: If percentage is negative or greater than 100.

    Examples:
        >>> calculate_grade(92.5)
        'A'
        >>> calculate_grade(85.0)
        'B'
        >>> calculate_grade(58.0)
        'F'
        >>> calculate_grade(85.0, {80: 'Excellent', 70: 'Good', 0: 'Needs Work'})
        'Excellent'
    """
    if percentage < 0 or percentage > 100:
        raise ValueError("percentage must be between 0 and 100")
    
    # Default grading scale
    if scale is None:
        scale = {
            90.0: "A",
            80.0: "B",
            70.0: "C",
            60.0: "D",
            0.0: "F",
        }
    
    # Sort thresholds in descending order
    sorted_thresholds = sorted(scale.keys(), reverse=True)
    
    # Find the appropriate grade
    for threshold in sorted_thresholds:
        if percentage >= threshold:
            return scale[threshold]
    
    # Fallback (should not reach here with proper scale)
    return scale[min(scale.keys())]
