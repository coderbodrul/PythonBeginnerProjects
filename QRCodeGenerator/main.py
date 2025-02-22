import qrcode

data = input('txt or url: ').strip()
file_name = input('Enter the file name: ').strip()

qr = qrcode.QRCode(box_size=7, border=3)
qr.add_data(data)
image = qr.make_image(fill_color = 'black', back_color = 'white')
image.save(file_name)
print(f"QR code saved as {file_name}")