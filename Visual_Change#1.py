# Name: Mason McWilliams
# Student ID: 6874614

# Import all the required modules/functions
import image
import random as r
import distance as d
import math as m



def Assignment3(file_name, min_stars, max_stars):
	Picture = image.FileImage(file_name)
	Window_1 = image.ImageWin(Picture.getWidth(), Picture.getHeight(), 'Original Picture')
	Picture.draw(Window_1) # Here the original picture is produced so the user of the program is able to see the difference
	num_stars = r.randint(min_stars, max_stars) # a random number of stars is choosen between the minimum and maximum entered by user
	p_sky = image.Pixel(70,90,100) # A pixel is created based on the sky for use of the distance function
	Small_stars = 0
	Big_stars = 0
	obscure = 0 
	Width = Picture.getWidth()
	Height = Picture.getHeight()
	for i in range(0, num_stars): # Create a loop that continues until all stars are created
		col = r.randint(0, Width - 2) 
		row = r.randint(0, Height - 2)
		p = Picture.getPixel(col, row) # Using col and row to find a random pixel placement
		p1 = Picture.getPixel(col+1,row) # Used for distance function when regarding the adjacent pixels of the large star
		p2 = Picture.getPixel(col-1,row)
		p3 = Picture.getPixel(col,row+1)
		p4 = Picture.getPixel(col,row-1)
		Star_Type = r.randint(0,1) # Make a coin toss like simulation to determine whether it will be a small or large star
		if d.distance(p, p_sky) < 35: # Use Distance code to make sure base pixel of star is placed in the sky and not on Moon, Tree, or Bird
			if Star_Type == 0: # Create a Small Star
				p.setRed(255)
				p.setGreen(255)
				p.setBlue(255)
				Picture.setPixel(col, row, p)
				Small_stars = Small_stars + 1 # Count the number of small stars
			elif Star_Type == 1: # When it is 1, base of large star is made
				p.setRed(255)
				p.setGreen(255)
				p.setBlue(255)
				Picture.setPixel(col, row, p)
				Big_stars = Big_stars + 1 # Count the number of large stars
				if d.distance(p1, p_sky) < 35: #There is than a sequence of code to check if the 4 adjacent pixels are able to be placed next to the base, if not it is counted as obscured
					p.red = 255            
					p.green  = 255 
					p.blue = 255
					Picture.setPixel(col + 1, row, p)
				else:
					obscure = obscure + 1
				if d.distance(p2, p_sky) < 35:
					p.red = 255            
					p.green  = 255 
					p.blue = 255
					Picture.setPixel(col - 1, row, p)
				else:
					obscure = obscure + 1
				if d.distance(p3, p_sky) < 35:
					p.red = 255            
					p.green  = 255 
					p.blue = 255
					Picture.setPixel(col, row + 1, p)
				else:
					obscure = obscure + 1
				if d.distance(p4, p_sky) < 35:
					p.red = 255            
					p.green  = 255 
					p.blue = 255
					Picture.setPixel(col, row - 1, p)
				else:
					obscure = obscure + 1
	Window_2 = image.ImageWin(Picture.getWidth(), Picture.getHeight(), 'Stars Included')
	Picture.draw(Window_2) # Create the second image after the stars have been added
	Total_stars = Big_stars + Small_stars
	print("Total Number of Stars Added =", Total_stars) # Print all the added stars/obscurities
	print("Total Number of Small Stars Added =", Small_stars)
	print("Total Number of Large Stars Added =", Big_stars)
	print("Total Number of Obscured Stars =", obscure)

Assignment3('harvestMoon.jpg',300,500) # Use of the function


