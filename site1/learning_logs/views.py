from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic
from .models import Content
from .forms import TopicForm
from .forms import ContentForm


def check_topic_owner(request, topic):
    """ 检查主题所有者 """
    if request.user != topic.owner:
        raise Http404


# Create your views here.
def index(request):
    """ 学习笔记的主页 """
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """ 显示所有主题 """
    topics = Topic.objects.filter(owner=request.user).order_by('date_add')
    content = {'topics': topics}
    return render(request, 'learning_logs/topics.html', content)


@login_required
def topic(request, topic_id):
    """ 显示单个主题及所有的条目 """
    topic = Topic.objects.get(id=topic_id)
    # 检查所有者
    check_topic_owner(request, topic)

    contents = topic.content_set.order_by('-date_add')
    content = {'topic': topic, 'entries': contents}
    return render(request, 'learning_logs/topic.html', content)


@login_required
def new_topic(request):
    """ 创建新主题 """
    if request.method != 'POST':
        """ 未提交数据，创建一个新表单 """
        form = TopicForm()
    else:
        """ POST提交的数据，对提交的数据进行处理 """
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    content = {'form': form}
    return render(request, 'learning_logs/new_topic.html', content)


@login_required
def new_content(request, topic_id):
    """ 在特定的主题中添加新条目 """
    topic = Topic.objects.get(id=topic_id)
    # 检查所有者
    check_topic_owner(request, topic)

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


@login_required
def edit_content(request, content_id):
    """ 编辑既有条目 """
    entry = Content.objects.get(id=content_id)
    topic = entry.topic
    # 检查所有者
    check_topic_owner(request, topic)

    if request.method != 'POST':
        """ 除此请求，创建表单 """
        form = ContentForm(instance=entry)
    else:
        form = ContentForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_content.html', context)


@login_required
def delete_content(request, content_id):
    entry = Content.objects.get(id=content_id)
    topic = entry.topic
    # 检查所有者
    check_topic_owner(request, topic)
    entry.delete()

    return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))


@login_required
def delete_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    # 检查所有者
    check_topic_owner(request, topic)
    topic.delete()

    return HttpResponseRedirect(reverse('learning_logs:topics'))
