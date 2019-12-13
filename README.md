**The Goal of the app:

This application return the similar images based on the images exists the database using Edge Histogram Distance.
------------------------------------------------------
**Packages required :

*Python 3.6
* pymongo
*sklearn.cluster
------------------------------------------------------
**Files :

insert.py:  inject the edge histogram (eh) files in the Mongodb with their indexes and clusters. 
on travaille ici seulement avec 80000 images   
app.py: the web app (http://localhost:5000) using Flask.
templates/index.html : html file of the app

-------------------------------------------------------
**Steps to use the app :

1. Add images to ./static/img
2. Open MongoDB
3. Change the path of the input files (eh)
4. Run insert.py
5. Run app.py
6. Enter : http://localhost:5000 in your browser 
7. Enjoy it !

---------------------------------------------------
A report written in french is provided




