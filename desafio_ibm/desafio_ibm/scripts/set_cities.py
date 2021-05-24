from desafio_ibm.users.models import City


def run():
    cities = open("data/cities.csv")

    for city in cities:
        City(name=city.strip()).save()
