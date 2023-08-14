from django.urls import path
from .views import TransactionView, TransformationBlockView, TransformProcess

urlpatterns = [
    path('transactions/', TransactionView.as_view(), name='transaction-list'),
    path('transformationBlock/', TransformationBlockView.as_view(),
         name='transformationBlock-list'),
    path('process/', TransformProcess.as_view(), name='transformation-process'),
]
