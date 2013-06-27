import urllib
import simplejson

def coordinates(address):
    url = 'http://maps.google.com/maps/api/geocode/json?address=%s&sensor=false' % address
    coord = simplejson.load(
        urllib.urlopen(url)
    )

    if coord['status'] == 'OK':
        return {
            'lat': coord['results'][0]['geometry']['location']['lat'],
            'lng': coord['results'][0]['geometry']['location']['lng'],
        }
    else:
        return {
            'lat': '',
            'lng': '',
            }
