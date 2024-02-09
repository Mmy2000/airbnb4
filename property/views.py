from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView , DetailView , CreateView
from .models import Property
from django.views.generic.edit import FormMixin
from .forms import PropertyBookForm , PropertyImageFormset , PropertyForm
from . filter import PropertyFilter
from django_filters.views import FilterView
from property.models import PropertyBook
from .forms import PropertyReviewForm
from django.urls import reverse
from property.models import PropertyBook , Property,PropertyReview
from property.forms import PropertyReviewForm
from django.contrib import messages




class PropertyList(FilterView):
    model = Property 
    paginate_by = 9
    filterset_class = PropertyFilter
    template_name = 'property/property_list.html'

    # filter

class PropertyDetail(FormMixin , DetailView):
    model = Property
    form_class = PropertyBookForm


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = Property.objects.filter(category=self.get_object().category)[:2]
        context["reviews"] = PropertyReview.objects.filter(property=self.get_object().id , status=True)
        return context
    
    
    
    def post(self , request , *args , **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.property= self.get_object()
            myform.user = request.user
            myform.save()

            return redirect('/')

class AddListing(CreateView):
    model = Property
    form_class = PropertyForm


    def get(self , request , *args , **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        image_formset = PropertyImageFormset
        return self.render_to_response(self.get_context_data(
            form = form , 
            image_formset = image_formset ,
        ))

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        image_formsets = PropertyImageFormset(self.request.POST , self.request.FILES)
        if form.is_valid() and image_formsets.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            room = Property.objects.get(id=myform.id)
            for form in image_formsets:
                myform2 = form.save(commit = False)
                myform2.property = room
                myform2.save()

            ### send gmail message

            return redirect(reverse('property:property_list'))

