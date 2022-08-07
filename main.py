from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont

def drawText(img, text, width, height):
	fontSize=int(width/7)

	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("font/arial.ttf", fontSize)
	draw.text((width/2, height-(fontSize-50)), text, (255, 255, 255), font=font, anchor="mm")


def main():
	imgName=str(input("Enter file's name: "))
	img = Image.open(imgName)
	width, height = img.size # Get Widht & Height from image

	enhancer = ImageEnhance.Color(img)      # Adjust image color balance
	img = enhancer.enhance(1.2)

	enhancer = ImageEnhance.Contrast(img)   # Adjust image contrast
	img = enhancer.enhance(1.2)

	enhancer = ImageEnhance.Brightness(img) # Adjust image brightness
	img = enhancer.enhance(1.1)

	enhancer = ImageEnhance.Sharpness(img)  # Adjust image sharpness
	img = enhancer.enhance(2)
	

	text = str(input("Enter text: "))
	drawText(img, text, width, height)

	# Blur
	img = img.filter(ImageFilter.GaussianBlur(radius=2))

	# Decrease size
	img = img.resize((int(width/7), int(height/7)), Image.Resampling.LANCZOS)
	
	# Resize to orignal size (decrise quality)
	img = img.resize((width, height), Image.Resampling.LANCZOS)

	# img.show(optimize=False, quality=10)
	img.save("shitpost."+(imgName.split('.')[1]) ,optimize=False, quality=10)

if __name__ == '__main__':
	main()
