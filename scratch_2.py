from pdf2image import convert_from_path

pages = convert_from_path('C:/Users/eliza/Desktop/sample_data/combining/output1.pdf')

for page in pages:
    page.save('out.jpg', 'JPEG')