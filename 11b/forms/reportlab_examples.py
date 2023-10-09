# reportlab
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

# Устанавливаем кодировку UTF-8
pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))


def generate_pdf(filename):
    c = canvas.Canvas(filename)
    # Устанавливаем шрифт с поддержкой UTF-8
    c.setFont('Arial', 12)
    # Добавляем текст с символами UTF-8
    c.drawString(100, 750, "Привет, это отчет!")
    c.save()


generate_pdf("example.pdf")
