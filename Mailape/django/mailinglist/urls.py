from django.urls import path

from mailinglist import views

app_name = 'mailinglist'

urlpatterns = [
    path('<uuid:pk>/delete', views.DeleteMailingListView.as_view(), name='delete_mailinglist'),
    path('<uuid:pk>/manage', views.MailingListDetailView.as_view(), name='manage_mailinglist'),
    path('<uuid:pk>/subscribe', views.SubscribeToMailingListView.as_view(), name='subscribe'),
    path('<uuid:pk>/thankyou', views.ThankYouForSubsribingView.as_view(), name='subscriber_thankyou'),
    path('subscibe/confirmation/<uuid:pk>', views.ConfirmSubsriiptionView.as_view(), name='confirm_subscription'),
    path('unsubscribe/<uuid:pk>', views.UnsubscribeView.as_view(), name='unsubscribe'),
    path('<uuid:pk>/message/new', views.CreateMessageView.as_view(), name='create_message'),
    path('message/<uuid:pk>', views.MessageDetailView.as_view(), name='view_message'),
    path('new', views.CreateMailingListView.as_view(), name='create_mailinglist'),
    path('', views.MailingListListView.as_view(), name='mailinglist_list'),
]