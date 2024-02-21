import arrr
from pyscript import document
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np


def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = arrr.translate(english)

