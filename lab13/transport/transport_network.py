from typing import List


class Stop:
    @property
    def name(self):
        pass

    @property
    def latitude(self):
        pass

    @property
    def longitude(self):
        pass


class BusNetwork:
    def __init__(self) -> None:
        pass

    def load_stops(self, f_name: str) -> None:
        pass

    def load_connections(self, f_name: str) -> None:
        pass

    def get_stop(self, stop_name: str) -> Stop:
        pass

    def get_line(self, from_stop_name: str, to_stop_name: str) -> str:
        pass

    def compute_itinerary(self, from_stop_name: str, to_stop_name: str) -> List[str]:
        pass



