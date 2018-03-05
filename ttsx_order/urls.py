from django.conf.urls import url, include
import views
urlpatterns = [
    url('^$', views.do_order),
]