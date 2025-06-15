from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework import routers

from .forms.auth import LoginForm
from .views.auth import RegistrationView
from .views.cooking_tool import CookingToolViewSet
from .views.dish import DishViewSet, DishStep1View, DishStep2View, DishStep3View, DishStep4View, DishStep5View
from .views.index import IndexView
from .views.product import ProductViewSet
from .views.unit import UnitViewSet


router = routers.DefaultRouter()
router.register('cooking_tool', CookingToolViewSet, basename='cooking_tool')
router.register('dish', DishViewSet, basename='dish')
router.register('product', ProductViewSet, basename='product')
router.register('unit', UnitViewSet, basename='unit')


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),

    path('dish/create/step1/', DishStep1View.as_view(), name='app_html/dish/step-1'),
    path('dish/<int:pk>/edit/step1/', DishStep1View.as_view(), name='app_html/dish/edit-step-1'),
    path('dish/<int:dish_id>/step2/', DishStep2View.as_view(), name='app_html/dish/step-2'),
    path('dish/<int:dish_id>/step3/', DishStep3View.as_view(), name='app_html/dish/step-3'),
    path('dish/<int:dish_id>/step4/', DishStep4View.as_view(), name='app_html/dish/step-4'),
    path('dish/<int:dish_id>/step4/', DishStep5View.as_view(), name='app_html/dish/step-5'),

    path('api/v1/', include(router.urls)),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', auth_views.LoginView.as_view(
        template_name='auth/login.html',
        authentication_form=LoginForm,
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)