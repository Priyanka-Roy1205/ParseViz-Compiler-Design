import re
import html
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ParseViz",
    page_icon="🌳",
    layout="wide"
)


def tokenize(expr):
    expr = re.sub(r"\s+", "", expr)
    pattern = r"\d+(?:\.\d+)?|[A-Za-z_]\w*|[()+\-*/]"
    tokens = re.findall(pattern, expr)

    if not expr or "".join(tokens) != expr:
        raise ValueError("Enter a valid arithmetic expression.")

    return tokens


def evaluate_postfix(postfix):
    stack = []

    for token in postfix:
        if re.fullmatch(r"\d+(?:\.\d+)?", token):
            stack.append(float(token))

        elif token in ["+", "-", "*", "/"]:
            if len(stack) < 2:
                raise ValueError("Invalid expression.")

            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b == 0:
                    raise ValueError("Division by zero.")
                stack.append(a / b)

        else:
            raise ValueError(
                "Evaluation is available for numeric expressions only."
            )

    if len(stack) != 1:
        raise ValueError("Invalid expression.")

    return stack[0]


def build_visualization(tokens):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    operators = []
    output = []
    steps = []
    expect_operand = True

    def record(token, action):
        steps.append({
            "Input Token": token,
            "Operator Stack": " ".join(operators) or "∅",
            "Postfix Output": " ".join(output) or "∅",
            "Action": action
        })

    for token in tokens:
        is_operand = re.fullmatch(
            r"\d+(?:\.\d+)?|[A-Za-z_]\w*",
            token
        )

        if is_operand:
            if not expect_operand:
                raise ValueError("Missing operator between operands.")

            output.append(token)
            record(token, f"Add operand '{token}' to output")
            expect_operand = False

        elif token == "(":
            if not expect_operand:
                raise ValueError("Missing operator before '('.")

            operators.append(token)
            record(token, "Push '(' onto stack")
            expect_operand = True

        elif token == ")":
            if expect_operand:
                raise ValueError(
                    "Unexpected ')' or empty parentheses."
                )

            while operators and operators[-1] != "(":
                op = operators.pop()
                output.append(op)
                record(token, f"Pop '{op}' to output")

            if not operators:
                raise ValueError("Mismatched parentheses.")

            operators.pop()
            record(token, "Remove matching '('")
            expect_operand = False

        elif token in precedence:
            if expect_operand:
                raise ValueError(f"Unexpected operator '{token}'.")

            while (
                operators
                and operators[-1] in precedence
                and precedence[operators[-1]] >= precedence[token]
            ):
                op = operators.pop()
                output.append(op)
                record(token, f"Pop '{op}' due to precedence")

            operators.append(token)
            record(token, f"Push operator '{token}'")
            expect_operand = True

    if expect_operand:
        raise ValueError("Expression cannot end with an operator.")

    while operators:
        op = operators.pop()

        if op == "(":
            raise ValueError("Mismatched parentheses.")

        output.append(op)
        record("END", f"Pop remaining operator '{op}'")

    nodes = []

    for token in output:
        if token in precedence:
            if len(nodes) < 2:
                raise ValueError("Invalid arithmetic expression.")

            right = nodes.pop()
            left = nodes.pop()

            nodes.append({
                "value": token,
                "children": [left, right]
            })
        else:
            nodes.append({
                "value": token,
                "children": []
            })

    if len(nodes) != 1:
        raise ValueError("Invalid arithmetic expression.")

    return steps, output, nodes[0]


def render_tree(node):
    label = html.escape(node["value"])
    children = node["children"]

    if not children:
        return f'<div class="branch"><div class="node leaf">{label}</div></div>'

    child_html = "".join(render_tree(child) for child in children)

    return f"""
    <div class="branch">
        <div class="node">{label}</div>
        <div class="children">{child_html}</div>
    </div>
    """


# Streamlit user interface

st.title("🌳 ParseViz")
st.subheader("Parser Stack Operation and Parse Tree Visualizer")
st.write("Compiler Design Project-Based Learning")

st.markdown("""
### Grammar

- E → E + T | E - T | T
- T → T * F | T / F | F
- F → (E) | id

Multiplication and division have higher precedence than
addition and subtraction. Parentheses can override precedence.
""")

expression = st.text_input(
    "Enter an arithmetic expression",
    value="a+b*c",
    placeholder="Example: (a+b)*c"
)

if st.button("Visualize Expression", type="primary"):
    try:
        tokens = tokenize(expression)
        steps, postfix, tree = build_visualization(tokens)

        st.success("Expression parsed successfully!")

        try:
            result = evaluate_postfix(postfix)
            st.metric("Evaluation Result", f"{result:g}")
        except ValueError:
            st.info(
                "Evaluation is available for numeric expressions only."
            )

        st.header("1. Token Sequence")
        st.code(" → ".join(tokens))

        st.header("2. Parser Stack Operations")
        st.caption(
            "Operator-stack parsing using the shunting-yard algorithm."
        )
        st.dataframe(
            steps,
            use_container_width=True,
            hide_index=True
        )

        st.header("3. Postfix Expression")
        st.code(" ".join(postfix))

        st.header("4. Parse Tree")

        tree_html = render_tree(tree)

        components.html(
            f"""
            <!DOCTYPE html>
            <html>
            <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    background: white;
                    color: #222;
                }}

                .tree {{
                    display: flex;
                    justify-content: center;
                    padding: 30px 10px;
                    overflow: auto;
                }}

                .branch {{
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }}

                .node {{
                    border: 2px solid #5276A7;
                    border-radius: 8px;
                    padding: 10px 16px;
                    background: #EAF2FF;
                    font-weight: bold;
                    text-align: center;
                }}

                .leaf {{
                    background: #E4F5E9;
                    border-color: #43875A;
                }}

                .children {{
                    display: flex;
                    justify-content: center;
                    gap: 24px;
                    padding-top: 28px;
                    position: relative;
                }}

                .children:before {{
                    content: "";
                    position: absolute;
                    top: 0;
                    left: 25%;
                    right: 25%;
                    border-top: 2px solid #888;
                }}

                .children > .branch:before {{
                    content: "";
                    height: 14px;
                    border-left: 2px solid #888;
                    margin-top: -28px;
                    margin-bottom: 14px;
                }}
            </style>
            </head>
            <body>
                <div class="tree">{tree_html}</div>
            </body>
            </html>
            """,
            height=380,
            scrolling=True
        )

    except ValueError as error:
        st.error(str(error))

st.divider()
st.caption("ParseViz | Compiler Design PBL")

