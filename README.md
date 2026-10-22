# ParseViz: Parser Stack Operation and Parse Tree Visualizer

## Project Overview

ParseViz is an interactive Python application developed as part of a Compiler Design Project-Based Learning (PBL) project. It visualizes parser stack operations, postfix expression conversion, expression evaluation, and parse tree construction.

The application uses Streamlit to provide a simple, interactive web interface for understanding how arithmetic expressions are processed.

## Objectives

- Understand expression parsing and operator precedence.
- Visualize stack operations during expression processing.
- Convert infix expressions into postfix notation.
- Generate a parse tree for an arithmetic expression.
- Evaluate supported arithmetic expressions.

## Features

- Interactive expression input.
- Token sequence visualization.
- Parser stack operation steps.
- Postfix expression generation.
- Parse tree visualization.
- Arithmetic expression evaluation.
- Support for parentheses and operator precedence.

## Technologies Used

- Python
- Streamlit
- Regular Expressions
- Recursive-Descent Parsing
- Stack-Based Expression Processing

## Grammar

The application uses the following expression grammar for constructing parse trees:

```text
E → E + T | E - T | T
T → T * F | T / F | F
F → (E) | id
```

## Installation and Execution

1. Install Python.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Install the required dependency:

```bash
pip install -r requirements.txt
```

5. Start the application:

```bash
python -m streamlit run app.py
```

6. Open the local URL displayed in the terminal.

## Example

Input expression:

```text
2+3*4
```

Expected postfix expression:

```text
2 3 4 * +
```

Expected evaluation result:

```text
14
```

## Testing

Run the automated tests using:

```bash
python -m unittest test_parseviz.py
```

## Project Type

Compiler Design — Project-Based Learning (PBL)

## Author

Priyanka Roy
B.Tech — Computer Science and Engineeringt


