class SymbolTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def add_symbol(self, symbol_type, key, value):
        index = self._hash(key)
        if len(self.table[index]) >= self.size:
            print("Cannot add symbol. Bucket is full.")
            return
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, symbol_type, value])

    def get_value(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[2]
        return None

    def remove_symbol(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
        print("Symbol not found")

    def search_symbol(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return True
        return False

    def display_table(self):
        print("Symbol Table:")
        print("{:<15} {:<15} {:<15}".format("Identifier", "Type", "Value"))
        print("-" * 45)
        for bucket in self.table:
            for pair in bucket:
                print("{:<15} {:<15} {:<15}".format(pair[0], pair[1], pair[2]))


# Example usage:
size = int(input("Enter the size of the symbol table: "))
symbol_table = SymbolTable(size)

while True:
    print("\nOptions:")
    print("1. Add Symbol")
    print("2. Remove Symbol")
    print("3. Search Symbol")
    print("4. Display Symbol Table")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        symbol_type = input("Enter symbol type: ")
        key = input("Enter identifier: ")
        value = input("Enter value: ")
        symbol_table.add_symbol(symbol_type, key, value)
    elif choice == "2":
        key = input("Enter identifier to remove: ")
        symbol_table.remove_symbol(key)
    elif choice == "3":
        key = input("Enter identifier to search: ")
        if symbol_table.search_symbol(key):
            print(f"'{key}' is present in the symbol table.")
        else:
            print(f"'{key}' is not present in the symbol table.")
    elif choice == "4":
        symbol_table.display_table()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
