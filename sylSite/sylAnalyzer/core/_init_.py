"""
This will be our hub. From here we will create the doc object,
send it to be manipulated, and return it to the views as needed.
"""

from .doc_creation import init

def _init_(filename):
    doc = init(filename)
    print(doc)