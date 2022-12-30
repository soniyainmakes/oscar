from django.urls import path
from. import views
app_name='storyapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('story/<int:story_id>/',views.detail,name='detail'),
    path('add/',views.add_story,name='add_story'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete')

]
