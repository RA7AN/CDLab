import ast

def generate_intermediate_code(input_code):
    # Parse the Python code into an abstract syntax tree (AST)
    parsed_code = ast.parse(input_code)

    # Initialize an empty list to store intermediate code
    intermediate_code = []

    # Traverse the AST nodes and generate intermediate code
    for node in ast.walk(parsed_code):
        if isinstance(node, ast.Expr):
            # Expression statement, generate intermediate code for expression
            intermediate_code.append(f"EVAL   {ast.dump(node.value)}")
        elif isinstance(node, ast.Assign):
            # Assignment statement, generate intermediate code for assignment
            for target in node.targets:
                intermediate_code.append(f"STORE   {ast.dump(target)}  ,  {ast.dump(node.value)}")
        # Add more conditions for other types of statements if needed

    return intermediate_code

# Example usage
python_code = """
y = 2
x = 3+2
print(y)
print(x)
"""
intermediate_code = generate_intermediate_code(python_code)
for code_line in intermediate_code:
    print(code_line)