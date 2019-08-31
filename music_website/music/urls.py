from django.conf.urls import url
from music import views


urlpatterns = [
    # 首页
    url(r'^$', views.index, name='index'),
    # 搜索
    url(r'^search/$', views.search, name='search'),
    # 随机
    url(r'^goodluck/$', views.good_luck, name='goodluck'),
]