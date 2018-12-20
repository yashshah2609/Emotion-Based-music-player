Emotion-Based-music-player
It's music player with chrome as face which has the capablity of detecting emotion from face with the help of machine learning.  
Credits of this project goes to @yashshah2609 and @PartheshSoni.
Description :

      In this project we used libraryis of python mainly like OpenCV, EEL, numpy etc.

      OpenCV : We have used this for capturing photes from webcam as well as processing on it. make implemantation of fisherface 			 methodology of opencv.

      FisherFace : use for train the madel, create it and store it in a .xml model file. While using player it uses for prediction 				 for emotion.
      
      --> Because of songs classification categories of # 4	we have make corr 4 categories of emotions.
      	  1>angry
      	  2>happy
      	  3>sad
      	  4>neutral

      **--> We have also used haarcascade trained model provided by OpenCV for face detection in the captured image.

      EEl : It's a way to connect javascript with python in our project. The reason for chosing this was the frontend of html with  	  css give us too much facilities for our project. In javascript we have given all the posssible ways for playing the 		  music.

HOW TO RUN ?

--> download whole project in single folder as uploaded. If U r familiar with jss by understanding the js model u can easly insert # 	 of songs bcz we have make the whole javascript code dynamicaly such that by just inserting data in the correct dictionary in js 	 u can make no. of songs to be added.

--> make sure u have installed openCV, opencv contrib, eel, numpy and all it's dependancies.

*--> Just run capture.py file.

-->u can see the images on which assumption of emotion is made in the images folder.
   I advise u to train the model in your pc and then use it.
   To retrain the model with ur photoes just add them according the classification in the data set. I suggest u to take ur images with    the help of running code and copy the optimised images from the images folder where ur realtime photoes with crop,gray and of prefered size u get. only add those gray images to dataset as ur expression and then train model. U can just run hard_update to do so. 
for any query u can ask.
