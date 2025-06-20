"""This is the server module
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    """Call func to detect emotion"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['disgust'] is None:
        return "Invalid text! Please try again!."
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']}, 'sadness': {response['sadness']}."
        f"The dominant emotion is {response['dominant_emotion']}."
        )

@app.route("/")
def render_index_page():
    """Return standard webpage."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
