from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'viewsbasics'
urlpatterns = [
    path('', TemplateView.as_view(template_name='viewsbasics/index.html')),
    path('funktionally', views.funktionally),
    path('danger', views.danger),
    path('safer', views.safer),
    path('prettyurldata/<thing>', views.prettyurldata),
    path('bounce', views.bounce),
    path('icecream', views.Icecream.as_view(), name='icecream'),

    path('apple/<slug:number>', views.Apple.as_view(), name='apple'),
    path('banana/<slug:number>', views.Banana.as_view(), name = 'banana'),
    path('orange/<slug:number>', views.Orange.as_view(), name = 'orange'),
    path('bmi/<slug:weight>/<slug:height>', views.BMI.as_view(), name = 'bmi'),
    path('finalvelocity/<slug:vi>/<slug:a>/<slug:t>', views.Finalvelocity.as_view(), name = 'finalvelocity'),

]    
