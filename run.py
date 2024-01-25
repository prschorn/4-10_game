from itertools import permutations, combinations
import warnings

def generate_parentheses_placements(operators):
    indices = list(range(len(operators)))
    parentheses_placements = list(combinations(indices, 2))

    return parentheses_placements

def apply_parentheses(expression, placement):
    return (
        expression[:placement[0]*2 + 1] +
        '(' +
        expression[placement[0]*2 + 1:placement[1]*2 + 1] +
        ')' +
        expression[placement[1]*2 + 1:]
    )

def find_operations_with_parentheses(digits, target):
    digit_permutations = permutations(digits)

    operations = ['+', '-', '*', '/']

    parentheses_placements = generate_parentheses_placements([1,'+',1,'+',1,'+',1])

    for perm in digit_permutations:
        for op1 in operations:
            for op2 in operations:
                for op3 in operations:
                    expression_without_parentheses = f"{perm[0]} {op1} {perm[1]} {op2} {perm[2]} {op3} {perm[3]}"

                    try:
                        result_without_parentheses = eval(expression_without_parentheses)

                        if result_without_parentheses == target:
                            return expression_without_parentheses

                    except:
                        pass

                    for placement in parentheses_placements:
                        expression_with_parentheses = f"{perm[0]} {op1} {perm[1]} {op2} {perm[2]} {op3} {perm[3]}"
                        expression_with_parentheses = apply_parentheses(expression_with_parentheses, placement)

                        try:
                            result_with_parentheses = eval(expression_with_parentheses)

                            if result_with_parentheses == target:
                                return expression_with_parentheses

                        except:
                            pass

    return None

message = input("what are the 4 digits presented on the game screen? Please separate them by space.")

digits = message.split(" ")
target_result = 10
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    solution = find_operations_with_parentheses(digits, target_result)

    if solution:
        print(f"Solution found: {solution}")
    else:
        print("No solution found.")
