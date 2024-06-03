import tkinter as tk
from tkinter import messagebox, filedialog
from java_babilon_parserListener import java_babilon_parserListener
from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from java_babilon_lexer import java_babilon_lexer  # Import lexer
from java_babilon_parser import java_babilon_parser  # Import parser
import subprocess

class JavaToPythonConverter:
    def __init__(self, master):
        self.master = master
        master.title("Java to Python Converter")

        self.java_code_label = tk.Label(master, text="Java Code:")
        self.java_code_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.java_code_text = tk.Text(master, height=20, width=60)
        self.java_code_text.grid(row=1, column=0, padx=10, pady=5)

        self.python_code_label = tk.Label(master, text="Python Code:")
        self.python_code_label.grid(row=0, column=1, sticky="w", padx=10, pady=5)

        self.python_code_text = tk.Text(master, height=20, width=60)
        self.python_code_text.grid(row=1, column=1, padx=10, pady=5)

        self.error_label = tk.Label(master, text="Error:")
        self.error_label.grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        self.error_text = tk.Text(master, height=10, width=130)
        self.error_text.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.output_label = tk.Label(master, text="Output:")
        self.output_label.grid(row=4, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        self.output_text = tk.Text(master, height=10, width=130)
        self.output_text.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.grid(row=6, column=0, pady=5)

        self.clear_button = tk.Button(master, text="Clear", command=self.clear_text)
        self.clear_button.grid(row=6, column=1, pady=5)

        self.save_button = tk.Button(master, text="Save Python Code", command=self.save_python_code)
        self.save_button.grid(row=6, column=2, pady=5)

        self.compile_button = tk.Button(master, text="Compile and Run", command=self.compile_and_run)
        self.compile_button.grid(row=6, column=3, pady=5)

    def convert(self):
        java_code = self.java_code_text.get("1.0", tk.END)
        listener = java_babilon_parserListener()
        stream = InputStream(java_code)
        lexer = java_babilon_lexer(stream)  # Tworzenie instancji lekserskiej
        token_stream = CommonTokenStream(lexer)
        parser = java_babilon_parser(token_stream)

        try:
            tree = parser.program()
            walker = ParseTreeWalker()
            walker.walk(listener, tree)
            self.python_code_text.delete("1.0", tk.END)
            self.python_code_text.insert("1.0", listener.python_code)
            self.error_text.delete("1.0", tk.END)  # W przypadku sukcesu czyścimy ewentualne poprzednie błędy
        except Exception as e:
            self.error_text.delete("1.0", tk.END)
            self.error_text.insert("1.0", str(e))

    def clear_text(self):
        self.java_code_text.delete("1.0", tk.END)
        self.python_code_text.delete("1.0", tk.END)
        self.error_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)

    def save_python_code(self):
        python_code = self.python_code_text.get("1.0", tk.END)
        if python_code.strip():
            file_path = filedialog.asksaveasfilename(defaultextension=".py",
                                                     filetypes=[("Python files", "*.py"), ("All files", "*.*")])
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(python_code)
        else:
            messagebox.showwarning("Warning", "No Python code to save!")

    def compile_and_run(self):
        python_code = self.python_code_text.get("1.0", tk.END)
        if python_code.strip():
            with open("temp.py", "w") as file:
                file.write(python_code)
            try:
                result = subprocess.run(["python", "temp.py"], capture_output=True, text=True)
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert("1.0", result.stdout + result.stderr)
            except Exception as e:
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert("1.0", str(e))
        else:
            messagebox.showwarning("Warning", "No Python code to compile and run!")

def main():
    root = tk.Tk()
    app = JavaToPythonConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
