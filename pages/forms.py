from django import forms




class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100,label='Your Name')
    email = forms.EmailField(required=False,label='Your e-mail address')
    #phonenumber = forms.CharField(max_length=15, required=False, label='Phone')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

