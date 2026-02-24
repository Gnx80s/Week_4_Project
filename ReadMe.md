#  Password Strength Analyzer

## Overview

The **Password Strength Analyzer** is a lightweight Python application that evaluates the strength of a password based on key security factors such 
as length, character diversity, and unpredictability. It instantly classifies any password as *Weak*, *Moderate*, or *Strong* and provides improvement suggestions.
This project was developed for educational purposes and cybersecurity awareness.

---

## Features

- Evaluates passwords instantly through the command line
- Checks for uppercase, lowercase, numeric, and special characters
- Detects common or predictable password patterns
- Displays personalized improvement feedback
- Uses a scoring system (0–10 points)
- 100% local execution — no data storage or external connection

---

##  Strength Criteria 

| Category               | Description                                |
|------------------------|--------------------------------------------|
| **Length**             | Passwords ≥ 12 characters score highest    |
| **Uppercase**          | Adds security by including capital letters |
| **Lowercase**          | Ensures readability and diversity          |
| **Numbers**            | Introduces additional complexity           |
| **Special characters** | Adds entropy and unpredictability          |
| **Avoid common terms** | Prevents easy guessing attacks             |

---

## System Flow

1. **Input Stage**  
   User enters a password via the command line.

2. **Evaluation Stage**  
   The analyzer checks:
   - Minimum length requirements  
   - Uppercase and lowercase characters  
   - Numbers and special characters  
   - Predictable/common phrases  

3. **Scoring Stage**  
   Each satisfied condition adds to a cumulative score (maximum of 10 points).

4. **Classification**
   - **Weak:** 0–3 points  
   - **Moderate:** 4–6 points  
   - **Strong:** 7–10 points  

5. **Feedback Output**  
   Suggestions are generated to help improve weak areas.

---

## Installation & Usage

### Requirements

- Python 3.8 or higher

### Installation

```bash
git clone https://github.com/Gnx80s/Password-Strength-Analyzer.git
cd Password-Strength-Analyzer

