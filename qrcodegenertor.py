import qrcode
import image
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)

data = "https://www.youtube.com/watch?v=bho8Eo-J8ds&t=1749s" #link qrcode

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", back_color = "white") #setting warna
img.save("link.png")