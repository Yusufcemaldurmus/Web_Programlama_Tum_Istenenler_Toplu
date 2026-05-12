from django.db import models
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import Choice, Question, Category


class IndexView(LoginRequiredMixin, generic.ListView):
    """
    Handles the display of the main index page, listing active questions.
    """
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Retrieves the standard queryset for the index view, with optional search filtering.
        
        Returns:
            QuerySet: The filtered and ordered questions, excluding future ones.
        """
        query = self.request.GET.get("q")
        queryset = Question.objects.filter(pub_date__lte=timezone.now())
        if query:
            queryset = queryset.filter(question_text__icontains=query)
        return queryset.order_by("-pub_date")[:5]

    def get_context_data(self, **kwargs):
        """
        Injects system-wide statistics into the index context using optimized queries.
        """
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        
        # Optimized: Single aggregation for total votes across active polls
        total_votes = Choice.objects.filter(
            question__pub_date__lte=now
        ).aggregate(models.Sum('votes'))['votes__sum'] or 0
        
        # Optimized: Count distinct questions that have at least one vote
        completed_polls = Question.objects.filter(
            pub_date__lte=now,
            choice__votes__gt=0
        ).distinct().count()
        
        context['total_votes_all'] = total_votes
        context['completed_polls_count'] = completed_polls
        context['search_query'] = self.request.GET.get("q", "")
        return context


class DetailView(LoginRequiredMixin, generic.DetailView):
    """
    Handles the display of a specific question's voting form.
    """
    model = Question
    template_name = "polls/detail.html"
    
    def get_object(self, queryset=None):
        """
        Retrieves the question object and increments its view count.
        """
        obj = super().get_object(queryset=queryset)
        obj.views = F('views') + 1
        obj.save(update_fields=['views'])
        obj.refresh_from_db()
        return obj

    def get_queryset(self):
        """
        Restrict the queryset to exclude unpublished (future) questions.
        
        Returns:
            QuerySet: Questions published up to the current timestamp.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(LoginRequiredMixin, generic.DetailView):
    """
    Handles the visualization of voting results for a specific question.
    """
    model = Question
    template_name = "polls/results.html"

    def get_context_data(self, **kwargs):
        """
        Injects additional context, including percentage calculations for choices.
        
        Args:
            **kwargs: Dictionary of keyword arguments to pass to the view.
            
        Returns:
            dict: The context dictionary containing 'sorted_choices' and 'total_votes'.
        """
        context = super().get_context_data(**kwargs)
        question = context['question']
        choices = question.choice_set.all()
        total_votes = sum(choice.votes for choice in choices)
        
        sorted_choices = []
        for choice in choices:
            percentage = (choice.votes / total_votes * 100) if total_votes > 0 else 0
            choice.percentage = percentage
            sorted_choices.append(choice)
            
        sorted_choices.sort(key=lambda x: x.votes, reverse=True)
        
        context['sorted_choices'] = sorted_choices
        context['total_votes'] = total_votes

        # Determine next and previous questions based on publication date order
        context['prev_question'] = Question.objects.filter(pub_date__gt=question.pub_date, pub_date__lte=timezone.now()).order_by('pub_date').first()
        context['next_question'] = Question.objects.filter(pub_date__lt=question.pub_date).order_by('-pub_date').first()
        
        return context


@login_required
def vote(request, question_id):
    """
    Processes the voting submission for a given question.
    
    Args:
        request (HttpRequest): The incoming HTTP request payload.
        question_id (int): The primary key of the question being voted on.
        
    Returns:
        HttpResponseRedirect: Redirects into the Results view on successful vote.
        HttpResponse: Renders the detail view with an error message on failure.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form due to missing choice parameter.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        # Atomic increment to prevent race conditions during high concurrency.
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after processing POST data.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

def signup(request):
    """
    Handles user registration using Django's built-in UserCreationForm.
    Logs the user in upon successful registration and redirects to the index.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('polls:index'))
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def add_poll(request):
    """
    Renders and processes the form to add a new custom poll.
    """
    if request.method == "POST":
        question_text = request.POST.get("question_text", "").strip()
        category_id = request.POST.get("category")
        
        # Validate main fields
        if not question_text:
            categories = Category.objects.all()
            return render(request, "polls/add_poll.html", {
                "categories": categories,
                "error_message": "Soru metni boş bırakılamaz."
            })
            
        category = None
        if category_id:
            try:
                category = Category.objects.get(pk=category_id)
            except Category.DoesNotExist:
                pass

        # Validate that at least two choices are provided
        raw_choices = []
        for key in request.POST:
            if key.startswith("choice_"):
                val = request.POST[key].strip()
                if val:
                    raw_choices.append(val)
        
        if len(raw_choices) < 2:
            categories = Category.objects.all()
            return render(request, "polls/add_poll.html", {
                "categories": categories,
                "question_text": question_text,
                "error_message": "Bir anketin en az 2 şıkkı olmalıdır."
            })

        # Save to DB
        new_question = Question.objects.create(
            question_text=question_text,
            pub_date=timezone.now(),
            category=category,
            views=0
        )
        
        for c_text in raw_choices:
            Choice.objects.create(
                question=new_question,
                choice_text=c_text,
                votes=0
            )
            
        return HttpResponseRedirect(reverse("polls:index"))

    # GET request
    categories = Category.objects.all()
    return render(request, "polls/add_poll.html", {"categories": categories})
