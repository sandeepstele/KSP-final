from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.http import JsonResponse
import os
from django.db.models import Count, Avg
from .models import *
import plotly.express as px
from .crime_forecast import *

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Quest"
    return render(request,"crimeDetection/index.html",{'username':username})

def district(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Quest"  
          
    district_group = ["Bagalkot","Ballari","Belagavi City","Belagavi Dist","Bengaluru City","Bengaluru Dist","Bidar","Chamarajanagar","Chickballapura","Chikkamagaluru","Chitradurga","CID","Coastal Security Police","Dakshina Kannada","Davanagere","Dharwad","Gadag","Hassan","Haveri","Hubballi Dharwad City","K.G.F","Kalaburagi"]    
    option1 = request.GET.get("district_wise_name")
    
    if(option1 != "" and option1 != None):
        print(option1)
        context= {'username' : username,
              "crime":option1,
              'display':"block",
              "file_name":"District",
              'district_group':district_group,
              }
        return render(request,"crimeDetection/district.html",context)
    context= {'username' : username,
              'display':"none",
              'district_group':district_group,
              }
    return render(request,"crimeDetection/district.html",context)
    
def crime(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Quest"  
          
    crime_name = Crime.objects.all()
    option1 = request.GET.get("crime_wise_name")
    
    if(option1 != "" and option1 != None):
        crime = Crime.objects.get(name=option1)
        print(crime)
        context= {'username' : username,
              "crime_name":crime_name,
              "crime":crime,
              'display':"block",
              "file_name":"Crime_group",
              }
        return render(request,"crimeDetection/crime.html",context)
    
    context= {'username' : username,
              "crime_name":crime_name,
              'display':"none",
              }
    return render(request,"crimeDetection/crime.html" ,context)

def district_crime(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Quest"    
        
    districts = District.objects.all()
    option1 = request.GET.get('district')
    option2 =request.GET.get('crime')
    district_name = request.GET.get('district_name')
    print(option1,option2)

    # District name selection and crime group selection
    if(option1 != "" and option1!= None):
        districts = District.objects.all()
        district = District.objects.get(name=option1)
        crimes = CrimeGroup.objects.filter(district=district)
        print(district)
        context = {'username' : username,
                   'districts':districts,
                   'district_name':district.name,
                   'crimes':crimes,
                }
        return render(request,"crimeDetection/hotspot.html" ,context)  
    
    # Crime group selection based on the district selection
    elif(district_name != "" and district_name!= None) and (option2 != "" and option2 != None):
        print(district_name,option2)
        districts = District.objects.all()
        district = District.objects.get(name=district_name)
        crimes = CrimeGroup.objects.filter(district=district)
        print(district) 
        context = {'username' : username,
                   'districts':districts,
                   'district_name':district.name,
                   'district_name_space':district_name.replace(" ",""),
                   'crime':option2,
                   'crime_space':option2.replace(" ",""),
                   'crimes':crimes,
                   'display':"block",
                }
        return render(request,"crimeDetection/hotspot.html",context)
    
    context= {'username' : username,
              'districts':districts,
              'display':"none",
              "district_name":"",
              }
    return render(request,"crimeDetection/hotspot.html" ,context)    

def behavioral(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Quest"        
    crime = request.GET.get('crime')
    crime_group = Victim_Crime.objects.all()
    if(crime):
        victims = Victim.objects.filter(crime = crime)
        criminal = Criminal.objects.filter(crime=crime)
        victim_profession_count = victims.values('crime', 'profession').annotate(count=Count('id'))
        avg_age_victim = victims.aggregate(avg_age_victim=Avg('age'))
        
        criminal_profession_count = criminal.values('crime','profession').annotate(count=Count('id'))
        avg_age_criminal = criminal.aggregate(avg_age_criminal=Avg('age'))
        
        District_count = criminal.values('crime','district').annotate(count=Count('id'))
        
        Caste_count = victims.values('crime','caste').annotate(count=Count('id'))
            
        context = {
        'username':username,
        'crime_group':crime_group,
        'crime':crime,
        'victim_profession_count':victim_profession_count,
        'criminal_profession_count':criminal_profession_count,
        'District_count':District_count,
        'caste_count':Caste_count,
        'display':"block",
        'avg_age_victim':round(avg_age_victim['avg_age_victim'],2),
        'avg_age_criminal':round(avg_age_criminal['avg_age_criminal'],2),
        }
        return render(request,"crimeDetection/behavioral.html" ,context)
        
    
    context = {
        'username':username,
        'crime_group':crime_group,
        'crime':crime,
        'display':"none",
    }
    return render(request,"crimeDetection/behavioral.html" ,context)

def beat_duty(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Quest"
    return render(request,"crimeDetection/beat_duty.html" ,{'username':username})

def rowdy_sheeters(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Quest"
    return render(request,"crimeDetection/rowdy_sheeters.html" ,{'username':username})

def crime_correlation(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Quest"    
        
    chart = forecast_prophet_plot(34)
    context={
        'username':username,
        'chart':chart,
    }
    return render(request,"crimeDetection/crime_correlation.html" ,context )

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "crimeDetection/login.html", {
                "message": "Invalid username and/or password.",
            })
    else:
        return render(request, "crimeDetection/login.html")       

def get_data(request):
    if request.method == "POST":    
        option = request.POST.get("options")
        if (option == "District"):
            folder_path = 'static/sampleData/district_hotspots_maps/'
            files = os.listdir(folder_path)
            file_names = [file_name for file_name in files if file_name.endswith('.html')]
            print(file_names)
            return render(request,"crimeDetection/hotspot.html",{'file': file_names})
        elif (option == "Crime"):
            folder_path = 'static/sampleData/Hotspot based on Crime/'
            files = os.listdir(folder_path)
            file_names = [file_name for file_name in files if file_name.endswith('.html')]
            print(file_names)
            return render(request,"crimeDetection/hotspot.html",{'file': file_names})
        else:
            return render(request,"crimeDetection/hotspot.html")
        
        return HttpResponseRedirect(reverse("hotspot"))
    

def logout_view(request):
    logout(request)
    return render(request,"crimeDetection/login.html")  

def profile(request,user_id):
    user = get_object_or_404(User, id=user_id)
    
    # save changes
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email_id')
        password = request.POST.get('current_password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            return render(request, 'crimeDetection/profile.html', {'error_message': 'Passwords do not match'})

        if(request.user.id == user_id):
            # Update user information
            if username:
                user.username = username
            else:
                user.username = user.username
            
            if email:
                user.email = email 
            else:
                user.email = user.email                 
           
            if password:  # Check if a new password was provided
                user.set_password(password)

            user.save() # Add this line to confirm if the user information was updated
        else:
            return render(request, 'crimeDetection/profile.html', {'error_message': 'You are not the current user'})

        return redirect('profile', user_id=user.id)

    context = {
        'username': user,
    }
    
    return render(request, 'crimeDetection/profile.html', context)

def register(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST.get("password1")
        confirmation = request.POST.get("password2")
        print(password,confirmation)
        if password != confirmation:
            return render(request, "crimeDetection/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "crimeDetection/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "crimeDetection/register.html")
    
    

'''
def hotspot(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Quest"    
        
    districts = District.objects.all()
    crime_name = Crime.objects.all()
    district_group = ["Bagalkot","Ballari","Belagavi City","Belagavi Dist","Bengaluru City","Bengaluru Dist","Bidar","Chamarajanagar","Chickballapura","Chikkamagaluru","Chitradurga","CID","Coastal Security Police","Dakshina Kannada","Davanagere","Dharwad","Gadag","Hassan","Haveri","Hubballi Dharwad City","K.G.F","Kalaburagi"]
    option1 = request.GET.get('district')
    option2 =request.GET.get('crime')
    district_name = request.GET.get('district_name')
    print(option1,option2)
    
    # District name selection and crime group selection
    if(option1 != "" and option1!= None):
        districts = District.objects.all()
        district = District.objects.get(name=option1)
        crimes = CrimeGroup.objects.filter(district=district)
        print(district)
        context = {'username' : username,
                   'districts':districts,
                   'district_name':district.name,
                   "crime_name":crime_name,
                   'crimes':crimes,
                   'display':"block",
                   'district_group':district_group,
                }
        return render(request,"crimeDetection/hotspot.html" ,context)  
    
    # Crime group selection based on the district selection
    elif(district_name != "" and district_name!= None) and (option2 != "" and option2 != None):
        print(district_name,option2)
        districts = District.objects.all()
        district = District.objects.get(name=district_name)
        crimes = CrimeGroup.objects.filter(district=district)
        print(district) 
        context = {'username' : username,
                   'districts':districts,
                   'district_name':district.name,
                   'district_name_space':district_name.replace(" ",""),
                   'crime':option2,
                   "crime_name":crime_name,
                   'crime_space':option2.replace(" ",""),
                   'crimes':crimes,
                   'display':"block",
                   'district_group':district_group,
                }
        return render(request,"crimeDetection/hotspot.html",context)
    
    context= {'username' : username,
              'districts':districts,
              "crime_name":crime_name,
              'display':"none",
              "district_name":"",
              'district_group':district_group,
              }
    return render(request,"crimeDetection/hotspot.html" ,context)     

def district(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Quest"    
        
    district_group = ["Bagalkot","Ballari","Belagavi City","Belagavi Dist","Bengaluru City","Bengaluru Dist","Bidar","Chamarajanagar","Chickballapura","Chikkamagaluru","Chitradurga","CID","Coastal Security Police","Dakshina Kannada","Davanagere","Dharwad","Gadag","Hassan","Haveri","Hubballi Dharwad City","K.G.F","Kalaburagi"]
    districts = District.objects.all()
    crime_name = Crime.objects.all()
    
    option1 = request.GET.get("district_wise_name")
    option2 = request.GET.get("crime_wise_name")
    print(option1,option2)
    if(option1 != "" and option1 != None):
        print(option1)
        context= {'username' : username,
              'districts':districts,
              "crime_name":crime_name,
              "crime":option1,
              'display':"block",
              "file_name":"District",
              "district_name":"",
              'district_group':district_group,
              }
        return render(request,"crimeDetection/district_crime.html",context)
    
    elif(option2 != "" and option2 != None):
        crime = Crime.objects.get(name=option2)
        print(crime)
        context= {'username' : username,
              'districts':districts,
              "crime_name":crime_name,
              "crime":crime,
              'display':"block",
              "file_name":"Crime_group",
              "district_name":"",
              'district_group':district_group,
              }
        return render(request,"crimeDetection/district_crime.html",context)
    
    context= {'username' : username,
              'districts':districts,
              "crime_name":crime_name,
              'display':"none",
              "district_name":"",
              'district_group':district_group,
              }
    return render(request,"crimeDetection/district_crime.html" ,context)  
    '''
