from django.shortcuts import render

from .models import Course
from .forms import ContactCourse

def courses(request):
	courses = Course.objects.all()
	context = {
		'courses':courses
	}
	return render(request, 'cursos.html', context)

def details(request, slug):
	course = Course.objects.get(slug=slug)
	context = {}
	if request.method == 'POST':
		form = ContactCourse(request.POST)
		if form.is_valid():
			context['is_valid'] = True
			form.send_mail(course)
			form = ContactCourse()
	else:
		form = ContactCourse()
	context['form'] = form
	context['course'] = course
	template_name = 'details.html'
	return render(request, template_name, context)
