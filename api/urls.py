from django.conf.urls.static import static
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

from Rareeram import settings
from . import views
from .views import LoginView
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from rest_framework.routers import DefaultRouter

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
router = DefaultRouter()
urlpatterns = [
                #   path('hello/', views.HelloView.as_view(), name='hello'),  # for testing
                    path('login/', views.LoginView),   
                                 #   # path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
                #   path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
                  path('test-api/', views.testapi.as_view(), name='register'),  # for testing
                path('register/dealer/', views.DealerRegisterView.as_view(), name='auth_register'),
                #   path('register/scientist/', views.ScientistRegisterView.as_view(), name='auth_register'),
                #   path('register/farmer/', views.FarmerRegisterView.as_view(), name='auth_register'),
                #   path('zone/', views.ZoneView.as_view(), name='api_zone'),
                #   path('district/', views.DistrictView.as_view(), name='api_district'),
                #   path('block/', views.BlockView.as_view(), name='api_block'),
                #   path('krishi-bhavan/', views.KrishiBhavanView.as_view(), name='api_krishi_bhavan'),
                #   path('college/', views.CollegeView.as_view(), name='api_college'),
                #   path('department/<int:college_id>', views.DepartmentByCollegeIdView.as_view(),
                #        kwargs=dict(model=models.Department), name='api_department_by_college_id'),
                #   path('department/', views.DepartmentView.as_view(), name='api_department'),
                #   path('ticket/generate/', views.TicketGenerateView.as_view(), name='api_ticket_generate'),
                #   path('upload/', views.ImageViewSet.as_view(), name='upload'),
                #   path('farmer-type/', views.FarmerTypeView.as_view(), name='farmer_type'),
                #   path('crop-type/', views.CropTypeView.as_view(), name='crop_type'),
                #   path('disease-type/', views.DiseaseTypeView.as_view(), name='disease_type'),
                #   path('notification/', views.TickeNotificationView.as_view(), name='notification'),
                #   path('ticket-images/<int:pk>', views.TicketImagesViewSet.as_view(), name='ticket_details'),
                #   path('ticket-update/<int:pk>', views.TicketUpdateViewSet.as_view(), name='ticket_update'),
                #   path('create-followup/', views.CreateFollowUp.as_view(), name='create_followup'),
                #   path('ticket-followup/<int:pk>', views.TicketFollowUpsViewSet.as_view(), name='ticket_followup'),
                #   path('krishibhavan-tickets/<int:pk>', views.KrishiBhavanTicketsViewSet.as_view(), name='krishibhavan_ticket'),
                #   path('search/<int:user_id>/<str:user_type>/<str:query>', views.SearchViewSet.as_view(), name='search'),
                #   path('devices', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'),
                #   path('get-announcement/<int:user_id>', GetAnnouncementView.as_view(), name='get_announcement'),
                #   path('get-cat/', GetCategoryView.as_view(),name='get_category'),
                #   # path('fgtpsswd/',restapi.as_view(), name="reset_password"),
                #   path('getImagesForGallery', views.GetGalleryView.as_view(),name='get_gallery'),
                #   path('fgtpsswd/',restapi.as_view(), name="reset_password"),
                #   path('reset_password_fn/', views.resetpassword.as_view(), name="resetpassword"),
                #   path('reset_password/<str:username>',views.PasswordReset.as_view(), name="PasswordReset"),

               #    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
               #    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
               #    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

                  # path('device-token/update/', views.UpdateDeviceTokenViewSet.as_view(), name='update_device_token'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

