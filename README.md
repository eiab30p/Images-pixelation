"# Images-pixelation" 


Honor Code:
	“On my honor, I have not given, nor received, nor witnessed any unauthorized assistance on this work.”

High Level Description:
	For this project, I tried to create a program that makes any image look like a retro 8-bit pixelated image. I came up with this idea while playing Mario Kart with some friends. I started the process by reading about Dither. I eventually wrote Dither algorithm but it came out as more noise than pixelated. Therefore, with some influence of Dither’s Algorithm, I wrote a program that met most of my expectations. As you can see in the images below I took the original selfie and made it pixelated.

Low Level Description:
Below is a work flow of how the program works to create the pixelated image above. The majority of the processing happens between steps 4 and 5. This can be slightly confusing when looking at the flow chart therefore below is a more detailed description and example of these steps
Step 4 and 5 Description
1)	Starting with the pixel at (0, 0) the program will iterate to our limit which is calculated by taking our starting point and adding the pixel_size. This is done for our x and y axis.
a.	The pixel_size is calculated in step 3, it is found by taking the length of the image and dividing it by 64. I picked 64 as a number to divide against, because between multiple images 64 gave us a result closer to 8. 8 also seemed to be a good range to create the pixelated area. When doing the division we used the double / to get the floor value.
2)	During the process the program will collect the color and coordinates of each pixel within this range.
a.	The color collection is done with a dictionary where the key is the color (RGB) and value is the number of times that color appeared.
3)	Once that iteration has finished, the program will get the most common color by getting the max count in the dictionary.
4)	Then it will iterate over each pixel that it just visited once again and assign each pixel that most common color found in the dictionary.
5)	Once completed, it will go back to the parent loop which will go to the next pixel iterating by the length of pixel_size, for example from 0 to 8
