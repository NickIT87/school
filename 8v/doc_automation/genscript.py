import datetime
import time
from docxtpl import DocxTemplate, RichText


doc = DocxTemplate("my_word_template.docx")

user_name       = "Іванов Іван Іванович"
school_class    = "8в"
project_name    = "контрольна робота"
link_text       = "https://google.com/"
middle: int     = 8
prefered: int   = 9
difference: int = prefered - middle
date_time       = datetime.datetime.fromtimestamp(
    time.time()).strftime("%Y-%m-%d %H:%M:%S")


rt = RichText("hyperlink: ", color='#ff00ff')
rt.add(
    project_name,
    url_id = doc.build_url_id(link_text), 
    color='#3a86ff'
)

# кінцева частина програми
context = { 
    'name' : user_name,
    'school_class': school_class,
    'rt': rt,
    'middle': middle,
    'prefered': prefered,
    'difference': difference,
    'date_time': date_time,
}

doc.render(context)
doc.save("generated_doc.docx")