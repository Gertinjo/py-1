from abc import ABC , abstractmethod


class DigitalSchool:
    def __init__(self, city, state , courses):
        self.__city = city
        self.__state = state
        self.__courses = courses

    @property
    def city(self):
        return self.__city
    @property
    def state(self):
        return self.__state
    @property
    def courses(self):
        return self.__courses
    @city.setter
    def city(self, city):
        self.__city = city
    @state.setter
    def state(self, state):
        self.__state = state
    @courses.setter
    def courses(self, courses):
        self.__courses = courses

    def show_school_info(self, city , state, course):
        return (
            "City" , self.__city,
            "state" , self.__state,
            "courses" , self.__courses
        )
    def oragnise_hackathon(self):
        pass

class DS_Prishtina (DigitalSchool):
    def __init__(self, city , state , courses):