from rest_framework import serializers


class Dashboard(object):
    def __init__(self, new, going, next_event, unpaid):
        self.new_event = new
        self.going_event = going
        self.unpaid = unpaid
        self.next_event = next_event


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = "__all__"