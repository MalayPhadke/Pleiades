#parse and generate source code AST
#Transform AST to target language AST
#Generate target language source code

import ast
from typing import Any

class PythonToCVisitor(ast.NodeVisitor):
    def __init__(self):
        self.c_code = "#include <PlutoPilot.h>\n"
        self.is_inside_function = False
        self.first_visit = True

    def generic_visit(self, node):
        # For unknown node types, just visit its children
        for child_node in ast.iter_child_nodes(node):
            # if hasattr(node.value, "value"):
            # print(node.value.value.id)
            self.visit(child_node)

    def visit_Module(self, node):
        # For the top-level module, visit its body nodes
        for body_node in node.body:
            self.visit(body_node)

    def visit_FunctionDef(self, node):
        # For function definitions, generate C code for functions
        function_name = node.name
        arguments = ', '.join(arg.arg for arg in node.args.args)
        return_type = "void"  # Assuming all Python functions return void in C
        # self.is_inside_function = True
        # Generate the function signature and visit its body
        self.c_code += f"{return_type} {function_name}({arguments}) {{\n"
        for stmt in node.body:
            self.visit(stmt)
        self.c_code += "}\n\n"

        # self.is_inside_function = False

    def visit_Return(self, node):
        # For return statements, generate C return statement
        if node.value:
            self.c_code += f"return {self.visit(node.value)};\n"
        else:
            self.c_code += "return;\n"

    def visit_BinOp(self, node):
        # For binary operations, generate C equivalent
        left = self.visit(node.left)
        op = self.visit(node.op)
        right = self.visit(node.right)
        return f"({left} {op} {right})"

    def visit_Add(self, node):
        return "+"

    def visit_Sub(self, node):
        return "-"
    
    # Add similar methods for other binary operators if needed
    def visit_Mult(self, node):
        return "*"
    
    def visit_Div(self, node):
        return "/"
    
    def visit_FloorDiv(self, node):
        return "//"
    
    def visit_Mod(self, node):
        return "%"
    
    def visit_Pow(self, node):
        return "**"
    
    def visit_Call(self, node):
            # For function calls, generate the C equivalent
            func_name = self.visit(node.func)
            args = ', '.join(self.visit(arg) for arg in node.args)
            if func_name == "print":
                args = ', '.join(self.visit(arg) for arg in node.args)
                self.c_code += f"Monitor.print({args});\n"
                return
            if not self.is_inside_function:
                self.c_code += f"{func_name}({args});\n" 
            else:
                return f"{func_name}({args})"

    
    def visit_Assign(self, node):
        variable = node.targets[0].id
        self.is_inside_function = True
        val = self.visit(node.value)
        # print(variable, val)
        self.c_code += f"{variable} = {val};\n"
        self.is_inside_function = False

    def visit_Constant(self, node):
        # For constants, generate C code based on their Python type
        if isinstance(node.value, int):
            return str(node.value)
        elif isinstance(node.value, float):
            return str(node.value)
        elif isinstance(node.value, str):
            return f'"{node.value}"'
        elif isinstance(node.value, bool):
            return "true" if node.value else "false"
        elif node.value is None:
            return "NULL"
        else:
            raise ValueError(f"Unsupported constant type: {type(node.value)}")

    def visit_Import(self, node):
        for module in list(node.names):
            self.c_code += f"#include<{module.name}.h>\n"
    
    def visit_ImportFrom(self, node):
        self.c_code += f"#include<{node.module}.h>\n"
        # print(node._fields)

    def visit_Name(self, node):
        # For variable names, just return the name
        return node.id

    def visit_ClassDef(self, node):
        print(node._fields)

    def visit_Attribute(self, node):
        return f"{self.visit(node.value)}.{node.attr}"
    
    def visit_BoolOp(self, node):
        op = self.visit(node.op)
        return f" {op} ".join(self.visit(value) for value in node.values)
    def visit_And(self, node):
        return "&&"
    def visit_Or(self, node):
        return "||"
    def visit_Compare(self, node):
        left = self.visit(node.left)
        ops = [self.visit(op) for op in node.ops]
        comparators = [self.visit(cmp) for cmp in node.comparators]
        return f"{left} {' '.join(f'{op} {cmp}' for op, cmp in zip(ops, comparators))}"

    def visit_Lt(self, node):
        return "<"

    def visit_LtE(self, node):
        return "<="

    def visit_Gt(self, node):
        return ">"

    def visit_GtE(self, node):
        return ">="

    def visit_Eq(self, node):
        return "=="

    def visit_NotEq(self, node):
        return "!="
    

    def visit_If(self, node):
        if self.first_visit:
            self.c_code += f"if ({self.visit(node.test)}) {{\n"

            for stmt in node.body:
                self.visit(stmt)

            self.c_code += "}\n"
            self.first_visit = False
        else:
            self.c_code += f"else if ({self.visit(node.test)}) {{\n"

            for stmt in node.body:
                self.visit(stmt)

            self.c_code += "}\n"
        if node.orelse:
            if isinstance(node.orelse[0], ast.If):
                self.visit_If(node.orelse[0])
            else:
                self.c_code += "else {\n"
                for stmt in node.orelse:  # Visit statements inside the else block
                    self.visit(stmt)
                self.c_code += "}\n"    # Add other visit methods for different types of nodes as 
