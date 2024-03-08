from rest_framework import routers
from .views import BooksViewSet, RequestViewSet

app_name = "books"

router = routers.DefaultRouter()
router.register(r"books_list", BooksViewSet)
router.register(r"requests", RequestViewSet)

urlpatterns = [

]
urlpatterns += router.urls
