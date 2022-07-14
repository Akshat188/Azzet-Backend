from django.urls import path
from .views import *
app_name = 'core'
urlpatterns = [
	path('login/',login,name='login'),
	path('signup/',signUp,name='signup'),
	path('contests/',getAllLiveContests),
	path('join/',joinContest),
	path('trade/',Trade)
]