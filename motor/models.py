from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Site(models.Model):
    site_id = models.AutoField(primary_key=True)
    site_name = models.CharField(max_length=155, verbose_name='Nombre del Sitio')
    #quien_modifica = models.ForeignKey(User, verbose_name="Quien es el Autorizado")
    class Meta:
        db_table = u'site'

    def __str__(self):
        return self.site_name



class PageType(models.Model):
    type_id = models.AutoField(primary_key=True, verbose_name='Id')
    type_name = models.CharField(max_length=155, verbose_name='Tipo de Pagina')

    class Meta:
        db_table = u'page_type'

    def __str__(self):
        return self.type_name

        
class Page(models.Model):
    page_id = models.AutoField(primary_key=True, verbose_name='Id')
    site_id = models.ForeignKey(Site, verbose_name='Nombre del Sitio')
    type = models.ForeignKey(PageType, verbose_name='Tipo de pagina')
    class Meta:
        db_table = u'page'

    def __str__(self):
        return '%s'%self.site_id
        
class Lang(models.Model):
    lang_id = models.AutoField(primary_key=True, verbose_name='Id')
    lang_name = models.CharField(max_length=50,verbose_name='Nombre del Idioma')
    lang_code = models.CharField(max_length=4, verbose_name='Codigo')
    class Meta:
        db_table = u'lang'

    def __str__(self):
        return self.lang_name

class Site(models.Model):
    site_id = models.AutoField(primary_key=True, verbose_name='Id')
    site_name = models.CharField(max_length=155, verbose_name='Nombre del Sitio')
    class Meta:
        db_table = u'site'

    def __str__(self):
        return self.site_name

class SiteDetail(models.Model):
    site_detail_id = models.AutoField(primary_key=True, verbose_name='Id')
    site_detail_url = models.CharField(max_length=255, verbose_name='URL')
    lang = models.ForeignKey(Lang,verbose_name='Idioma')
    site = models.ForeignKey(Site, verbose_name='Sitio')
    class Meta:
        db_table = u'site_detail'

    def __str__(self):
        return self.site_detail_url

class PageDetail(models.Model):
    page_detail_id = models.AutoField(primary_key=True)
    page_title = models.CharField(max_length=155)
    page_content = models.TextField()
    meta_title = models.CharField(max_length=155)
    meta_keywords = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    page = models.ForeignKey(Page)
    site_detail = models.ForeignKey(SiteDetail)
    class Meta:
        db_table = u'page_detail'

    def __str__(self):
        return self.page_title

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    page = models.ForeignKey(Page)
    location_point = models.CharField(max_length=155)
    class Meta:
        db_table = u'location'

    def __str__(self):
        return '%s'%self.page

class MapZones(models.Model):
    map_zone_id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location)
    map_zone_point = models.CharField(max_length=155)
    page = models.ForeignKey(Page)
    class Meta:
        db_table = u'map_zones'

    def __str__(self):
        return '%s'%self.location


class Media(models.Model):
    media_id = models.AutoField(primary_key=True)
    media_name = models.CharField(max_length=155)
    media_type_id = models.IntegerField(unique=True)
    class Meta:
        db_table = u'media'

    def __str__(self):
        return self.media_name

class MediaDetail(models.Model):
    media_detail_id = models.AutoField(primary_key=True)
    media_title = models.CharField(max_length=155)
    media_alt = models.CharField(max_length=155)
    media = models.ForeignKey(Media)
    site_detail = models.ForeignKey(SiteDetail)
    class Meta:
        db_table = u'media_detail'

    def __str__(self):
        return self.media_title

class Promotion(models.Model):
    promotion_id = models.AutoField(primary_key=True)
    promotion_bw_start = models.DateField()
    promotion_bw_end = models.DateField()
    promotion_tw_start = models.DateField()
    promotion_tw_end = models.DateField()
    promotion_discount = models.CharField(max_length=20)
    promotion_paynights = models.SmallIntegerField()
    promotion_freenights = models.SmallIntegerField()
    promotion_freeguest = models.CharField(max_length=255)
    promotion_rooms = models.CharField(max_length=255)
    promotion_blackout = models.CharField(max_length=255)
    promotion_minstay = models.SmallIntegerField()
    promotion_release = models.SmallIntegerField()
    promotion_weekday = models.CharField(max_length=20)
    page = models.ForeignKey(Page)
    class Meta:
        db_table = u'promotion'

    def __str__(self):
        return '%s'%self.page

class PageMedia(models.Model):
    page_media_id = models.AutoField(primary_key=True)
    page = models.ForeignKey(Page)
    media = models.ForeignKey(Media)
    page_media_order = models.SmallIntegerField()
    class Meta:
        db_table = u'page_media'

    def __str__(self):
        return '%s'%self.page

class PriceModel(models.Model):
    price_model_id = models.AutoField(primary_key=True)
    price_model_calculation = models.SmallIntegerField()
    page = models.ForeignKey(Page)
    class Meta:
        db_table = u'price_model'

    def __str__(self):
        return '%s'%self.page

class PriceModelDetail(models.Model):
    price_model_detail_id = models.AutoField(primary_key=True)
    price_model_description = models.CharField(max_length=155)
    price_model = models.ForeignKey(PriceModel)
    site_detail_id = models.ForeignKey(SiteDetail)
    class Meta:
        db_table = u'price_model_detail'

    def __str__(self):
        return '%s'%self.price_model


class Season(models.Model):
    season_id = models.AutoField(primary_key=True)
    season_weekday = models.CharField(max_length=50)
    season_daterange = models.TextField()
    page = models.ForeignKey(Page)
    class Meta:
        db_table = u'season'

    def __str__(self):
        return '%s'%self.page
        
class Rate(models.Model):
    rate_id = models.AutoField(primary_key=True)
    season = models.ForeignKey(Season)
    rate_price_class = models.SmallIntegerField()
    class Meta:
        db_table = u'rate'

    def __str__(self):
        return self.season

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_capacity = models.SmallIntegerField()
    room_base = models.SmallIntegerField()
    room_order = models.SmallIntegerField()
    room_main = models.BooleanField()
    page = models.ForeignKey(Page)
    class Meta:
        db_table = u'room'

    def __str__(self):
        return '%s'%self.page


class RateDetail(models.Model):
    rate_detail_id = models.AutoField(primary_key=True)
    rate = models.ForeignKey(Rate)
    room_id = models.ForeignKey(Room)
    rate_detail = models.TextField()
    class Meta:
        db_table = u'rate_detail'

    def __str__(self):
        return self.rate



class Availability(models.Model):
    availability_id = models.AutoField(primary_key=True)
    availability_daterange = models.CharField(max_length=255)
    availability_quantity = models.SmallIntegerField()
    room = models.ForeignKey(Room)
    class Meta:
        db_table = u'availability'

    def __str__(self):
        return self.availability_daterange


class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    page = models.ForeignKey(Page)
    location = models.ForeignKey(Location)
    hotel_rating = models.CharField(max_length=25)
    hotel_family = models.SmallIntegerField()
    hotel_acommodation = models.SmallIntegerField()
    hotel_point = models.CharField(max_length=155)
    map_zone = models.ForeignKey(MapZones)
    
    class Meta:
        db_table = u'hotel'

    def __str__(self):
        return '%s'%self.page



class Profile(models.Model):
    user = models.OneToOneField(User, unique=True)
    hotel = models.CharField(max_length=100)
    is_admin = models.BooleanField()
    
    def __str__(self):
        return '%s'%self.user
    


