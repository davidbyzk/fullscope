from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin


from coffeehouse.items.urls import urlpatterns as items_url_patterns

urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='homepage.html'),name="homepage"),
    url(r'^about/', include('coffeehouse.about.urls',namespace="about")),
    url(r'^items/', include(items_url_patterns,namespace="items")),    
    url(r'^stores/',include('coffeehouse.stores.urls',namespace="stores")),
    url(r'^online/',include('coffeehouse.online.urls',namespace="online")),
    url(r'^social/',include('coffeehouse.social.urls',namespace="social")),        
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_framework.urls',namespace='rest_framework')),    
]
