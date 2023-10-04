"""
Project Name    :   Crime Investigation System

Group Members   :   Nikhil Kiran Patkal
                    Kanifnath Adinath Ghanwat
                    Aniket Bhanudas Bhise

Start Date      :   11/04/2023

Complete Date   :   10/05/2023


Project Set-up Commands:

1)  Create environment      :   py -m venv env
2)  Environment activate    :   env\scripts\activate
3)  Install Djano           :   py -m pip install Django   or   pip install django
4)  Create project          :   django-admin startproject crimeproject
5)  Go in Project           :   cd crimeproject
6)  Create app              :   python manage.py startapp crimeapp
7)  Run project             :   py manage.py runserver
8)  Make migrations         :   py manage.py makemigrations
9)  Migrate                 :   py manage.py migrate
10) Create admin panel      :   python manage.py createsuperuser


Admin Credentials
ID              :   Project@123
Pass            :   12345

"""

from audioop import reverse
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from flask import Response   # , authenticate, login
from crimeapp.forms import UserForm
from datetime import date
from django.contrib.auth.models import User


from django.http import HttpResponse
from django.views.generic import View

from crimeapp import models

from .models import UserFeedback, policestationreg, demo, slidermodel,station_register, saveuserModel, savepolicestationModel, fir_register, GraphType,card_img,printed_gallary1, PhotoGallery, OnlineComplaint,greeting_message, UserCharCertificateData1,UserRegistration,insert_staff,PublicAlert,missing



# import mysql.connector
# con=mysql.connector.connect(host="localhost",user="root",password="",port="3306",database="collegeproject",charset="utf8mb4")
       

'''con = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='collegeproject',
                              charset='utf8mb4')
'''


# Create your views here.
def home(req):
    if(req.session.has_key('page_refresh')):
        req.session['page_refresh']=req.session['page_refresh']+1
    else:
        req.session['page_refresh']=1
    #del req.session['page_refresh'] it use to delet the record of session
    print('user visite home page ',req.session['page_refresh'])
    sliders = slidermodel.objects.all()
    logo = demo.objects.all()
    card= greeting_message.objects.all()
    # people = UserCharCertificateData.objects.raw("SELECT Date_time FROM UserCharCertificateData where char_adhar='wwww'")
    # print("Hello Datatime: ",people)
    obj = {'slider_list':sliders, 'logo1':logo,'card':card}
    return render(req,'home.html',obj)


def station_register(req):
    return render(req,'station_register.html')


# Officer Login form

def officer_login(req):
    return render(req, 'officer_login.html')

# Officer gegistration form
def officer_reg_html(request):
    return render(request, 'officer_registration.html')


# Officer registration save
def save_officer_login(req):
    newuser=saveuserModel(
          user_name=req.POST.get('user_name'),
          user_age=req.POST.get('user_age'),
          user_add=req.POST.get('user_add')
    )
    newuser.save()
    return HttpResponse("<script>alert('save user');location.href='/'</script>")


# Police station registration form
def station_reg_html(req):
    return render(req, 'station_register.html')


# Police station regisration form save
def station_reg(req):
    newuser1=savepolicestationModel(
        st_name=req.POST.get('st_name'),
        st_id=req.POST.get('st_id'),
        st_pass=req.POST.get('st_pass'),
        st_con_pass=req.POST.get('st_con_pass'),
        st_address=req.POST.get('st_address')
    )
    newuser1.save()
    return HttpResponse("<script>alert('save user');location.href='/station_reg_html'</script>")


# Police station Login form
def st_login(req):
    return render(req,'police_station_login.html')


# Police station Login validations
def login_process(request):
    global st_id1
    st_id1 = request.POST.get('st_id')
    st_pass1 = request.POST.get('st_pass')
    count = savepolicestationModel.objects.filter(st_id=st_id1,st_pass=st_pass1).count()
    print(count)
    if count > 0:
        #mydata1 = savepolicestationModel.objects.filter(st_id=st_id1)
        mydata = savepolicestationModel.objects.filter(st_id=st_id1).values()
        obj={'key':mydata}
        # sliders = slidermodel.objects.all()
        # logo = demo.objects.all()
        # obj = {'slider_list':sliders, 'logo1':logo}
        return render(request, 'police_home.html',obj)
    else:
        return HttpResponse("<script>alert('Login failed...! Incorrect Credincials...?');location.href='/st_login'</script>")

def criminal_back(req):
    print("the global value",st_id1)
    print(st_id1)
    mydata = savepolicestationModel.objects.filter(st_id=st_id1).values()
    obj={'key':mydata}
    return render(req,'police_home.html',obj)


