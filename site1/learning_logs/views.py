from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm
from .forms import ContentForm


# Create your views here.
def index(request):
    """ 学习笔记的主页 """
    return render(request, 'learning_logs/index.html')


def topics(request):
    """ 显示所有主题 """
    topics = Topic.objects.order_by('date_add')
    content = {'topics': topics}
    return render(request, 'learning_logs/topics.html', content)


def topic(request, topic_id):
    """ 显示单个主题及所有的条目 """
    topic = Topic.objects.get(id=topic_id)
    contents = topic.content_set.order_by('-date_add')
    content = {'topic': topic, 'entries': contents}
    return render(request, 'learning_logs/topic.html', content)


def new_topic(request):
    """ 创建新主题 """
    if request.method != 'POST':
        """ 未提交数据，创建一个新表单 """
        form = TopicForm()
    else:
        """ POST提交的数据，对提交的数据进行处理 """
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    content = {'form': form}
    return render(request, 'learning_logs/new_topic.html', content)


def new_content(request, topic_id):
    """ 在特定的主题中添加新条目 """
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        """ 未提交数据，创建空表单 """
        form = ContentForm()
    else:
        """ 提交数据，进行处理 """
        form = ContentForm(data=request.POST)
        if form.is_valid():
            new_content = form.save(commit=False)
            new_content.topic = topic
            new_content.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    content = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_content.html', content)
