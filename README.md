# Cognifyz Technologies - Software Development Internship

![Cognifyz Technologies](https://img.shields.io/badge/Cognifyz-Technologies-orange)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Status](https://img.shields.io/badge/Status-Complete-success)

## 📋 About This Project

This repository contains complete solutions for the **Cognifyz Technologies Software Development Internship Program**. All 6 tasks across 3 difficulty levels (Beginner, Intermediate, and Advanced) have been implemented with clean, well-documented code.

## 🎯 Internship Overview

**Company:** Cognifyz Technologies  
**Program:** Software Development Internship  
**Requirement:** Complete at least 4 out of 6 tasks  
**Status:** ✅ All 6 tasks completed

## 📁 Project Structure

```
cognifyz/
├── level1_task1_game.py              # Number Guessing Game
├── level1_task2_patterns.py          # Number Pattern Generator
├── level2_task3_crud.py              # Task Manager (CRUD Application)
├── level2_task4_temperature.py       # Temperature Converter
├── level3_task6_webscraping.py       # Web Scraping Program
├── requirements.txt                   # Python dependencies
└── README.md                         # Project documentation
```

## 🚀 Tasks Completed

### Level 1: Beginner

#### ✅ Task 1: Text-Based Number Guessing Game
**File:** `level1_task1_game.py`

**Features:**
- Three difficulty levels (Easy, Medium, Hard)
- Dynamic attempt limits based on difficulty
- Input validation and error handling
- Play again functionality
- User-friendly interface with emojis

**How to Run:**
```bash
python level1_task1_game.py
```

---

#### ✅ Task 2: Number Pattern Generator
**File:** `level1_task2_patterns.py`

**Features:**
- 5 different pattern types:
  - Number Pyramid
  - Reverse Pyramid
  - Diamond Pattern
  - Floyd's Triangle
  - Pascal's Triangle
- Interactive menu system
- Customizable row count
- Input validation

**How to Run:**
```bash
python level1_task2_patterns.py
```

---

### Level 2: Intermediate

#### ✅ Task 3: CRUD Task Manager Application
**File:** `level2_task3_crud.py`

**Features:**
- **Create:** Add new tasks with title, description, priority
- **Read:** View all tasks or detailed task information
- **Update:** Modify task details (title, description, status, priority)
- **Delete:** Remove tasks with confirmation
- **Persistent Storage:** Save/load tasks from JSON file
- Task attributes: ID, title, description, status, priority, timestamp
- Error handling for file operations

**How to Run:**
```bash
python level2_task3_crud.py
```

**Note:** This task also fulfills **Level 3 Task 5** requirements (File I/O persistence).

---

#### ✅ Task 4: Temperature Converter
**File:** `level2_task4_temperature.py`

**Features:**
- Bidirectional conversions between:
  - Celsius ↔ Fahrenheit
  - Celsius ↔ Kelvin
  - Fahrenheit ↔ Kelvin
- "Convert All" feature for comprehensive conversion
- Temperature context information (freezing/boiling points)
- Input validation and error handling
- User-friendly interface

**How to Run:**
```bash
python level2_task4_temperature.py
```

---

### Level 3: Advanced

#### ✅ Task 5: File I/O Enhancement
**Integrated in:** `level2_task3_crud.py`

**Features:**
- JSON-based persistent storage
- Automatic save on exit
- Load tasks on startup
- Error handling for file operations
- Data integrity maintenance

**Implementation Details:**
- `save_to_file()` method: Saves tasks to JSON
- `load_from_file()` method: Loads tasks from JSON
- Automatic ID management after loading

---

#### ✅ Task 6: Interactive Web Scraping Program
**File:** `level3_task6_webscraping.py`

**Features:**
- Scrape data from multiple websites:
  - **Quotes:** quotes.toscrape.com (quotes, authors, tags)
  - **News:** Hacker News (headlines, URLs)
  - **Books:** books.toscrape.com (titles, prices, ratings)
- User-friendly data presentation
- Save scraped data to JSON files with timestamps
- Error handling for network requests
- Interactive menu system

**How to Run:**
```bash
# Install dependencies first
pip install -r requirements.txt

# Run the program
python level3_task6_webscraping.py
```

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository:**
```bash
git clone https://github.com/MishalHQ/cognifyz.git
cd cognifyz
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run any task:**
```bash
# Example: Run the guessing game
python level1_task1_game.py

# Example: Run the task manager
python level2_task3_crud.py

# Example: Run web scraper
python level3_task6_webscraping.py
```

---

## 📦 Dependencies

```
requests==2.31.0
beautifulsoup4==4.12.2
```

**Note:** Only required for Task 6 (Web Scraping). Other tasks use Python standard library only.

---

## 💡 Key Features Across All Tasks

- ✅ Clean, well-documented code
- ✅ Comprehensive error handling
- ✅ User-friendly interfaces
- ✅ Input validation
- ✅ Modular design with functions/classes
- ✅ Professional formatting and structure
- ✅ Extensive comments and docstrings

---

## 🎓 Learning Outcomes

Through this internship, I've demonstrated proficiency in:

1. **Python Fundamentals:**
   - Conditional statements and loops
   - Functions and classes
   - File I/O operations
   - Exception handling

2. **Data Structures:**
   - Lists and dictionaries
   - JSON data manipulation
   - Object-oriented programming

3. **External Libraries:**
   - Web scraping with BeautifulSoup
   - HTTP requests with requests library

4. **Software Development Best Practices:**
   - Code organization and modularity
   - Documentation and comments
   - User experience design
   - Error handling and validation

---

## 📸 Screenshots & Demo

### Task 1: Number Guessing Game
```
==================================================
Welcome to the Number Guessing Game!
==================================================

Select Difficulty:
1. Easy (1-50, 10 attempts)
2. Medium (1-100, 7 attempts)
3. Hard (1-200, 5 attempts)
```

### Task 3: Task Manager
```
================================================================================
ID    Title                Status       Priority   Created             
================================================================================
1     Complete Project     In Progress  High       2026-01-06 18:30:00
2     Review Code          Pending      Medium     2026-01-06 18:31:00
================================================================================
```

---

## 🤝 Acknowledgments

- **Cognifyz Technologies** for providing this learning opportunity
- The internship program for structured learning paths
- Open-source community for tools and libraries

---

## 📞 Contact

**Mohammed Mishal**  
- GitHub: [@MishalHQ](https://github.com/MishalHQ)
- Email: mohammedmishal2004@gmail.com

---

## 📄 License

This project is created for educational purposes as part of the Cognifyz Technologies internship program.

---

## 🏷️ Hashtags

#cognifyz #cognifyzTech #cognifyzTechnologies #SoftwareDevelopment #PythonProgramming #InternshipProject

---

## ⭐ Show Your Support

If you found this project helpful, please consider giving it a star! ⭐

---

**Last Updated:** January 6, 2026  
**Version:** 1.0.0  
**Status:** Complete ✅
