import pytest
from src.calculator.evaluator import evaluate_postfix

def test_evaluate_postfix_basic_operations():
    assert evaluate_postfix(["1", "2", "+"]) == 3
    assert evaluate_postfix(["10", "5", "-"]) == 5
    assert evaluate_postfix(["3", "4", "*"]) == 12
    assert evaluate_postfix(["10", "2", "/"]) == 5

def test_evaluate_postfix_order_of_operations():
    assert evaluate_postfix(["1", "2", "3", "*", "+"]) == 7  # 1 + (2 * 3)
    assert evaluate_postfix(["3", "4", "2", "*", "1", "5", "-", "/", "+"]) == 1.0  # 3 + (4 * 2 / (1 - 5))

def test_evaluate_postfix_with_floats():
    assert evaluate_postfix(["1.5", "2.5", "+"]) == 4.0
    assert evaluate_postfix(["5.0", "2.0", "*", "1.5", "-"]) == 8.5

def test_evaluate_postfix_division_by_zero():
    with pytest.raises(ValueError, match="Division by zero"):
        evaluate_postfix(["10", "0", "/"])

def test_evaluate_postfix_invalid_expression_missing_operand():
    with pytest.raises(ValueError, match="Invalid postfix expression: missing operand"):
        evaluate_postfix(["+", "1", "2"])
    with pytest.raises(ValueError, match="Invalid postfix expression: missing operand"):
        evaluate_postfix(["1", "+"])

def test_evaluate_postfix_invalid_expression_too_many_operands():
    with pytest.raises(ValueError, match="Invalid postfix expression: too many operands"):
        evaluate_postfix(["1", "2", "3", "+"])

def test_evaluate_postfix_empty_expression():
    with pytest.raises(ValueError, match="Invalid postfix expression: cannot evaluate empty expression"):
        evaluate_postfix([])

def test_evaluate_postfix_single_number():
    assert evaluate_postfix(["100"]) == 100
