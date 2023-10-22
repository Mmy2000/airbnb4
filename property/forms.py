from django import forms
from django.forms.models import inlineformset_factory
from .models import PropertyImages , Property

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
        fields = ['rate','feedback']

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
    class Meta:
        model = Property
        exclude = ('slug','owner')