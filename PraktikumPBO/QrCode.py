import qrcode
img = qrcode.make('https://media.tenor.com/EVzpU6EwQpAAAAAM/daxtar-gif-yang-buka-monyet.gif')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")