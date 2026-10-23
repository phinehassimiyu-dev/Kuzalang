import re

class KuzalangInterpreter:
    def __init__(self):
        # A dictionary to store your language's variables (state memory)
        self.variables = {}

    def execute_line(self, line: str):
        # Clean up whitespace and ignore empty lines or comments
        line = line.strip()
        if not line or line.startswith("//"):
            return

        # 1. Handle "let <var> = <value>" (Variable Declaration)
        let_match = re.match(r"^let\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.+)$", line)
        if let_match:
            var_name, var_value_raw = let_match.groups()
            self.variables[var_name] = self.evaluate_expression(var_value_raw)
            return

        # 2. Handle "Show <expression>" (Output Command)
        show_match = re.match(r"^Show\s+(.+)$", line)
        if show_match:
            expr_raw = show_match.group(1)
            value = self.evaluate_expression(expr_raw)
            print(value)
            return

        # 3. Handle "<var> = <value>" (Variable Reassignment)
        reassign_match = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.+)$", line)
        if reassign_match:
            var_name, var_value_raw = reassign_match.groups()
            if var_name in self.variables:
                self.variables[var_name] = self.evaluate_expression(var_value_raw)
            else:
                print(f"Error: Variable '{var_name}' must be declared with 'let' first.")
            return

        print(f"Syntax Error: Invalid Kuzalang instruction -> '{line}'")

    def evaluate_expression(self, expr: str):
        expr = expr.strip()

        # Handle String Literals wrapped in quotes (e.g., "phenshas")
        if (expr.startswith('"') and expr.endswith('"')) or (expr.startswith("'") and expr.endswith("'")):
            return expr[1:-1]

        # Handle Integer Literals (e.g., 19 or 10)
        if expr.isdigit():
            return int(expr)

        # Handle Variable Lookups (e.g., Show name)
        if expr in self.variables:
            return self.variables[expr]

        # Default fall-through fallback
        return expr

    def run(self, code_source: str):
        # Run code block line by line
        for line in code_source.splitlines():
            self.execute_line(line)

# TEST DRIVE: Running a Kuzalang program!

if __name__ == "__main__":
    # This matches the exact test logic written in your notebook pages!
    kuzalang_code = """
    let name = "phenshas"
    let age = 19
    Show name
    Show age

    let score = 10
    Show score
    score = 20
    Show score
    """

    print("Executing Kuzalang Program ")
    interpreter = KuzalangInterpreter()
    interpreter.run(kuzalang_code)
    print(" ")
