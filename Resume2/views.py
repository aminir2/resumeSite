from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from contact.models import ContactModel, ContactInfo
from contact.forms import ContactForm
from index_page.models import *
from about_me.models import *
from skills.models import *
from blog.models import *


# class index_page(TemplateView):
#
#     def get(self, request, *args, **kwargs):
#         jobs_data = []
#         all_info = IndexPage.objects.first()
#         all_jobs = Jobs.objects.all()
#         about = AboutPage.objects.first()
#         doing_data = []
#         doing_data2 = []
#         doings = Doing.objects.all()
#         doings2 = Doing2.objects.all()
#         code_data = []
#         design_data = []
#         knowledge_data = []
#         education_data = []
#         experience_data = []
#         post_data = []
#         codes = CodeSkill.objects.all()
#         designs = DesignSkill.objects.all()
#         knowledges = Knowledge.objects.all()
#         educations = Education.objects.all()
#         experiences = Experience.objects.all()
#         # blog page
#         posts = BlogPost.objects.filter(active=True)
#         # contact form
#         contact_form = ContactForm(request.POST)
#         if contact_form.is_valid():
#             fullname = contact_form.cleaned_data.get('fullname')
#             email = contact_form.cleaned_data.get('email')
#             subject = contact_form.cleaned_data.get('subject')
#             message = contact_form.cleaned_data.get('message')
#             ContactModel.objects.create(fullname=fullname, email=email, message=message, subject=subject, is_read=False)
#             if message is None:
#                 contact_form.add_error('message', 'نام فیلم را وارد کنید')
#             elif email is None:
#                 contact_form.add_error('email', 'ایمیل خود را وارد کنید')
#             elif fullname is None:
#                 contact_form.add_error('fullname', 'نام خود را وارد کنید')
#             elif subject is None:
#                 contact_form.add_error('subject', 'نام خود را وارد کنید')
#             else:
#                 return redirect("/sent")
#             # # todo : show user a success message
#             contact_form = ContactForm()
#
#         for education in educations:
#             education_data.append({
#                 'year': education.year,
#                 'what': education.what,
#                 'where': education.where,
#                 'description': education.description,
#             })
#
#         for experience in experiences:
#             experience_data.append({
#                 'year': experience.year,
#                 'what': experience.what,
#                 'where': experience.where,
#                 'description': experience.description,
#             })
#
#         for knowledge in knowledges:
#             knowledge_data.append({
#                 'name': knowledge.name,
#             })
#         for design in designs:
#             design_data.append({
#                 'title': design.title,
#                 'number': design.number,
#             })
#         for code in codes:
#             code_data.append({
#                 'title': code.title,
#                 'number': code.number,
#             })
#         for doing in doings:
#             doing_data.append({
#                 'flag': doing.flag,
#                 'title': doing.title,
#                 'description': doing.description,
#             })
#         for doing in doings2:
#             doing_data2.append({
#                 'flag': doing.flag,
#                 'title': doing.title,
#                 'description': doing.description,
#             })
#
#         context = {
#             'posts': posts,
#             'jobs': all_jobs,
#             'setting_data': all_info,
#             'doings': doing_data,
#             'doings2': doing_data2,
#             'about': about,
#             'code': code_data,
#             'design': design_data,
#             'names': knowledge_data,
#             'educations': education_data,
#             'experiences': experience_data,
#             'form': contact_form,
#         }
#
#         return render(request, 'index.html', context)

# contact_form = ContactForm(request.POST or None)
# if contact_form.is_valid():
#     fullname = contact_form.cleaned_data.get('fullname')
#     email = contact_form.cleaned_data.get('email')
#     subject = contact_form.cleaned_data.get('subject')
#     message = contact_form.cleaned_data.get('message')
#     ContactModel.objects.create(fullname=fullname, email=email, subject=subject, message=message)

