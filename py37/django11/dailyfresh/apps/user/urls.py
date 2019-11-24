from django.conf.urls import url
# 函数视图方式
# from user import views
# 类视图方式
from user.views import RegisterView,ActiveView,LoginView

urlpatterns = [
    # 函数视图方式
    # url(r'^register$', views.register, name='register'), # 注册
    # url(r'^register_handle$', views.register_handle, name='register_handle')
    # 类视图方式
    url(r'^register$', RegisterView.as_view(), name='register'),
    url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),
    url(r'^login$', LoginView.as_view(), name="login")
]



