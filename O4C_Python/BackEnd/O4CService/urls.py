from django.conf.urls import url, include
from django.contrib import admin
#from django.conf.urls import include
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
from hacks.views import PiloList, EventList, EventOrganization, GroupsList, EventManage, GroupsCount, TTQ
from datas import views as dataviews
from tools import views as toolviews
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
#from rest_framework.authtoken import views
from rest_framework_expiring_authtoken import views

router = routers.DefaultRouter()
router.register('images', dataviews.MyUser, 'images')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pilots/ ', PiloList.as_view()),
    url(r'^hacks/', EventList.as_view()),
    url(r'^hack/(?P<ev_id>\d+)', EventManage.as_view()),
    url(r'^tags/', dataviews.TagList.as_view()),
    url(r'^suggestion/', dataviews.SuggestionManager.as_view()),
    url(r'^users/', dataviews.MyUser.as_view()),
    url(r'^user/(?P<event_id>\d+)', dataviews.NewUser.as_view()),
    url(r'^groups/', GroupsList.as_view()),
    url(r'^groupscount/', GroupsCount.as_view()),
    url(r'^register', dataviews.NewUser.as_view()),
    url(r'^reset/', dataviews.ManagingUser.as_view()),
    url(r'^datasets/', dataviews.DatasetList.as_view()),
    url(r'^dataset/(?P<data_id>\d+)', dataviews.DatasetListSelected.as_view()),
    url(r'^process/', toolviews.HackProcesList.as_view()),
    url(r'^proces/(?P<proces_id>\d+)', toolviews.HackProcesSelected.as_view()),
    url(r'^hacksubscribed/', EventOrganization.as_view()),
    url(r'^hacksubscribed/(?P<hack_id>\d+)', EventOrganization.as_view()),
    url(r'^tools/', toolviews.OutilList.as_view()),
    url(r'^tool/(?P<outil_id>\d+)', toolviews.OutilSelected.as_view()),
    url(r'^requettools/(?P<event_id>\d+)', toolviews.SelectedToolsForEvent.as_view()),
    url(r'^flipcards/', toolviews.FlipcardManger.as_view()),
    url(r'^flipTcards/(?P<category>\w+)', toolviews.FlipcardManger.as_view()),
    url(r'^project/', toolviews.ProjectManagers.as_view()),
    url(r'^projects/(?P<event_ID>\d+)', toolviews.ProjectManagers.as_view()),
    url(r'^myprojects/', toolviews.MyProjects.as_view()),
    url(r'^groupa/(?P<Gid>\d+)', TTQ.as_view()),
    url(r'^auth/', views.obtain_expiring_auth_token)
]


#urlpatterns = format_suffix_patterns(urlpatterns)
#in Prodction change the url to store files on a different server then the source code

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
