import pytest
from src.calculator.parser import tokenize, infix_to_postfix

def test_tokenize_basic_expression():
    assert tokenize("1+2-3") == ["1", "+", "2", "-", "3"]
    assert tokenize("10*20/5") == ["10", "*", "20", "/", "5"]
    assert tokenize(" ( 1 + 2 ) * 3 ") == ["(", "1", "+", "2", ")", "*", "3"]

def test_tokenize_with_floats():
    assert tokenize("1.5+2.5") == ["1.5", "+", "2.5"]

def test_tokenize_invalid_characters():
    with pytest.raises(ValueError, match="Invalid character: @"):
        tokenize("1+2@3")

def test_tokenize_empty_string():
    assert tokenize("") == []

def test_tokenize_whitespace_only():
    assert tokenize("   ") == []

def test_infix_to_postfix_basic_operations():
    assert infix_to_postfix(["1", "+", "2"]) == ["1", "2", "+"]
    assert infix_to_postfix(["1", "+", "2", "*", "3"]) == ["1", "2", "3", "*", "+"]
    assert infix_to_postfix(["1", "*", "2", "+", "3"]) == ["1", "2", "*", "3", "+"]

def test_infix_to_postfix_with_parentheses():
    assert infix_to_postfix(["(", "1", "+", "2", ")", "*", "3"]) == ["1", "2", "+", "3", "*"]
    assert infix_to_postfix(["1", "*", "(", "2", "+", "3", ")"]) == ["1", "2", "3", "+", "*"]

def test_infix_to_postfix_complex_expression():
    assert infix_to_postfix(["3", "+", "4", "*", "2", "/", "(", "1", "-", "5", ")"]) == ["3", "4", "2", "*", "1", "5", "-", "/", "+"]

def test_infix_to_postfix_invalid_expression_missing_operand():
    with pytest.raises(ValueError, match="Invalid expression: missing operand or operator"):
        infix_to_postfix(["1", "+", "*", "2"])

def test_infix_to_postfix_invalid_expression_mismatched_parentheses():
    with pytest.raises(ValueError, match="Mismatched parentheses"):
        infix_to_postfix(["(", "1", "+", "2"])
    with pytest.raises(ValueError, match="Mismatched parentheses"):
        infix_to_postfix(["1", "+", "2", ")"])
