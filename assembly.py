def generate_assembly_code(operation, operand1, operand2, result):
    assembly_code = ""
    

    assembly_code += ".text\n"
    assembly_code += ".globl _start\n"
    assembly_code += "_start:\n"
    

    if operation == "add":
        assembly_code += f"    mov ${operand1}, %eax\n"
        assembly_code += f"    add ${operand2}, %eax\n"
        assembly_code += f"    mov %eax, ${result}\n"
    

    assembly_code += "    mov $1, %eax\n"
    assembly_code += "    mov $0, %ebx\n"
    assembly_code += "    int $0x80\n"
    
    return assembly_code

operation = "add"
operand1 = "10"
operand2 = "20"
result = "sum"

assembly_code = generate_assembly_code(operation, operand1, operand2, result)
print(assembly_code)