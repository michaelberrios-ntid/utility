# Educational Utility Tools

A Python 3.10+ utility repository for reusable educational tools. Includes importable modules and command-line utilities for grading calculations, rubric generation, and LMS-friendly exports. Designed for clarity, reusability, and easy extension for teaching and academic workflows.

**✨ Features:**
- 🎓 **Grade Calculator**: Convert scores to percentages and letter grades
- 📋 **Rubric Exporter**: Create and export grading rubrics in CSV/JSON format
- 🔧 **Importable Business Logic**: Use as a library in your own Python projects
- 🖥️ **CLI Tools**: User-friendly command-line interfaces with argparse
- 🌍 **Cross-Platform**: Works on Windows and Linux
- 📝 **Type Hints & Docstrings**: Clean, beginner-readable code style
- 🎯 **Zero External Dependencies**: Uses only Python standard library

## Requirements

- Python 3.10 or higher
- Operating System: Windows or Linux

## Installation

### From Source (Development)

```bash
# Clone the repository
git clone https://github.com/michaelberrios-ntid/utility.git
cd utility

# Install in editable mode
pip install -e .
```

## Usage

### 1. Grade Calculator

#### As a Python Library

```python
from utility.core.grade_calculator import calculate_grade, score_to_percentage

# Convert score to percentage
percentage = score_to_percentage(85, 100)  # Returns 85.0

# Calculate letter grade
grade = calculate_grade(92.5)  # Returns 'A'
grade = calculate_grade(85.0)  # Returns 'B'

# Use custom grading scale
custom_scale = {
    90.0: "A", 
    80.0: "B", 
    70.0: "C", 
    60.0: "D", 
    0.0: "F"
}
grade = calculate_grade(85.0, custom_scale)  # Returns 'B'
```

#### Command-Line Interface

```bash
# Calculate grade from raw score
grade-calc --score 85 --max-score 100

# Calculate grade from percentage
grade-calc --percentage 92.5

# Use custom grading scale
grade-calc --percentage 85 --scale "90:A" "80:B" "70:C" "60:D" "0:F"
```

### 2. Rubric Exporter

#### As a Python Library

```python
from utility.core.rubric_exporter import RubricExporter, RubricCriterion

# Define criteria
criteria = [
    RubricCriterion(
        name="Code Quality",
        description="Clean, readable code",
        max_points=25.0,
        levels={
            "Excellent": 25.0,
            "Good": 20.0,
            "Fair": 15.0,
            "Poor": 10.0
        }
    ),
    RubricCriterion(
        name="Documentation",
        description="Comprehensive docstrings",
        max_points=15.0
    )
]

# Create and export rubric
rubric = RubricExporter("Assignment 1", criteria)
rubric.export_csv("rubric.csv")
rubric.export_json("rubric.json")

# Get total points
total = rubric.total_points()  # Returns 40.0
```

#### Command-Line Interface

```bash
# Export from JSON definition file
rubric-export --input examples/sample_rubric.json --output rubric.csv --format csv

# Quick rubric from command line
rubric-export --title "Assignment 1" \
  --criteria "Code Quality" 25 \
  --criteria "Documentation" 15 \
  --output rubric.csv \
  --format csv

# Export to JSON format
rubric-export --input examples/sample_rubric.json --output rubric.json --format json
```

## Examples

Run the example scripts to see the tools in action:

```bash
# Grade calculator examples
python examples/grade_calculator_example.py

# Rubric exporter examples
python examples/rubric_exporter_example.py
```

### Sample Rubric JSON Format

See `examples/sample_rubric.json` for a complete example. The JSON format is:

```json
{
  "title": "Assignment Title",
  "criteria": [
    {
      "name": "Criterion Name",
      "description": "What this evaluates",
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
```

## Project Structure

```
utility/
├── utility/                  # Main package
│   ├── __init__.py          # Package exports
│   ├── core/                # Business logic (importable)
│   │   ├── __init__.py
│   │   ├── grade_calculator.py
│   │   └── rubric_exporter.py
│   └── cli/                 # CLI interfaces (argparse)
│       ├── __init__.py
│       ├── grade_calculator.py
│       └── rubric_exporter.py
├── examples/                # Usage examples
│   ├── grade_calculator_example.py
│   ├── rubric_exporter_example.py
│   └── sample_rubric.json
├── pyproject.toml          # Project metadata
├── README.md               # This file
└── .gitignore             # Git ignore patterns
```

## Design Principles

1. **Separation of Concerns**: Business logic (`core/`) is separate from CLI code (`cli/`)
2. **Importable**: All core modules can be imported and used in other projects
3. **Type Safety**: Comprehensive type hints for better IDE support and fewer bugs
4. **Documentation**: Every function has docstrings with examples
5. **Cross-Platform**: Uses `pathlib.Path` for file operations
6. **Beginner-Friendly**: Clear, readable code with educational comments

## Development

### Code Style

This project follows:
- PEP 8 style guidelines
- Type hints for all function signatures
- Docstrings with examples for all public functions
- Maximum line length of 100 characters

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please ensure:
- Code follows PEP 8 style guidelines
- All functions have type hints and docstrings
- Changes work on both Windows and Linux
- Existing tests pass (if applicable)

## Author

Michael Berrios