# Fir registartion form
def fir_reg(req):
    return render(req,"fir_reg.html")


# Fir registration form save
def save_fir_reg(req):
    fir_adhar = req.POST.get('fir_adhar')
    print(fir_adhar)
    newuser1=fir_register(
        fir_date=date.today(),
        fir_police_station=req.POST.get('fir_policstation_name'),
        fir_id = req.POST.get('fir_id'),
        fir_adhar = req.POST.get('fir_adhar'),
        fir_fullname = req.POST.get('fir_fullname'),
        fir_age = req.POST.get('fir_age'),
        fir_gender = req.POST.get('fir_gender'),
        fir_phone = req.POST.get('fir_phone'),
        fir_address = req.POST.get('fir_address'),
        fir_register_by= req.POST.get('fir_register_by'),
        fir_photo = req.POST.get('fir_photo'),
        fir_type = req.POST.get('fir_type'),
        fir_subject = req.POST.get('fir_subject')
    )
    newuser1.save()
    return HttpResponse("<script>alert('FIR register successfully...');location.href='/fir_reg'</script>")





# View criminal html file
def view_criminal(req):
    return render(req,'view_criminals.html')


# Criminal search validation
def criminal_search(req):
    id = req.POST.get('search')
    mydata = fir_register.objects.filter(fir_id=id).values()
    print(id)
    mydata1 = fir_register.objects.filter(fir_id=id)
    if mydata1:
        print("hello")
        obj={'key':mydata}
        return render(req,'view_criminals.html',obj)
    else:
        return HttpResponse("<script>alert('FIR is not found...?');location.href='/view_criminal'</script>")


# Show all criminal list
def all_criminal(req):
    data=fir_register.objects.all()
    obj={'key':data}
    return render(req,'view_criminals.html',obj)

def generate_pdf(req):
    return render(req,"generate_pdf.html")

def delete(req,fir_id):
    rec_delete=fir_register.objects.get(fir_id=fir_id)
    rec_delete.delete()
    return render(req,'view_criminals.html')

def update(req,fir_id):
    rec_update=fir_register.objects.get(fir_id=fir_id)
    return render(req,"update.html",{'rec_update':rec_update})


def do_update(req,fir_id):
    fir_adhar_new = req.POST['fir_adhar']
    fir_fullname_new = req.POST['fir_fullname']
    fir_age_new = req.POST.get('fir_age')
    fir_gender_new = req.POST.get('fir_gender')
    fir_phone_new = req.POST.get('fir_phone')
    fir_address_new = req.POST.get('fir_address')
    fir_register_by_new= req.POST.get('fir_register_by')
    fir_photo_new = req.POST.get('fir_photo')
    fir_type_new = req.POST.get('fir_type')
    fir_subject_new = req.POST.get('fir_subject')
    
    fir=fir_register.objects.get(fir_id=fir_id)
    fir.fir_adhar=fir_adhar_new
    fir.fir_fullname= fir_fullname_new
    fir.fir_age =fir_age_new 
    fir.fir_gender=fir_gender_new
    fir.fir_phone=fir_phone_new
    fir.fir_address=fir_address_new
    fir.fir_register_by=fir_register_by_new
    fir.fir_photo=fir_photo_new
    fir.fir_type=fir_type_new
    fir.fir_subject=fir_subject_new
    fir.save()
    return redirect("/all_criminal/")


def more(req,fir_id):
    info_data=fir_register.objects.get(fir_id=fir_id)
    return render(req,'more.html',{'info_data':info_data})


