from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request,'index.html')


from keras.models import load_model
from keras.preprocessing import image
import json
import numpy as np



def result(request):
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)
    testimage='.'+filePathName

    context = {
        'filePath': filePathName,
        'predictionLabel': testimage,
    }
    return render(request, 'result.html', context=context)