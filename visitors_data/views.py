from django.shortcuts import render, redirect
from .models import Visitor
import qrcode
from .forms import VisitorForm
import cv2
import re
import base64
from IPython import embed

# Create your views here.

def home(request):
    context = {

    }
    return render(request, 'visitors_data/home.html', context)

# def create(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/form.html', context)

def citizen(request): # POST
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            # visitor = form.save()
            visitor = form.save()
            return redirect('visitors_data:confirm', visitor.pk)
    else:
        form = VisitorForm()
    context = {
        'form': form,
    }
    return render(request, 'visitors_data/citizen.html', context)

## https://docs.djangoproject.com/en/3.0/ref/contrib/messages/    => error message custom

def foreigner(request): # POST
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     number = request.POST.get('number')

    #     visitor = Visitor(name=name, number=number)
    #     visitor.save()
    
    #     return redirect('visitors_data:detail', visitor.pk)

    # else:
    context = {

    }
    return render(request, 'visitors_data/foreigner.html', context)

def confirm(request, pk):
    visitor = Visitor.objects.get(pk=pk)
    context = {
        'visitor': visitor,

    }
    
   
    return render(request, 'visitors_data/confirm.html', context)

def qr(request, pk):
    visitor = Visitor.objects.get(pk=pk)
    qr = qrcode.QRCode(version=2, error_correction=qrcode.constants.ERROR_CORRECT_H)
    info = visitor.name + '/' + visitor.number + '/' + 'PK:' + str(visitor.pk)
    qr.add_data(info)
    qr.make
    img = qr.make_image(fill_color='black', back_color='white')
    img.save('./static/images/qrcode.png', format='PNG')

    return render(request, 'visitors_data/qr.html')

# def read_qr(request):

#     # img = cv2.imread('./static/images/qrcode.png')
#     # detector = cv2.QRCodeDetector()
#     # data, bbox, straight_qrcode = detector.detectAndDecode(img)
    
#     # video

#     # initalize the cam

#     cap = cv2.VideoCapture(0)
#     # initialize the cv2 QRCode detector
#     detector = cv2.QRCodeDetector()
#     while True:
#         _, img = cap.read()
#         # detect and decode
#         data, bbox, _ = detector.detectAndDecode(img)
#         # check if there is a QRCode in the image
#         if bbox is not None:~
#             # display the image with lines
#             for i in range(len(bbox)):
#                 # draw all lines
#                 cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
#             if data:
#                 print("[+] QR Code detected, data:", data)
#                 cap.release()
#                 cv2.destroyAllWindows()
#         # display the result
#         cv2.imshow("img", img)    
#         if cv2.waitKey(1) == ord("q"):
#             break

#     # PK 추출
#     p = re.compile("P+K+[:]+[0-9]+")
#     pk_number = p.findall(data)[0]

#     p1 = re.compile("[0-9]+")
#     current_pk = p1.findall(pk_number)[0]

#     # DB 수정 (check='TRUE')
#     visitor = Visitor.objects.get(pk=current_pk)
#     visitor.check = "TRUE"
#     visitor.save()

#     context = {

#     }
#     return render(request, 'visitors_data/read_qr.html', context)

def read_qr(request):
    return render(request, 'visitors_data/read_qr.html')


def create_qr(request):
    personal_info = request.POST.get('content')

    p = re.compile("P+K+[:]+[0-9]+")
    pk_number = int(p.findall(personal_info)[0][3:])
    
    visitor = Visitor.objects.get(pk=pk_number)
    visitor.check = "TRUE"
    
    if visitor.check == "FALSE":
        print('신규 방문자')
        visitor.check = "TRUE"
        visitor.save()
    # 재방문자
    else:
        print('재방문자')
        visitor.save()

    return render(request, 'visitors_data/result.html')


def make_crop_image(request):
    return render(request, 'visitors_data/make_crop_image.html')


def get_crop_image(request, visitor_pk):
    crop_image = request.POST.get('image')
    # embed()
    # print(crop_image)

    visitor = Visitor.objects.get(pk=visitor_pk)
    visitor.image = crop_image
    visitor.save()
    context = {
        'visitor': visitor,
    }
    return render(request, 'visitors_data/get_crop_image.html')