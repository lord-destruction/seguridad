import qrcode
from PIL import Image


url = "https://system---failure.blogspot.com/"
qr = qrcode.QRCode (version=1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size=7, border=3)
qr.add_data(url)
qr.make(fit=True)


image = qr.make_image(fill_color = "black", back_color = "blue")

 
logo = Image.open("/Users/lord-drestuction/Documents/cursodesarrollo/python/clcodinglogo.png")
logo_size = image.size[0] // 8

logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
image.paste (logo, ((image.size [0] - logo.size [0]) // 2, (image.size [1] - logo.size [1]) // 2 ))

image.save("qr_code.png")
Image.open("qr_code.png")
