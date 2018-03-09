import gpxpy
from django.contrib.gis.geos import Point, LineString, MultiLineString


def equal_points(p1, p2):
    if p1.time == p2.time or (p1.longitude == p2.longitude and
                              p1.latitude == p2.latitude and
                              p1.elevation == p2.elevation):
        return True
    return False


def gpx2dict(file):
    gpx = gpxpy.parse(file)
    res = dict()
    for track in gpx.tracks:
        # max speed
        name = track.name
        segments = []
        max_speed = 0
        for segment in track.segments:
            if len(segment.points) > 1:
                points = []
                prev_point = None
                for point in segment.points:
                    if prev_point and not equal_points(point, prev_point):
                        if point.speed_between(prev_point) > max_speed:
                            max_speed = point.speed_between(prev_point)
                    points.append(Point(point.longitude, point.latitude, point.elevation))
                    prev_point = point
                segments.append(LineString(points))
        multiline = MultiLineString(segments)
        res[name] = {
            'start_date': track.get_time_bounds().start_time,
            'finish_date': track.get_time_bounds().end_time,
            'length': track.length_3d() / 1000,
            'speed': track.length_3d() / 1000 / (track.get_duration() / 3600),
            'speed_max': max_speed,
            'altitude_gain': track.get_uphill_downhill().uphill,
            'altitude_loss': track.get_uphill_downhill().downhill,
            'altitude_min': track.get_elevation_extremes().minimum,
            'altitude_max': track.get_elevation_extremes().maximum,
            'geom': multiline
        }
    return res