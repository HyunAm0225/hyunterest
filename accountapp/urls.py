from django.urls import path
from .views import hello, AccountCreateView, AccountDetailView
from django.contrib.auth.views import LoginView, LogoutView
app_name = "accountapp"

urlpatterns = [
    path('hello/', hello, name="hello"),
    path('create/', AccountCreateView.as_view(), name='create'),

    # 로그인 뷰, 로그아웃 뷰 설정
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>/', AccountDetailView.as_view(), name='detail'),

]
