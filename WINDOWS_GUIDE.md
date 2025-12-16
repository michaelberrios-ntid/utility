# Windows User Guide

This guide shows how to use the educational utility tools on Windows systems.

## Installation on Windows

```powershell
# Using PowerShell or Command Prompt
cd path\to\utility
pip install -e .
```

## Usage Examples (Windows)

### Grade Calculator

```powershell
# Calculate grade from raw score
grade-calc --score 85 --max-score 100

# Calculate grade from percentage
grade-calc --percentage 92.5

# Use custom grading scale
grade-calc --percentage 85 --scale "90:A" "80:B" "70:C" "60:D" "0:F"
```

### Rubric Exporter

```powershell
# Export from JSON file (Windows path style)
rubric-export --input examples\sample_rubric.json --output C:\Users\YourName\Documents\rubric.csv --format csv

# Quick rubric creation
rubric-export --title "Assignment 1" --criteria "Code Quality" 25 --criteria "Documentation" 15 --output rubric.csv --format csv

# Export to desktop (common Windows path)
rubric-export --input examples\sample_rubric.json --output %USERPROFILE%\Desktop\rubric.json --format json
```

### Running Examples on Windows

```powershell
# Run example scripts
python examples\grade_calculator_example.py
python examples\rubric_exporter_example.py
python examples\full_demo.py
```

## Cross-Platform Path Handling

The utility package uses Python's `pathlib.Path` module internally, which automatically handles path differences between Windows and Linux:

- **Windows**: `C:\Users\Name\Documents\rubric.csv`
- **Linux**: `/home/name/documents/rubric.csv`

Both work seamlessly when passed to the tools!

## Python Code Usage (Windows)

```python
# Works identically on Windows and Linux
from pathlib import Path
from utility import RubricExporter, RubricCriterion

# Windows-style path
output = Path(r"C:\Users\Name\Documents\rubric.csv")

# Or use forward slashes (Python handles it!)
output = Path("C:/Users/Name/Documents/rubric.csv")

# Export works the same way
criterion = RubricCriterion("Test", "Description", 10.0)
rubric = RubricExporter("My Rubric", [criterion])
rubric.export_csv(output)
```

## Common Windows Paths

```python
from pathlib import Path

# User's home directory
home = Path.home()  # C:\Users\YourName

# Desktop
desktop = home / "Desktop"

# Documents
documents = home / "Documents"

# Downloads
downloads = home / "Downloads"

# Temporary files
import tempfile
temp_dir = Path(tempfile.gettempdir())  # C:\Users\YourName\AppData\Local\Temp
```

## Tips for Windows Users

1. **Backslashes**: Use raw strings (`r"C:\path"`) or forward slashes (`"C:/path"`) in Python
2. **Environment Variables**: Use `%USERPROFILE%` in CLI, `Path.home()` in Python
3. **Path Separators**: `pathlib.Path` handles separator differences automatically
4. **File Extensions**: Windows doesn't require execute permissions like Linux

## Troubleshooting

### Command Not Found
If `grade-calc` or `rubric-export` commands don't work:

```powershell
# Ensure pip's script directory is in PATH
python -m utility.cli.grade_calculator --help
python -m utility.cli.rubric_exporter --help
```

### Python Version
Verify you have Python 3.10 or higher:

```powershell
python --version
```

Should show Python 3.10.0 or higher.

## Need Help?

All features work identically on Windows and Linux. If you encounter any platform-specific issues, please report them!
