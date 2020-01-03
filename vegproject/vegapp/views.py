from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect , HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader


from django.urls import reverse
from django.views import generic
from .models import Blog, MyForm

from vegapp.forms import MyForm


class IndexView(generic.ListView):
    template_name = 'index.html'
    
    def get_queryset(self):
        pass

class AboutView(generic.ListView):
    template_name = 'about.html'
    
    def get_queryset(self):
        pass

class BlogView(generic.ListView):
    template_name = 'blog.html'
    model = Blog
    
    def get_queryset(self) :
        queryset = Blog.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['blogdata_list'] = context['blog_list']
        # context['bdata'] = "kkkkkk"
        return context 

class ContactView(generic.ListView):
    template_name = 'contact.html'
    
    def get_queryset(self):
        pass



# def contactform(request):
#     form = MyForm()

#     return render(request, 'contactform.html', {'form':form});


# class ResponseForm(generic.ListView):
#     template_name = 'responseform.html'
    
#     def get_queryset(self):
#         pass

def responseform(request):
 #if form is submitted
    if request.method == 'POST':
        myForm_form = MyForm(request.POST)
        
        if myForm_form.is_valid():
            name = myForm_form.cleaned_data['name']
            email = myForm_form.cleaned_data['email']
            feedback = myForm_form.cleaned_data['feedback']
            
            context = {
            'name': name,
            'email': email,
            'feedback': feedback
            }

            myForm_form.save()

           

            # template = loader.get_template('thankyou.html')

            # return HttpResponse(template.render(context, request))

            



    else:
         form = MyForm()

    return render(request, 'responseform.html', {'form':form});