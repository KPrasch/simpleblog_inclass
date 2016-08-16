from geopy.geocoders import Nominatim
address = '2626 SW Corbett Ave'
city = 'Portland'


geolocator = Nominatim()
location = geolocator.geocode(str(address) + ', ' + str(city))
print(location.latitude)
print(location.longitude)

# from django.db.models.signals import post_save
#
#
# class Marker(models.Model):
#     name = models.CharField( max_length=255)
#     lat = models.CharField( max_length=255)
#     lon = models.CharField( max_length=255)
#
#
# class Vendor(models.Model):
#     name = models.CharField(max_length=50)
#     address_1 = models.CharField( max_length=128)
#     city = models.CharField( max_length=64, default="Seal Rock")
#     state = models.CharField( max_length=2, default="OR")
#     zip_code = models.CharField(max_length=5, default="97376")
#     location = (,).join([name, address_1, city, state, zip_code])
# 	marker = models.ManyToManyField(Marker)
#
#
# # Create instances of each beer to be associated with locations
# class Beer(models.Model):
#     name = models.CharField(max_length=50)
#     bottles = models.BooleanField(default=0)
#     keg = models.BooleanField(default=0)
#     vendor = models.ManyToManyField(Vendor)
#
#
# def lat_lon_save(sender, instance, created, **kwargs):
#     if created:
#         geolocator = Nominatim()
#         location = geolocator.geocode(str(instance.address) + ', ' + str(instance.city))
#
#         marker = Marker()
#         marker.lat = location.latitude
#         marker.lon = location.longitude
#         marker.name = instance.name
#         marker.save()
#         instance.marker.add(marker)
#         instance.save()
#
# post_save.connect(lat_lon_save, sender=Vendor)
