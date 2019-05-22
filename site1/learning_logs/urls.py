""" 定义learning_logs的url匹配模式 """
from django.conf.urls import url
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    # 显示
    url(r'^topics/$', views.topics, name='topics'),
    # 特定主题的详细页面
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # 创建新主题
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # 创建新条目
    url(r'^new_content/(?P<topic_id>\d+)/$', views.new_content, name='new_content')
]
