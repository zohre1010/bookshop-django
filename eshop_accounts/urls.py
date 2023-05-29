from django.urls import path
from .views import user_account_main_page, edit_user_profile,favorite_product,favorite,signin,signout,signup

app_name = 'eshop_accounts' 
urlpatterns = [
    path('login/', signin, name='user_login'),
    path('register/', signup, name='user_register'),
    path('logout/', signout, name='user_logout'),
    path('user/', user_account_main_page,name='user'),
    path('user/edit', edit_user_profile,name='user_edit'),
    path('favorite/<int:productId>/', favorite_product, name='favorite'),
    path('favorites/',favorite,name='favorites')
    
    ]