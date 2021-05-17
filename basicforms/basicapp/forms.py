from django import forms
from django.core import validators




class FormName(forms.Form):
    name = forms.CharField(max_length=264)
    email = forms.EmailField()
    verifyemail = forms.EmailField(label='Enter Email Again')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verifyemail']

        if email != vmail:
            raise forms.ValidationError('Emails do not match')

    # botcatcher = forms.CharField(required=False,
    #                              widget=forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT")
    #     return botcatcher

    # def check_for_z(value):
    #     if value[0].lower() != 'z':
    #         raise forms.ValidationError("SHOULD START WITH Z")
