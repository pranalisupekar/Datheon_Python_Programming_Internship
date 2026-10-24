# Task 4: Rule-Based Customer Support Chatbot

## Description

This project implements an interactive rule-based customer support chatbot using Python. It identifies user queries using keywords and regular expressions and retrieves predefined answers from a JSON FAQ dataset.

## Features

* Greeting detection
* FAQ loading from a JSON file
* Keyword matching using regular expressions
* Multi-intent response handling
* Fallback responses for unknown questions
* Exit commands: `bye`, `exit`, and `quit`
* Error handling for missing or invalid JSON files
* Basic conversational state management

## Technologies Used

* Python 3
* JSON
* Regular Expressions (`re`)

## Project Structure

```text
Task-4-Rule-Based-Chatbot/
├── chatbot.py
├── sample_faq.json
└── README.md
```

## How to Run

1. Install Python 3.

2. Open a terminal in the project folder.

3. Run:

   `python chatbot.py`

4. Enter a question when prompted.

5. Type `bye`, `exit`, or `quit` to stop the chatbot.

## Example Questions

* Hello
* What are your hours of operation?
* How do I submit my internship project?
* When will I receive my certificate?

## Expected Behavior

The chatbot responds to recognized greetings and FAQs, combines multiple matching responses where applicable, and displays a fallback message for unknown questions.
