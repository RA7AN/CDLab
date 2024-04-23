def compute_follow(grammar):
    follow = {}

    # Initialize follow sets for all non-terminals to empty sets
    for non_terminal in grammar.keys():
        follow[non_terminal] = set()

    # Adding $ (end of input marker) to the follow set of the start symbol
    start_symbol = list(grammar.keys())[0]
    follow[start_symbol].add('$')

    # Iteratively update follow sets until no more changes occur
    while True:
        updated = False

        for non_terminal, productions in grammar.items():
            for production in productions:
                for i in range(len(production)):
                    symbol = production[i]

                    # If the symbol is a non-terminal, update its follow set
                    if symbol in grammar:
                        if i == len(production) - 1:
                            # If the symbol is the last in the production, add follow of LHS
                            if follow[non_terminal] != follow[non_terminal].union(follow[symbol]):
                                prev_follow = follow[non_terminal].copy()
                                follow[non_terminal] |= follow[symbol]
                                if prev_follow != follow[non_terminal]:
                                    updated = True
                        else:
                            next_symbol = production[i + 1]

                            # If next symbol is terminal, add it to follow set
                            if next_symbol not in grammar:
                                if next_symbol not in follow[symbol]:
                                    prev_follow = follow[symbol].copy()
                                    follow[symbol].add(next_symbol)
                                    if prev_follow != follow[symbol]:
                                        updated = True
                            else:
                                # If next symbol is non-terminal, add first set of next symbol
                                first_next = set(grammar[next_symbol])
                                first_next.discard('epsilon')
                                if follow[symbol] != follow[symbol].union(first_next):
                                    prev_follow = follow[symbol].copy()
                                    follow[symbol] |= first_next
                                    if prev_follow != follow[symbol]:
                                        updated = True
                                if 'epsilon' in grammar[next_symbol]:
                                    if i + 1 == len(production) - 1:
                                        if follow[non_terminal] != follow[non_terminal].union(follow[symbol]):
                                            prev_follow = follow[non_terminal].copy()
                                            follow[non_terminal] |= follow[symbol]
                                            if prev_follow != follow[non_terminal]:
                                                updated = True
                                    else:
                                        next_next_symbol = production[i + 2]
                                        if next_next_symbol not in grammar:
                                            if follow[non_terminal] != follow[non_terminal].union(follow[symbol]):
                                                prev_follow = follow[non_terminal].copy()
                                                follow[non_terminal] |= follow[symbol]
                                                if prev_follow != follow[non_terminal]:
                                                    updated = True

        if not updated:
            break

    return follow

def main():
    grammar = {}
    print("Enter the grammar (one production per line, use '->' as separator, epsilon should be written as 'epsilon', e.g., S -> aA | bB):")
    while True:
        production = input().strip()
        if not production:
            break
        left_prod, right_prod = production.split(" -> ")
        right_prod = [prod.split() for prod in right_prod.split(" | ")]
        grammar[left_prod] = right_prod

    follow_result = compute_follow(grammar)

    print("\nFollow sets:")
    for non_terminal, follow_set in follow_result.items():
        print(f"Follow({non_terminal}): {follow_set}")

if __name__ == "__main__":
    main()
