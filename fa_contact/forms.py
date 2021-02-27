from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام کامل خود را وارد کنید'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'ایمل خود را وارد کنید', 'id': "form_email", 'type': "email", 'name': "email", 'class': "form-control",
               'required': "required"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'موضوع را وارد کنید'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'پیام شما', 'id': "form_message", 'name': "message", 'class': "form-control", 'rows': "7",
               'required': "required"}))
