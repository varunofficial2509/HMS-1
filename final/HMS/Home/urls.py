from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='Home'),
    path('student_login/',views.studentlogin,name='studentlogin'),
    path('admin_login/',views.adminlogin,name='adminlogin'),
    path('student_register/',views.studentregister,name='studentregister'),
    path('Godavari_hostel/', views.godavari, name='godavari'),
    path('krishna_hostel/', views.krishna, name='krishna'),
    path('Saraswathi_hostel/', views.saraswathi, name='saraswathi'),
    path('Sharadha_hostel/', views.sharadha, name='sharadha'),
    path('logout/', views.logoutUser, name="logout"),
    path('add_caretaker/',views.AddCaretaker,name='AddCaretaker'),
    path('add_HM/',views.AddHM,name='AddHM'),
    path('HM_home/',views.HMhome,name='HMhome'),
    path('caretaker_home/',views.caretakerhome,name='caretakerhome'),
    path('student_home/',views.studenthome,name='studenthome'),
    path('student_profile/<str:pk>/',views.studentprofile,name='studentprofile'),
    path('student_update_profile/<str:pk>/',views.studentupdateprofile,name='studentupdateprofile'),
    path('student_pending_requests/<str:pk>/',views.studentpendingrequests,name='studentpendingrequests'),
    path('delete_request/<str:pk>/',views.deleterequest,name='deleterequest'),
    path('caretaker_profile/<str:pk>/',views.caretakerprofile,name='caretakerprofile'),
    path('caretaker_update_profile/<str:pk>/',views.caretakerupdateprofile,name='caretakerupdateprofile'),
    path('HM_profile/<str:pk>/',views.HMprofile,name='HMprofile'),
    path('HM_update_profile/<str:pk>/', views.HMupdateprofile, name='HMupdateprofile'),
]