#!/usr/bin/python3

import tkinter as tk
from tkinter import filedialog
import analyze_results


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GPM Fungicide Assay Results Analyzer")
        self.filepaths = []

        # Set window size to 50% of screen size
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = int(screen_width / 2)
        window_height = int(screen_height / 2)
        self.geometry(f"{window_width}x{window_height}")

        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menu_bar = tk.Menu(self)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_files)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu_bar)

    def create_widgets(self):
        file_label = tk.Label(self, text="No files currently open.")
        file_label.pack(pady=10)

        run_button = tk.Button(self, text="Run", command=self.run_analysis)
        run_button.pack(pady=10)

        self.file_label = file_label

    def open_files(self):
        self.filepaths = filedialog.askopenfilenames(
            title="Open CSV", filetypes=[("CSV files", "*.csv")]
        )
        if self.filepaths:
            self.file_label.configure(text="\n".join(self.filepaths))
        else:
            self.file_label.configure(text="No files currently open.")

    def run_analysis(self):
        if self.filepaths:
            hr0_filepaths = [fp for fp in self.filepaths if "0hr" in fp]
            if hr0_filepaths:
                for filepath in hr0_filepaths:
                    analyze_results.main(filepath)
                print("Analysis complete.")
            else:
                print("No CSV files with '0hr' in their name found.")
        else:
            print("Please open at least one CSV file first.")


if __name__ == "__main__":
    app = App()
    app.mainloop()
