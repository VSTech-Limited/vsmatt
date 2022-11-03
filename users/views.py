from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import ImageUploadForm
from core.models import Language
from .models import Profile


# Create your views here.
@login_required
def profile(request):
    upload = ImageUploadForm(instance=request.user.profile)
    if request.method == 'POST':
        upload = ImageUploadForm(
            instance=request.user.profile,
            files=request.FILES
        )
        if upload.is_valid():
            cd = getCleanFormData(request)
            user_profile: Profile = upload.save(commit=False)
            user: User = request.user
            user.first_name = cd.get("first_name")
            user.last_name = cd.get("last_name")
            user.email = cd.get("email")
            user.save()
            user_profile.user = user
            user_profile.gender = cd.get("gender")
            user_profile.phone_number = cd.get("phone_number")
            user_profile.facebook_url = cd.get("facebook_url")
            user_profile.twitter_url = cd.get("twitter_url")
            user_profile.linkedin_url = cd.get("linkedin_url")
            user_profile.github_url = cd.get("github_url")
            user_profile.bio = cd.get("bio")
            # lang: Language = user_profile.languages
            # lang.name = cd.get('language')
            # lang.save()
            # user_profile.languages.add(lang)
            user_profile.save()
        else:
            print("-------------------------------------------------------------")
            print("eeror")

    return render(request, 'profile.html', {'upload': upload})


def getCleanFormData(request) -> dict:
    # todo Kindly validate the data received
    cleaned_data = {
        'first_name': request.POST.get("firstName"), 'last_name': request.POST.get("lastName"),
        'email': request.POST.get("email"), 'gender': request.POST.get("gender"),
        'phone_number': request.POST.get("phoneNumber"), 'facebook_url': request.POST.get("facebook_url"),
        'twitter_url': request.POST.get("twitter_url"), 'linkedin_url': request.POST.get("linkedin_url"),
        'github_url': request.POST.get("github_url"), 'bio': request.POST.get("bio"),
        'language': request.POST.get("language")
    }
    return cleaned_data
