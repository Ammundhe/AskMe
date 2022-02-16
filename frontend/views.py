from django.shortcuts import redirect, render
from django.views import View
from .forms import askquestion_form, answer_form
from question.models import question, questionCategory
from answer.models import answer
from blog.models import blog


class HomePage(View):
    template_name='home-page.html'

    def get(self, request):
        questionCategories=questionCategory.objects.all()
        questions=question.objects.all().order_by('-id')[:6]
        answers=answer.objects.all()
        new_post=blog.objects.all().order_by('-id')[:3]

        context={
            'questionCategories':questionCategories,
            'questions':questions,
            'answers':answers,
            'new_post':new_post,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        if request.POST.get('question_upvote'):
            question_id=request.POST.get('question_upvote')
            update_upvote=question.objects.get(id=question_id)
            update_upvote.upvote=int(update_upvote.upvote)+1
            update_upvote.save()
        if request.POST.get('question_downvote'):
            question_id=request.POST.get('question_downvote')
            update_downvote=question.objects.get(id=question_id)
            update_downvote.downvote=int(update_downvote.downvote)+1
            update_downvote.save()
        if request.POST.get('answer_upvote'):
            answer_id=request.POST.get('answer_upvote')
            update_upvote=answer.objects.get(id=answer_id)
            update_upvote.upvote=int(update_upvote.upvote)+1
            update_upvote.save()
        if request.POST.get('answer_downvote'):
            answer_id=request.POST.get('answer_downvote')
            update_downvote=answer.objects.get(id=answer_id)
            update_downvote.downvote=int(update_downvote.downvote)+1
            update_downvote.save()
        
        return redirect("HomePage")

class Askquestion(View):
    template_name='ask-question.html'
    form_class=askquestion_form
    questionCategories=questionCategory.objects.all()

    def get(self, request):
        form=self.form_class()
        context={
            'questionCategories':self.questionCategories,
            'form':form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form=self.form_class(data=request.POST)
        if form.is_valid():
            category=form.cleaned_data.get('category')
            new_question=form.cleaned_data.get('question')
            date=form.cleaned_data.get('date')
            question.objects.create(
                category=category,
                question=new_question,
                author=request.user,
                date=date
            )
            return redirect("HomePage")
        context={
            'questionCategories':self.questionCategories,
            'form':form,
        }
        return render(request, self.template_name, context)


class Question(View):
    template_name='question.html'

    def get(self, request, slug=None):
        if slug:
            questionCategories=questionCategory.objects.all()
            questions=question.objects.filter(question=slug)
            context={
                'questionCategories':questionCategories,
                'questions':questions,
            }
            return render(request, self.template_name, context)
        questionCategories=questionCategory.objects.all()
        questions=question.objects.all()
        context={
            'questionCategories':questionCategories,
            'questions':questions,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        if request.POST.get('question_upvote'):
            question_id=request.POST.get('question_upvote')
            update_upvote=question.objects.get(id=question_id)
            update_upvote.upvote=int(update_upvote.upvote)+1
            update_upvote.save()
        if request.POST.get('question_downvote'):
            question_id=request.POST.get('question_downvote')
            update_downvote=question.objects.get(id=question_id)
            update_downvote.downvote=int(update_downvote.downvote)+1
            update_downvote.save()
        return redirect("Question")

class Category(View):
    template_name='category.html'

    def get(self, request, category_id=None):
        if category_id:
            questionCategories=questionCategory.objects.all()
            questions=question.objects.filter(category_id=category_id)
            context={
                'questionCategories':questionCategories,
                'questions':questions
            }
            return render(request, self.template_name, context)

        questionCategories=questionCategory.objects.all()
        questions=question.objects.all()
        context={
            'questionCategories':questionCategories,
            'questions':questions
        }
        return render(request, self.template_name, context)
    def post(self, request, category_id=None):
        if request.POST.get('question_upvote'):
            question_id=request.POST.get('question_upvote')
            update_upvote=question.objects.get(id=question_id)
            update_upvote.upvote=int(update_upvote.upvote)+1
            update_upvote.save()
        if request.POST.get('question_downvote'):
            question_id=request.POST.get('question_downvote')
            update_downvote=question.objects.get(id=question_id)
            update_downvote.downvote=int(update_downvote.downvote)+1
            update_downvote.save()
        questionCategories=questionCategory.objects.all()
        questions=question.objects.filter(category_id=category_id)
        context={
            'questionCategories':questionCategories,
            'questions':questions
        }
        return render(request, self.template_name, context)

class questionAnswer(View):

    template_name='question-answers.html'
    questionCategories=questionCategory.objects.all()

    def get(self, request):
        if request.GET.get('search'):
            questions=question.objects.filter(question__icontains=request.GET.get('search'))
            context={
                'questionCategories':self.questionCategories,
                'questions':questions
            }
            return render(request, self.template_name, context)
        questions=question.objects.all()
        context={
            'questionCategories':self.questionCategories,
            'questions':questions
        }
        return render(request, self.template_name, context)

    def post(self, request):
        if request.POST.get('answer_upvote'):
            answer_id=request.POST.get('answer_upvote')
            update_upvote=answer.objects.get(id=answer_id)
            update_upvote.upvote=int(update_upvote.upvote)+1
            update_upvote.save()
        if request.POST.get('answer_downvote'):
            answer_id=request.POST.get('answer_downvote')
            update_downvote=answer.objects.get(id=answer_id)
            update_downvote.downvote=int(update_downvote.downvote)+1
            update_downvote.save()
        return redirect("Answer")

class Answer(View):
    template_name='answer.html'
    form_class=answer_form
    questionCategories=questionCategory.objects.all()


    def get(self, request, question_id=None):
        form=self.form_class()
        context={
            'questionCategories':self.questionCategories,
            'form':form,
        }
        return render(request, self.template_name, context)

    def post(self, request, question_id=None):
        new_answer=request.POST.get('answer')
        image=request.POST.get('image')
        date=request.POST.get('date')
        answers, created= answer.objects.get_or_create(question_id=question_id, author_id=request.user)
        if created:
            answer.objects.create(
                question_id=question_id,
                answer=new_answer,
                image=image,
                author=request.user,
                date=date
            )
        else:
            answers.question_id=question_id
            answers.answer=new_answer
            answers.image=image
            answers.author=request.user
            answers.date=date
            answers.save()
        return redirect("Answer",question_id=question_id)
