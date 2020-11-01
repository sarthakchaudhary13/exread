from django.urls import path
from .views import Upload

app_name = "vendors"

urlpatterns = [
    path("upload/", Upload.as_view(), name="upload"),
]
