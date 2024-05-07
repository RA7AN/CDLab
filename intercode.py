class AddressCodeGenerator:
    def __init__(self):
        self.next_temp = 0
        self.code = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def gen_temp(self):
        temp = f"T{self.next_temp}"
        self.next_temp += 1
        return temp

    def gen_code(self, op, arg1, arg2, result):
        self.code.append((op, arg1, arg2, result))

    def generate_address_code(self, expression):
        tokens = self.tokenize(expression)
        stack = []
        operators = []
        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                stack.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    operator = operators.pop()
                    arg2 = stack.pop()
                    arg1 = stack.pop()
                    result_temp = self.gen_temp()
                    self.gen_code(operator, arg1, arg2, result_temp)
                    stack.append(result_temp)
                operators.pop()  # Discard '('
            elif token in '+-*/':
                while (operators and operators[-1] in '+-*/' and
                        self.precedence[operators[-1]] >= self.precedence[token]):
                    operator = operators.pop()
                    arg2 = stack.pop()
                    arg1 = stack.pop()
                    result_temp = self.gen_temp()
                    self.gen_code(operator, arg1, arg2, result_temp)
                    stack.append(result_temp)
                operators.append(token)
        while operators:
            operator = operators.pop()
            arg2 = stack.pop()
            arg1 = stack.pop()
            result_temp = self.gen_temp()
            self.gen_code(operator, arg1, arg2, result_temp)
            stack.append(result_temp)
        return stack[0]

    def tokenize(self, expression):
        tokens = []
        current_token = ""
        for char in expression:
            if char.isdigit() or char == '.' or (char == '-' and (not current_token or current_token[-1] in '*/(')):
                current_token += char
            else:
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
                if char.strip():
                    tokens.append(char)
        if current_token:
            tokens.append(current_token)
        return tokens

    def print_code(self):
        expressions = []
        for instr in self.code:
            expression = f"{instr[3]} = {instr[1]} {instr[0]} {instr[2]}"
            expressions.append(expression)
        return expressions

# Example usage
if __name__ == "__main__":
    expression = input("Enter arithmetic expression: ")
    generator = AddressCodeGenerator()
    result = generator.generate_address_code(expression)
    expressions = generator.print_code()
    for expr in expressions:
        print(expr)
