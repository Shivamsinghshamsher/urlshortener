from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

# Function to shorten URLs
def shorten_url(long_url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(long_url)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['long_url']
    if long_url:
        try:
            short_url = shorten_url(long_url)
            return render_template('index.html', short_url=short_url)
        except Exception as e:
            error_message = f"Error: {e}"
            return render_template('index.html', error=error_message)
    return render_template('index.html', error="Please provide a valid URL.")

if __name__ == '__main__':
    app.run(debug=True)
