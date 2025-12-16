"""
Example usage of the rubric exporter module.

This script demonstrates how to create and export rubrics programmatically.
"""

from pathlib import Path
from utility.core.rubric_exporter import RubricExporter, RubricCriterion


def main() -> None:
    """Run rubric exporter examples."""
    print("=" * 60)
    print("Rubric Exporter Examples")
    print("=" * 60)
    
    # Example 1: Simple rubric without levels
    print("\n1. Simple Rubric (No Performance Levels)")
    print("-" * 40)
    
    simple_criteria = [
        RubricCriterion(
            name="Code Functionality",
            description="Code runs without errors and meets all requirements",
            max_points=30.0
        ),
        RubricCriterion(
            name="Code Quality",
            description="Clean, readable, and well-organized code",
            max_points=20.0
        ),
        RubricCriterion(
            name="Documentation",
            description="Comprehensive comments and docstrings",
            max_points=15.0
        ),
        RubricCriterion(
            name="Testing",
            description="Adequate test coverage and test quality",
            max_points=15.0
        ),
    ]
    
    simple_rubric = RubricExporter("Programming Assignment 1", simple_criteria)
    print(f"Title: {simple_rubric.title}")
    print(f"Total Points: {simple_rubric.total_points()}")
    print(f"Number of Criteria: {len(simple_rubric.criteria)}")
    
    # Export to files
    output_dir = Path("/tmp/rubric_examples")
    output_dir.mkdir(exist_ok=True)
    
    simple_csv = output_dir / "simple_rubric.csv"
    simple_json = output_dir / "simple_rubric.json"
    
    simple_rubric.export_csv(simple_csv)
    simple_rubric.export_json(simple_json)
    print(f"\nExported to:\n  - {simple_csv}\n  - {simple_json}")
    
    # Example 2: Detailed rubric with performance levels
    print("\n2. Detailed Rubric (With Performance Levels)")
    print("-" * 40)
    
    detailed_criteria = [
        RubricCriterion(
            name="Algorithm Design",
            description="Quality and efficiency of algorithmic approach",
            max_points=25.0,
            levels={
                "Excellent": 25.0,
                "Good": 20.0,
                "Satisfactory": 15.0,
                "Needs Improvement": 10.0,
                "Unsatisfactory": 0.0
            }
        ),
        RubricCriterion(
            name="Code Style",
            description="Adherence to style guidelines and best practices",
            max_points=15.0,
            levels={
                "Exemplary": 15.0,
                "Proficient": 12.0,
                "Developing": 9.0,
                "Beginning": 5.0
            }
        ),
        RubricCriterion(
            name="Error Handling",
            description="Proper handling of edge cases and errors",
            max_points=10.0,
            levels={
                "Complete": 10.0,
                "Adequate": 7.0,
                "Minimal": 4.0,
                "None": 0.0
            }
        ),
    ]
    
    detailed_rubric = RubricExporter("Advanced Programming Project", detailed_criteria)
    print(f"Title: {detailed_rubric.title}")
    print(f"Total Points: {detailed_rubric.total_points()}")
    
    detailed_csv = output_dir / "detailed_rubric.csv"
    detailed_json = output_dir / "detailed_rubric.json"
    
    detailed_rubric.export_csv(detailed_csv)
    detailed_rubric.export_json(detailed_json)
    print(f"\nExported to:\n  - {detailed_csv}\n  - {detailed_json}")
    
    # Example 3: Display rubric as dictionary
    print("\n3. Rubric as Dictionary (for API/web use)")
    print("-" * 40)
    rubric_dict = simple_rubric.to_dict()
    print(f"Title: {rubric_dict['title']}")
    print(f"Total: {rubric_dict['total_points']} points")
    print(f"Criteria ({len(rubric_dict['criteria'])}):")
    for criterion in rubric_dict['criteria']:
        print(f"  - {criterion['name']}: {criterion['max_points']} pts")
    
    print("\n" + "=" * 60)
    print(f"\nAll example files created in: {output_dir}")


if __name__ == "__main__":
    main()
