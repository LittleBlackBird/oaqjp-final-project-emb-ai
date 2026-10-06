#Iimport the requests library to handle HTTP requests and json for fomatting
import requests
import json

# Define function
def emotion_detector(text_to_analyze):
    # URL of the emotion predict
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Headers required for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Create a dictionary with the text to be analyzed
    json_obj = { "raw_document": { "text": text_to_analyze } }
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = json_obj, headers = header)
    # Format the response into a dictionary
    formatted_response = json.loads(response.text)
    # Extract the dictionary of emotions from the raw payload
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Calculate the dominant emotion using the max() function
    dominant_emotion = max(emotions, key=emotions.get)

    # Return the required formatted dictionary
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
