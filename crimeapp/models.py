from django.db import models

# Create your models here.

class policestationreg(models.Model):
    st_id=models.IntegerField()
    st_pass=models.CharField(max_length=15)
    station_name=models.CharField(max_length=200)
    city_name=models.CharField(max_length=200)


class demo(models.Model):
    picture=models.ImageField(upload_to='static/')



class slidermodel(models.Model):
    slider_title = models.CharField(max_length=200)
    slider_headerline = models.CharField(max_length=200)
    slider_details = models.CharField(max_length=200)
    slider_image = models.ImageField(upload_to="static/")


class station_register(models.Model):
    st_name = models.CharField(max_length=200)
    st_id = models.CharField(max_length=200)
    st_pass = models.CharField(max_length=200)
    st_con_pass = models.CharField(max_length=200)
    st_address = models.CharField(max_length=200)





class savepolicestationModel(models.Model):
    st_name=models.CharField(max_length=200)
    st_id=models.TextField()
    st_pass=models.TextField()
    st_con_pass=models.TextField()
    st_address=models.TextField()

    def __str__(self):
        return self.st_name



class saveuserModel(models.Model):
    user_name=models.CharField(max_length=200)
    user_age=models.IntegerField()
    user_add=models.TextField()


class GraphType(models.Model):
    type = models.CharField(max_length=200)




class fir_register(models.Model):
    fir_date=models.DateField()
    fir_police_station=models.CharField(max_length=200)
    fir_id = models.CharField(max_length=200)
    fir_adhar = models.CharField(max_length=15)
    fir_fullname = models.CharField(max_length=200)
    fir_age = models.IntegerField()
    fir_gender = models.CharField(max_length=200)
    fir_phone= models.CharField(max_length=20)
    fir_address = models.CharField(max_length=200)
    fir_register_by = models.CharField(max_length=200)
    fir_photo = models.ImageField(upload_to="static/")
    fir_type = models.CharField(max_length=200)
    fir_subject = models.CharField(max_length=200)


#model for gallary section
class card_img(models.Model):
    card_picture=models.ImageField(upload_to='static/')
    card_title=models.TextField()
    card_info=models.TextField()

#model for printed gallary
class printed_gallary1(models.Model):
    printed_photo=models.ImageField(upload_to='static/')
    printed_title=models.TextField()

class PhotoGallery(models.Model):
    photo = models.ImageField(upload_to='static/')


# Online complaint
class OnlineComplaint(models.Model):
    comp_id = models.CharField(max_length=200)
    comp_adhar = models.CharField(max_length=15)
    comp_fullname = models.CharField(max_length=200)
    comp_age = models.IntegerField()
    comp_gender = models.CharField(max_length=200)
    comp_phone= models.CharField(max_length=20)
    comp_address = models.CharField(max_length=200)
    comp_register_by = models.CharField(max_length=200)
    comp_photo = models.ImageField(upload_to="static/")
    comp_type = models.CharField(max_length=200)
    comp_subject = models.CharField(max_length=200)
    comp_station = models.CharField(max_length=200)


class greeting_message(models.Model):
    greeting_photo= models.ImageField(upload_to="static/")
    greeting_info=models.TextField()
    greeting_name=models.CharField(max_length=50)
    greeting_position=models.CharField(max_length=60)


class UserRegistration(models.Model):
    user_fullname = models.CharField(max_length=200)
    user_phone= models.CharField(max_length=20)
    user_pass = models.CharField(max_length=200)


class UserCharCertificateData1(models.Model):
    char_date = models.DateField()
    char_fullname = models.CharField(max_length=200)
    char_adhar = models.CharField(max_length=15)
    char_age = models.IntegerField()
    char_gender = models.CharField(max_length=200)
    char_phone= models.CharField(max_length=20)
    char_police_station = models.CharField(max_length=200)
    char_address = models.CharField(max_length=200)




class UserFeedback(models.Model):
    fed_date=models.DateField()
    fed_name = models.CharField(max_length=100)
    fed_email = models.CharField(max_length=100)
    fed_subject = models.CharField(max_length=200)
    fed_message = models.TextField()
    fed_stationname = models.CharField(max_length=100)


class insert_staff(models.Model):
    insert_staff_adhar=models.CharField(max_length=100)
    insert_staff_last_name=models.CharField(max_length=100)
    insert_staff_first_name=models.CharField(max_length=100)
    insert_staff_midd_name=models.CharField(max_length=100)
    insert_staff_birth=models.DateField()
    insert_staff_office_name=models.CharField(max_length=100)
    insert_staff_mobile=models.CharField(max_length=100)
    insert_staff_joning_date=models.CharField(max_length=100)
    insert_staff_education=models.CharField(max_length=100)
    insert_staff_address=models.CharField(max_length=300)
    insert_staff_gender=models.CharField(max_length=100)
    insert_staff_email=models.CharField(max_length=100)


# class GraphType(models.Model):
#     type=models.CharField(max_length=20)
   

class PublicAlert(models.Model):
    alert_title=models.CharField(max_length=200)
    audio_file = models.FileField( upload_to =  'static/')


class missing(models.Model):
    missing_name=models.CharField(max_length=100)
    missing_phone=models.CharField(max_length=100)
    missing_description=models.CharField(max_length=500)
    missing_adhar=models.CharField(max_length=200)
    missing_image=models.ImageField(upload_to="static/")
    missing_address=models.CharField(max_length=200)

