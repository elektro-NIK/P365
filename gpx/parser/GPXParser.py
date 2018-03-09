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
            name = track.name
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

    def routes(self):
        res = {}
        for route in self._gpx.routes:
            name = route.name
            description = route.description if route.description else route.comment
            points = [Point(i.longitude, i.latitude, 0) for i, j in route.walk()]
            for i, _ in route.walk():
                points.append(Point(i.longitude, i.latitude, 0))
            line = LineString(points)
            res[name] = {
                'description': description,
                'length': route.length() / 1000,
                'geom': line
            }
        return res
