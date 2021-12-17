import pandas as pd
from PIL import Image , ImageDraw, ImageFont
import barcode
from barcode.writer import ImageWriter
df = pd.read_excel('./barcodes.xlsx', index_col = 'indexes')
lenght = df.shape[0]
H = 456 #set label size ( this size is for 58 mm * 40 mm labels)
W = 314
i = 1
while i in range(0,lenght+1):
    price = df.loc[i]['price']
    price_print = ('Price: ' + str(price) + ' dollars') #set inscription price and currency on required language
    companyname = ('Companyname') #set company name
    nomenclature = df.loc[i]['nomenclature']
    barcodenum = df.loc[i]['barcode']
    bc = barcode.get('code128', str(barcodenum), writer=ImageWriter())
    bcadr = bc.save('bc' + nomenclature)
    bcimg = Image.open(bcadr)
    new_img = Image.new('1', (H, W), 'white')
    font = ImageFont.truetype(r'./AlkesLight.ttf', size = 25) #set fonts and sizes
    font2 = ImageFont.truetype(r'./AlkesLight.ttf', size = 35)
    font3 = ImageFont.truetype(r'./AlkesLight.ttf', size = 35)
    fontbar = ImageFont.truetype(r'./code128.ttf', size = 70)
    fontbarlow = ImageFont.truetype(r'./AlkesLight.ttf', size = 14)
    pencil = ImageDraw.Draw(new_img)
    wc, hc = pencil.textsize(nomenclature, font=font) #calculate text size
    wn, hn = pencil.textsize(nomenclature, font = font2)
    wp, hp = pencil.textsize(price_print,  font = font3)
    wb1, hb1 = fontbar.getsize(price_print)
    wb2, hb2 = fontbarlow.getsize(price_print)
    resizedbc = bcimg.resize((int(W), int(H/3.5)), Image.ANTIALIAS)
    pencil.text(((H-wc)/2,10), companyname,  font = font, fill = 'black', encoding = 'UTF-8') #draw texts
    pencil.text(((H-wn)/2,70), nomenclature,  font = font2, fill = 'black', encoding = 'UTF-8')
    pencil.text(((H-wp)/2,140),  price_print,  font = font3, fill = 'black', encoding = 'UTF-8')
    new_img.paste(resizedbc, (int(W/3.5),180)) #paste barcode into label
    new_img.show() #show result

    new_img.save(nomenclature + '.png') #save result
    i = i + 1
