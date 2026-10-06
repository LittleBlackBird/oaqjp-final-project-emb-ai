from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def e_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('text_to_analyze')
    
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Using implicit string concatenation to keep the code readable 
    # while outputting a single continuous sentence.
    return (
        f"""For the given statement, the system response is "
        'anger': {response['anger']}, 
        'disgust': {response['disgust']}, 
        'fear': {response['fear']}, 
        'joy': {response['joy']} and 
        'sadness': {response['sadness']}. 
        The dominant emotion is {response['dominant_emotion']}."""
    )

@app.route("/")
def render_index_page():
    # Renders the main application page
    return render_template('index.html')

if __name__ == "__main__":
    # Runs the Flask application on port 5000
    app.run(host="0.0.0.0", port=5000)
