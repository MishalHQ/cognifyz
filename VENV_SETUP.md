# Virtual Environment Setup Guide (macOS/Linux)

## 🚨 If You Get "externally-managed-environment" Error

This is normal on macOS with Homebrew Python. Follow these steps:

---

## ✅ Solution: Use Virtual Environment (Recommended)

### Step 1: Create Virtual Environment

```bash
# Navigate to project directory
cd /Users/11b51/Downloads/Projects/cognifyz/cognifyz

# Create virtual environment
python3 -m venv venv
```

### Step 2: Activate Virtual Environment

```bash
# Activate (macOS/Linux)
source venv/bin/activate

# You should see (venv) in your terminal prompt
```

### Step 3: Install Dependencies

```bash
# Now install packages (inside virtual environment)
pip install requests beautifulsoup4

# Or use requirements.txt
pip install -r requirements.txt
```

### Step 4: Run Tasks

```bash
# Run any task (while venv is activated)
python level3_task6_webscraping.py

# Or any other task
python level1_task1_game.py
```

### Step 5: Deactivate When Done

```bash
# Exit virtual environment
deactivate
```

---

## 🎯 Quick Copy-Paste Commands

```bash
# All in one - Copy and paste this entire block
cd /Users/11b51/Downloads/Projects/cognifyz/cognifyz
python3 -m venv venv
source venv/bin/activate
pip install requests beautifulsoup4
python level3_task6_webscraping.py
```

---

## 🔄 Next Time You Want to Run Tasks

```bash
# Navigate to project
cd /Users/11b51/Downloads/Projects/cognifyz/cognifyz

# Activate virtual environment
source venv/bin/activate

# Run any task
python level3_task6_webscraping.py

# Deactivate when done
deactivate
```

---

## 🛠️ Alternative Solutions (If You Don't Want Virtual Environment)

### Option 1: Install with --user flag
```bash
pip3 install --user requests beautifulsoup4
```

### Option 2: Use --break-system-packages (Not Recommended)
```bash
pip3 install --break-system-packages requests beautifulsoup4
```

### Option 3: Use pipx (For Applications)
```bash
brew install pipx
pipx install requests beautifulsoup4
```

---

## 📁 What is venv/ folder?

After creating virtual environment, you'll see a `venv/` folder:

```
cognifyz/
├── venv/                          # Virtual environment (don't commit to git)
├── level1_task1_game.py
├── level1_task2_patterns.py
├── ...
```

**Note:** The `venv/` folder is already in `.gitignore` so it won't be committed to GitHub.

---

## ✅ Verify Installation

```bash
# Activate venv first
source venv/bin/activate

# Check if packages are installed
python -c "import requests; import bs4; print('✅ All dependencies installed!')"
```

---

## 🎓 Understanding Virtual Environments

**What is it?**
- Isolated Python environment for your project
- Doesn't affect system Python
- Each project can have different package versions

**Why use it?**
- ✅ Avoids conflicts between projects
- ✅ Keeps system Python clean
- ✅ Recommended best practice
- ✅ Required on modern macOS

**When to activate?**
- Every time you want to run Task 6 (web scraping)
- Other tasks (1-5) don't need it

---

## 🚀 Pro Tip: Create Alias

Add to your `~/.zshrc` or `~/.bash_profile`:

```bash
alias cognifyz='cd /Users/11b51/Downloads/Projects/cognifyz/cognifyz && source venv/bin/activate'
```

Then just type:
```bash
cognifyz
python level3_task6_webscraping.py
```

---

## 📝 Summary

**For Task 6 (Web Scraping):**
1. Create venv: `python3 -m venv venv`
2. Activate: `source venv/bin/activate`
3. Install: `pip install requests beautifulsoup4`
4. Run: `python level3_task6_webscraping.py`
5. Deactivate: `deactivate`

**For Tasks 1-5:**
- No virtual environment needed
- Run directly: `python3 level1_task1_game.py`

---

## ❓ Troubleshooting

### "venv: command not found"
```bash
python3 -m venv venv
```

### "Permission denied"
```bash
chmod +x venv/bin/activate
source venv/bin/activate
```

### "Still getting errors"
```bash
# Remove old venv and recreate
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install requests beautifulsoup4
```
