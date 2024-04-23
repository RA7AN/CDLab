def find_first(grammar):
    first = {}

    # Helper function to recursively find first set for a symbol
    def find_first_set(symbol):
        if symbol in first:
            return first[symbol]
        
        first_set = set()

        # If symbol is a terminal, its first set is itself
        if symbol not in grammar:
            first_set.add(symbol)
        else:
            # For each production of the symbol
            for production in grammar[symbol]:
                # If the production starts with a terminal, add it to the first set
                if production[0] not in grammar:
                    first_set.add(production[0])
                # If the production starts with a non-terminal
                else:
                    # Find the first set of that non-terminal
                    first_of_production = find_first_set(production[0])
                    # Add all symbols from the first set, except epsilon
                    first_set.update(first_of_production - {'epsilon'})
                    # If epsilon is in the first set of the non-terminal, consider the next symbol in the production
                    if 'epsilon' in first_of_production:
                        first_set.update(find_first_set(symbol) - {'epsilon'})

        first[symbol] = first_set
        return first_set

    # Iterate through each symbol in the grammar
    for symbol in grammar:
        find_first_set(symbol)

    return first

def main():
    grammar = {}
    print("Enter the grammar (one production per line, use '->' as separator, epsilon should be written as 'epsilon', e.g., S -> aS | b):")
    while True:
        production = input().strip()
        if not production:
            break
        symbol, production_rules = production.split(" -> ")
        production_rules = production_rules.split(" | ")
        grammar[symbol] = [rule.split() for rule in production_rules]

    first = find_first(grammar)

    print("\nFirst sets:")
    for symbol, first_set in first.items():
        print(f"First({symbol}): {first_set}")

if __name__ == "__main__":
    main()
