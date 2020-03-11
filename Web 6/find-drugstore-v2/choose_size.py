def choose_size_geocoder(json_response):
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(' ')

    # Долгота и широта прямоугольника
    size = toponym["boundedBy"]["Envelope"]
    lower_corner_longitude, lower_corner_lattitude = map(float, size["lowerCorner"].split())
    upper_corner_longitude, upper_corner_lattitude = map(float, size["upperCorner"].split())

    # Размер прямоугольника в градусной мере
    delta = str(min(upper_corner_longitude - lower_corner_longitude, upper_corner_lattitude -
                    lower_corner_lattitude))

    return toponym_longitude, toponym_lattitude, delta


def choose_size_search_api(json_response):
    toponym = json_response
    toponym_coodrinates = toponym['geometry']['coordinates']
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates
    # Долгота и широта прямоугольника
    size = toponym['properties']['boundedBy']
    lower_corner_longitude, lower_corner_lattitude = size[0]
    upper_corner_longitude, upper_corner_lattitude = size[1]

    # Размер прямоугольника в градусной мере
    delta = str(min(abs(upper_corner_longitude - lower_corner_longitude),
                    abs(upper_corner_lattitude - lower_corner_lattitude)))

    return toponym_longitude, toponym_lattitude, delta
