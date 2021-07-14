from pdf2image import convert_from_path
from pdf2image import pdfinfo

pdfinfo('C:/Users/eliza/Desktop/sample_data/combining/output1.pdf')
pages = convert_from_path('C:/Users/eliza/Desktop/sample_data/combining/output1.pdf', 169)

for page in pages:
    page.save('out.jpg', 'JPEG')