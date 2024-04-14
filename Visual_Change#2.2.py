import turtle

# In this program it asks the user to provide coordinates to place the pictures produced from Program_A
# First it starts off by asking the X-coordinate for the first picture and than the Y_coordinate for the first picture
# This will continue for all four pictures
# If the picture is out of the canvas or is overlapping another photo it will re-prompt the user to enter new coordinates

# If there is repeated code I will not as notes for simplicity of reader

def Create_A_Collage():
	canvas = turtle.Screen() # Setup a screen to show the collage
	canvas.setup(1000,800) # Set the width and height of the canvas of the collage

	# Since canvas is 1000 by 800 the domain is (-500, 500) and the range is (-400, 400)

	turtle.bgcolor("grey") # Set background colour to grey so images are easily visable
	t = turtle.Turtle()
	t.speed(0) # Make the collage instantly as commands are entered
	t.penup()

	txt = open('File.txt','r')
	values = txt.readlines() # Create a list from values entered in Program_A

	Sepia_X = int(input("Enter X Coordinate for Sepia Tone Picture: ")) # Request X-Coordinate
	Sepia_Y = int(input("Enter Y Coordinate for Sepia Tone Picture: ")) # Request Y-Coordinate

	Sepia_X_Half = (int(values[1]) / 2) # Get half of the width of the picture
	Sepia_Y_Half = (int(values[2]) / 2) # Get Half of the height of the picture

	Sepia_X = Sepia_X + Sepia_X_Half # Create a new placement point so point of placement is the bottom left of the photo and not the middle, as requested by user
	Sepia_Y = Sepia_Y + Sepia_Y_Half


	Left1 = Sepia_X - Sepia_X_Half # Create a box of values which will be used to check if there is overlapping between photos
	Right1 = Sepia_X + Sepia_X_Half
	Top1 = Sepia_Y + Sepia_Y_Half
	Bot1 = (Sepia_Y - Sepia_Y_Half) - 20 # -20 so it takes into account the title of the photo
	Title1 = str(values[0]) # Assign a variable with title of photo

	while ((Sepia_X - Sepia_X_Half) < -500) or ((Sepia_X + Sepia_X_Half) > 500): # Make sure that the value entered is within domain of canvas
		print('ERROR, picture is off of canvas please change X coordinate') # If not in the domain request the value to be re-entered
		Sepia_X = int(input("Re-Enter X Coordinate for Sepia Tone Picture: ")) # Request new X value
		Sepia_X = Sepia_X + Sepia_X_Half # Create the new values based on input of user
		Left1 = Sepia_X - Sepia_X_Half # Recalculate left and right values based on new input
		Right1 = Sepia_X + Sepia_X_Half
	while ((Sepia_Y - Sepia_Y_Half) < -400) or ((Sepia_Y + Sepia_Y_Half) > 400): # Make sure that the input is within the range of the canvas
		print('ERROR, picture is off of canvas please change Y coordinate') # If not in the domain request the value to be re-entered
		Sepia_Y = int(input("Re-Enter Y Coordinate for Sepia Tone Picture: ")) # Request new Y value
		Sepia_Y = Sepia_Y + Sepia_Y_Half # Create the new values based on user input
		Top1 = Sepia_Y + Sepia_Y_Half # Recalculate the top and bottom variables based on new inputs
		Bot1 = (Sepia_Y - Sepia_Y_Half) - 20
	else:
		t.goto(Sepia_X, Sepia_Y) # Once the designated coordinates are inside the canvas go to where the user requested
		canvas.addshape('SepiaTone_Image.gif') # Add the image produced in Program_A as a shape
		t.shape('SepiaTone_Image.gif') # Make the shape of the turtle the image which has been modified
		t.stamp() # Stamp the image in the designated place
		t.shape('classic') # Return the shape of the turtle to classic arrow
		t.penup() # Lift up the pen
		t.goto(Left1, Bot1) # Go to the place where the title shall be added
		t.write(Title1[0:-1], font=("Calibri", 16, "bold")) # Write the title of the picture under the picture

	# Most of the code below this point is repeated just using different values

	Negative_X = int(input("Enter X Coordinate for Negative Picture: "))
	Negative_Y = int(input("Enter Y Coordinate for Negative Picture: "))

	Negative_X_Half = (int(values[4]) / 2)
	Negative_Y_Half = (int(values[5]) / 2)

	Negative_X = Negative_X + Negative_X_Half
	Negative_Y = Negative_Y + Negative_Y_Half

	Left2 = Negative_X - Negative_X_Half
	Right2 = Negative_X + Negative_X_Half
	Top2 = Negative_Y + Negative_Y_Half
	Bot2 = (Negative_Y - Negative_Y_Half) - 20
	Title2 = str(values[3])



	while (Left1 <= Right2) and (Right1 >= Left2) and (Bot1 <= Top2) and (Top1 >= Bot2): # Check the picture does not overlap the first picture
		print('There was a problem with overlapping photos please try again!') # Tell the user that the photos overlapped
		Negative_X = int(input("Enter X Coordinate for Negative Picture: ")) # Request new X and Y Coordinates
		Negative_Y = int(input("Enter Y Coordinate for Negative Picture: "))

		Negative_X_Half = (int(values[4]) / 2) # Create the new neccesary values based off of the new inputs from the user
		Negative_Y_Half = (int(values[5]) / 2)

		Negative_X = Negative_X + Negative_X_Half
		Negative_Y = Negative_Y + Negative_Y_Half

		Left2 = Negative_X - Negative_X_Half
		Right2 = Negative_X + Negative_X_Half
		Top2 = Negative_Y + Negative_Y_Half
		Bot2 = (Negative_Y - Negative_Y_Half) -20
	else:
		while ((Negative_X - Negative_X_Half) < -500) or ((Negative_X + Negative_X_Half) > 500):
			print('ERROR, picture is off of canvas please change X coordinate')
			Negative_X = int(input("Re-Enter X Coordinate for Negative Picture: "))
			Negative_X = Negative_X + Negative_X_Half
			Left2 = Negative_X - Negative_X_Half
			Right2 = Negative_X + Negative_X_Half
		while ((Negative_Y - Negative_Y_Half) < -400) or ((Negative_Y + Negative_Y_Half) > 400):
			print('ERROR, picture is off of canvas please change Y coordinate')
			Negative_Y = int(input("Re-Enter Y Coordinate for Negative Picture: "))
			Negative_Y = Negative_Y + Negative_Y_Half
			Top2 = Negative_Y + Negative_Y_Half
			Bot2 = (Negative_Y - Negative_Y_Half - 20)
		else:
			t.goto(Negative_X, Negative_Y)
			canvas.addshape('Negative_Image.gif')
			t.shape('Negative_Image.gif')
			t.stamp()
			t.shape('classic')
			t.penup()
			t.goto(Left2,Bot2)
			t.write(Title2[0:-1], font=("Calibri", 16, "bold"))


	Red_X = int(input("Enter X Coordinate for Only Red Picture: "))
	Red_Y = int(input("Enter Y Coordinate for Only Red Picture: "))

	Red_X_Half = (int(values[7]) / 2)
	Red_Y_Half = (int(values[8]) / 2)

	Red_X = Red_X + Red_X_Half
	Red_Y = Red_Y + Red_Y_Half

	Left3 = Red_X - Red_X_Half
	Right3 = Red_X + Red_X_Half
	Top3 = Red_Y + Red_Y_Half
	Bot3 = (Red_Y - Red_Y_Half) - 20
	Title3 = str(values[6])

	while ((Left1 <= Right3) and (Right1 >= Left3) and (Bot1 <= Top3) and (Top1 >= Bot3)) or ((Left2 < Right3) and (Right2 > Left3) and (Bot2 < Top3) and (Top2 > Bot3)):
		print('There was a problem with overlapping photos please try again!')
		Red_X = int(input("Enter X Coordinate for Only Red Picture: "))
		Red_Y = int(input("Enter Y Coordinate for Only Red Picture: "))

		Red_X_Half = (int(values[7]) / 2)
		Red_Y_Half = (int(values[8]) / 2)

		Red_X = Red_X + Red_X_Half
		Red_Y = Red_Y + Red_Y_Half

		Left3 = Red_X - Red_X_Half
		Right3 = Red_X + Red_X_Half
		Top3 = Red_Y + Red_Y_Half
		Bot3 = (Red_Y - Red_Y_Half) - 20
	else:
		while ((Red_X - Red_X_Half) < -500) or ((Red_X + Red_X_Half) > 500):
			print('ERROR, picture is off of canvas please change X coordinate')
			Red_X = int(input("Re-Enter X Coordinate for Only Red Picture: "))
			Red_X = Red_X + Negative_X_Half
			Left3 = Red_X - Red_X_Half
			Right3 = Red_X + Red_X_Half
		while ((Red_Y - Red_Y_Half) < -400) or ((Red_Y + Red_Y_Half) > 400):
			print('ERROR, picture is off of canvas please change Y coordinate')
			Red_Y = int(input("Re-Enter Y Coordinate for Only Red Picture: "))
			Red_Y = Red_Y + Red_Y_Half
			Top3 = Red_Y + Red_Y_Half
			Bot3 = (Red_Y - Red_Y_Half) -20
		else:
			t.goto(Red_X, Red_Y)
			canvas.addshape('Only_Red_Image.gif')
			t.shape('Only_Red_Image.gif')
			t.stamp()
			t.shape('classic')
			t.penup()
			t.goto(Left3,Bot3)
			t.write(Title3[0:-1], font=("Calibri", 16, "bold"))


	GreyScale_X = int(input("Enter X Coordinate for Grey Scale Picture: "))
	GreyScale_Y = int(input("Enter Y Coordinate for Grey Scale Picture: "))

	GreyScale_X_Half = (int(values[10]) / 2)
	GreyScale_Y_Half = (int(values[11]) / 2)

	GreyScale_X = GreyScale_X + GreyScale_X_Half
	GreyScale_Y = GreyScale_Y + GreyScale_Y_Half

	Left4 = GreyScale_X - GreyScale_X_Half
	Right4 = GreyScale_X + GreyScale_X_Half
	Top4 = GreyScale_Y + GreyScale_Y_Half
	Bot4 = (GreyScale_Y - GreyScale_Y_Half) - 20
	Title4 = str(values[9])


	while ((Left1 <= Right4) and (Right1 >= Left4) and (Bot1 <= Top4) and (Top1 >= Bot4)) or ((Left2 < Right4) and (Right2 > Left4) and (Bot2 < Top4) and (Top2 > Bot4)) or ((Left3 <= Right4) and (Right3 >= Left4) and (Bot3 <= Top4) and (Top3 >= Bot4)):
		print('There was a problem with overlapping photos please try again!')
		GreyScale_X = int(input("Enter X Coordinate for Grey Scale Picture: "))
		GreyScale_Y = int(input("Enter Y Coordinate for Grey Scale Picture: "))

		GreyScale_X_Half = (int(values[10]) / 2)
		GreyScale_Y_Half = (int(values[11]) / 2)

		GreyScale_X = GreyScale_X + GreyScale_X_Half
		GreyScale_Y = GreyScale_Y + GreyScale_Y_Half

		Left4 = GreyScale_X - GreyScale_X_Half
		Right4 = GreyScale_X + GreyScale_X_Half
		Top4 = GreyScale_Y + GreyScale_Y_Half
		Bot4 = (GreyScale_Y - GreyScale_Y_Half) - 20
	else:
		while ((GreyScale_X - GreyScale_X_Half) < -500) or ((GreyScale_X + GreyScale_X_Half) > 500):
			print('ERROR, picture is off of canvas please change X coordinate')
			GreyScale_X = int(input("Re-Enter X Coordinate for Grey Scale Picture: "))
			GreyScale_X = GreyScale_X + GreyScale_X_Half
			Left4 = GreyScale_X - GreyScale_X_Half
			Right4 = GreyScale_X + GreyScale_X_Half
		while ((GreyScale_Y - GreyScale_Y_Half) < -400) or ((GreyScale_Y + GreyScale_Y_Half) > 400):
			print('ERROR, picture is off of canvas please change Y coordinate')
			GreyScale_Y = int(input("Re-Enter Y Coordinate for Grey Scale Picture: "))
			GreyScale_Y = GreyScale_Y + GreyScale_Y_Half
			Top4 = GreyScale_Y + GreyScale_Y_Half
			Bot4 = (GreyScale_Y - GreyScale_Y_Half) - 20
		else:
			t.goto(GreyScale_X, GreyScale_Y)
			canvas.addshape('GreyScale_Image.gif')
			t.shape('GreyScale_Image.gif')
			t.stamp()
			t.shape('classic')
			t.penup()
			t.goto(Left4, Bot4)
			t.write(Title4[0:-1], font=("Calibri", 16, "bold"))

	turtle.exitonclick() # Once done looking at the collage click on the screen it is opened on

Create_A_Collage()