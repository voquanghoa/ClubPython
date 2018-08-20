from django import forms


class RegisterForm(forms.Form):
    event_id = forms.IntegerField(required=True, min_value=1)
    user_id = forms.IntegerField(required=True, min_value=1)

