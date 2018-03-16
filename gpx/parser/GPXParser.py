import gpxpy
from django.contrib.gis.geos import Point, LineString, MultiLineString


class GPXParser:
    def __init__(self, file):
        self._gpx = gpxpy.parse(file)

    @staticmethod
    def _equal_points(p1, p2):
        return p1.time == p2.time

    def tracks(self):
        res = {}
        for track in self._gpx.tracks:
            segments, max_speed = [], 0
            for segment in track.segments:
                if len(segment.points) > 1:
                    points, prev_point = [], None
                    for point, _ in segment.walk():
                        if prev_point and not self._equal_points(point, prev_point):
                            if point.speed_between(prev_point) > max_speed:
                                max_speed = point.speed_between(prev_point)
                        points.append(Point(point.longitude, point.latitude, point.elevation))
                        prev_point = point
                    segments.append(LineString(points))
            multiline = MultiLineString(segments)
            res[track.name] = {
                'description': track.description if track.description else track.comment,
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

    def routes(self):
        res = {}
        for route in self._gpx.routes:
            points = [Point(i.longitude, i.latitude, i.elevation or 0) for i, _ in route.walk()]
            res[route.name] = {
                'description': route.description if route.description else route.comment,
                'length': route.length() / 1000,
                'geom': LineString(points)
            }
        return res

    def pois(self):
        res = {}
        for poi in self._gpx.waypoints:
            res[poi.name] = {
                'description': poi.description if poi.description else poi.comment,
                'created': poi.time,
                'geom': Point(poi.longitude, poi.latitude, poi.elevation or 0)
            }
        return res
