"""meteringdatabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import path, include
from metering_database import views

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('success', views.success, name = 'success'),
    path('submission', views.submission, name = 'submission'),
    path('new_submission', views.new_submission, name = 'new_submission'),
    path('welcome', views.welcome, name = 'welcome'),
    path('fillform', views.fillform, name = 'fillform'),
    path('newmeter', views.newmeter, name = 'newmeter'),
    path('querries',views.querries, name = 'querries'),
    path('homepage', views.homepage, name = 'homepage'),
    path('querriesback', views.querriesback, name = 'querriesback'),
    #path('create', v.create, name = 'create'),
    path('meterrecord', views.meterrecord, name = 'meterrecord'),
    path('sub_meterrecord', views.sub_meterrecord, name = 'sub_meterrecord'),
    path('standalone', views.standalone, name = 'standalone'),
    path('substation', views.substation, name = 'substation'),
    path('monthly_LP', views.monthly_LP, name = 'monthly_LP'),
    path('new_LP', views.new_LP, name = 'new_LP'),
    path('LP_plot', views.LP_plot, name = 'LP_plot'),
    path('umeme', views.umeme, name = 'umeme'),
    path('bill_gen', views.bill_gen, name = 'bill_gen'),
    path('hist_records', views.hist_records, name = 'hist_records'),
    path('bill_sub', views.bill_sub, name = 'bill_sub'),
    path('ipp', views.ipp, name = 'ipp'),
    path('ipp_insert', views.ipp_insert, name = 'ipp_insert'),
    path('meter_summary', views.meter_summary, name = 'meter_summary'),
    path('new_job', views.new_job, name = 'new_job'),
    path('store_newjob', views.store_newjob, name = 'store_newjob'),
    path('energy_loss', views.energy_loss, name = 'energy_loss'),
    path('ipp_analysis_month', views.ipp_analysis_month, name = 'ipp_analysis_month'),
    path('feeder_list', views.feeder_list, name='feeder_list'),
    path('ipp_feeder_list', views.ipp_feeder_list, name='ipp_feeder_list'),
    path('stand_feeder_list', views.stand_feeder_list, name='stand_feeder_list'),
    path('plotly_lp', views.plotly_lp, name='plotly_lp'),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('plotly_lp_one', views.plotly_lp_one, name='plotly_lp_one'),
    path('prometer', views.prometer, name='prometer'),
    path('prometer_100', views.prometer_100, name='prometer_100'),
    path('load_profile_cewe_prometer',views.load_profile_cewe_prometer,name='load_profile_cewe_prometer'),	
    path('config_file_page', views.config_file_page, name='config_file_page'),
    path('EM_details', views.EM_details, name='EM_details'), #ENERGY METER SEARCH AND QUERIES
    path('EM_sub_details', views.EM_sub_details, name='EM_sub_details'),#ENERGY QUERRY RETURNS
    path('EM_ipp_details', views.EM_ipp_details, name='EM_ipp_details'),
    path('EM_stand_details', views.EM_stand_details, name='EM_stand_details'),
    path('sub_node_report', views.sub_node_report, name='sub_node_report'),
    path('ipp_land_details', views.ipp_land_details, name='ipp_land_details'),

    path('update_node_details', views.update_node_details, name='update_node_details'),  #UPDATING EXISTING NODE
    path('update_form_I', views.update_form_I, name='update_form_I'),
    path('update_form_II', views.update_form_II, name='update_form_II'),
    path('update_form_III', views.update_form_III, name='update_form_III'),
    path('update_form_IV', views.update_form_IV, name='update_form_IV'),
    path('update_form_V', views.update_form_V, name='update_form_V'),

	#LANDIS MONTHLY FILES
    path('landis', views.landis, name='landis'),



    #AJAX CALLS

    path('sub_node_loss', views.sub_node_loss, name='sub_node_loss'),
    path('meter_update', views.meter_update, name='meter_update'),

      
     #IPP DISPATCH URLS
    path('ipp_dispatch_sub', views.ipp_dispatch_sub, name='ipp_dispatch_sub'),
    path('dispatch_success', views.dispatch_success, name='dispatch_success'),
    path('uetcl_dispatch_sub', views.uetcl_dispatch_sub, name='uetcl_dispatch_sub'),
    path('uetcl_dispatch_success', views.uetcl_dispatch_success, name='uetcl_dispatch_success'),
    path('schedule', views.schedule, name='schedule'),
   path('viewipp_schedule', views.viewipp_schedule, name='viewipp_schedule'),
    path('ippview_declared', views.ippview_declared, name='ippview_declared'),

   #ADDING NEW IPPS ONTO THE DISPATCH SCHEDULE
    path('new_ipp', views.new_ipp, name='new_ipp'),

    #CHANGE PASSWORD
    path('change_pw', views.change_pw, name='change_pw'),
    path('comfirm_change_pw', views.comfirm_change_pw, name='comfirm_change_pw'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
