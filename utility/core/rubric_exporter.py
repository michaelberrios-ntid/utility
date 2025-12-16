"""
Rubric export utilities for MyCourses and other LMS platforms.

This module provides classes and functions to create and export grading
rubrics in various formats (CSV, JSON) that can be imported into Learning
Management Systems like MyCourses/Brightspace.
"""

import csv
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any


@dataclass
class RubricCriterion:
    """
    A single criterion in a grading rubric.

    Attributes:
        name: The name/title of the criterion (e.g., "Code Quality").
        description: Detailed description of what this criterion evaluates.
        max_points: Maximum points possible for this criterion.
        levels: Optional dict mapping level names to point values.
                Example: {"Excellent": 10, "Good": 7, "Fair": 5, "Poor": 0}
    """
    name: str
    description: str
    max_points: float
    levels: dict[str, float] | None = None

    def __post_init__(self) -> None:
        """Validate criterion data after initialization."""
        if self.max_points < 0:
            raise ValueError("max_points cannot be negative")
        if self.levels:
            for level_name, points in self.levels.items():
                if points < 0 or points > self.max_points:
                    raise ValueError(
                        f"Level '{level_name}' points must be between 0 and {self.max_points}"
                    )


class RubricExporter:
    """
    Export grading rubrics to various file formats.

    This class handles the creation and export of rubrics for use in
    Learning Management Systems. Supports CSV and JSON formats with
    cross-platform file path handling.
    """

    def __init__(self, title: str, criteria: list[RubricCriterion]) -> None:
        """
        Initialize a rubric exporter.

        Args:
            title: The title/name of the rubric.
            criteria: List of RubricCriterion objects defining the rubric.

        Raises:
            ValueError: If criteria list is empty.
        """
        if not criteria:
            raise ValueError("At least one criterion is required")
        self.title = title
        self.criteria = criteria

    def total_points(self) -> float:
        """
        Calculate the total maximum points for this rubric.

        Returns:
            The sum of all criteria max_points.
        """
        return sum(criterion.max_points for criterion in self.criteria)

    def to_dict(self) -> dict[str, Any]:
        """
        Convert rubric to a dictionary representation.

        Returns:
            Dictionary with rubric title, criteria, and total points.
        """
        return {
            "title": self.title,
            "total_points": self.total_points(),
            "criteria": [asdict(criterion) for criterion in self.criteria],
        }

    def export_json(self, filepath: str | Path) -> None:
        """
        Export rubric to a JSON file.

        Args:
            filepath: Path where the JSON file will be saved.
                     Can be string or pathlib.Path (cross-platform).

        Examples:
            >>> rubric = RubricExporter("Assignment 1", criteria_list)
            >>> rubric.export_json("rubric.json")
        """
        filepath = Path(filepath)
        with filepath.open("w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2)

    def export_csv(self, filepath: str | Path) -> None:
        """
        Export rubric to a CSV file.

        The CSV format includes columns: Criterion, Description, Max Points.
        If levels are defined, additional columns are added for each level.

        Args:
            filepath: Path where the CSV file will be saved.
                     Can be string or pathlib.Path (cross-platform).

        Examples:
            >>> rubric = RubricExporter("Assignment 1", criteria_list)
            >>> rubric.export_csv("rubric.csv")
        """
        filepath = Path(filepath)
        
        # Determine if any criteria have levels
        has_levels = any(c.levels for c in self.criteria)
        
        with filepath.open("w", encoding="utf-8", newline="") as f:
            if has_levels:
                # Complex format with levels
                writer = csv.writer(f)
                writer.writerow(["Criterion", "Description", "Max Points", "Levels"])
                
                for criterion in self.criteria:
                    levels_str = ""
                    if criterion.levels:
                        levels_str = "; ".join(
                            f"{name}: {points}" for name, points in criterion.levels.items()
                        )
                    writer.writerow([
                        criterion.name,
                        criterion.description,
                        criterion.max_points,
                        levels_str
                    ])
            else:
                # Simple format without levels
                writer = csv.writer(f)
                writer.writerow(["Criterion", "Description", "Max Points"])
                
                for criterion in self.criteria:
                    writer.writerow([
                        criterion.name,
                        criterion.description,
                        criterion.max_points
                    ])
