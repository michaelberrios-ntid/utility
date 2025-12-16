"""
Example usage of the grade calculator module.

This script demonstrates how to use the grade calculator functions
programmatically in Python code.
"""

from utility.core.grade_calculator import calculate_grade, score_to_percentage


def main() -> None:
    """Run grade calculator examples."""
    print("=" * 60)
    print("Grade Calculator Examples")
    print("=" * 60)
    
    # Example 1: Convert score to percentage
    print("\n1. Score to Percentage Conversion")
    print("-" * 40)
    score = 85
    max_score = 100
    percentage = score_to_percentage(score, max_score)
    print(f"Score: {score}/{max_score}")
    print(f"Percentage: {percentage:.2f}%")
    
    # Example 2: Calculate letter grade from percentage
    print("\n2. Percentage to Letter Grade")
    print("-" * 40)
    test_percentages = [95, 87, 75, 65, 55]
    for pct in test_percentages:
        grade = calculate_grade(pct)
        print(f"{pct:>5.1f}% → {grade}")
    
    # Example 3: Custom grading scale
    print("\n3. Custom Grading Scale")
    print("-" * 40)
    custom_scale = {
        93.0: "A",
        90.0: "A-",
        87.0: "B+",
        83.0: "B",
        80.0: "B-",
        77.0: "C+",
        73.0: "C",
        70.0: "C-",
        60.0: "D",
        0.0: "F"
    }
    test_scores = [(95, "Should be A"), (91, "Should be A-"), (85, "Should be B+")]
    for pct, expected in test_scores:
        grade = calculate_grade(pct, custom_scale)
        print(f"{pct}% → {grade} ({expected})")
    
    # Example 4: Complete workflow
    print("\n4. Complete Workflow: Score → Percentage → Grade")
    print("-" * 40)
    assignments = [
        ("Quiz 1", 18, 20),
        ("Homework 1", 47, 50),
        ("Midterm Exam", 82, 100),
        ("Final Project", 93, 100),
    ]
    
    for name, earned, possible in assignments:
        pct = score_to_percentage(earned, possible)
        grade = calculate_grade(pct)
        print(f"{name:20s}: {earned:>3}/{possible:<3} = {pct:>6.2f}% ({grade})")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
