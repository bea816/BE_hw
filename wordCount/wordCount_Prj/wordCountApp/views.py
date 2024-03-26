from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def wordCount(request):
    return render(request, "wordCount.html")

def result(request):
    entered_text = request.GET['fulltext'] #입력된 데이터(fulltext) 가져오기
    word_list = entered_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    word_num = len(entered_text)
    word_num_except_space = word_num - entered_text.count(' ')

    return render(request, "result.html", {'alltext': entered_text, 'dictionary': word_dictionary.items(), 'total': len(word_list), 'word_num': word_num, 'word_num_except_space': word_num_except_space})

def hello(request):
    name = request.GET['getName']
    return render(request, "hello.html", {'name': name})

