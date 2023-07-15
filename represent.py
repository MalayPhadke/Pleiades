import ast

def print_ast_tree(node, level=0):
    indent = "    " * level
    node_type = node.__class__.__name__
    print(f"{indent}{node_type}")

    for child_node in ast.iter_child_nodes(node):
        print_ast_tree(child_node, level + 1)

if __name__ == "__main__":
    with open("main.py", "r") as f:
        python_code = f.read()

    tree = ast.parse(python_code)
    print_ast_tree(tree)