def All(request):
    jobs_data = []
    all_info = IndexPage.objects.first()
    all_jobs = Jobs.objects.all()
    about = AboutPage.objects.first()
    doing_data = []
    doing_data2 = []
    doings = Doing.objects.all()
    doings2 = Doing2.objects.all()
    code_data = []
    design_data = []
    knowledge_data = []
    education_data = []
    experience_data = []
    post_data = []
    codes = CodeSkill.objects.all()
    designs = DesignSkill.objects.all()
    knowledges = Knowledge.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    # blog page
    posts = BlogPost.objects.filter(active=True)
    # contact form
    contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
        fullname = contact_form.cleaned_data.get('fullname')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        message = contact_form.cleaned_data.get('message')
        ContactModel.objects.create(fullname=fullname, email=email, message=message, subject=subject, is_read=False)
        if message is None:
            contact_form.add_error('message', 'نام فیلم را وارد کنید')
        elif email is None:
            contact_form.add_error('email', 'ایمیل خود را وارد کنید')
        elif fullname is None:
            contact_form.add_error('fullname', 'نام خود را وارد کنید')
        elif subject is None:
            contact_form.add_error('subject', 'نام خود را وارد کنید')
        else:
            return redirect("/sent")
        # # todo : show user a success message
        contact_form = ContactForm()

    info = ContactInfo.objects.first()
    for education in educations:
        education_data.append({
            'year': education.year,
            'what': education.what,
            'where': education.where,
            'description': education.description,
        })

    for experience in experiences:
        experience_data.append({
            'year': experience.year,
            'what': experience.what,
            'where': experience.where,
            'description': experience.description,
        })

    for knowledge in knowledges:
        knowledge_data.append({
            'name': knowledge.name,
        })
    for design in designs:
        design_data.append({
            'title': design.title,
            'number': design.number,
        })
    for code in codes:
        code_data.append({
            'title': code.title,
            'number': code.number,
        })
    for doing in doings:
        doing_data.append({
            'flag': doing.flag,
            'title': doing.title,
            'description': doing.description,
        })
    for doing in doings2:
        doing_data2.append({
            'flag': doing.flag,
            'title': doing.title,
            'description': doing.description,
        })

    context = {
        'posts': posts,
        'jobs': all_jobs,
        'setting_data': all_info,
        'doings': doing_data,
        'doings2': doing_data2,
        'about': about,
        'code': code_data,
        'design': design_data,
        'names': knowledge_data,
        'educations': education_data,
        'experiences': experience_data,
        'form': contact_form,
        'info': info,
    }

    return render(request, 'index.html', context)


def Fa_All(request):
    jobs_data = []
    all_info = IndexPage.objects.first()
    all_jobs = Jobs.objects.all()
    about = AboutPage.objects.first()
    doing_data = []
    doing_data2 = []
    doings = Doing.objects.all()
    doings2 = Doing2.objects.all()
    code_data = []
    design_data = []
    knowledge_data = []
    education_data = []
    experience_data = []
    post_data = []
    codes = CodeSkill.objects.all()
    designs = DesignSkill.objects.all()
    knowledges = Knowledge.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    # blog page
    posts = BlogPost.objects.filter(active=True)
    # contact form
    contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
        fullname = contact_form.cleaned_data.get('fullname')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        message = contact_form.cleaned_data.get('message')
        ContactModel.objects.create(fullname=fullname, email=email, message=message, subject=subject, is_read=False)
        if message is None:
            contact_form.add_error('message', 'نام فیلم را وارد کنید')
        elif email is None:
            contact_form.add_error('email', 'ایمیل خود را وارد کنید')
        elif fullname is None:
            contact_form.add_error('fullname', 'نام خود را وارد کنید')
        elif subject is None:
            contact_form.add_error('subject', 'نام خود را وارد کنید')
        else:
            return redirect("/sent")
        # # todo : show user a success message
        contact_form = ContactForm()

    info = ContactInfo.objects.first()
    for education in educations:
        education_data.append({
            'year': education.year,
            'what': education.what,
            'where': education.where,
            'description': education.description,
        })

    for experience in experiences:
        experience_data.append({
            'year': experience.year,
            'what': experience.what,
            'where': experience.where,
            'description': experience.description,
        })

    for knowledge in knowledges:
        knowledge_data.append({
            'name': knowledge.name,
        })
    for design in designs:
        design_data.append({
            'title': design.title,
            'number': design.number,
        })
    for code in codes:
        code_data.append({
            'title': code.title,
            'number': code.number,
        })
    for doing in doings:
        doing_data.append({
            'flag': doing.flag,
            'title': doing.title,
            'description': doing.description,
        })
    for doing in doings2:
        doing_data2.append({
            'flag': doing.flag,
            'title': doing.title,
            'description': doing.description,
        })

    context = {
        'posts': posts,
        'jobs': all_jobs,
        'setting_data': all_info,
        'doings': doing_data,
        'doings2': doing_data2,
        'about': about,
        'code': code_data,
        'design': design_data,
        'names': knowledge_data,
        'educations': education_data,
        'experiences': experience_data,
        'form': contact_form,
        'info': info,
    }

    return render(request, 'fa-index.html', context)


def sent(request):
    return render(request, 'sent.html')
