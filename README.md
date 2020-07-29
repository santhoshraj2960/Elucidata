# Elucidata

Interview task (Protein analaysis)

Elucidata is a tool designed for **graphical visualization** of proteins' data.

Requirements
 1) Django 1.8
 2) Python 2.7
 
 **Screen shots:** https://github.com/santhoshraj2960/Elucidata/tree/master/screen_shots
 
![Image of social media scheduler](https://github.com/santhoshraj2960/Protein-Analysis/blob/master/screen_shots/Screen%20Shot%202018-07-09%20at%2012.23.23.png)

![Image of social media scheduler](https://github.com/santhoshraj2960/Protein-Analysis/blob/master/screen_shots/Screen%20Shot%202018-07-09%20at%2012.24.15.png)


# How to set it up
1) Download or Clone the git repo on your local system
2) Navigate inside elucidata directory
3) Run the following command
   python manage.py migrate
4) Then start the server using the following command
   python manage.py runserver
   
1) After starting the server go to http://localhost:8000/metabolites/
2) Select a protein type from the drop down and click on submit button. 
3) Now you will be able to graphically see the "NA corrected with zero" values of that protein structure in the form of a bar graph.
You can verify this data by opening the metabolites.csv file present inside the elucidata directory.

Also refer to the screenshots directory to get an idea of how your graph might look like
https://github.com/santhoshraj2960/Elucidata/tree/master/screen_shots
