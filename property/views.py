from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView , DetailView , CreateView
from .models import Property , Category ,Place
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

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        image_formset = PropertyImageFormset()
        return self.render_to_response(self.get_context_data(
            form=form,
            image_formset=image_formset,
        ))

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        image_formset = PropertyImageFormset(self.request.POST, self.request.FILES)
        
        if form.is_valid() and image_formset.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            
            new_category = form.cleaned_data.get('new_category')
            existing_category = form.cleaned_data.get('existing_category')
            new_place = form.cleaned_data.get('new_place')
            existing_place = form.cleaned_data.get('existing_place')
            
            if new_category:
                category_instance, created = Category.objects.get_or_create(name=new_category)
                myform.category = category_instance
            else:
                myform.category = existing_category
            
            if new_place:
                place_instance, created = Place.objects.get_or_create(name=new_place)
                myform.place = place_instance
            else:
                myform.place = existing_place
            
            myform.save()
            
            for image_form in image_formset:
                myform2 = image_form.save(commit=False)
                myform2.property = myform
                myform2.save()
                
            ### send gmail message
            
            return redirect(reverse('property:property_list'))
        else:
            return self.render_to_response(self.get_context_data(
                form=form,
                image_formset=image_formset,
            ))

