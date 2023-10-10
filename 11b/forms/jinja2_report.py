from jinja2 import Template

def generate_html(filename):
    template = Template(
        """<html>
                <head><meta charset="UTF-8"></head>
                <body>
                    <h1>{{ title }}</h1>
                    <p>{{ content }}</p>
                </body>
            </html>"""
    )
    rendered = template.render(
        title="Приклад автоматичного звіту",
        content="Текст з головною інформацією звіту"
    )
    with open(filename, "w") as file:
        file.write(rendered)

generate_html("example.html")
