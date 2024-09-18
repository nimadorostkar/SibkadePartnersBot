from django.urls import path
from accounts.views import Logout,Profile,Refresh,RefreshAccess,OverView,SendOTP,VerifyOTP,UserValidationView
from accounts.student_views import StudentLogin,StudentOverview,StudentInstituteData
from accounts.institute_views import InstituteOverview,Institute,InstituteStudent,ZarinpalMerchantID, InstituteStudentMultiple
from accounts.management_panel_view import InstituteLists,StudentLists,FreelanceLists
from accounts.visitors_views import InstituteLists as VisitList


urlpatterns = [
    path("otp", SendOTP.as_view(), name="send_otp"),
    path("otp/verify", VerifyOTP.as_view(), name="verify_otp"),
    path("refresh", Refresh.as_view(), name="refresh"),
    path("refresh-access", RefreshAccess.as_view(), name="refresh-access"),
    path("logout", Logout.as_view(), name="logout"),
    path("profile", Profile.as_view(), name="profile"),
    path("overview", OverView.as_view(), name="overview"),
    path("is-valid", UserValidationView.as_view(), name="is-valid"),
    #
    path("student-login", StudentLogin.as_view(), name="student-login"),
    path("student-overview", StudentOverview.as_view(), name="student-overview"),
    path("student-institute-data", StudentInstituteData.as_view(), name="student-institute-data"),
    #
    path("institute-overview", InstituteOverview.as_view(), name="institute-overview"),
    path("institute", Institute.as_view(), name="institute"),
    path("institute-student", InstituteStudent.as_view(), name="institute-student"),
    path("institute-student-multiple", InstituteStudentMultiple.as_view(), name="institute-student-multiple"),
    path("zp-id", ZarinpalMerchantID.as_view(), name="zp-id"),
    #
    path("institute-lists", InstituteLists.as_view(), name="institute-lists"),
    path("student-lists", StudentLists.as_view(), name="student-lists"),
    path("freelance-lists", FreelanceLists.as_view(), name="freelance-lists"),
    #
    path("visit", VisitList.as_view(), name="visit"),
]


