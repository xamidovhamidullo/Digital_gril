from django.urls import path
from main.views import *
from adminstrator.views import *
urlpatterns = [
     path("digital/", digital_view),
     path("direction/", direction_view),
     path('create-user/', create_user),
     path("get-question/", get_question_view),
     path("get_test/", get_test),
     path("create_result/", create_result),
     path("is_logic_directions/", is_logic_directions),
     path('create-user-answer/', create_user_answer),
     path("create-is-logic-question/", create_is_logic_question_view),
     path("logo/", digital_gril_view),
     path("profilo", profilo_view, name='profilo'),

]


