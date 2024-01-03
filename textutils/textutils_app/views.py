# Views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")


def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    count_chars = request.GET.get('count_chars', 'off')

    # Check which checkbox is on
    if removepunc == "on" and count_chars == "on":
    # Your code for removing punctuations and counting characters goes here
    # For example: 1,2,3
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = "".join([char for char in djtext if char not in punctuations])
        noofchars = len(analyzed)
        params = {'purpose': 'Removed Punctuations & Count Characters', 'analyzed_text': analyzed, 'no_of_characters': noofchars}
        return render(request, 'analyze.html', params)
    
   
    # for uppercase
    elif fullcaps=="on" and count_chars == "on":
        analyzed = ''.join([char.upper() for char in djtext])
        noofchars = len(analyzed)
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed, 'no_of_characters': noofchars}
        return render(request, 'analyze.html', params)
    
    # remove newlines in code
    elif newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n":
                analyzed=analyzed+char
                params = {'purpose': 'remove new lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif spaceremover=="on":
        # analyzed=''.join(djtext.split())
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        # Check if count_chars is also selected
        if count_chars == "on":
            noofchars = len(analyzed)
            params = {'purpose': 'Removed extra spaces and Counted Characters', 'analyzed_text': analyzed, 'no_of_characters': noofchars}
        else:
            params = {'purpose': 'Removed extra spaces', 'analyzed_text': analyzed}
        
        return render(request, 'analyze.html', params)
         
        # text_without_extra_spaces = ' '.join(djtext.split())
        #params = {'purpose': 'removed extra spaces', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
    
    else:
            return HttpResponse('Error')    

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")

