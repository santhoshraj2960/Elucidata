# Elucidata
Interview task (Protein analaysis)

Elucidata is a tool designed for graphical visualization of proteins' data.

Requirements

Django 1.8
Python 2.7
How to set it up

Download or Clone the git repo on your local system

Navigate inside elucidata directory

Run the following command python manage.py migrate

Then start the server using the following command python manage.py runserver

After starting the server go to http://localhost:8000/metabolites/

Select a protein type from the drop down and click on submit button.

Now you will be able to graphically see the "NA corrected with zero" values of that protein structure in the form of a bar graph. You can verify this data by opening the metabolites.csv file present inside the elucidata directory.

Also refer to the screenshots directory to get an idea of how your graph might look like
