import tkinter as tk
from tkinter import messagebox, filedialog
from java_babilon_parserListener import java_babilon_parserListener
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Tree import TerminalNodeImpl
from java_babilon_lexer import java_babilon_lexer  # Import lexer
from java_babilon_parser import java_babilon_parser  # Import parser
import subprocess


class CustomErrorListener(ErrorListener):
    def __init__(self, error_text_widget):
        super(CustomErrorListener, self).__init__()
        self.error_text_widget = error_text_widget

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"line {line}:{column} {msg}\n"
        self.error_text_widget.insert(tk.END, error_message)


class TextWithLineNumbers(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.text = tk.Text(self, **kwargs)
        self.line_numbers = tk.Text(self, width=4, padx=4, takefocus=0, border=0, background='lightgrey',
                                    state='disabled')

        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.on_scrollbar)
        self.text.configure(yscrollcommand=self.on_textscroll)

        self.line_numbers.pack(side="left", fill="y")
        self.scrollbar.pack(side="right", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<KeyRelease>", self.update_line_numbers)
        self.text.bind("<MouseWheel>", self.update_line_numbers)
        self.text.bind("<Button-1>", self.update_line_numbers)
        self.text.bind("<Return>", self.update_line_numbers)
        self.text.bind("<BackSpace>", self.update_line_numbers)
        self.update_line_numbers()

    def on_scrollbar(self, *args):
        self.text.yview(*args)
        self.line_numbers.yview(*args)
        self.update_line_numbers()

    def on_textscroll(self, *args):
        self.scrollbar.set(*args)
        self.line_numbers.yview_moveto(args[0])

    def update_line_numbers(self, event=None):
        self.line_numbers.config(state='normal')
        self.line_numbers.delete('1.0', tk.END)
        i = self.text.index("@0,0")
        while True:
            dline = self.text.dlineinfo(i)
            if dline is None:
                break
            linenum = str(i).split(".")[0]
            self.line_numbers.insert(tk.END, linenum + "\n")
            i = self.text.index("%s+1line" % i)
        self.line_numbers.config(state='disabled')

    def get(self, *args):
        return self.text.get(*args)

    def delete(self, *args):
        return self.text.delete(*args)

    def insert(self, *args):
        return self.text.insert(*args)


class JavaToPythonConverter:
    def __init__(self, master):
        self.master = master
        master.title("Java to Python Converter")
        master.configure(bg="#ADD8E6")  # Set background color of the main window

        self.java_code_label = tk.Label(master, text="Java Code:", bg="#ADD8E6")  # Set background color of the label
        self.java_code_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.java_code_text = TextWithLineNumbers(master, height=15, width=50)
        self.java_code_text.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        self.python_code_label = tk.Label(master, text="Python Code:", bg="#ADD8E6")  # Set background color of the label
        self.python_code_label.grid(row=0, column=1, sticky="w", padx=10, pady=5)

        self.python_code_text = TextWithLineNumbers(master, height=15, width=50)
        self.python_code_text.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

        self.error_label = tk.Label(master, text="Error:", bg="#ADD8E6")  # Set background color of the label
        self.error_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        self.error_text = TextWithLineNumbers(master, height=5, width=100)
        self.error_text.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")

        self.output_label = tk.Label(master, text="Output:", bg="#ADD8E6")  # Set background color of the label
        self.output_label.grid(row=2, column=1, sticky="w", padx=10, pady=5)

        self.output_text = TextWithLineNumbers(master, height=5, width=100)
        self.output_text.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")

        self.button_frame = tk.Frame(master, bg="#ADD8E6")  # Set background color of the frame
        self.button_frame.grid(row=4, column=0, columnspan=2, pady=5)

        self.convert_button = tk.Button(self.button_frame, text="Convert", command=self.convert, width=10)
        self.convert_button.pack(side="left", padx=5)

        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear_text, width=10)
        self.clear_button.pack(side="left", padx=5)

        self.save_button = tk.Button(self.button_frame, text="Save Python Code", command=self.save_python_code, width=15)
        self.save_button.pack(side="left", padx=5)

        self.compile_button = tk.Button(self.button_frame, text="Compile and Run", command=self.compile_and_run, width=15)
        self.compile_button.pack(side="left", padx=5)

    def convert(self):
        java_code = self.java_code_text.get("1.0", tk.END)
        listener = java_babilon_parserListener()
        stream = InputStream(java_code)
        lexer = java_babilon_lexer(stream)  # Tworzenie instancji lekserskiej
        token_stream = CommonTokenStream(lexer)
        parser = java_babilon_parser(token_stream)

        # Clear previous error messages
        self.error_text.delete("1.0", tk.END)

        # Set up custom error listener
        lexer.removeErrorListeners()
        lexer.addErrorListener(CustomErrorListener(self.error_text))
        parser.removeErrorListeners()
        parser.addErrorListener(CustomErrorListener(self.error_text))

        try:
            tree = parser.program()
            walker = ParseTreeWalker()
            walker.walk(listener, tree)
            self.python_code_text.delete("1.0", tk.END)
            self.python_code_text.insert("1.0", listener.python_code)
        except Exception as e:
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


