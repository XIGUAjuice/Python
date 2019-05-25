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
    url(r'^new_content/(?P<topic_id>\d+)/$', views.new_content, name='new_content'),
    # 修改条目
    url(r'^edit_content/(?P<content_id>\d+)/$', views.edit_content, name='edit_content'),
    # 删除条目
    url(r'^delete_content/(?P<content_id>\d+)/$', views.delete_content, name='delete_content'),
    # 删除主题
    url(r'^delete_topic/(?P<topic_id>\d+)/$', views.delete_topic, name='delete_topic'),
]
