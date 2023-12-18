from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import JobPosting


def index(request):
    active_postings = JobPosting.objects.filter(
        is_active=True).order_by('-published_at')
    context = {"job_posting": active_postings}
    return render(request, 'JobBoard/index.html', context)


def job_details(request, id):
    job_posting = get_object_or_404(JobPosting, id=id, is_active=True)
    context = {"posting": job_posting}
    return render(request, 'JobBoard/job_details.html', context)

