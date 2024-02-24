import arrr
from pyscript import document, window, Element


def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = arrr.translate(english)



input_text = Element("input_text")

output = Element("output")

def clear(event):
    input_text.clear()
    # print(output.innerText)
    # output.write(input_text.value)
    

    
def submit(event):    
    from pyscript import window, document

    my_element = document.querySelector("#output")
    my_element.innerText = window.location.hostname

    #output.text(input_text.value)
    


