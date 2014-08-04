from io import BytesIO
from pdfdocument.document import PDFDocument

def gen_pdf(fname, num_of_files,seed_text):
	f = BytesIO()
	pdf = PDFDocument(f)
	pdf.init_letter()
	pdf.h1('Test')
	pdf.p('{}'.format(seed_text))
	pdf.generate()

	for x in range(0,num_of_files):
		with open('data/{}_{}.pdf'.format(fname,x),'w') as pdfout:
			pdfout.write(f.getvalue())
	pdfout.close()

if __name__ == '__main__':
	print(gen_pdf("testpdf",2,"test file"))