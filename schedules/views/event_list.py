from django.views.generic import ListView

from schedules.models import Event


class AllEventsListView(ListView):
    """ All event list views """

    template_name = "schedules/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_all_events(user=self.request.user)


class RunningEventsListView(ListView):
    """ Running events list view """

    template_name = "schedules/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_running_events(user=self.request.user)
