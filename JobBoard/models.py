from django.db import models
from datetime import datetime, timedelta


class JobPosting(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20)
    published_at = models.DateTimeField(auto_now_add=True)
    company = models.CharField(max_length=100, blank=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    experience_required = models.CharField(max_length=50,
                                           null=True,
                                           blank=True)
    qualifications = models.TextField(null=True, blank=True)
    application_deadline = models.DateTimeField(default=datetime.now() +
                                                timedelta(days=60),
                                                blank=True)

    def is_active_recent(self):
        return self.published_at >= datetime.utcnow() - timedelta(days=60)

    def __str__(self):
        return f'{self.title} | {self.company} | {self.location}'
