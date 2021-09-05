travel_log = [
    {'Country': "France",
     "citis_visited": ['Paris', 'Lille', 'Dijon'],
     "total_visits": 12,
        "distance_traveld": 46,

     },
    {'Country': "Germany",
        "citis_visited": ['Berlin', 'Munich', 'hamburg'],
        "total_visits": 24,
        "distance_traveld": 51,
     }
]


def add_new_country(country, visits, cities):
    new_dict = {
        'Country': country,
        'cities_visited': cities,
        'total_visits': visits,
    }
    travel_log.append(new_dict)


add_new_country('Russia', 2, ["Moscow", "Saint Petersberg"])

print(travel_log)
