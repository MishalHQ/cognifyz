# Setup Guide for Cognifyz Internship Tasks

## Quick Start

### Step 1: Install Python Dependencies

For **Task 6 (Web Scraping)** only, you need to install external libraries:

```bash
pip3 install requests beautifulsoup4
```

Or using the requirements file:

```bash
pip3 install -r requirements.txt
```

### Step 2: Verify Installation

```bash
python3 -c "import requests; import bs4; print('Dependencies installed successfully!')"
```

---

## Task-by-Task Requirements

### Level 1 Tasks (No Dependencies)
- ✅ **Task 1:** `python3 level1_task1_game.py` - No dependencies needed
- ✅ **Task 2:** `python3 level1_task2_patterns.py` - No dependencies needed

### Level 2 Tasks (No Dependencies)
- ✅ **Task 3:** `python3 level2_task3_crud.py` - No dependencies needed
- ✅ **Task 4:** `python3 level2_task4_temperature.py` - No dependencies needed

### Level 3 Tasks
- ✅ **Task 5:** `python3 level3_task5_file_io.py` - No dependencies needed
- ⚠️ **Task 6:** `python3 level3_task6_webscraping.py` - **Requires:** requests, beautifulsoup4

---

## Installation Methods

### Method 1: Using pip3 (Recommended)
```bash
pip3 install requests beautifulsoup4
```

### Method 2: Using pip
```bash
pip install requests beautifulsoup4
```

### Method 3: Using requirements.txt
```bash
pip3 install -r requirements.txt
```

### Method 4: Using Python 3.13 specifically
```bash
/opt/homebrew/bin/python3.13 -m pip install requests beautifulsoup4
```

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'requests'"

**Solution:**
```bash
# Install for your specific Python version
/opt/homebrew/bin/python3.13 -m pip install requests beautifulsoup4
```

### Issue: "pip: command not found"

**Solution:**
```bash
# Install pip first
python3 -m ensurepip --upgrade
```

### Issue: Permission denied

**Solution:**
```bash
# Install for user only (no sudo needed)
pip3 install --user requests beautifulsoup4
```

---

## Running Tasks

### Run All Tasks (Test Everything)
```bash
# Level 1
python3 level1_task1_game.py
python3 level1_task2_patterns.py

# Level 2
python3 level2_task3_crud.py
python3 level2_task4_temperature.py

# Level 3
python3 level3_task5_file_io.py
python3 level3_task6_webscraping.py  # Requires dependencies
```

---

## For Your Specific Setup (macOS with Homebrew Python)

```bash
# Navigate to project directory
cd /Users/11b51/Downloads/Projects/cognifyz/cognifyz

# Install dependencies for Python 3.13
/opt/homebrew/bin/python3.13 -m pip install requests beautifulsoup4

# Run Task 6
/opt/homebrew/bin/python3.13 level3_task6_webscraping.py
```

---

## Verify Your Python Version

```bash
python3 --version
which python3
```

---

## Alternative: Run Tasks Without Dependencies

If you want to complete the internship without installing dependencies, you can skip Task 6 and complete any 4 of the other 5 tasks:

- ✅ Task 1: Number Guessing Game
- ✅ Task 2: Pattern Generator
- ✅ Task 3: CRUD Application
- ✅ Task 4: Temperature Converter
- ✅ Task 5: File I/O Enhancement

**Note:** The internship requires completing at least 4 out of 6 tasks.
