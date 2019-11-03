# Import the required module for text  
# to speech conversion 
#pip install gtts
#Resource: https://www.geeksforgeeks.org/convert-text-speech-python/
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
import os 
  
# The text that you want to convert to audio 
mytext = 'Public Service Employees shall:                                                                                                                    Carry out their responsibilities in a way that is fair, just and equitable and reflects the Public Service commitment to equality and diversity; Serve the Government of the day, whatever its political persuasion, to the best of their ability in a way that maintains political impartiality and is in line with the requirements as outlined in the code, no matter what their political beliefs are;                                                                                                               Not act in a way that unjustifiably favours or discriminates against particular individuals or interests!'
  
# Language in which you want to convert 
#language = 'pt-br' #Portuguese (Brazil)
language = 'en' #English
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("welcome.mp3") 
  
# Playing the converted file 
os.system("start welcome.mp3")  #This command is for windows only for either operating systems download mpg321 and use os.system("mpg321 welcome.mp3") 
