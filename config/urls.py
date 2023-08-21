from django.contrib import admin
from django.urls import include, path
from usuario.router import router as usuario_router
from rest_framework.routers import DefaultRouter
from garagem.views import CategoriaViewSet, VeiculoViewSet, AcessorioViewSet, CorViewSet, MarcaViewSet, ModeloViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"veiculos", VeiculoViewSet)
router.register(r"acessorios", AcessorioViewSet)
router.register(r"cores", CorViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"modelos", ModeloViewSet)


urlpatterns = [ 
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(usuario_router.urls)),
]

