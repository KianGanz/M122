# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
import os
from dotenv import load_dotenv
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

load_dotenv()

api_key = os.getenv('stripe.api_key')

stripe.api_key = api_key

charges = stripe.Charge.list(limit=1)

test = print(charges)

fileName = 'Betrag.pdf'
documentTitle = 'sample'
title = 'Modul 122'
subTitle = 'Betrag Informationen'
textLines = print(charges)
image = 'OIP.jfif'

pdf = canvas.Canvas(fileName)

pdf.setTitle(documentTitle)

pdf.drawCentredString(300, 770, title)

pdf.setFillColorRGB(0, 0, 255)
pdf.setFont("Courier-Bold", 24)
pdf.drawCentredString(290, 720, subTitle)

pdf.line(30, 710, 550, 710)

text = pdf.beginText(40, 680)
text.setFont("Courier", 18)
text.setFillColor(colors.red)
  
for line in textLines:
    text.textLine(line)
      
pdf.drawText(text)

pdf.drawInlineImage(image, 130, 400)

pdf.save()




