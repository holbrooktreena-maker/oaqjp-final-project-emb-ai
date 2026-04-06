"""
Executing this function initiates the application of emotion
detection to be executed over the Flask channel and deployed on
localhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    This code receives the text from the HTML interface and 
    runs emotion detection over it using emotion_detector()
    function. The output returned is the raw dictionary format.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Task 7: Error handling for blank entries or invalid input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    # Return the dictionary directly to match the customer's requested format
    return response

@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application
    page over the Flask channel.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Deploys the flask app on localhost:5000
    app.run(host="0.0.0.0", port=5000)