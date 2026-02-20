import requests

def get_user_location():
    try:
        # API 1: Localización por IP
        res = requests.get("http://ip-api.com/json/", timeout=5).json()
        if res.get("status") == "success":
            return res.get("city", "Mexico City"), res.get("countryCode", "MX")
        return "Mexico City", "MX"
    except Exception as e:
        print(f"Error en ubicación: {e}")
        return "Mexico City", "MX"

def get_environmental_data():
    city, country = get_user_location()
    
    # API 2: Calidad del Aire (OpenAQ)
    try:
        air_res = requests.get(
            f"https://api.openaq.org/v2/latest?city={city}&limit=1", 
            timeout=5,
            headers={'accept': 'application/json'}
        ).json()
        
        if air_res.get("results") and len(air_res["results"]) > 0:
            measurements = air_res["results"][0].get("measurements", [])
            if measurements:
                measure = measurements[0]
                air = {
                    "value": round(measure.get('value', 12.4), 1), 
                    "unit": measure.get('unit', 'µg/m³'), 
                    "city": city
                }
            else:
                air = {"value": 12.4, "unit": "µg/m³", "city": city}
        else:
            air = {"value": 12.4, "unit": "µg/m³", "city": city}
    except Exception as e:
        print(f"Error en OpenAQ: {e}")
        air = {"value": 12.4, "unit": "µg/m³", "city": city}

    # API 3: Posts de DummyJSON
    try:
        posts_res = requests.get("https://dummyjson.com/posts?limit=5", timeout=5).json()
        posts = posts_res.get("posts", [])
    except Exception as e:
        print(f"Error en DummyJSON: {e}")
        posts = []

    # API 4: Videos de YouTube - IDs verificados que funcionan
    videos = [
    {"id": "wc_65-yf6zU", "title": "🌱 ¿En qué consiste la economía circular? | ACCIONA"},
    {"id": "3pX5raKTYQc", "title": "⚡ Energías Renovables y No Renovables | A Cierta Ciencia"},
    {"id": "Wka0KQmCL3w", "title": "💧 ¿Cómo superar la Crisis Mundial del Agua? | CuriosaMente"}
    ]

    return air, posts, videos