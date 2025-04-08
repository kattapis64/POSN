def generate_nested_function(n):
    func_lines = []
    indent = ""

    # Start building nested defs
    for i in range(1, n + 1):
        arg = f"x{i}"
        func_name = f"f{i}"
        func_lines.append(f"{indent}def {func_name}({arg}):")
        indent += "    "

    # Inside innermost function: return all variables combined
    args = [f"x{i}" for i in range(1, n + 1)]
    return_line = f'{indent}return ' + ' + " - " + '.join(args)
    func_lines.append(return_line)

    # Now build return chaining (like: return f3("z"))
    for i in range(n, 0, -1):
        indent = "    " * (i - 1)
        args_chain = '"' + chr(96 + i) + '"'  # just example letters: "a", "b", "c", ...
        func_lines.append(f"{indent}return f{i}({args_chain})")

    # Wrap in outer function
    full_code = ["def outer():"] + ["    " + line for line in func_lines]
    full_code.append("result = outer()")
    full_code.append("print(result)")

    # Combine and run
    code_str = "\n".join(full_code)
    exec(code_str, globals())

# Try it
generate_nested_function(3)
#hello