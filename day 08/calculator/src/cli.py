import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator.parser import tokenize, infix_to_postfix
from src.calculator.evaluator import evaluate_postfix

def main():
    if len(sys.argv) < 2:
        print("Error: No expression provided.", file=sys.stderr)
        sys.exit(1)

    expression = sys.argv[1]

    if not expression.strip():
        print("Error: No expression provided.", file=sys.stderr)
        sys.exit(1)

    try:
        tokens = tokenize(expression)
        postfix_tokens = infix_to_postfix(tokens)
        result = evaluate_postfix(postfix_tokens)
        print(result)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
