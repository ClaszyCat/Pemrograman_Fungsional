from PIL import Image

background_path = "C:\\Users\\yovii\\Documents\\FIle kuliah\\Semester 5\\Fungsional ngoding\\Praktikum 6\\Latihan\\asset\\background.jpg"
overlay_path = "C:\\Users\\yovii\\Documents\\FIle kuliah\\Semester 5\\Fungsional ngoding\\Praktikum 6\\Latihan\\asset\\overlay.png"
background = Image.open(background_path)
overlay = Image.open(overlay_path)
overlay = overlay.convert("RGBA")
overlay = overlay.resize((400, 400))

x_position = 50
y_position = 100
background.paste(overlay, (x_position, y_position), overlay)
output_path = "output.jpg"
background.save(output_path)
background.show()