from docxtpl import DocxTemplate, RichText

doc = DocxTemplate("my_word_template.docx")

rt = RichText("hyperlink: ")
rt.add(
    'google',
    url_id=doc.build_url_id('http://google.com'), 
    color='#ff00ff'
)

context = { 
    'company_name' : "8 в",
    'rt': rt
}

doc.render(context)
doc.save("generated_doc.docx")
