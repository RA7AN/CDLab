class CodeOptimizer:
    def __init__(self, code):
        self.code = code

    def constant_folding(self):
        optimized_code = []
        
        for op, arg1, arg2, result in self.code:
            try:
                arg1_val = int(arg1)
                arg2_val = int(arg2)
                if op == '+':
                    result_val = arg1_val + arg2_val
                elif op == '-':
                    result_val = arg1_val - arg2_val
                elif op == '*':
                    result_val = arg1_val * arg2_val
                elif op == '/':
                    result_val = arg1_val / arg2_val
                else:
                    result_val = None  # Unsupported operation
                optimized_code.append((None, None, None, result_val))
            except ValueError:
                optimized_code.append((op, arg1, arg2, result))
                
        return optimized_code

    def common_subexpression_elimination(self):
        optimized_code = []
        expressions = {}
        
        for op, arg1, arg2, result in self.code:
            expression = (op, arg1, arg2)
            if expression in expressions:
                result_temp = expressions[expression]
            else:
                result_temp = f"T{len(expressions)}"
                expressions[expression] = result_temp
                optimized_code.append((op, arg1, arg2, result_temp))
                
        return optimized_code

# Example usage
if __name__ == "__main__":
    # Unoptimized target code: (op, arg1, arg2, result)
    target_code = [
        ('+', '10', '20', 'T1'),
        ('-', 'T1', '5', 'T2'),
        ('*', 'T2', '2', 'T3'),
        ('+', 'T3', '30', 'T4')
    ]
    
    print("Unoptimized code:")
    for op, arg1, arg2, result in target_code:
        print(f"{result} = {arg1} {op} {arg2}")

    optimizer = CodeOptimizer(target_code)
    
    # Optimized version using constant folding
    optimized_cf = optimizer.constant_folding()
    print("\nOptimized version using constant folding:")
    for op, arg1, arg2, result in optimized_cf:
        if result is not None:
            print(f"{result} = Constant")
        else:
            print(f"{arg1} {op} {arg2} = {result}")
            
    # Optimized version using common subexpression elimination
    optimized_cse = optimizer.common_subexpression_elimination()
    print("\nOptimized version using common subexpression elimination:")
    for op, arg1, arg2, result in optimized_cse:
        print(f"{result} = {arg1} {op} {arg2}")
