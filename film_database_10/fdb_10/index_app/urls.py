from django.urls import path
from index_app import views
app_name = "filmapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:film_id>/', views.detail, name="detail"),
    path('add_film/', views.add_film, name='add_film'),
    path('update/', views.redirect_f, name='redirect'),
    path('delete/', views.redirect_f, name='redirect'),
    path('update/<int:id>/', views.update_film, name='update'),
    path('delete/<int:id>/', views.delete_film, name='delete'),
]

