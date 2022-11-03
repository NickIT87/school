from docxtpl import DocxTemplate, RichText

doc = DocxTemplate("my_word_template.docx")

rt = RichText("hyperlink: ", color='#ff00ff')
rt.add(
    'google',
    url_id=doc.build_url_id('http://google.com'), 
    color='#ff00ff'
)

context = { 
    'company_name' : "10 б",
    'rt': rt
}

doc.render(context)
doc.save("generated_doc.docx")
