from rest_framework.routers import SimpleRouter

from users.views import UserViewSet

users_router = SimpleRouter()

users_router.register(r'users', UserViewSet)
