from django.contrib import admin

from club.models.event import Event, EventForm
from club.models.money import Money, MoneyForm
from club.models.outcome import Outcome, OutcomeForm
from club.models.user import Profile, ProfileForm

admin.site.register(Event, EventForm)
admin.site.register(Money, MoneyForm)
admin.site.register(Profile, ProfileForm)
admin.site.register(Outcome, OutcomeForm)