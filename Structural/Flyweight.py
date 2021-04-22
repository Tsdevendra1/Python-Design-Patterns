"""
Why: You have memory constraints, and want to create a lot instances of a particular class. But creating, for example, 1,000,000 instances would be
unfeasible if they all share similar but slightly different state. To get around this, you extract common state in these classes and cache the instances
based on this common state.

Example: You have a shape class. You want to draw it at x and y coordinate. This x and y will be "unique" state which can be changed. However, an instance of
a shape, e.g. a red square can be cached and re-used whenever you need a red square.

"""


class FlyWeightShape:

    def __init__(self, color: str, shape: str):
        self.__shape = shape
        self.__color = color

    def draw(self, x_coordinate: int, y_coordinate: int):
        # Implemenentation omitted
        pass


class FlyWeightContainer:
    __flyweights: {(str, str): FlyWeightShape} = {}

    def __init__(self, required_initial_flyweights: [(str, str)]):
        for (color, shape) in required_initial_flyweights:
            self.__flyweights[(color, shape)] = FlyWeightShape(color=color, shape=shape)

    def get_fly_weight_shape(self, color: str, shape: str):
        cache_key = (color, shape)
        cached_value = self.__flyweights.get(cache_key)
        if cached_value is not None:
            print("found cached value")
            return cached_value

        print("didn't find cached value")
        new_flyweight = FlyWeightShape(color=color, shape=shape)
        self.__flyweights[cached_value] = new_flyweight
        return new_flyweight


def main():
    container = FlyWeightContainer(required_initial_flyweights=[("red", "square"), ("blue", "triangle")])
    flyweight = container.get_fly_weight_shape(color="red", shape="square")
    flyweight.draw(x_coordinate=1, y_coordinate=34)

    flyweight = container.get_fly_weight_shape(color="blue", shape="square")
    flyweight.draw(x_coordinate=1, y_coordinate=34)


if __name__ == "__main__":
    main()
