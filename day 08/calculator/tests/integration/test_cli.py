import subprocess
import sys
import pytest

# Assuming cli.py is in src/
CLI_PATH = [sys.executable, "src/cli.py"]

def test_cli_basic_addition():
    result = subprocess.run(CLI_PATH + ["2+2"], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout.strip() == "4.0"

def test_cli_basic_subtraction():
    result = subprocess.run(CLI_PATH + ["10-5"], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout.strip() == "5.0"

def test_cli_basic_multiplication():
    result = subprocess.run(CLI_PATH + ["3*4"], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout.strip() == "12.0"

def test_cli_basic_division():
    result = subprocess.run(CLI_PATH + ["10/2"], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout.strip() == "5.0"

def test_cli_order_of_operations():
    result = subprocess.run(CLI_PATH + ["2+3*4"], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout.strip() == "14.0"

def test_cli_with_parentheses():
    result = subprocess.run(CLI_PATH + ["(2+3)*4"], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout.strip() == "20.0"

def test_cli_division_by_zero():
    result = subprocess.run(CLI_PATH + ["10/0"], capture_output=True, text=True)
    assert result.returncode == 1 # Expect non-zero for error
    assert "Error: Division by zero" in result.stderr.strip()

def test_cli_invalid_expression():
    result = subprocess.run(CLI_PATH + ["2++3"], capture_output=True, text=True)
    assert result.returncode == 1 # Expect non-zero for error
    assert "Error: Invalid expression" in result.stderr.strip() or "Error: Invalid character" in result.stderr.strip()

def test_cli_empty_input():
    result = subprocess.run(CLI_PATH + [""], capture_output=True, text=True)
    assert result.returncode == 1
    assert "Error: No expression provided" in result.stderr.strip()
