from tools.geo_location.const import capitais_brasil, geo_rules
import math
import random

class State:

    def __init__(self, name: str) -> None:
        self.name = name
        self.obj = self.get_info()

        if self.obj:
            self.capital = self.obj['capital']
            self.pop = self.obj['pop']
            self.area = self.obj['area']
            self.rule = self.get_rule()
            self.center_point = {'lat': self.obj['lat'], 'lon': self.obj['lon']}
            self.city_square = self.create_square()
            self.locations = self.generate_random_points()
        else:
            self.pop = None
            self.capital = None
            self.center_point = None
            self.area = None
            self.rule = None
            self.locations = None
            self.city_square = None

    def get_info(self):
        return capitais_brasil.get(self.name.upper())

    def get_pop(self):
        return self.pop

    def get_capital(self):
        return self.capital

    def get_geo_location(self):
        return self.center_point

    def get_area(self):
        return self.area

    def get_rule(self):
        pop = self.pop

        if pop is not None:
            rules = geo_rules

            for rule, (lower_limit, upper_limit) in rules.items():
                if lower_limit <= pop <= upper_limit:
                    return int(rule)
        return None
    
    def move_horizontal(self, initial_longitude, distance_km, direction='right'):
        # Average radius of the Earth in kilometers
        earth_radius_km = 6371.0

        # Convert longitude to radians
        initial_lon_rad = math.radians(initial_longitude)

        # Calculate new longitude based on direction
        if direction == 'right':
            new_lon_rad = initial_lon_rad + (distance_km / earth_radius_km) / math.cos(math.radians(self.center_point['lat']))
        elif direction == 'left':
            new_lon_rad = initial_lon_rad - (distance_km / earth_radius_km) / math.cos(math.radians(self.center_point['lat']))
        else:
            raise ValueError("Invalid direction. Use 'right' or 'left'.")

        # Convert back to degrees
        new_longitude = math.degrees(new_lon_rad)

        return new_longitude

    def move_vertical(self, initial_latitude, distance_km, direction='up'):
        # Average radius of the Earth in kilometers
        earth_radius_km = 6371.0

        # Convert latitude to radians
        initial_lat_rad = math.radians(initial_latitude)

        # Calculate new latitude based on direction
        if direction == 'up':
            new_lat_rad = initial_lat_rad + (distance_km / earth_radius_km)
        elif direction == 'down':
            new_lat_rad = initial_lat_rad - (distance_km / earth_radius_km)
        else:
            raise ValueError("Invalid direction. Use 'up' or 'down'.")

        # Ensure the latitude is within the valid range [-pi/2, pi/2] radians
        new_lat_rad = max(min(new_lat_rad, math.pi / 2), -math.pi / 2)

        # Convert back to degrees
        new_latitude = math.degrees(new_lat_rad)

        return new_latitude
    
    def create_square(self):
        dist = math.sqrt(self.area)/2
        north_point = {'lat': self.move_vertical(self.center_point['lat'], dist, "up") , "lon" : self.center_point['lon']}
        south_point = {'lat': self.move_vertical(self.center_point['lat'], dist, "down"), "lon" : self.center_point['lon']}
        east_point = {'lat': self.center_point['lat'], "lon" : self.move_horizontal(self.center_point['lon'], dist, "right")}
        west_point = {'lat': self.center_point['lat'], "lon" : self.move_horizontal(self.center_point['lon'], dist, "left")}

        return [(north_point['lat'], north_point['lon']),(south_point['lat'], south_point['lon']),(east_point['lat'], east_point['lon']),(west_point['lat'], west_point['lon'])]

    def generate_random_points(self):

        vertices  = self.create_square()
        n = self.rule

        x_values, y_values = zip(*vertices)

        random_points = []

        for _ in range(n):
            # Generate random x and y coordinates within the limits of the quadrilateral
            random_x = round(random.uniform(min(x_values), max(x_values)), 4)
            random_y = round(random.uniform(min(y_values), max(y_values)), 4)

            random_points.append((random_x, random_y))

        unique_points = list(set(random_points))
        return unique_points