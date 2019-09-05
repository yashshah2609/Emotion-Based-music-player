Emotion-Based-music-player
It's music player with chrome as front-End which has the capablity to detect emotions from the face of user with the help of machine learning algorithm.  
Credits of this project goes to @yashshah2609 and @PartheshSoni.
Description :

      In this project we have used libraries like OpenCV, EEL, numpy etc.

      OpenCV : for capturing images from webcam as well as for processing purpose. made implemantation of fisherface 			 methodology of opencv for classification.

      FisherFace : to train the madel and store it in a model-file(.xml). While using player it uses for prediction 				 for emotion.
      
      **--> We have used haarcascade trained model provided by OpenCV for face segmentation from the captured image.

      --> Because the mapping of the genere of songs to the emotion we had decided to put only 4 emotions into consideration for model.
      	  1>angry
      	  2>happy
      	  3>sad
      	  4>neutral

      EEl library: It proveds connectivity of javascript with python. Like we can say as html-JS as frontend and python as backend. The reason for chosing this was the frontend of html with css give us too many facilities for our project. in the HTML-CSS based Music player There are mostly all preferable options are given with a option based on mood which will ignite python script to work.

The Flow goes like :: run the capture.py file it will trigger html file which will show you CSS-HTML based music player(webpage) -> Want to play any music just click on play-button shown on song or have plus sign to add it to queue.
->another option of based on emotion will be shown on right uper side, select it. JS will trigger python function.
->camera will start and record your image in backend and go for 10 successful image which contains any face.
->generate emotion prediction on those images and get aggregate result of those 10 result and choose appropriate emotion and forward it to JS script.
->JS chose random song of that genere to play.
->Whenever song will go to end It will repeat the same process in backend such that user can't not know that.

HOW TO RUN ?

--> download whole project in single folder as uploaded. If U r familiar with jss by understanding the js model u can easly insert # 	 of songs bcz we have make the whole javascript code dynamically such that, just by inserting data inyo the correct dictionary in js will make the project to show and run your own choosed musics.

--> make sure u have installed openCV, opencv contrib, eel, numpy and all it's dependancies.
library of eel : https://drive.google.com/open?id=1LphmYEBwa-SXbTFXuxIKBAt4iQ1Z2JA8
*--> Just run capture.py file.

-->u can see the images on which assumption of emotion is made in the images folder.
   I advise u to train the model in your pc and then use it(I case you are using any new or updated dataset).
   
-->for any query u can mail on shahyash2609@gmail.com.
Thank You.