# Graphical view
def graph_data(req):
    entity = req.POST.get('entity')
    graph_type = req.POST.get('graph_type')

    t1 = GraphType.objects.get(type = graph_type)
    print(t1)

    if entity == 'gender':
        count_male = fir_register.objects.filter(fir_gender = 'Male').count()
        count_female = fir_register.objects.filter(fir_gender = 'Female').count()
        count_other = fir_register.objects.filter(fir_gender = 'Other').count()
        print(count_male)
        print(count_female)
        print(count_other)

        data_points = [
        { "label": "Male",  "y": count_male  },
        { "label": "Female", "y": count_female  },
        { "label": "Other", "y": count_other  }
        ]
        # hello(req, graph_type)
        # d = {'graph_type' : graph_type}
        return render(req, 'index.html', { "data_points" : data_points,'key' : t1})

        
    elif entity == 'age':

        lower = 0  # 18 - 22
        middle = 0  # 23 - 30
        higher = 0  # 31 - 40
        old = 0     # 41 - above

        for p in fir_register.objects.raw("SELECT id, fir_age FROM crimeapp_fir_register where fir_age > 17 AND fir_age < 23"):
            lower += 1

        for p in fir_register.objects.raw("SELECT id, fir_age FROM crimeapp_fir_register where fir_age > 22 AND fir_age < 31"):
            middle += 1
        
        for p in fir_register.objects.raw("SELECT id, fir_age FROM crimeapp_fir_register where fir_age > 30 AND fir_age < 41"):
            higher += 1
        
        for p in fir_register.objects.raw("SELECT id, fir_age FROM crimeapp_fir_register where fir_age > 40"):
            old += 1
    
        data_points = [
        { "label": "Lower age (18-22)",  "y": lower  },
        { "label": "Middle age (23-30)", "y": middle  },
        { "label": "Higher age (31-40)", "y": higher  },
        { "label": "Old age (41-above)", "y": old  }
        ]  
        return render(req, 'index.html', { "data_points" : data_points })
    

    elif entity == 'crime':
        Murdder = fir_register.objects.filter(fir_type = 'Murdder').count()
        Kidnap = fir_register.objects.filter(fir_type = 'Kidnap').count()
        Harashment = fir_register.objects.filter(fir_type = 'Harashment').count()
        Rape = fir_register.objects.filter(fir_type = 'Rape').count()
        Political = fir_register.objects.filter(fir_type = 'Political').count()
        Robbery = fir_register.objects.filter(fir_type = 'Robbery').count()
        Vehical = fir_register.objects.filter(fir_type = 'Motor vehicle').count()
        Property = fir_register.objects.filter(fir_type = 'Property crimes').count()
        Other = fir_register.objects.filter(fir_type = 'Other').count()
        
        data_points = [
        { "label": "Murdder",  "y": Murdder  },
        { "label": "Kidnap", "y": Kidnap  },
        { "label": "Harashment", "y": Harashment  },
        { "label": "Rape",  "y": Rape  },
        { "label": "Political", "y": Political  },
        { "label": "Robbery", "y": Robbery  },
        { "label": "Motor vehicle",  "y": Vehical  },
        { "label": "Property crimes", "y": Property  },
        { "label": "Other", "y": Other  }
        ]
        # d = {'graph_type' : graph_type}

        
        return render(req, 'index.html', { "data_points" : data_points })
    
    elif entity == 'Select':
        return HttpResponse("<script>alert('Please select type...?');location.href='/graph_data'</script>")
    
    else:
        return render(req, 'index.html')

def index(request):
    return render(request, 'index.html')

def graph_from_html(req):
    return render(req, 'graph_from_html.html')

# Grafical view end

def card_picture(req):
    # sliders = slidermodel.objects.all()
    logo = card_img.objects.all()
    obj = { 'logo':logo}
    return render(req,'home.html',obj)

    

def gallary1(req):
    logo = card_img.objects.all()
    obj = {'key':logo}
    return render(req,"gallary.html",obj)

def printed_gallary(req):
    logo = printed_gallary1.objects.all()
    obj = {'logo':logo}
    return render(req,'printed_gallary.html',obj)

def photo_gallery(req):
    logo = PhotoGallery.objects.all()
    obj = {'logo':logo}
    return render(req,'photo_gallery.html',obj)

## Public section
def online_complaint(req):
    data = savepolicestationModel.objects.all()
    obj={'station_name':data}
    return render(req,'online_complent.html',obj)

def save_comp_reg(req):
    a= req.POST.get('comp_id')
    cha_count=OnlineComplaint.objects.filter(comp_id=a).count()
    newuser1=OnlineComplaint(
        comp_id = req.POST.get('comp_id'),
        comp_adhar = req.POST.get('comp_adhar'),
        comp_fullname = req.POST.get('comp_fullname'),
        comp_age = req.POST.get('comp_age'),
        comp_gender = req.POST.get('comp_gender'),
        comp_phone = req.POST.get('comp_phone'),
        comp_address = req.POST.get('comp_address'),
        comp_register_by= req.POST.get('comp_register_by'),
        comp_photo = req.POST.get('comp_photo'),
        comp_type = req.POST.get('comp_type'),
        comp_subject = req.POST.get('comp_subject')
    )
    newuser1.save()
    return HttpResponse("<script>alert('Complaint sent successfully...');location.href='/'</script>")


def viewcomplaint(req,comp_station):
    data = OnlineComplaint.objects.all()
    obj={'key':data}
    return render(req,'view_complaint.html',obj)

def comp_delete(req,comp_id):
    rec_delete=OnlineComplaint.objects.get(comp_id=comp_id)
    rec_delete.delete()
    return HttpResponse("<script>alert('Complaint delete successfully...');location.href='/viewcomplaint/<str:comp_station>'</script>")


