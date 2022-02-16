from django.shortcuts import render
from django.views import View
from question.models import questionCategory
from .models import blog


class BlogPost(View):

    template_name='blog.html'

    def get(self, request):
        questionCategories=questionCategory.objects.all()
        new_post=blog.objects.all()
        context={
            'questionCategories':questionCategories,
            'new_post':new_post,
        }

        return render(request, self.template_name, context)


class Post(View):
    template_name='post.html'

    def get(self, request, slug):
        questionCategories=questionCategory.objects.all()
        post=blog.objects.get(slug=slug)
        context={
            'questionCategories':questionCategories,
            'post':post
        }
        return render(request, self.template_name, context)
