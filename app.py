from flask import Flask, render_template, request, jsonify
from translatepy import Translator

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate', methods=['POST'])
def translate():
    text_to_translate = request.form.get('textToTranslate', '')
    target_language = request.form.get('targetLanguage', 'en')  # Default to English

    # Use translatepy for translation
    translator = Translator()
    translation_result = translator.translate(text_to_translate, target_language)

    # Access the translated text using the 'text' attribute
    translated_text = translation_result.result

    return jsonify({'translatedText': translated_text})


if __name__ == '__main__':
    app.run(debug=True)
