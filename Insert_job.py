# Insert_job.py

import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from JobBoard.models import JobPosting

jobs_data = [
    {
        "title": "Machine Learning Engineer",
        "description": "Join our cutting-edge machine learning team and contribute to the development of innovative AI solutions...",
        "location": "Sweden, Stockholm",
        "job_type": "Full-time",
        "company": "AI Innovations Co.",
        "salary": 95000,
        "is_active": True,
        "experience_required": "4+ years",
        "qualifications": "Master's or PhD in Computer Science or related field",
    },
    {
        "title": "Digital Marketing Manager",
        "description": "Lead our digital marketing efforts, devise strategies, and drive online visibility and engagement...",
        "location": "Spain, Barcelona",
        "job_type": "Full-time",
        "company": "Digital Impact Solutions",
        "salary": 70000,
        "is_active": True,
        "experience_required": "5+ years",
        "qualifications": "Bachelor's degree in Marketing or a related field",
    },
    {
        "title": "Business Intelligence Analyst",
        "description": "Transform data into actionable insights, drive data-driven decision-making, and enhance business performance...",
        "location": "United Kingdom, London",
        "job_type": "Contract",
        "company": "Insightful Analytics Ltd.",
        "salary": 80000,
        "is_active": True,
        "experience_required": "3+ years",
        "qualifications": "Bachelor's or Master's degree in Business Analytics or a related field",
    },
    {
        "title": "UX/UI Designer",
        "description": "Create engaging user experiences and visually appealing interfaces for our digital products...",
        "location": "Germany, Berlin",
        "job_type": "Full-time",
        "company": "Design Innovations GmbH",
        "salary": 85000,
        "is_active": True,
        "experience_required": "4+ years",
        "qualifications": "Bachelor's degree in Design or a related field",
    },
    {
        "title": "Financial Analyst",
        "description": "Conduct financial analysis, prepare reports, and provide insights to support strategic decisions...",
        "location": "Canada, Toronto",
        "job_type": "Full-time",
        "company": "Finance Excellence Corp.",
        "salary": 75000,
        "is_active": True,
        "experience_required": "3+ years",
        "qualifications": "Bachelor's degree in Finance or Accounting",
    },
    {
        "title": "Network Administrator",
        "description": "Manage and maintain our company's network infrastructure, ensuring optimal performance...",
        "location": "Australia, Sydney",
        "job_type": "Contract",
        "company": "Connectivity Solutions Pty Ltd.",
        "salary": 70000,
        "is_active": True,
        "experience_required": "2+ years",
        "qualifications": "Bachelor's degree in IT or a related field",
    },
    {
        "title": "Human Resources Coordinator",
        "description": "Support HR activities, coordinate recruitment processes, and contribute to a positive workplace culture...",
        "location": "Singapore",
        "job_type": "Part-time",
        "company": "HR Dynamics Inc.",
        "salary": 50000,
        "is_active": True,
        "experience_required": "1+ year",
        "qualifications": "Bachelor's degree in Human Resources or a related field",
    },
    {
        "title": "Sales Representative",
        "description": "Drive sales, build client relationships, and meet revenue targets for our innovative products...",
        "location": "France, Paris",
        "job_type": "Full-time",
        "company": "SalesPro Solutions",
        "salary": 60000,
        "is_active": True,
        "experience_required": "2+ years",
        "qualifications": "Bachelor's degree in Business or a related field",
    },
    {
        "title": "Customer Support Specialist",
        "description": "Provide excellent customer service, resolve inquiries, and ensure customer satisfaction...",
        "location": "India, Mumbai",
        "job_type": "Full-time",
        "company": "SupportTech Inc.",
        "salary": 55000,
        "is_active": True,
        "experience_required": "1+ year",
        "qualifications": "Bachelor's degree in a relevant field",
    },
]

for job_data in jobs_data:
    JobPosting.objects.create(**job_data)

print("Example job postings created successfully.")
