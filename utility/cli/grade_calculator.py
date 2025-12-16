"""
Command-line interface for grade calculation.

This CLI tool wraps the grade_calculator core module, providing a
user-friendly command-line interface using argparse.
"""

import argparse
import sys
from utility.core.grade_calculator import calculate_grade, score_to_percentage


def main() -> None:
    """
    Main entry point for the grade calculator CLI.

    Parses command-line arguments and calculates letter grades from scores.
    """
    parser = argparse.ArgumentParser(
        description="Calculate letter grades from scores and percentages.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Calculate grade from raw score
  %(prog)s --score 85 --max-score 100
  
  # Calculate grade from percentage
  %(prog)s --percentage 92.5
  
  # Use custom grading scale
  %(prog)s --percentage 85 --scale "90:A" "80:B" "70:C" "60:D" "0:F"
        """
    )
    
    # Input options (mutually exclusive)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        "--score",
        type=float,
        help="Raw score earned by student"
    )
    input_group.add_argument(
        "--percentage",
        type=float,
        help="Percentage score (0-100)"
    )
    
    # Additional options
    parser.add_argument(
        "--max-score",
        type=float,
        help="Maximum possible score (required with --score)"
    )
    parser.add_argument(
        "--scale",
        nargs="+",
        metavar="THRESHOLD:GRADE",
        help='Custom grading scale as "min_percentage:grade" pairs (e.g., "90:A" "80:B")'
    )
    
    args = parser.parse_args()
    
    try:
        # Calculate percentage if score is provided
        if args.score is not None:
            if args.max_score is None:
                parser.error("--max-score is required when using --score")
            percentage = score_to_percentage(args.score, args.max_score)
            print(f"Score: {args.score}/{args.max_score}")
            print(f"Percentage: {percentage:.2f}%")
        else:
            percentage = args.percentage
            print(f"Percentage: {percentage:.2f}%")
        
        # Parse custom scale if provided
        scale = None
        if args.scale:
            scale = {}
            for item in args.scale:
                try:
                    threshold_str, grade = item.split(":")
                    threshold = float(threshold_str)
                    scale[threshold] = grade
                except ValueError:
                    parser.error(f"Invalid scale format: {item}. Use THRESHOLD:GRADE")
        
        # Calculate and display grade
        grade = calculate_grade(percentage, scale)
        print(f"Letter Grade: {grade}")
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
