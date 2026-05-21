import qrcode

def qr_generate():

    qr = qrcode.QRCode(
        version=1,
        box_size=10
    )
    string = input("What link do you want to go to?")
    qr.add_data(string)

    img = qr.make_image(fill_color = "black", back_color = "white")

    img.save("workspace_epd/image.png")