from typing import Any, Dict
from django.db.models.query import QuerySet
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all().order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        return context
    
class AuthorView(generic.ListView):
    template_name = 'news/author_stories.html'
    context_object_name = "author_stories"

    def get_queryset(self):
        author_id = self.kwargs.get('author_id')
        return NewsStory.objects.filter(author=author_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allowEdit'] = True
        return context



class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'


class AddStoryView(LoginRequiredMixin, generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

@login_required

def edit_story(request, story_id):
    story = get_object_or_404(NewsStory, id = story_id)
    if request.method == 'POST':
        form = StoryForm(request.POST, instance=story)
        if form.is_valid():
            form.save()
            return redirect('news:story', story_id=story.id)
    else:
        form = StoryForm(instance=story)
    return render(request, 'news/edit_story.html', {'form': form})


@login_required

def delete_story(request, story_id):
    story = get_object_or_404(NewsStory, id = story_id)
    if request.method == 'POST':
        story.delete()
        return render(request, 'news/story_deleted.html')
    return render(request, 'news/delete_story.html', {'story':story})