from django.urls import path, re_path
from . import views
from django.views.static import serve
from django.conf import settings


# app_name = "soosapp"
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('write/', views.write, name='write'),
    path('write/write_ok/', views.write_ok, name='write_ok'),
    path('update/<int:id>', views.update, name='update'),
    path('update/update_ok/<int:id>', views.update_ok, name='update_ok'),
    # 게시판
    path('b_list/', views.b_list, name='b_list'),
    path('b_write/', views.b_write, name='b_write'),
    path('b_delete/<int:id>', views.b_delete, name='b_delete'),
    path('b_list/<int:id>', views.b_content, name='b_content'),
    path('b_write/write_ok/', views.b_write_ok, name='b_write_ok'),
    path('b_update/<int:id>/', views.b_update, name='b_update'),
    path('b_update/update_ok/<int:id>', views.b_update_ok, name='b_update_ok'),
]

urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

# 로그인, 로그아웃
urlpatterns += [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]