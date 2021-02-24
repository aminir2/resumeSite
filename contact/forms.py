from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'id': "form_email", 'type': "email", 'name': "email", 'class': "form-control",
               'required': "required"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Message', 'id': "form_message", 'name': "message", 'class': "form-control", 'rows': "7",
               'required': "required"}))
