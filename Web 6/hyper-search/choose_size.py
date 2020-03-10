def choose_size(json_response):
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    # Долгота и широта прямоугольника
    size = toponym["boundedBy"]["Envelope"]
    lower_corner_longitude, lower_corner_lattitude = map(float, size["lowerCorner"].split())
    upper_corner_longitude, upper_corner_lattitude = map(float, size["upperCorner"].split())

    # Размер прямоугольника в градусной мере
    delta = str(min(upper_corner_longitude - lower_corner_longitude, upper_corner_lattitude -
                    lower_corner_lattitude))

    return toponym_longitude, toponym_lattitude, delta