from django.urls import path, include
from orderapp.views import MenuViewset, OrderViewset, MenuDetailViewset
from django.conf.urls.static import static
from django.conf import settings


menulist = MenuViewset.as_view({
    'get': 'list',
    'post': 'create',
    }
)

order_item = OrderViewset.as_view(
    {
        'get' : 'list',
    }
)

menu_detail = MenuDetailViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', menulist, name='menu-list'),
    path('menu/<int:pk>', menu_detail, name='menu-detail'),
    path('api-auth/', include('rest_framework.urls')),
    path('order', order_item, name ="order-item")
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
