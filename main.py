import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    if split_message[-1] == 'salir':
        exit()
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Un saludote de ogro!', ['hola', 'buenas tardes', 'saludos', 'buenas'], single_response = True)
        response('Que adentro!', ['mejor afuera', 'mejor fuera'], single_response = True)
        response('No tengo amigos', ['amigos', 'tienes', 'tengo'], required_words=['amigos'])
        response('Vivo en una ciénaga, he puesto carteles y soy un ogro aterrador. ¿Qué tendré que hacer para tener intimidad?'
            , ['vives', 'ubicado', 'visitarte', 'visito', 'eres'], required_words=['donde'], single_response = True)
        response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
        response('Doy clases los jueves no cobro mucho', ['das', 'tienes', 'cuando'], required_words=['clases'], single_response=True)
        response('Los ogros son… ¡cómo cebollas!', ['ogro', 'eres', 'es'],required_words=['que'])
        response('No quisiera que nos apresuráramos a tener una relación más íntima. No estoy emocionalmente preparado para un compromiso tan… tan grandísimo'
                , ['besar'], required_words=['puedo'],single_response=False)
        response('Esto es de antología… el ogro se ha enamorado de la princesa', ['amor', 'gustas', 'amas', 'quieres'], required_words=['me'])
        response('Auch, oye, cuidado con mis nachas!', ['toque', 'tocar', 'agarrar', 'abrazar'], required_words=['te'])
        response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)
        response('Vamos princesa, no eres tan fea. Bueno, sí. Eres fea, pero sólo eres así doce horas al día.',
                    ['soy', 'estoy', 'que tan'] , required_words=['guapo'] , single_response=True)

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknownResponse() if highest_prob[best_match] < 1 else best_match

def unknownResponse():
    response = ['¿Quién dijo eso? No fue el burrito', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][random.randrange(3)]
    return response

def main():
    print('--- Bienvenido al ShrekBot ---')
    print('Escribe "salir" para terminar la conversación')
    while True:
        print("Shrek: " + get_response(input('Tu: ')))

if (__name__ == '__main__'):
    main()