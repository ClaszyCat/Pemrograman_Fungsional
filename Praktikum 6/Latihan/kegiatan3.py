from PIL import Image, ImageEnhance

img = Image.open("C:\\Users\\yovii\\Documents\\FIle kuliah\\Semester 5\\Fungsional ngoding\\Praktikum 6\\Latihan\\asset\\Foto_user.jpg")

enhancer = ImageEnhance.Brightness(img)
brightened = enhancer.enhance(1.5)

enhancer = ImageEnhance.Contrast(brightened)
final = enhancer.enhance(1.2)

final.save("enhanced.jpg")
final.show()