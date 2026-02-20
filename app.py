from flask import Flask, render_template, request, redirect, url_for
from services.api_manager import get_environmental_data
import uuid

app = Flask(__name__)
user_tips = [] 

@app.route("/")
def index():
    air, posts, videos = get_environmental_data()
    return render_template("index.html", air=air, tips=user_tips)

@app.route("/comunidad")
def comunidad():
    _, _, videos = get_environmental_data()
    
    
    eco_articles = [
        {"titulo": "Océanos de Plástico", "desc": "8 millones de toneladas de basura llegan al mar cada año, afectando a 700 especies.", "img": "https://images.unsplash.com/photo-1621451537084-482c73073a0f?w=600&auto=format&fit=crop"},
        {"titulo": "Energía del Futuro", "desc": "La energía solar fotovoltaica ya es la fuente de electricidad más barata en la historia.", "img": "https://images.unsplash.com/photo-1509391366360-2e959784a276?w=600&auto=format&fit=crop"},
        {"titulo": "Deforestación Global", "desc": "Perdemos 10 millones de hectáreas de bosque al año, un área del tamaño de Islandia.", "img": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=600&auto=format&fit=crop"},

{"titulo": "Abejas en Peligro", "desc": "El 75% de los cultivos dependen de polinizadores. Su extinción amenaza la seguridad alimentaria.", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Apis_mellifera_Western_honey_bee.jpg/600px-Apis_mellifera_Western_honey_bee.jpg"},

{"titulo": "Glaciares en Retroceso", "desc": "El Ártico se calienta 4 veces más rápido que el resto del planeta por el efecto albedo.", "img": "https://images.pexels.com/photos/533769/pexels-photo-533769.jpeg?auto=compress&cs=tinysrgb&w=600"},
 {"titulo": "Moda Sostenible", "desc": "La industria textil consume 93 mil millones de m³ de agua al año. El reciclaje es clave.", "img": "https://images.unsplash.com/photo-1523381210434-271e8be1f52b?w=600&auto=format&fit=crop"}
    ]
    return render_template("comunidad.html", articles=eco_articles, videos=videos)

@app.route("/add_tip", methods=["POST"])
def add_tip():
    text = request.form.get("tip")
    if text:
      
        eco_images = [
            "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?w=400&h=250&fit=crop",
            "https://images.unsplash.com/photo-1470115636492-6d2b56f9146d?w=400&h=250&fit=crop",
            "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=400&h=250&fit=crop",
            "https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=400&h=250&fit=crop",
            "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=400&h=250&fit=crop"
        ]
        import random
        img_url = random.choice(eco_images)
        
        new_tip = {"id": str(uuid.uuid4()), "text": text, "img": img_url}
        user_tips.insert(0, new_tip)
    return redirect(url_for('index'))

@app.route("/delete_tip/<string:id>")
def delete_tip(id):
    global user_tips
    user_tips = [t for t in user_tips if t['id'] != id]
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
