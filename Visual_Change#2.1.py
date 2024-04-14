import image

# In this program you are asked four times to enter the file name of which photo you would like to manipulate.
# Than after providing the file name you are asked to provide a title for the picture that will be produced.
# The pictures created will be saved to the users folder, as well as a txt file containing the Width and Height of the pictures along with the title.

# Some of the commands are repeated through the different functions, so it'll only have a note beside it once for simplicity

def SepiaTone():
	file_name = input("Enter the picture file name of which you would like to apply sepia tone: ") # Get the name of the file
	Imported_Picture = image.FileImage(file_name) # Define image.FileImage with the name of the picture being used
	txt.write(input("Enter title of picture used for sepia tone: ") + '\n') # Enter the title for the picture that is being created
	txt.write(str(Imported_Picture.getWidth()) + '\n')
	txt.write(str(Imported_Picture.getHeight()) + '\n') # Adding the width and height of selected image to txt file 
	for row in range(Imported_Picture.getWidth()):
		for col in range(Imported_Picture.getHeight()): #Changing each pixel to apply the changes
			k = Imported_Picture.getPixel(row,col)
			Red = k.getRed() # Get red, green, and blue values of the selected pixel
			Green = k.getGreen() 
			Blue = k.getBlue()
			New_Red = int(0.393 * Red + 0.769 * Green + 0.189 * Blue) # Apply the Sepia Tone filter values to each of the values to create a new red, green, blue
			New_Green = int(0.349 * Red + 0.686 * Green + 0.168 * Blue)
			New_Blue = int(0.272 * Red + 0.534 * Green + 0.131 * Blue)
			if New_Red > 255: # Make sure the values of the colours do no exceed the range of 255 otherwise make them 255
				New_Red = 255
			if New_Green > 255:
				New_Green = 255
			if New_Blue > 255:
				New_Blue = 255
			New_Pixel = image.Pixel(New_Red, New_Green, New_Blue) # Create new pixel out of the equation provided earlier
			Imported_Picture.setPixel(row, col, New_Pixel) #Apply the newly created pixel to the selected row and col
	Imported_Picture.save('SepiaTone_Image.gif') # Save the image with filter



def Make_Negative(): # Function was created with help from the slide lessons provided
	file_name = input("Enter the picture file name of which you would like to make negative: ")
	Imported_Picture = image.FileImage(file_name)
	txt.write(input("Enter title of picture used for making picture negative: ") + '\n')
	txt.write(str(Imported_Picture.getWidth()) + '\n')
	txt.write(str(Imported_Picture.getHeight()) + '\n')
	for row in range(Imported_Picture.getWidth()):
		for col in range(Imported_Picture.getHeight()):
			k = Imported_Picture.getPixel(row,col) # Select every pixel in picture using for loop
			Red = k.getRed() 
			Green = k.getGreen() 
			Blue = k.getBlue()
			New_Red = 255 - Red # Reverse the red, green, and blue values by subtracting the max value (255) by the current values of red, green, and blue
			New_Green = 255 - Green
			New_Blue = 255 - Blue
			New_Pixel = image.Pixel(New_Red, New_Green, New_Blue)
			Imported_Picture.setPixel(row, col, New_Pixel)
	Imported_Picture.save('Negative_Image.gif')


def Only_Red():
	file_name = input("Enter the picture file name of which you would like to make only red: ")
	Imported_Picture = image.FileImage(file_name)
	txt.write(input("Enter title of picture that is only red: ") + '\n')
	txt.write(str(Imported_Picture.getWidth()) + '\n')
	txt.write(str(Imported_Picture.getHeight()) + '\n')
	for row in range(Imported_Picture.getWidth()):
		for col in range(Imported_Picture.getHeight()):
			k = Imported_Picture.getPixel(row,col) 
			New_Green = k.getGreen() - k.getGreen() # Remove the green and blue values completely so that the photo is only different shades of red
			New_Blue = k.getBlue() - k.getBlue()
			New_Pixel = image.Pixel(k.getRed(), New_Green, New_Blue)
			Imported_Picture.setPixel(row, col, New_Pixel)
	Imported_Picture.save('Only_Red_Image.gif')



def GreyScale():
	file_name = input("Enter the picture file name of which you would like to apply grey scale: ")
	Imported_Picture = image.FileImage(file_name)
	txt.write(input("Enter title of picture used for grey scale: ") + '\n')
	txt.write(str(Imported_Picture.getWidth()) + '\n')
	txt.write(str(Imported_Picture.getHeight()) + '\n')
	for row in range(Imported_Picture.getWidth()):
		for col in range(Imported_Picture.getHeight()):
			k = Imported_Picture.getPixel(row,col)
			Intensity = int((k.getRed() + k.getGreen() + k.getGreen()) / 3) # Using the formula to convert a pixel to grey scale use it on each of the values
			New_Pixel = image.Pixel(Intensity, Intensity, Intensity) # Use intensity for all three values of the pixel to produce different shades of grey based on the pixel
			Imported_Picture.setPixel(row, col, New_Pixel)
	Imported_Picture.save('GreyScale_Image.gif')


txt = open("File.txt","w") # Open a text file that can be written in after the functions are used
SepiaTone() # Apply the functions so there is some type of information in the txt file
Make_Negative()
Only_Red()
GreyScale()
txt = open("File.txt", "r") # Open the file so it can be read



