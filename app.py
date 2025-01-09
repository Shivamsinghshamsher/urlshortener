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

@app.route('/about')
def about():
    content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About Us</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
                line-height: 1.6;
                color: #333;
            }
            h1, h2, h3 {
                color: #0056b3;
            }
            ul {
                padding-left: 20px;
            }
            li {
                margin-bottom: 10px;
            }
            .container {
                max-width: 800px;
                margin: auto;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 8px;
                background: #f9f9f9;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>About Shivam's URL Shortener</h1>
            <p>
                Welcome to Shivam's URL Shortener, a platform designed to make long and cumbersome URLs short, manageable, and shareable.
            </p>
            <h2>Our Mission</h2>
            <p>
                Our mission is to simplify your online interactions by providing a reliable and efficient URL shortening service. 
                We aim to help individuals, businesses, and developers optimize their link-sharing process while maintaining the integrity 
                and security of their content.
            </p>
            <h2>Why Choose Us?</h2>
            <ul>
                <li><strong>User-Friendly:</strong> No complicated steps—just paste your URL, click shorten, and you’re good to go!</li>
                <li><strong>Secure Links:</strong> Your privacy matters. We ensure that your links are safe and trustworthy.</li>
                <li><strong>Customizable:</strong> Create custom aliases for your links to make them more personal or brand-aligned.</li>
                <li><strong>Analytics:</strong> Gain insights into how your links perform with advanced click tracking (upcoming feature).</li>
            </ul>
            <h2>How It Works</h2>
            <ol>
                <li>Paste: Enter your long URL into our input field.</li>
                <li>Shorten: Click the "Shorten" button, and within seconds, get a short and shareable link.</li>
                <li>Share: Use the shortened link anywhere—social media, emails, or blogs.</li>
            </ol>
            <h2>About the Creator</h2>
            <p>
                Shivam Singh, the founder of Shivam's URL Shortener, is passionate about simplifying everyday tasks using technology. 
                With expertise in Python development and a drive to create user-friendly tools, Shivam strives to deliver services that make a difference.
            </p>
        </div>
    </body>
    </html>
    """
    return content

@app.route('/contact')
def contact():
    content = """
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        p {
            font-size: 1.1em;
            line-height: 1.6;
            color: #555;
        }
        .contact-info {
            margin-top: 20px;
            padding: 10px;
            background-color: #f0f0f0;
            border-radius: 8px;
        }
        .contact-info strong {
            color: #333;
        }
        .contact-info a {
            color: #007bff;
            text-decoration: none;
        }
    </style>
    
    <div class="container">
        <h1>Contact Us</h1>
        <p>If you have any questions or need assistance, feel free to reach out to us.</p>
        
        <div class="contact-info">
            <p><strong>Mobile Number:</strong> 7667265451</p>
            <p><strong>Email:</strong> <a href="mailto:kumarshivam3133s@gmail.com">kumarshivam3133s@gmail.com</a></p>
        </div>

        <p>We are always happy to assist you!</p>
    </div>
    """
    return content



if __name__ == '__main__':
    app.run(debug=True)
