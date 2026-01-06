# Cognifyz Technologies - Software Development Internship

![Cognifyz Technologies](https://img.shields.io/badge/Cognifyz-Technologies-orange)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Status](https://img.shields.io/badge/Status-Complete-success)

## 📋 About This Project

This repository contains complete solutions for the **Cognifyz Technologies Software Development Internship Program**. All 6 tasks across 3 difficulty levels (Beginner, Intermediate, and Advanced) have been implemented with clean, well-documented code following the exact PDF specifications.

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
├── level3_task5_file_io.py           # Enhanced CRUD with Text File I/O
├── level3_task6_webscraping.py       # Web Scraping Program
├── requirements.txt                   # Python dependencies
└── README.md                         # Project documentation
```

## 🚀 Tasks Completed

### Level 1: Beginner

#### ✅ Task 1: Text-Based Number Guessing Game
**File:** `level1_task1_game.py`

**Objective:** Implement a simple game using conditional statements for game logic.

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

**Steps Implemented:**
1. ✅ Chose game type: Number guessing game
2. ✅ Defined game rules and logic
3. ✅ Used conditional statements to manage game flow
4. ✅ Tested and debugged for correctness

---

#### ✅ Task 2: Number Pattern Generator
**File:** `level1_task2_patterns.py`

**Objective:** Utilize loops to control the structure of number patterns.

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

**Steps Implemented:**
1. ✅ Selected pattern types (pyramid and more)
2. ✅ Developed program to generate patterns
3. ✅ Used loops to control pattern structure
4. ✅ Verified correctness of generated patterns

---

### Level 2: Intermediate

#### ✅ Task 3: CRUD Task Manager Application
**File:** `level2_task3_crud.py`

**Objective:** Implement Create, Read, Update, and Delete operations using arrays or lists for data storage.

**Features:**
- **Create:** Add new tasks with title, description, priority
- **Read:** View all tasks or detailed task information
- **Update:** Modify task details (title, description, status, priority)
- **Delete:** Remove tasks with confirmation
- Task attributes: ID, title, description, status, priority, timestamp
- JSON-based storage for convenience

**How to Run:**
```bash
python level2_task3_crud.py
```

**Steps Implemented:**
1. ✅ Defined Task class with necessary attributes
2. ✅ Implemented functionality to create new tasks
3. ✅ Developed method to read and display tasks
4. ✅ Allowed users to update task details
5. ✅ Provided option to delete tasks
6. ✅ Tested application with various scenarios

---

#### ✅ Task 4: Temperature Converter
**File:** `level2_task4_temperature.py`

**Objective:** Enable users to input temperatures and choose the conversion direction between Fahrenheit and Celsius.

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

**Steps Implemented:**
1. ✅ Designed program to accept temperature input
2. ✅ Implemented logic for temperature conversion
3. ✅ Allowed users to choose conversion direction
4. ✅ Tested program with different input values

---

### Level 3: Advanced

#### ✅ Task 5: Enhanced CRUD with File I/O
**File:** `level3_task5_file_io.py`

**Objective:** Implement file storage for tasks to enable saving and loading from a text file.

**Features:**
- **Plain text file storage** (as specified in PDF)
- Persistent data storage using `.txt` format
- Auto-save after create/update/delete operations
- Manual save/load options
- Comprehensive error handling:
  - FileNotFoundError
  - PermissionError
  - IOError
  - General exceptions
- **Test Persistence** feature to verify data integrity
- Pipe-delimited format for easy parsing

**How to Run:**
```bash
python level3_task5_file_io.py
```

**Steps Implemented:**
1. ✅ Modified application to read and write tasks to text file
2. ✅ Implemented error handling for file operations
3. ✅ Tested persistence of task data with dedicated test function

**File Format:**
```
# Task Manager Data File
# Format: ID|Title|Description|Status|Priority|CreatedAt
1|Complete Project|Finish internship tasks|In Progress|High|2026-01-06 18:30:00
2|Review Code|Check for bugs|Pending|Medium|2026-01-06 18:31:00
```

---

#### ✅ Task 6: Interactive Web Scraping Program
**File:** `level3_task6_webscraping.py`

**Objective:** Fetch data from a website and present it in a user-friendly way using a simple web scraping library.

**Features:**
- Scrape data from multiple websites:
  - **Quotes:** quotes.toscrape.com (quotes, authors, tags)
  - **News:** Hacker News (headlines, URLs)
  - **Books:** books.toscrape.com (titles, prices, ratings)
- User-friendly data presentation with formatted output
- Save scraped data to JSON files with timestamps
- Error handling for network requests
- Interactive menu system
- Uses BeautifulSoup4 (simple web scraping library as specified)

**How to Run:**
```bash
# Install dependencies first
pip install -r requirements.txt

# Run the program
python level3_task6_webscraping.py
```

**Steps Implemented:**
1. ✅ Selected websites and identified data to scrape
2. ✅ Utilized web scraping library (BeautifulSoup) to fetch data
3. ✅ Designed user-friendly presentation format
4. ✅ Tested program with different websites

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
# Level 1 Tasks
python level1_task1_game.py
python level1_task2_patterns.py

# Level 2 Tasks
python level2_task3_crud.py
python level2_task4_temperature.py

# Level 3 Tasks
python level3_task5_file_io.py
python level3_task6_webscraping.py
```

---

## 📦 Dependencies

```
requests==2.31.0
beautifulsoup4==4.12.2
```

**Note:** Only required for Task 6 (Web Scraping). All other tasks use Python standard library only.

---

## 💡 Key Features Across All Tasks

- ✅ **Strictly follows PDF specifications**
- ✅ Clean, well-documented code
- ✅ Comprehensive error handling
- ✅ User-friendly interfaces
- ✅ Input validation
- ✅ Modular design with functions/classes
- ✅ Professional formatting and structure
- ✅ Extensive comments and docstrings
- ✅ All steps from PDF implemented

---

## 🎓 Learning Outcomes

Through this internship, I've demonstrated proficiency in:

1. **Python Fundamentals:**
   - Conditional statements and loops
   - Functions and classes
   - File I/O operations (text files)
   - Exception handling

2. **Data Structures:**
   - Lists and dictionaries
   - Arrays for data storage
   - Object-oriented programming

3. **External Libraries:**
   - Web scraping with BeautifulSoup
   - HTTP requests with requests library

4. **Software Development Best Practices:**
   - Code organization and modularity
   - Documentation and comments
   - User experience design
   - Error handling and validation
   - Data persistence

---

## 📸 Example Outputs

### Task 1: Number Guessing Game
```
==================================================
Welcome to the Number Guessing Game!
==================================================

Select Difficulty:
1. Easy (1-50, 10 attempts)
2. Medium (1-100, 7 attempts)
3. Hard (1-200, 5 attempts)

Enter choice (1-3): 2

I'm thinking of a number between 1 and 100
You have 7 attempts to guess it!
```

### Task 2: Number Patterns
```
Select a pattern:
1. Number Pyramid
2. Reverse Pyramid
3. Diamond Pattern
4. Floyd's Triangle
5. Pascal's Triangle

Enter number of rows: 5

    1 
   1 2 
  1 2 3 
 1 2 3 4 
1 2 3 4 5 
```

### Task 3: Task Manager
```
======================================================================================
ID    Title                Status       Priority   Created             
======================================================================================
1     Complete Project     In Progress  High       2026-01-06 18:30:00
2     Review Code          Pending      Medium     2026-01-06 18:31:00
======================================================================================
```

### Task 5: File Persistence Test
```
Testing Data Persistence
============================================================
1. Current tasks in memory: [Shows all tasks]
2. Saving to file...
💾 Tasks saved to tasks.txt
3. Clearing memory...
   Memory cleared. Tasks in memory: 0
4. Loading from file...
📂 Loaded 2 task(s) from tasks.txt
5. Tasks after loading: [Shows all tasks restored]

✅ Persistence test PASSED! All tasks restored successfully.
```

---

## 📋 PDF Requirements Checklist

### Level 1
- ✅ Task 1: Text-based game with conditional statements
- ✅ Task 2: Number patterns using loops

### Level 2
- ✅ Task 3: CRUD operations with arrays/lists
- ✅ Task 4: Temperature converter with user input

### Level 3
- ✅ Task 5: File I/O with **text file** storage and error handling
- ✅ Task 6: Web scraping with simple library (BeautifulSoup)

### General Requirements
- ✅ Separate file for each task
- ✅ All steps from PDF implemented
- ✅ Proper error handling
- ✅ User-friendly interfaces
- ✅ Testing completed

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
- LinkedIn: [Connect with me](https://www.linkedin.com/in/mohammed-mishal/)

---

## 📝 Submission Guidelines (From PDF)

1. ✅ Create professional video showcasing projects
2. ✅ Host video on LinkedIn
3. ✅ Tag @cognifyz-Technologies
4. ✅ Use hashtags: #cognifyztechnologies #cognifyz #cognifyztech
5. ✅ Make separate file for each level
6. ⏳ Wait for submission form

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
**Version:** 1.0.1  
**Status:** Complete ✅ (All PDF requirements strictly followed)
