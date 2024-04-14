from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_view, name="login"),
    path('register/',views.register,name="register"),
    path('profile/<int:user_id>/',views.profile,name="profile"),
    path('home/',views.index,name="index"),
    path('logout/',views.logout_view,name="logout"),
    path('hotspot/district/',views.district,name="hotspot_district"),
    path('hotspot/crime',views.crime,name="hotspot_crime"),
    path('hotspot/district/crime/',views.district_crime,name="hotspot_district_crime"),  
    path('hostspot/district/',views.district,name="district"),
    path('behavioral/',views.behavioral,name="behavioral"),
    path('beat_duty/',views.beat_duty,name="beat_duty"),
    path('rowdy_sheeters/',views.rowdy_sheeters,name="rowdy_sheeters"),
    path('crime_correlation/',views.crime_correlation,name="crime_correlation"),
    path('crime_group_distribution/',views.crime_group_distribution,name="crime_group_distribution"),
    path('crime_forecasting',views.crime_forecasting,name="crime_forecasting"),
]
