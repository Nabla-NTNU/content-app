from django.conf.urls import url
from .views import (
    AdministerRegistrationsView,
    calendar,
    UserEventView,
    RegisterUserView,
    EventDetailView,
    EventRegistrationsView,
    ical_event,
)
from .feeds import RecentEvents

urlpatterns = [
    url(r'^arrangement/(?P<pk>\d{1,8})/admin2$',
        AdministerRegistrationsView.as_view(),
        name='event_admin'),

    url(r'^arrangement/$',
        calendar,
        name='event_list'),

    url(r'^arrangement/(\d{4})/(\d{1,2})/$',
        calendar,
        name='event_list'),

    url(r'^mine/$',
        UserEventView.as_view(),
        name="view_user_events"),

    url(r'^arrangement/(?P<pk>\d{1,8})/registration$',
        RegisterUserView.as_view(),
        name='registration'),

    url(r'^arrangement/(?P<pk>\d{1,8})-(?P<slug>[-\w]*)$',
        EventDetailView.as_view(),
        name='event_detail'),

    url(r'^arrangement/reg/(?P<pk>\d{1,8})$',
        EventRegistrationsView.as_view(),
        name='event_registrations'),

    url(r'^arrangement/(?P<event_id>\d{1,8}).ics$',
        ical_event,
        name="ical_event"),

    url(r'^feed/$',
        RecentEvents(),
        name="event_feed"),
]