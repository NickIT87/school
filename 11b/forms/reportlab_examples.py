# reportlab
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

# set encoding UTF-8
pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))

def generate_pdf(filename):
    c = canvas.Canvas(filename)
    # set font UTF-8
    c.setFont('Arial', 12)
    # add some text UTF-8
    c.drawString(100, 750, "Приклад тексту звіту")
    c.save()

generate_pdf("example.pdf")