def comp_add_fir(req,comp_id):
    rec_delete=OnlineComplaint.objects.get(comp_id=comp_id)
    # fir=fir_register.objects.get(comp_id=comp_id) 
    newuser1=fir_register(
    #fir_id=rec_delete.comp_id,
    fir_fullname = rec_delete.comp_adhar,
    fir_adhar = rec_delete.comp_adhar,
    fir_age = rec_delete.comp_age,
    fir_gender = rec_delete.comp_gender,
    fir_phone = rec_delete.comp_phone,
    fir_address = rec_delete.comp_address,
    fir_register_by = rec_delete.comp_register_by,
    fir_photo = rec_delete.comp_photo,
    fir_type = rec_delete.comp_type,
    fir_subject = rec_delete.comp_subject
    )
    newuser1.save()
    rec_delete.delete()
    return HttpResponse("<script>alert('Complaint add to fir successfully...');location.href='/view_criminal'</script>")
    
    
def comp_more(req,comp_id):
    info_data=OnlineComplaint.objects.get(comp_id=comp_id)
    return render(req,'complait_more.html',{'info_data':info_data})



################## Character Certificate  #################

def public_login(req):
    return render(req,'public_login.html')

def user_registration(req):
 
    return render(req,'user_registration.html')


def char_certificate(req):
    char_id = req.POST.get('char_id')
    char_pass=req.POST.get('char_pass')

    cha_count=UserRegistration.objects.filter(user_fullname=char_id , user_pass=char_pass).count()
    if(cha_count>0):
        return render(req,'char_certificate.html')
    else:
        return HttpResponse("<script>alert('Username and password not valid ...');location.href='/public_login'</script>")

def char_reg(req):
    char_name = req.POST.get('char_name')
    cha_count=UserRegistration.objects.filter(user_fullname=char_name).count()
    print(cha_count)
    if(cha_count==0):
        newuser1=UserRegistration(
         user_fullname = req.POST.get('char_name'),
         user_phone = req.POST.get('char_phone'),
         user_pass = req.POST.get('char_pass')
        )
        newuser1.save()
        return HttpResponse("<script>alert('regestraction succesfullay...');location.href='/public_login'</script>")
        
    else:
        return HttpResponse("<script>alert('Username already exsist...');location.href='/user_registration'</script>")

a = 0
def save_user(req):
    global a
    a = req.POST.get('char_adhar')
    today = date.today()
    count = fir_register.objects.filter(fir_adhar = a).count()
    count1 = UserCharCertificateData1.objects.filter(char_adhar = a).count()
    data=UserCharCertificateData1.objects.filter(char_adhar = a)
    print("THE VALUE OF ADATA",count)
    if(count == 0  and count1==0):
        newuser1=UserCharCertificateData1(
            char_date = today,
            char_fullname = req.POST.get('char_fullname'),
            char_adhar = req.POST.get('char_adhar'),
            char_age = req.POST.get('char_age'),
            char_gender = req.POST.get('char_gender'),
            char_phone = req.POST.get('char_phone'),
            char_police_station = req.POST.get('char_police_station'),
            char_address = req.POST.get('char_address')
        )
        newuser1.save()
        return HttpResponse("<script>alert('User application sent successfully ...');location.href='/pdf/'</script>")
    else:
         return HttpResponse("<script>alert('User application have alredy ...');location.href='/char_certificate/'</script>")


from django.template.loader import render_to_string

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        count = fir_register.objects.filter(fir_adhar = a).count()
        if(count == 0):
            data = UserCharCertificateData1.objects.get(char_adhar = a)
            open('template/temp.html', "w").write(render_to_string('results.html', {'data': data}))
        else:
            data = fir_register.objects.get(fir_adhar = a)
            open('template/temp.html', "w").write(render_to_string('results2.html', {'data': data}))

        pdf = html_to_pdf('temp.html')
        return HttpResponse(pdf, content_type='application/pdf')


from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  

def html_to_pdf(template_src, context_dict={}):
     
     template = get_template(template_src)
     html  = template.render(context_dict)
     result = BytesIO()
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None


def feedback(req):
    data = savepolicestationModel.objects.all()
    obj={'station_name':data}
    return render(req,'feedback.html',obj)


def save_feedback(req):
    today1 = date.today()
    newuser1=UserFeedback(
            fed_date = today1,
            fed_name = req.POST.get('feedback_name'),
            fed_email = req.POST.get('feedback_email'),
            fed_subject = req.POST.get('feedback_subject'),
            fed_stationname = req.POST.get('feedback_station'),
            fed_message = req.POST.get('feedback_message')
            )
    newuser1.save()
    return HttpResponse("<script>alert('Feedback sent successfully ...');location.href='/feedback/'</script>")

