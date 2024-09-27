class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ):
        self.total_price = 0
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]):
        for car in cars:
            self.wash_single_car(car)
        return round(self.total_price, 1)

    def calculate_washing_price(self, car: Car):
        return round(car.comfort_class
                     * (self.clean_power
                        - car.clean_mark)
                     * self.average_rating
                     / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car):
        if self.clean_power > car.clean_mark:
            self.total_price += self.calculate_washing_price(car)
            car.clean_mark = self.clean_power

    def rate_service(self, mark: int):
        total_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round((total_rating + mark) / self.count_of_ratings, 1)
