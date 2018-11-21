import googlemaps

from .api_keys import ELEVATION_KEY


def normalize_lng(lng):
    # # normalize longitude:
    # # -inf...inf ===> 0...360
    # res = lng % 360
    # # 0...360 ===> -180...180
    # res = res - 360 if res > 180 else res
    # return res
    return lng % 360 - 360 if lng % 360 > 180 else lng % 360


def get_elevation(geom, step=512):
    from django.contrib.gis.geos import LineString
    if isinstance(geom, LineString):
        pois = [[normalize_lng(i[0]), i[1]] for i in geom]
        ds = [[[i[1], i[0]] for i in pois[j:j + step]] for j in range(0, len(pois), step)]
        alts = [j['elevation'] for i in ds for j in googlemaps.Client(key=ELEVATION_KEY).elevation(i)]
        return [pois[i] + [alts[i]] for i in range(len(pois))]
    else:
        lng = normalize_lng(geom[0])
        alt = googlemaps.Client(key=ELEVATION_KEY).elevation([[geom[1], lng]])[0]['elevation']
        return [lng, geom[1], alt]
