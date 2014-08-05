from __future__ import print_function
from io import BytesIO
from pdfdocument.document import PDFDocument
from docx import *
import xlsxwriter
import random
import datetime

relationships = relationshiplist()
appprops = appproperties()
contenttypes = contenttypes()
websettings = websettings()
wordrelationships = wordrelationships(relationships)


class Leviathan:

	def __init__(self):
		pass

	def generate_text_files(self, fname, num_of_files,seed_text):
		"""Usage: generate_text_files(fname,num_of_files,seed_text)"""
		try:
			with open("data/{}.txt".format(fname),'w') as txtfile:
				for i in range(1,num_of_files):
					txtfile.write(u'{}{}'.format(seed_text,i))
				txtfile.close()
		except Exception as e:
			print('Sorry an error has occured while generating text files: {}'.format(e))

	def generate_xlsx_files(self, fname, num_of_files):
		"""Usage: generate_xlsx_files(fname, num_of_files)"""
		for x in range(0, num_of_files):
			workbook = xlsxwriter.Workbook('data/{}_{}.xlsx'.format(fname,x))
			worksheet = workbook.add_worksheet()

			choices = ['Rent','Gas', 'Food','Gym','Cable TV','Internet','Cell Phone','Water']
			
			
			row = 0
			col = 0
			
			exspenses = (
				[random.choice(choices),random.randrange(300)],
				[random.choice(choices),random.randrange(300)],
				[random.choice(choices),random.randrange(300)],
				[random.choice(choices),random.randrange(300)],
				)

			try:

				for item, cost in (exspenses):
					worksheet.write(row, col, item)
					worksheet.write(row,col + 1, cost)
					row += 1
				worksheet.write(row, 0, 'Total')
				worksheet.write(row, 1, '=SUM(B1:B4)')
				workbook.close()

			except Exception as e:
				print("There was a problem saving your xlsx file: {}".format(e))

	def generate_docx_files(self, fname, num_of_files, seed_text):
		"""Usage: generate_docx_files(fname,num_of_files, seed_text)"""
		
		
		for x in range(0, num_of_files):
			document = newdocument()
			body = document.xpath('/w:document/w:body', namespaces=nsprefixes)[0]

			body.append(heading('eDiscovery Review Test Document',1))
			body.append(paragraph('{}'.format(seed_text)))

			title = 'Test Document'
			subject = 'test file generate by Don Johnson'
			creator = 'Don Johnson'
			keywords =['test','python','leviathan']

			coreprops = coreproperties(title=title, subject=subject, creator=creator, keywords=keywords)
			try:

				savedocx(document,coreprops, appprops, contenttypes, websettings, wordrelationships, 'data/{}_{}.docx'.format(fname,x))
			
			except Exception as e:
				print('There was a problem saving your docx file: {}'.format(e))

	def generate_pdf_files(self, fname, num_of_files,seed_text):
		"""Usage: gnerate_pdf_files"""
		now = datetime.datetime.now()
		f = BytesIO()
		pdf = PDFDocument(f)
		pdf.init_letter()
		pdf.h1('{}'.format(seed_text))
		pdf.p(str(now))
		pdf.generate()
		try:

			for x in range(0, num_of_files):
			
				with open("data/{}_{}.pdf".format(fname, x), 'w') as pdfout:
					pdfout.write(f.getvalue())
			pdfout.close()
		except Exception as e:
			print('There was a problem saving your pdf file: {}'.format(e))


def test():
	test_leviathan = Leviathan()
	test_leviathan.generate_text_files('text_file_test',1000,'text file test')
	test_leviathan.generate_xlsx_files('xlsx_file_test',1000)
	test_leviathan.generate_docx_files('docx_file_test',1000, 'docx file test')
	test_leviathan.generate_pdf_files('pdf_file_test',1000, 'pdf file test')


if __name__ == '__main__':
	test()
