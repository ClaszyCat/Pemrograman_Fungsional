from PIL import Image, ImageOps, ImageDraw, ImageFont

img = Image.open("C:\\Users\\yovii\\Documents\\FIle kuliah\\Semester 5\\Fungsional ngoding\\Praktikum 6\\Latihan\\asset\\Foto_user.jpg")

fontPath = "C:\\Users\\yovii\\Documents\\FIle kuliah\\Semester 5\\Fungsional ngoding\\Praktikum 6\\Latihan\\asset\\Poppins-Black.ttf"
customFont = ImageFont.truetype(fontPath, 28)

imgAfter = ImageOps.grayscale(img.copy())
draw = ImageDraw.Draw(imgAfter)
text = "Rafidhiya Bagus Farizki, 202110370311424"
image_width, image_height = img.size
# text_width, text_height = draw.textsize(text, font=customFont)
bbox = draw.textbbox((8, 8), text, font=customFont)
text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
text_position = ((image_width - text_width) // 2, (image_height - text_height) // 9)
draw.text(text_position, text, font=customFont, fill="black")


imgAfter.save("output_image.jpg")
imgAfter.show()