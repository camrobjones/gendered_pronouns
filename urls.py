from django.urls import path

from gender import views

urlpatterns = [
    path('', views.home),
    path('consent', views.consent),
    path('instructions', views.instructions),
    path('treatment', views.treatment),
    path('mediator', views.mediator),
    path('leaders', views.leaders),
    path('proposals', views.proposals),
    path('lgbt', views.lgbt),
    path('lgbt_social', views.lgbt_social),
    path('qualifier', views.qualifier),
    path('demographics', views.demographics),
    path('post_test', views.post_test),
    path('finish', views.finish),
    path('data', views.data)
    ]
