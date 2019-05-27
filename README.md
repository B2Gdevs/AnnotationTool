# image_checker_tool

![image](https://github.com/B2Gdevs/AnnotationTool/blob/master/Screenshot%20from%202018-12-18%2012-57-00.png)

**This repo is specifically for a tool made to be used to quickly identify bad and good images.**
It's only functionality is that it shows a picture and if the user clicks on the 'bad image' button 
then the image is moved to the output directory specified. 
This is useful for when one has to manually check each image and then separate the good and bad images.  
It has one more thing it can do.  It saves your checkpoint.  However, I believe that there is an error in that.  It saves the 
number of where the user was last, but that number is in relation to the amount of images that was currently in the folder
at the start of the program.  The number will be different if images have been moved adn you restart the program.
