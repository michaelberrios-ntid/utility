"""
Command-line interface for rubric export.

This CLI tool wraps the rubric_exporter core module, providing a
user-friendly command-line interface for creating and exporting rubrics.
"""

import argparse
import json
import sys
from pathlib import Path
from utility.core.rubric_exporter import RubricExporter, RubricCriterion


def main() -> None:
    """
    Main entry point for the rubric exporter CLI.

    Parses command-line arguments and exports rubrics to CSV or JSON format.
    """
    parser = argparse.ArgumentParser(
        description="Export grading rubrics for MyCourses and other LMS platforms.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Export from JSON rubric definition
  %(prog)s --input rubric_definition.json --output rubric.csv --format csv
  
  # Export to JSON format
  %(prog)s --input rubric_definition.json --output rubric.json --format json
  
  # Quick rubric from command line
  %(prog)s --title "Assignment 1" --criteria "Code Quality" 25 --criteria "Documentation" 15 --output rubric.csv

Rubric Definition JSON Format:
  {
    "title": "Assignment 1",
    "criteria": [
      {
        "name": "Code Quality",
        "description": "Clean, readable, and well-structured code",
        "max_points": 25,
        "levels": {
          "Excellent": 25,
          "Good": 20,
          "Fair": 15,
          "Poor": 10
        }
      }
    ]
  }
        """
    )
    
    # Input options
    parser.add_argument(
        "--input",
        type=str,
        help="Path to JSON file containing rubric definition"
    )
    parser.add_argument(
        "--title",
        type=str,
        help="Rubric title (for quick command-line creation)"
    )
    parser.add_argument(
        "--criteria",
        action="append",
        nargs=2,
        metavar=("NAME", "POINTS"),
        help="Add criterion: name and max_points (can be used multiple times)"
    )
    
    # Output options
    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="Output file path"
    )
    parser.add_argument(
        "--format",
        choices=["csv", "json"],
        required=True,
        help="Output format (csv or json)"
    )
    
    args = parser.parse_args()
    
    try:
        # Load rubric from input JSON or create from command line
        if args.input:
            # Load from JSON file
            input_path = Path(args.input)
            if not input_path.exists():
                print(f"Error: Input file not found: {args.input}", file=sys.stderr)
                sys.exit(1)
            
            with input_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            
            title = data["title"]
            criteria = [
                RubricCriterion(
                    name=c["name"],
                    description=c["description"],
                    max_points=c["max_points"],
                    levels=c.get("levels")
                )
                for c in data["criteria"]
            ]
        
        elif args.title and args.criteria:
            # Create from command-line arguments
            title = args.title
            criteria = [
                RubricCriterion(
                    name=name,
                    description=f"{name} evaluation",
                    max_points=float(points)
                )
                for name, points in args.criteria
            ]
        
        else:
            parser.error("Either --input or both --title and --criteria are required")
        
        # Create exporter and export
        exporter = RubricExporter(title, criteria)
        
        print(f"Rubric: {title}")
        print(f"Total Points: {exporter.total_points()}")
        print(f"Criteria: {len(criteria)}")
        
        output_path = Path(args.output)
        
        if args.format == "csv":
            exporter.export_csv(output_path)
            print(f"\nExported to CSV: {output_path}")
        else:
            exporter.export_json(output_path)
            print(f"\nExported to JSON: {output_path}")
        
    except (ValueError, KeyError, json.JSONDecodeError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
