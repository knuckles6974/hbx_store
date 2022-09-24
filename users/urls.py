from django.urls   import path
from users        import views


from rest_framework_simplejwt.views  import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup', views.SignupView.as_view()),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
