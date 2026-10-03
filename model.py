"""
RAG Pipeline

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - load_text_file
def load_text_file(path):
    # TODO: read a UTF-8 text file at `path` and return its contents as one string.
    with open(path) as f:
        return f.read()

# Step 2 - load_text_directory
def load_text_directory(directory):
    # TODO: read every .txt file in `directory` and return their contents as a list of strings
    
    return [load_text_file(f"{directory}/{f}") for f in sorted(os.listdir(directory)) if f[-4:] == ".txt"]

