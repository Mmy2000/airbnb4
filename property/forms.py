from django import forms
from django.forms.models import inlineformset_factory
from .models import PropertyImages , Property , Category , Place

from .models import PropertyBook , PropertyReview

class PropertyBookForm(forms.ModelForm):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'id':'checkin_date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'id':'checkin_date'}))
    class Meta:
        model = PropertyBook
        fields = ['date_from' , 'date_to' , 'guest' , 'children']


class PropertyReviewForm(forms.ModelForm):
    class Meta:
        model = PropertyReview
        fields = ['subject','review','rating']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImages
        fields = ['property' , 'image']

PropertyImageFormset = inlineformset_factory(
    Property , 
    PropertyImages , 
    form = PropertyImageForm ,
    fields = ['image'],
    extra=2 , 
    can_delete=True,
)


class PropertyForm(forms.ModelForm):
    new_category = forms.CharField(required=False)
    existing_category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    new_place = forms.CharField(required=False)
    existing_place = forms.ModelChoiceField(queryset=Place.objects.all(), required=False)

    class Meta:
        model = Property
        exclude = ('slug', 'owner', 'category', 'place')

    def clean(self):
        cleaned_data = super().clean()
        new_category = cleaned_data.get('new_category')
        existing_category = cleaned_data.get('existing_category')
        new_place = cleaned_data.get('new_place')
        existing_place = cleaned_data.get('existing_place')
        
        if new_category and existing_category:
            raise forms.ValidationError("Please enter either a new category or select an existing category, not both.")
        
        if not new_category and not existing_category:
            raise forms.ValidationError("Please provide a category.")
        
        if new_place and existing_place:
            raise forms.ValidationError("Please enter either a new place or select an existing place, not both.")
        
        if not new_place and not existing_place:
            raise forms.ValidationError("Please provide a place.")
        
        return cleaned_data