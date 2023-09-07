import pyshorteners
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

filename='shortened_url.pdf'

def shorten_url(link):
	shortener = pyshorteners.Shortener()

	shortened_url = shortener.tinyurl.short(link)

	print(shortened_url)


def save_to_pdf():
	c = canvas.Canvas(filename, pagesize=letter)
	c.setFont('Helvetica', 12)
	c.drawString(100, 700, link)
	c.save()


if __name__ == '__main__':
	link = input("Enter url: ")
	shorten_url(link)
	save_to_pdf()
