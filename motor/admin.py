__author__ = 'chente'

from motor.models import PageType,Page, Lang, Site, SiteDetail,PageDetail,Location, MapZones,Media,MediaDetail,Promotion, PageMedia,PriceModel, PriceModelDetail,Season, Rate, RateDetail, Room, Availability, Hotel, Profile
from django.forms.models import fields_for_model
from django.contrib import admin
from django.contrib.auth.models import User

class SiteAdmin(admin.ModelAdmin):
    list_display = ('site_id','site_name')
    search_fields  =  [ 'site_name' ]

class PageTypeAdmin(admin.ModelAdmin):
    list_display = ('type_id','type_name')
    search_fields = ['type_name']

class PageAdmin(admin.ModelAdmin):
    fields = ('site_id','type')
    list_display = ('page_id','site_id','type')

class LangAdmin(admin.ModelAdmin):
    fields = ('lang_name','lang_code')
    list_display = ('lang_id','lang_name','lang_code')
    search_fields = ['lang_name', 'lang_code']

class SiteDetailAdmin(admin.ModelAdmin):
    fields = ('site_detail_url','lang','site')
    list_display = ('site_detail_id','site_detail_url','lang','site')

class PageDetailAdmin(admin.ModelAdmin):
    fields = ('page_title','page_content','meta_title', 'meta_keywords','meta_description','page','site_detail')
    list_display = ('page_detail_id','page_title','page_content','meta_title', 'meta_keywords','meta_description','page','site_detail')

    class Media:
        js = ('/static/js/tiny_mce/tiny_mce.js',
              '/static/js/editores.js',)

class LocationAdmin(admin.ModelAdmin):
    fields = ('page','location_point')
    list_display = ('location_id','page','location_point')

class MapZonesAdmin(admin.ModelAdmin):
    fields =('location', 'map_zone_point', 'page')
    list_display = ('map_zone_id', 'location', 'map_zone_point', 'page')

class MediaAdmin(admin.ModelAdmin):
    fields = ('media_name','media_type_id')
    list_display = ('media_id','media_name','media_type_id')

class MediaDetailAdmin(admin.ModelAdmin):
    fields = ('media_title','media_alt', 'media','site_detail')
    list_display = ('media_detail_id','media_title','media_alt', 'media','site_detail')

class PromotionAdmin(admin.ModelAdmin):
    fields = ('promotion_bw_start','promotion_bw_end','promotion_tw_start','promotion_tw_end','promotion_discount','promotion_paynights','promotion_freenights','promotion_freeguest','promotion_rooms','promotion_blackout', 'promotion_minstay','promotion_release','promotion_weekday','page')
    list_display = ('promotion_id','promotion_bw_start','promotion_bw_end','promotion_tw_start','promotion_tw_end','promotion_discount','promotion_paynights','promotion_freenights','promotion_freeguest','promotion_rooms','promotion_blackout', 'promotion_minstay','promotion_release','promotion_weekday','page')

class PageMediaAdmin(admin.ModelAdmin):
    fields =('page', 'media', 'page_media_order')
    list_display = ('page_media_id', 'page', 'media', 'page_media_order')

class PriceModelAdmin(admin.ModelAdmin):
    fields = ('price_model_calculation','page')
    list_display = ('price_model_id','price_model_calculation','page')

class PriceModelDetailAdmin(admin.ModelAdmin):
    list_display = ('price_model_detail_id','price_model_description', 'price_model', 'site_detail_id')

class SeasonAdmin(admin.ModelAdmin):
    list_display = ('season_id','season_weekday','season_daterange','page')

    class Media:
        js = ('/static/js/tiny_mce/tiny_mce.js',
              '/static/js/editores.js',)

class RateAdmin(admin.ModelAdmin):
    list_display = ('rate_id','season', 'rate_price_class')

class RateDetailAdmin(admin.ModelAdmin):
    list_display = ('rate_detail_id','rate', 'room_id', 'rate_detail')

    class Media:
        js = ('/static/js/tiny_mce/tiny_mce.js',
              '/static/js/editores.js',)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id','room_capacity', 'room_base', 'room_order', 'room_main','page')

class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('availability_id','availability_daterange', 'availability_quantity', 'room')

class HoltelAdmin(admin.ModelAdmin):
    list_display = ('hotel_id','page', 'location', 'hotel_rating','hotel_family','hotel_acommodation', 'hotel_point','map_zone')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user','hotel')

admin.site.register(Site, SiteAdmin)
admin.site.register(PageType, PageTypeAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Lang, LangAdmin)
admin.site.register(SiteDetail, SiteDetailAdmin)
admin.site.register(PageDetail, PageDetailAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(MapZones, MapZonesAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(MediaDetail, MediaDetailAdmin)
admin.site.register(Promotion, PromotionAdmin)
admin.site.register(PageMedia, PageMediaAdmin)
admin.site.register(PriceModel, PriceModelAdmin)
admin.site.register(PriceModelDetail, PriceModelDetailAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Rate, RateAdmin)
admin.site.register(RateDetail, RateDetailAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Availability, AvailabilityAdmin)
admin.site.register(Hotel, HoltelAdmin)
admin.site.register(Profile, ProfileAdmin)
