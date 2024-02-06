from django.shortcuts import render
from core.models import GeneralSetting, ImageSetting

# Create your views here.
def index(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameters
    side_keywords = GeneralSetting.objects.get(name='side_keywords').parameters
    site_description = GeneralSetting.objects.get(name='site_description').parameters
    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').parameters
    home_banner_title = GeneralSetting.objects.get(name='home_banner_title').parameters
    home_banner_description = GeneralSetting.objects.get(name='home_banner_description').parameters
    about_myself_wellcome = GeneralSetting.objects.get(name='about_myself_wellcome').parameters
    about_myself_footer = GeneralSetting.objects.get(name='about_myself_footer').parameters
    #images
    header_logo = ImageSetting.objects.get(name='header_logo').file
    home_banner_image = ImageSetting.objects.get(name='home_banner_image').file
    site_logo = ImageSetting.objects.get(name='site_logo').file
    context = {
        'site_title': site_title,
        'side_keywords': side_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'about_myself_wellcome': about_myself_wellcome,
        'about_myself_footer': about_myself_footer,
        'header_logo': header_logo,
        'home_banner_image': home_banner_image,
        'site_logo': site_logo,
    }
    return render(request, 'index.html', context=context)