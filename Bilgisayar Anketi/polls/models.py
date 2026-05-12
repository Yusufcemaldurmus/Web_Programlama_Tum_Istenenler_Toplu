import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


class Category(models.Model):
    """
    Groups questions by specific cyber security topics.
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=30, default="bi-shield")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Question(models.Model):
    """
    Represents a specific poll question within the system.
    
    Attributes:
        question_text (models.CharField): The text of the cyber security question being asked.
        pub_date (models.DateTimeField): The date and time when the question was published.
        category (models.ForeignKey): The theme or category of this question.
        views (models.IntegerField): Total times this question's detail page was accessed.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        """Returns the string representation of the model (the question text)."""
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        """
        Determines if the question was published within the last day.
        
        Returns:
            bool: True if published within the last 24 hours (and not in the future), False otherwise.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """
    Represents a single answer choice associated with a specific Question.
    
    Attributes:
        question (models.ForeignKey): The Question this choice belongs to.
        choice_text (models.CharField): The text content of the choice.
        votes (models.IntegerField): The total number of votes this choice has received.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Returns the string representation of the specific choice."""
        return self.choice_text
