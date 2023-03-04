from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import date


# deneme

class Project(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = '100', 'Pending'
        ON_TRACK = '200', 'On Track'
        OFF_TRACK = '300', 'Off Track'
        AT_RISK = '400', 'At Risk'
        HOLD = '500', 'Hold'
        COMPLETED = '600', 'Completed'

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    purpose = models.TextField(blank=True)
    success_criteria = models.TextField(blank=True)
    start_date = models.DateField(default=date.today, editable=True)
    status = models.CharField(max_length=3, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    is_archived = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects')
    assigned_to = models.ManyToManyField(User, related_name='assigned_projects', null=True, blank=True)
    sponsor = models.ManyToManyField(User, related_name='sponsored_projects', null=True, blank=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    class PostTypes(models.TextChoices):
        UPDATE = 'UPDT', 'Update'
        LESSON = 'LESL', 'Lesson Learned'
        CHANGE = 'CHNG', 'Change Request'
        QUESTION = 'QUES', 'Question'
        EVENT = 'EVNT', 'Event'
        THANKS = 'THNK', 'Thanks'
        RISK = 'RISK', 'Risk'
        INFO = 'INFO', 'Information'

    summary = models.CharField(max_length=280)
    detail = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='updates')
    type = models.CharField(max_length=4, null=False, blank=False, choices=PostTypes.choices)
    files = models.FileField(blank=True, upload_to='files/')
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.summary


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(blank=True)
    image = models.ImageField(blank=True)
