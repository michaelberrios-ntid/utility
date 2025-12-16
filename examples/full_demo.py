"""
Full demonstration of all utility features.

This script showcases both the grade calculator and rubric exporter
in a realistic educational workflow scenario.
"""

from pathlib import Path
from utility.core.grade_calculator import calculate_grade, score_to_percentage
from utility.core.rubric_exporter import RubricExporter, RubricCriterion


def demo_grade_calculation() -> None:
    """Demonstrate complete grade calculation workflow."""
    print("=" * 70)
    print("GRADE CALCULATION DEMO")
    print("=" * 70)
    
    # Scenario: Student's performance on various assignments
    print("\nStudent Performance Summary")
    print("-" * 70)
    
    assignments = [
        ("Lab Assignment 1", 18, 20),
        ("Lab Assignment 2", 19, 20),
        ("Quiz 1", 42, 50),
        ("Quiz 2", 45, 50),
        ("Midterm Exam", 85, 100),
        ("Programming Project", 92, 100),
    ]
    
    total_earned = 0.0
    total_possible = 0.0
    
    print(f"{'Assignment':<25} {'Score':>10} {'Percentage':>12} {'Grade':>8}")
    print("-" * 70)
    
    for name, earned, possible in assignments:
        percentage = score_to_percentage(earned, possible)
        grade = calculate_grade(percentage)
        total_earned += earned
        total_possible += possible
        
        print(f"{name:<25} {earned:>3}/{possible:<3} {percentage:>10.2f}% {grade:>8}")
    
    print("-" * 70)
    
    # Calculate overall grade
    overall_percentage = score_to_percentage(total_earned, total_possible)
    overall_grade = calculate_grade(overall_percentage)
    
    print(f"{'OVERALL':<25} {total_earned:>3.0f}/{total_possible:<3.0f} "
          f"{overall_percentage:>10.2f}% {overall_grade:>8}")
    
    print("\n✅ Grade calculation complete!\n")


def demo_rubric_creation() -> None:
    """Demonstrate rubric creation and export."""
    print("=" * 70)
    print("RUBRIC CREATION DEMO")
    print("=" * 70)
    
    # Create a comprehensive programming assignment rubric
    print("\nCreating Programming Assignment Rubric...")
    
    criteria = [
        RubricCriterion(
            name="Algorithm & Logic",
            description="Correctness and efficiency of algorithmic approach",
            max_points=30.0,
            levels={
                "Excellent": 30.0,
                "Good": 24.0,
                "Satisfactory": 18.0,
                "Needs Work": 12.0,
                "Incomplete": 0.0
            }
        ),
        RubricCriterion(
            name="Code Quality",
            description="Readability, organization, and style adherence",
            max_points=20.0,
            levels={
                "Excellent": 20.0,
                "Good": 16.0,
                "Satisfactory": 12.0,
                "Needs Work": 8.0
            }
        ),
        RubricCriterion(
            name="Documentation",
            description="Docstrings, comments, and type hints",
            max_points=15.0,
            levels={
                "Complete": 15.0,
                "Adequate": 11.0,
                "Minimal": 7.0,
                "Missing": 0.0
            }
        ),
        RubricCriterion(
            name="Testing & Error Handling",
            description="Edge case handling and robust error management",
            max_points=15.0
        ),
        RubricCriterion(
            name="Version Control",
            description="Meaningful commits and proper Git usage",
            max_points=10.0
        ),
        RubricCriterion(
            name="Presentation & Demo",
            description="Code walkthrough and demonstration",
            max_points=10.0
        )
    ]
    
    rubric = RubricExporter("Python Programming Assignment - Final Project", criteria)
    
    print(f"\n✓ Title: {rubric.title}")
    print(f"✓ Total Points: {rubric.total_points()}")
    print(f"✓ Number of Criteria: {len(rubric.criteria)}")
    
    # Display criteria breakdown
    print("\nCriteria Breakdown:")
    print("-" * 70)
    for criterion in criteria:
        print(f"  • {criterion.name}: {criterion.max_points} points")
        if criterion.levels:
            print(f"    Performance levels: {len(criterion.levels)}")
    
    # Export to files
    output_dir = Path("/tmp/demo_output")
    output_dir.mkdir(exist_ok=True)
    
    csv_file = output_dir / "programming_rubric.csv"
    json_file = output_dir / "programming_rubric.json"
    
    rubric.export_csv(csv_file)
    rubric.export_json(json_file)
    
    print(f"\n✓ Exported to CSV: {csv_file}")
    print(f"✓ Exported to JSON: {json_file}")
    
    # Display sample of CSV content
    print("\nCSV Preview (first 3 lines):")
    print("-" * 70)
    with csv_file.open("r") as f:
        for i, line in enumerate(f):
            if i < 3:
                print(f"  {line.rstrip()}")
    
    print("\n✅ Rubric creation and export complete!\n")


def demo_grade_from_rubric() -> None:
    """Demonstrate grading a student using a rubric."""
    print("=" * 70)
    print("GRADING WITH RUBRIC DEMO")
    print("=" * 70)
    
    print("\nStudent Evaluation on Programming Assignment")
    print("-" * 70)
    
    # Simulate grading
    scores = {
        "Algorithm & Logic": 24.0,  # Good
        "Code Quality": 20.0,  # Excellent
        "Documentation": 11.0,  # Adequate
        "Testing & Error Handling": 12.0,
        "Version Control": 9.0,
        "Presentation & Demo": 8.0
    }
    
    max_points = {
        "Algorithm & Logic": 30.0,
        "Code Quality": 20.0,
        "Documentation": 15.0,
        "Testing & Error Handling": 15.0,
        "Version Control": 10.0,
        "Presentation & Demo": 10.0
    }
    
    print(f"{'Criterion':<30} {'Score':>10} {'Max':>8} {'%':>8}")
    print("-" * 70)
    
    total_score = 0.0
    total_max = 0.0
    
    for criterion, score in scores.items():
        max_pts = max_points[criterion]
        pct = score_to_percentage(score, max_pts)
        total_score += score
        total_max += max_pts
        print(f"{criterion:<30} {score:>10.1f} {max_pts:>8.1f} {pct:>7.1f}%")
    
    print("-" * 70)
    
    overall_pct = score_to_percentage(total_score, total_max)
    overall_grade = calculate_grade(overall_pct)
    
    print(f"{'TOTAL':<30} {total_score:>10.1f} {total_max:>8.1f} {overall_pct:>7.1f}%")
    print(f"\n{'Final Letter Grade:':<30} {overall_grade:>10}")
    
    print("\n✅ Student grading complete!\n")


def main() -> None:
    """Run all demonstrations."""
    print("\n" + "=" * 70)
    print(" " * 15 + "EDUCATIONAL UTILITY TOOLS - FULL DEMO")
    print("=" * 70 + "\n")
    
    demo_grade_calculation()
    demo_rubric_creation()
    demo_grade_from_rubric()
    
    print("=" * 70)
    print(" " * 20 + "ALL DEMONSTRATIONS COMPLETE!")
    print("=" * 70)
    print("\nThe utility package successfully demonstrates:")
    print("  ✓ Grade calculations (score → percentage → letter grade)")
    print("  ✓ Rubric creation with performance levels")
    print("  ✓ CSV and JSON export functionality")
    print("  ✓ Cross-platform file handling")
    print("  ✓ Type hints and comprehensive docstrings")
    print("  ✓ Separation of business logic from CLI code")
    print("\n🎓 Ready for use in educational workflows!\n")


if __name__ == "__main__":
    main()
