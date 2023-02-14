 
from django.urls import path  
from toolcre import views


urlpatterns = [
 
    path('numb', views.numb,name='numb'),  
    path('num',views.num,name='num'),
    path('ico',views.ico,name='ico'),
    #path('upload', views.upload_file, name='upload'),
    #path('success', views.success_view, name='success'),
   
    # path('edit/<int:id>', views.edit),  
    # path('update/<int:id>', views.update),  
    # path('delete/<int:id>', views.destroy), 
]



