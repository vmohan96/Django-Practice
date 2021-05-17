from django.conf.urls import url
from basicapp import views

# Alows for template tagging
app_name = 'basicapp'

urlpatterns = [
    url(r'relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other')
]
