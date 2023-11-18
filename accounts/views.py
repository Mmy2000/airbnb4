from django.shortcuts import render , redirect , get_object_or_404
from .forms import SignupForm , UserForm , ProfileForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login 
from property.models import PropertyBook , Property,PropertyReview
from property.forms import PropertyReviewForm
from django.contrib import messages




def signup(request):
    if request.method == "POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
            usernames = form.cleaned_data['username']
            passwords = form.cleaned_data["password1"]
            user = authenticate(username=usernames,password=passwords)
            login(request,user)

            return redirect('/account/profile')
            
    else:
        form=SignupForm()

    return render(request,'registration/signup.html',{'form':form})



def profile(request):
    profile=Profile.objects.get(user=request.user)

    return render(request,'profile/profile.html',{'profile':profile})


def edit_profile(requset):
    profile = Profile.objects.get(user=requset.user)
    if requset.method == "POST":
        user_form = UserForm(requset.POST , instance=requset.user)
        profile_form = ProfileForm(requset.POST,requset.FILES,instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            myprofile = profile_form.save(commit=False)
            myprofile.user = requset.user
            myprofile.save()
            return redirect('/accounts/profile')
    else:
        user_form = UserForm(instance=requset.user)
        profile_form = ProfileForm(instance=profile)

    return render(requset,'profile/profile_edit.html',{
        'user_form':user_form,
        'profile_form':profile_form
    })

def myreservation(request):
    property_list = PropertyBook.objects.filter(user=request.user)
    return render(request , 'profile/reservation.html',{'property_list':property_list})

def mylisting(request):
    property_list = Property.objects.filter(owner=request.user)
    return render(request , 'profile/mylisting.html',{'property_list':property_list})



def submit_review(request,property_id):
    url = request.META.get('HTTP_REFERER')
    if request.method =="POST":
        try:
            reviews = PropertyReview.objects.get(user__id=request.user.id , property_id=property_id)
            form = PropertyReviewForm(request.POST , instance=reviews)
            form.save()
            messages.success(request,'Thank You , Your Review has been updated.')
            return redirect(url)
        except PropertyReview.DoesNotExist:
            form = PropertyReviewForm(request.POST)
            if form.is_valid():
                data = PropertyReview()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.property_id = property_id
                data.user_id = request.user.id
                data.save()
                messages.success(request,'Thank You , Your Review has been submitted.')
                return redirect(url)
    return render(request,'profile/property_feedback.html')