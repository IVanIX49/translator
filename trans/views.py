from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import argostranslate.package
import argostranslate.translate
from django.http import JsonResponse, HttpResponse
from .forms import MyForm
import threading
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):

    context = ' '
    dir = {'title': 'Переводчик', 'context': context}
    if request.method == "POST":
        # в будущем можно будет писать свой текст
        context = request.POST.get('text')
        from_code = request.POST.get('language')
        print(f'{from_code} - на каком языке')
        to_code = request.POST.get('text_to')
        print(f'{to_code} - текст перевода')

        argostranslate.package.update_package_index()
        available_packages = argostranslate.package.get_available_packages()
        package_to_install = next(
            filter(
                lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
            )
        )
        argostranslate.package.install_from_path(package_to_install.download())
        translatedText = argostranslate.translate.translate(context, from_code, to_code)


        return JsonResponse({'translatedText': translatedText}, safe=False)


    return render(request,'trans/index.html', dir)







def new(request):
    context = 'Здарова, отец'

    to_code = "en"

    # argostranslate.package.update_package_index()
    # available_packages = argostranslate.package.get_available_packages()
    # package_to_install = next(
    #     filter(
    #         lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    #     )
    # )
    # argostranslate.package.install_from_path(package_to_install.download())
    # translatedText = argostranslate.translate.translate(context, from_code, to_code)


    return render(request,'trans/new.html')

