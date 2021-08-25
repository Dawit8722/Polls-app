from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('int:question_id/', views.detail, name='detail'),
    path('int:question_id>/results/', views.detail, name='results')
    path('int:question_id/vote/', views.detail, name='vote')
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
