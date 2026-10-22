# ParseViz: Parser Stack Operation and Parse Tree Visualizer

## Project Overview
ParseViz is a Python-based Compiler Design project that visualizes the parsing process of arithmetic expressions. It displays token sequences, parser stack operations, postfix expressions, and parse trees.

## Objectives
- Understand how arithmetic expressions are processed.
- Visualize operator-stack operations.
- Generate a parse tree from an expression.
- Evaluate valid numeric expressions.
- Demonstrate compiler design concepts through an interactive interface.

## Technologies Used
- Python
- Streamlit
- HTML and CSS
- Unit testing with Python's unittest module

## Features
- Interactive web interface
- Tokenization of arithmetic expressions
- Parser stack operation visualization
- Postfix expression generation
- Parse tree visualization
- Numeric expression evaluation
- Unit tests for important functions

## Supported Operators
Addition (+), subtraction (-), multiplication (*), and division (/), with parentheses for grouping.

## How to Run
1. Install Python.
2. Open a terminal in the project folder.
3. Install dependencies:

   `python -m pip install -r requirements.txt`

4. Start the application:

   `python -m streamlit run app.py`

5. Open the local URL shown in the terminal.

## Run Tests
Execute:

`python -m unittest test_parseviz.py`

## Project Files
- `app.py` — Main application
- `requirements.txt` — Required Python packages
- `test_parseviz.py` — Automated tests
- `README.md` — Project documentation

## Conclusion
ParseViz provides an interactive way to understand expression parsing, stack operations, postfix conversion, and parse-tree construction as part of Compiler Design.
