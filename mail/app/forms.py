from dataclasses import field
from django import forms
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from .models import Temp, Mail, Upld, Att


def validate_file_extension(value):
        if not value.name.endswith('.html'):
            raise forms.ValidationError("Only HTML file is accepted")

class TempForm(forms.ModelForm):
    template = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}),validators=[validate_file_extension])
    class Meta:
        model = Temp
        fields = "__all__"
    
class AttForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    message = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = Att
        fields = "__all__"
    

class EmailForm(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    inquiry = forms.CharField(max_length=70)
    message = forms.CharField(widget=forms.Textarea)


    def get_info(self):
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        email = cl_data.get('email')
        subject = cl_data.get('inquiry')
        msg = cl_data.get('message')

        return subject, msg, email

    def send(self):
        subject, msg, email = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
    class Meta:
        model = Mail
        fields = ["name", "email", "inquiry", "message"]

class UploadForm(forms.ModelForm):
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    inquiry = forms.CharField(max_length=70)
    message = forms.CharField(widget=forms.Textarea)
    # file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


    def get_info(self):
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        email = cl_data.get('email')
        subject = cl_data.get('inquiry')
        msg = cl_data.get('message')

        return subject, msg, email

    def send(self):
        subject, msg, email = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
    class Meta:
        model = Upld
        fields ='__all__'