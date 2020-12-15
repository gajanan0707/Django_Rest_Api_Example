from django.urls import path
from .views import article_list, article_detail
from .views import ArticleAPIView, ArticleDetails, GenericAPIView
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ArticleViewSet

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [

    path('articlefun/', article_list),
    path('detailfun/<int:pk>/', article_detail),
    path('articleclass/', ArticleAPIView.as_view()),
    path('detailclss/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/', GenericAPIView.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
    path('viewset/', include(router.urls))


]
