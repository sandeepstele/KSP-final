# KSP-final - Prototype


# Hi, We are Siren Squad! 👋

# Predictive Crime Analytics
Predictive Crime Analytics is a web-based application developed using Django that offers advanced crime analysis and prediction capabilities. Leveraging machine learning algorithms and historical crime data, the platform provides insights into crime hotspots, trends, and patterns. Users can explore crime statistics, conduct behavioral analysis of criminals and victims, and predict future crime occurrences based on past data. The application also offers month-wise crime group analysis, empowering law enforcement agencies and policymakers with valuable information for proactive crime prevention strategies. With its user-friendly interface and powerful analytics features, Predictive Crime Analytics aims to enhance public safety and support decision-making in combating crime.


# Technology Used:
- Python
- HTML
- CSS
- JavaScript
- Bootstrap
- Django
-
# Libraries Used:
- Seaborn
- Plotly
- numpy
- pandas
- fb prophet
- Scikit-learn
- folium
- geocoder
-matplotlib



# API Used:
- ApexCarts.js


# ScreenShots 


## Installation

Install my-project with `git clone `

##### Get started!

```bash
   create a folder in the name you needed `your folder name`
```
```bash
  git clone https://github.com/sandeepstele/KSP-final
```
    
## Environment Variables

To run this project, you will need to run the virtual Environment file `myVenv`

```bash
   source myVenv/Scripts/activate
```
If your system doesn't have the virtual Environment then,

```bash
   pip install venv
```
```bash
   python3 -m venv .venv

   source .venv/bin/activate
```
For Unix/MacOS


## To Run the project

### After cloning and running `myVenv` 
To run the `myVenv` in the `Git Bash` Terminal
```bash
source myVenv/Scripts/activate
```

Install django in the virtual environment

```bash
  pip install django
```

start the database to run

```bash
   python manage.py makemigrations
```
```bash
   python manage.py migrate
```

After migration to manage the database create a superuser

```bash
   python manage.py createsuperuser
```

Go to the project directory

```bash
  cd Datathon
```

Start the server

```bash
  python manage.py runserver
```

# Open Your Browser:
Visit http://localhost:8000 to start exploring Predictive Crime Analytics!

Features:

Geospatial Analysis using K-means and hotspot is visualised on Map
- District Based 
- Crime Based
- District and Crime inter-connected 

Socio-Economic Analysis of Data:
- Plotting heatmaps for understand the occupational distrobution among victims and criminals.
- Pie chart for understand the district distribution based on crime occurences.

Identify correlated crimes occurring together within the same timeline and visualise their distribution among beat duties:

- Correlated Crimes: Analyze most occurring time groups to find correlated crimes that frequently co-occur.
- Visualization: Create a bar graph showing counts of correlated crime pairs for quick insights.
- Beat Duty Distribution: Generate pie charts illustrating how occurrences are distributed among beat duties for each correlated crime pair.

