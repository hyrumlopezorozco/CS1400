import ast
import os


def _read_student_code():
    candidates = ["2area.py", "area.py", "main.py"]
    for filename in candidates:
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                return f.read()

    with open("2area.py", "r", encoding="utf-8") as f:
        return f.read()


def test_area_script():
    student_code = _read_student_code()
    tree = ast.parse(student_code)

    # 1. Check for 'import math' or 'from math import ...'
    has_math_import = any(
        (
            isinstance(node, ast.Import)
            and any(alias.name == "math" for alias in node.names)
        )
        or (
            isinstance(node, ast.ImportFrom)
            and node.module == "math"
        )
        for node in ast.walk(tree)
    )
    assert has_math_import, "Falta importar la biblioteca 'math'."

    # 2. Check for variable 'radio_circulo'
    has_radio_variable = any(
        (
            isinstance(node, ast.Assign)
            and any(
                isinstance(t, ast.Name) and t.id == "radio_circulo"
                for t in node.targets
            )
        )
        or (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == "radio_circulo"
        )
        for node in ast.walk(tree)
    )
    assert has_radio_variable, "Debes definir la variable 'radio_circulo'."

    # 3. Check math.pi usage
    uses_math_pi = any(
        isinstance(node, ast.Attribute)
        and isinstance(node.value, ast.Name)
        and node.value.id == "math"
        and node.attr == "pi"
        for node in ast.walk(tree)
    )
    assert uses_math_pi, "Debes utilizar 'math.pi' para realizar el cálculo."

    # 4. Check print() function call
    has_print = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "print"
        for node in ast.walk(tree)
    )
    assert has_print, "Debes utilizar la función 'print()' para mostrar el resultado."