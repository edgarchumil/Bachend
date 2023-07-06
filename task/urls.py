from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from task import views

router = routers.DefaultRouter()
router.register(r"employee", views.EmployeeView, "employee")

urlpatterns = [
    path("api/", include(router.urls)),
    path('docs/', include_docs_urls(title='Employee API')),
    ]