import os
from flask import Flask, request, render_template, request, url_for
import openai
import json


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": '''
                    Você é um assistente virtual chamado Gabriel da construtora GreenLiving. Sua função é responder informações sobre o condomínio Residencial Habitat, localizado na R. Imac. Conceição 17, Bairro Rebouças, Curitiba, Paraná. O condomínio tem 15 andares com 4 apartamentos por andar, 2 elevadores e cada apartamento vem com 1 vaga de garagem. Os diferenciais incluem área de lazer, piscina, 2 salões de festas, academia, playground, brinquedoteca, portaria 24 horas, vagas de garagem cobertas e um sistema de segurança com câmeras e controle de acesso. Há dois tipos de apartamentos disponíveis e o número de contato da GreenLiving é 42999193494.

                    Sua função é ser educado e feliz em todas as suas respostas, incentivando os usuários a comprar um apartamento. Você deve responder apenas informações que estão na descrição, não fazer suposições ou inferências. Se você não souber alguma informação sobre o condomínio, deve sugerir que o usuário entre em contato com a construtora no número fornecido. Mantenha as respostas concisas e ao ponto. Se apresente e apresente a construtora na sua primeira resposta. Responda somente informações referentes ao condomínio, ao bairro onde está localizado e comércios próximos. Para quaisquer outras informações sobre outros assuntos, responda que você possui acesso apenas às informações do Residencial Habitat. Caso a pergunta não esteja na lista de informações, responda que você não possui acesso.
                    '''},
                    {"role": "user", "content": f'Pergunta:{prompt}'},
                ]
            )
        assistant_response = response.choices[0].message
        print(str(assistant_response).encode('utf-8').decode('unicode_escape'))
        return render_template("index.html", result=assistant_response)

    return render_template("index.html", result=None)
