from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Respuestas predefinidas del chatbot
def chatbot_respuesta(pregunta):
    respuestas = {
        "hola": "¡Hola! ¿Cómo estás?",
        "¿cómo estás?": "Estoy bien, gracias por preguntar. ¿En qué puedo ayudarte?",
        "¿cuál es tu nombre?": "Soy un chatbot creado para ayudarte. ¿Cómo puedo asistirte?",
        "adiós": "¡Hasta luego! Que tengas un buen día.",
        "¿qué puedes hacer?": "Puedo responder preguntas simples y tener una conversación contigo. ¡Pregúntame lo que quieras!"
    }
    return respuestas.get(pregunta.lower(), "Lo siento, no entiendo tu pregunta.")

# Ruta para el chatbot
@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Falta el campo 'message' en la solicitud."}), 400

    pregunta = data.get("message")
    respuesta = chatbot_respuesta(pregunta)
    
    return jsonify({"response": respuesta})

if __name__ == "__main__":
    app.run(debug=True)
