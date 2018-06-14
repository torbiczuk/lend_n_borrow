from rest_framework import routers
from books.viewsets import UserViewSet


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)