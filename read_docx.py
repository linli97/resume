import docx
doc = docx.Document('c:/Users/LI LIN/Projects/resume/assets/CV-3.0-L.docx')
for para in doc.paragraphs:
    print(para.text)
