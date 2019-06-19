from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from first_anket.views import IndexView, SignUpView

from first_anket.views import DetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^detail/(?P<pk>\d+)', DetailView.as_view()),
    url(r'^$', IndexView.as_view()),
    url(r'^sign_up/$', SignUpView.as_view()),
]
