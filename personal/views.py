from django.shortcuts import render


def index(request):
    return render(request, 'personal/home.html')


def test():
    return 2 * 3


def contact(request):
    return render(request, 'personal/basic.html', {'content1': [
        'If you want to contact me, please email me', 'email.gmail.com',
    ],
        'fromFunction': test()
    })