def view_feedback(req,st_name):
    data = UserFeedback.objects.filter(fed_stationname = st_name)
    obj = {'key':data}
    return render(req,'view_feedback.html',obj)
    

def manage_staff(req,st_name):
    return render(req,'manage_staff.html')


def insert_new_staff(req):
    newuser1=insert_staff(
            insert_staff_adhar = req.POST.get('staff_adhar'),
            insert_staff_last_name = req.POST.get('staff_lastname'),
            insert_staff_first_name = req.POST.get('staff_firstname'),
            insert_staff_midd_name = req.POST.get('staff_middle_name'),
            insert_staff_birth = req.POST.get('staff_birth'),
            insert_staff_office_name = req.POST.get('staff_office'),
            insert_staff_mobile = req.POST.get('staff_mobile'),
            insert_staff_joning_date = req.POST.get('staff_joining'),
            insert_staff_education = req.POST.get('staff_education'),
            insert_staff_address = req.POST.get('staff_address'),
            insert_staff_gender = req.POST.get('staff_gender'),
            insert_staff_email = req.POST.get('staff_email')
            )
    newuser1.save()
    return HttpResponse("<script>alert('Record insert successfully...');location.href='/manage_staff/'</script>")



def update_staff(req):
    return render(req,'update_staff.html')


def doupdateStaff(req):
    #adhar = req.POST.get('staffupdateAdhar')
    adhar = req.GET["staffupdateAdhar"]
    print(adhar)
   
    data1=insert_staff.objects.filter(insert_staff_adhar=adhar).count()
    
    if (data1==1):
        data=insert_staff.objects.get(insert_staff_adhar=adhar)
        return render(req,'update_staff.html', {'key':data})
    else:
        return HttpResponse("<script>alert('Adhar not Found ...');location.href='/update_staff/'</script>")


def save_update_staff(req,insert_staff_adhar):
    #insert_staff_adhar = req.POST.get('staff_adhar')
    insert_staff_last_name = req.POST.get('staff_lastname')
    insert_staff_first_name = req.POST.get('staff_firstname')
    insert_staff_midd_name = req.POST.get('staff_middle_name')
    insert_staff_birth = req.POST.get('staff_birth')
    insert_staff_office_name = req.POST.get('staff_office')
    insert_staff_mobile = req.POST.get('staff_mobile')
    insert_staff_joning_date = req.POST.get('staff_joining')
    insert_staff_education = req.POST.get('staff_education')
    insert_staff_address = req.POST.get('staff_address')
    insert_staff_gender = req.POST.get('staff_gender')
    insert_staff_email = req.POST.get('staff_email')

    ins = insert_staff.objects.get(insert_staff_adhar =insert_staff_adhar)
    ins.insert_staff_last_name = insert_staff_last_name
    ins.insert_staff_first_name = insert_staff_first_name
    ins.insert_staff_midd_name = insert_staff_midd_name
    ins.insert_staff_birth = insert_staff_birth
    ins.insert_staff_office_name = insert_staff_office_name
    ins.insert_staff_mobile = insert_staff_mobile
    ins.insert_staff_joning_date = insert_staff_joning_date
    ins.insert_staff_education = insert_staff_education
    ins.insert_staff_address = insert_staff_address
    ins.insert_staff_gender = insert_staff_gender
    ins.insert_staff_email = insert_staff_email
    ins.save()
    return HttpResponse("<script>alert('Record Update Sucsessfull...');location.href='/update_staff/'</script>")


def view_staff(req):
    data = insert_staff.objects.all()
    obj = {'key' : data}
    return render(req,'view_staff.html',obj)



def public_alert(req):
    data = PublicAlert.objects.all()
    obj={'data':data}
    return render(req,'public_alert.html',obj)

def measing_people(req):
    data = missing.objects.all()
    obj = {'key' : data}
    return render(req,'measing_people.html',obj)

def insert_missing(req):
    return render(req,"insert_data_messing.html")

def insert_messing_people(req):
    newuser1=missing(
        missing_name = req.POST.get('miss_name'),
             missing_phone = req.POST.get('miss_phone'),
             missing_description = req.POST.get('description'),
             missing_adhar = req.POST.get('miss_adhar'),
             missing_image = req.POST.get('miss_image'),
             missing_address = req.POST.get('miss_adress')
            )
    newuser1.save()
    return HttpResponse("<script>alert('Record added Sucsessfull to public section...');location.href='/insert_missing/'</script>")






