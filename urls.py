from django.urls import path

from gender import views

urlpatterns = [
    path('', views.home),
    path('treatment', views.treatment),
    path('mediator', views.mediator),
    path('female_politicians', views.female_politicians),
    path('profemale', views.profemale),
    path('lgbt', views.lgbt),
    path('lgbt_social', views.lgbt_social),
    path('qualifier', views.qualifier),
    path('demographics', views.demographics),
    path('finish', views.finish)
    ]
