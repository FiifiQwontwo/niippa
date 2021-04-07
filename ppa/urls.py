from django.urls import path
from .views import *

app_name = 'ppa'

urlpatterns = [
    # list_urls
    # path('eventdates/', EventDateList.as_view(), name='event_date_list'),
    # path('events/', EventAttendanceList.as_view(), name='events_list'),
    # path('organisations/', OrganisationList.as_view(), name='organisation_list'),
    # path('member/', IndividualList.as_view(), name='participants_urls'),

    # details_urls
    # path('eventdates/<id>', EventDateDetail.as_view(), name='event_date_details'),
    # path('events/<id>', EventAttendanceDetail.as_view(), name='events_details '),
    # path('organisations/<id>', OrganisationDetail.as_view(), name='organisation_detail'),
    # path('member/<id>', IndividualDetail.as_view(), name='participants_details_urls'),

    # individual
    path('individuals/<pk>', IndividualViewSet.as_view({'get': 'retrieve', }), name='individuals_detail'),
    path('individuals/', IndividualViewSet.as_view({'get': 'list', }), name='individuals'),
    path('new_individuals/', IndividualViewSet.as_view({'post': 'create', }), name='new individuals'),
    path('individuals/<pk>/update', IndividualViewSet.as_view({'put': 'update', }), name='update_individual'),

    # Organisation
    path('organisation/<pk>', OrganisationViewSet.as_view({'get': 'retrieve', }), name='organisation_detail'),
    path('organisation/', OrganisationViewSet.as_view({'get': 'list', }), name='organisation'),
    path('new_organisation/', OrganisationViewSet.as_view({'post': 'create', }), name='new_organisations'),
    path('organisation/<pk>/update', OrganisationViewSet.as_view({'put': 'update', }), name='update_organisations'),

]
