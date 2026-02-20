# EcoPulse Dashboard

Aplicación web interactiva que visualiza datos ambientales en tiempo real, fomenta la conciencia ecológica y permite a los usuarios registrar sus acciones sostenibles.

## Capturas de Pantalla

### Página Principal (Dashboard)
<img width="1315" height="596" alt="image" src="https://github.com/user-attachments/assets/bef8c99c-e5b3-41bb-9694-c23cf97eb997" />

### Página Informativa (Comunidad)
<img width="1187" height="609" alt="image" src="https://github.com/user-attachments/assets/d87df17d-009c-4f5c-a5e5-8c1473c7aad4" />

---

## Descripción del Proyecto

**EcoPulse** es un dashboard educativo que conecta a los usuarios con información ambiental relevante a través de múltiples APIs. Su objetivo es sensibilizar sobre problemas ecológicos actuales y promover pequeñas acciones cotidianas que contribuyan al cuidado del planeta.

### Importancia
- **Conciencia Ambiental**: Presenta datos reales sobre calidad del aire, deforestación, crisis del agua y más.
- **Educación Interactiva**: Los usuarios pueden aprender mediante artículos verificados y videos educativos.
- **Participación Activa**: Permite registrar acciones sostenibles, creando un historial personal de logros.
- **Visualización Clara**: Diseño moderno e intuitivo que facilita la comprensión de la información.

---

---

## Funcionalidades Principales

### 🔹 Página Principal (Dashboard)
- **Calidad del Aire en Tiempo Real**: Muestra datos de PM2.5 de la ciudad del usuario vía API de OpenAQ.
- **Registro de Acciones Sostenibles**: Los usuarios pueden escribir y guardar sus "eco-acciones".
- **Historial Interactivo**: Listado de logros con imágenes aleatorias y opción de eliminar entradas.

### 🔹 Página Informativa (Comunidad)
- **Dossier Ambiental**: 6 tarjetas con problemáticas ecológicas actuales:
  - Océanos de Plástico
  - Energía del Futuro
  - Deforestación Global
  - Abejas en Peligro
  - Glaciares en Retroceso
  - Moda Sostenible
- **Eco-Streaming**: Reproductor de videos educativos de YouTube sobre:
  - Economía Circular
  - Energías Renovables
  - Crisis Mundial del Agua

---

## 🔌 APIs Utilizadas

| API | Propósito | Endpoint |
|-----|-----------|----------|
| **ip-api.com** | Geolocalización del usuario | `http://ip-api.com/json/` |
| **OpenAQ** | Calidad del aire por ciudad | `https://api.openaq.org/v2/latest` |
| **DummyJSON** | Posts de ejemplo (red social) | `https://dummyjson.com/posts` |
| **YouTube** | Videos educativos embebidos | IDs fijos de videos |

---

## ⚙️ Tecnologías Implementadas

- **Backend**: Python con Flask
- **Frontend**: HTML, Tailwind CSS, FontAwesome
- **APIs**: Requests (consumo de APIs REST)
- **Control de Versiones**: Git + GitHub

---
