import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_data = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = json_data, headers = header)
    formatted_resp = json.loads(response.text)
    print(response.status_code) 
    if response.status_code == 200:
        emotion_prediction = formatted_resp['emotionPredictions'][0]['emotion']
        max_key = max(emotion_prediction, key=emotion_prediction.get)
        return {'anger': emotion_prediction['anger'], 'disgust': emotion_prediction['disgust'], 'fear': emotion_prediction['fear'], 
                'joy': emotion_prediction['joy'], 'sadness': emotion_prediction['sadness'], 'dominant_emotion': max_key}
    # If the response status code is 500, set label and score to None
    elif response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None, 
                'joy': None, 'sadness': None, 'dominant_emotion': None}
    else:
        return {'anger': None, 'disgust': None, 'fear': None, 
                'joy': None, 'sadness': None, 'dominant_emotion': None}
