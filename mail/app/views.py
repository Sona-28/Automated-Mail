from re import U
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from mail.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
from .forms import EmailForm, AttForm, TempForm, UploadForm
from django.core.mail import EmailMessage
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.views import View
from .models import Upld

FILE_TYPES = ['csv']

def home(request):
    return render(request, 'home.html')

def sendMail(request):
    try:
        if request.method == 'POST':
            print('This is post')
            form = EmailForm(request.POST)
            if form.is_valid():
                print("Valid")
                form.send()
                print("Sent mail")
            return render(request, 'success.html')
        return render(request, 'index.html')
    except:
            print("Something is wrong")
            return render(request, 'error.html')

def upload(request):
    try:
        if request.method == 'POST':
            uploaded_file = request.FILES['formFile']
            file_data = uploaded_file.read().decode("utf-8")		
            lines = file_data.split("\n")
            for line in lines:
                line = line.strip()
                if not line:
                    continue						
                fields = line.split(",")
                data_dict = {}
                data_dict["id"] = fields[0]
                data_dict["name"] = fields[1]
                data_dict["email"] = fields[2]
                data_dict["inquiry"] = fields[3]
                data_dict["message"] = fields[4]
                list_1 = fields[2].split()
                html_msg=render_to_string('body.html')
                print(list_1)
                print(data_dict['message'])
                send_mail(data_dict['inquiry'], 
                data_dict['message'], EMAIL_HOST_USER, list_1, fail_silently = False)
                print("Mail sent")
            return render(request, 'success.html')
        return render(request, 'upload.html')
    except:
            print("Something is wrong")
            return render(request, 'error.html')

def Automated(request):
    # form_class = TempForm
    # def post(request):
    # try:
        if request.method == 'POST':
            print("Post")
            form = TempForm(request.POST, request.FILES)
            if form.is_valid():
                print("Valid")
                uploaded_file = request.FILES
                up_file = uploaded_file['formFile']
                # template_file = uploaded_file['template']
                template_file = str(request.FILES['template'])
                # print(render_to_string(template_file))
                file_data = up_file.read().decode("utf-8")		
                lines = file_data.split("\n")
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue						
                    fields = line.split(",")
                    data_dict = {}
                    data_dict["email"] = fields[0]
                    # ins = Email(data_dict['id'], data_dict['email'])
                    # ins.save()	
                    list_1 = fields[0].split()
                    html_message = render_to_string(template_file)
                    # plain_text= strip_tags(html_message)
                    send_mail('Automatic Email', 
                    "hi", EMAIL_HOST_USER, list_1, html_message=html_message)
                    print("Mail sent")
                return render(request, 'success.html')
            else:
                print("Not valid")
        return render(request, 'automated.html')
    # except:
    #     print("Something is wrong")
    #     return render(request, 'error.html')

class EmailAttachementView(View):
    form_class = AttForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'attach.html', {'email_form': form})

    def post(self, request, *args, **kwargs):
        try:
            form = self.form_class(request.POST, request.FILES)

            if form.is_valid():

                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                email = form.cleaned_data['email']
                files = request.FILES.getlist('attach')

                mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
                for f in files:
                    mail.attach(f.name, f.read(), f.content_type)
                mail.send()
                print("Mail sent")
                return render(request, 'success.html')
                
            return render(request, 'attach.html', {'email_form': form})
        except:
                print("Something is wrong")
                return render(request, 'error.html')

