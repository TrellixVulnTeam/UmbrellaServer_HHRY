from django.db import models
from django.db.models import CharField
from django_mysql.models import ListCharField
import datetime
from django.contrib.auth.models import User


# Create your models here.

class Userx(models.Model):
    user = models.OneToOneField(
    User,
    related_name="user_api", 
    on_delete=models.CASCADE, 
    default=None,
    null=True, 
    )
    nome= models.CharField(max_length=400)
    created_at = models.DateField(("Date"), default=datetime.date.today)
    identifier = models.CharField(max_length=200)
    actived = models.BooleanField(default=True)
    status=models.CharField(max_length=200,default=None,null=True)
    key=models.CharField(("Key"), max_length=200, default = None, null=True)


    class Meta:
        verbose_name_plural = "users"
    
    def __str__(self):
        return self.identifier

class Seguidores(models.Model):
    name_reference=models.CharField(max_length=100)
    status_follor = models.BooleanField(default=False)
    list_followers=ListCharField(
        base_field=CharField(max_length=200),
        size=600,
        max_length=600*1100
        )
    class Meta:
        verbose_name_plural="seguidores"

    def __str__(self):
        return self.name_reference

class Tags(models.Model):
    name_reference=models.CharField(max_length=100)
    list_tag=ListCharField(
        base_field=CharField(max_length=200),
        size=600,
        max_length=600*1100
        )

    class Meta:
        verbose_name_plural="tags"

    def __str__(self):
        return self.name_reference

class Posts(models.Model):
    name_reference=models.CharField(max_length=100)
    list_posts=ListCharField(
        base_field=CharField(max_length=200),
        size=600,
        max_length=600*1100
    )
    
    class Meta:
        verbose_name_plural="posts"

    def __str__(self):
        return self.name_reference

class Feedbacks(models.Model):
    name_reference=models.CharField(max_length=100)
    list_feedbacks=ListCharField(
        base_field=CharField(max_length=200),
        size=600,
        max_length=600*1100
    )
    
    class Meta:
        verbose_name_plural="feedbacks"
    def __str__(self):
        return self.name_reference
class Photos(models.Model):
    name_reference=models.CharField(max_length=100)
    list_photos_profile=ListCharField(base_field=CharField(max_length=200)
    ,size=600,
    max_length=600*1100)

class Perfis(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    amount=models.IntegerField(max_length=200,default = True)
    identifier = models.CharField(max_length=200,null=True)
    seguidores = models.ManyToManyField(Seguidores,null=True, default=None) 
    tags = models.ManyToManyField(Tags , null = True , default = None)
    posts = models.ManyToManyField(Posts , null = True , default = None)
    feedbacks = models.ManyToManyField(Feedbacks , null = True , default = None)
    photos = models.ManyToManyField(Photos,null=True,default=None)

    class Meta:
        verbose_name_plural="perfis"

    def __str__(self):
        return self.username

class Gestor(models.Model):
    identifier=models.CharField(max_length=100,null=True,default=None)
    user = models.OneToOneField(Userx,on_delete=models.CASCADE,null=True,blank=True, default =None)
    id_perfil_select = models.CharField(max_length=2000,null=True)
    id_gestor_select = models.CharField(max_length=2000,null=True)
    Perfis = models.ManyToManyField(Perfis, null=True, blank=True)

    class Meta:
        verbose_name_plural = "gestores"
    def __str__(self):
        return self.identifier