from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.ytvideosummarizerhome,name="ytvideosummarizerhome"),
    path('get-video-details/', views.get_video_details_ajax, name='get_video_details_ajax'),

]
