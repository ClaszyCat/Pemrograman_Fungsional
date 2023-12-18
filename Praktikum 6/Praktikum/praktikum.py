from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageEnhance, ImageFilter

#Input Media
background = Image.open ("C:\\Users\\yovii\\Documents\\FIle kuliah\\Semester 5\\Fungsional ngoding\\Praktikum 6\\Praktikum\\asset\\UMM langit.jpg")
overlay = Image.open ("C:\\Users\\yovii\\Documents\\FIle kuliah\\Semester 5\\Fungsional ngoding\\Praktikum 6\\Praktikum\\asset\\lambang umm.png")
fontPath= "C:\\Users\\yovii\\Documents\\FIle kuliah\\Semester 5\\Fungsional ngoding\\Praktikum 6\\Praktikum\\asset\\arial.ttf" 

#Grayscale, Rotated 30 Degree, and Blur Image Background
grayscale = ImageOps.grayscale(background.copy())
rotated = grayscale.rotate(30)
filter = rotated.filter(ImageFilter.BLUR)
finalBg = filter.resize((1980, 1080))

#Enhance brightness to 1.24 times and Contrast to 1.24 times for Overlay Image 
enhancer = ImageEnhance.Brightness(overlay)
brightened = enhancer.enhance(1.24)

enhancer = ImageEnhance.Contrast(brightened)
final = enhancer.enhance(1.24)

#Resize Overlay
overlay = final.resize((500, 500))

#Add text to Overlay image
padding = 170
customFont = ImageFont.truetype(fontPath, 24)
draw = ImageDraw.Draw(overlay)
text = "INFORMATIKA JOSSS!"
text_width = draw.textlength(text, font=customFont)
text_height = draw.textlength(text, font=customFont)
text_position = ((overlay.width - text_width) // 2, overlay.height - text_height + padding)
draw.text(text_position, text, font=customFont, fill="black")

# Calculate the position to center the overlay on the background
overlay_position = (
    (finalBg.width - overlay.width) // 2,
    (finalBg.height - overlay.height) // 2
)

# Paste the overlay onto the background at the calculated position
finalBg.paste(overlay, overlay_position)

# Show and save the final image
finalBg.show()
finalBg.save("C:\\Users\\yovii\\Documents\\FIle kuliah\\Semester 5\\Fungsional ngoding\\Praktikum 6\\Praktikum\\asset\\tugas_praktikum_enam.jpg")