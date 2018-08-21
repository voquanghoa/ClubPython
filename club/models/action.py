from django import forms


class EventRegisterForm(forms.Form):
    event_id = forms.IntegerField(required=True, min_value=1)
    user_id = forms.IntegerField(required=True, min_value=1)


class MoneyRegisterForm(forms.Form):
    money_id = forms.IntegerField(required=True, min_value=1)
    user_id = forms.IntegerField(required=True, min_value=1)
