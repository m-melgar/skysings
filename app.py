from flask import Flask, render_template
import test2
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)


@app.route('/')
def index():
    # Call the generate_image function
    out = test2.call_astral()

    data = [
        {"text": out["sun"], "gif": "sun.gif"},
        {"text": out["moon"], "gif": "moon.gif"},
        {"text": out["mercury"], "gif": "mercury.gif"},
        {"text": out["venus"], "gif": "venus.gif"},
        {"text": out["mars"], "gif": "mars.gif"},
        {"text": out["jupiter"], "gif": "jupiter.gif"},
        {"text": out["saturn"], "gif": "saturn.gif"},
        {"text": out["uranus"], "gif": "uranus.gif"},
        {"text": out["neptune"], "gif": "neptune.gif"},
        {"text": out["pluto"], "gif": "pluto.gif"},

        # Add more data for each GIF and text pair
    ]
    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('dynamic_template.html')

    # Render the template with the data
    html_output = template.render(items=data)

    # Save the generated HTML to a file
    with open('./templates/index.html', 'w') as f:
        f.write(html_output)

    # Render a simple HTML template
    return render_template('index.html')

@app.route('/horoscopo')
def horoscope():
    # Reverse the order of horoscope_data
    zodiac_data = test2.call_astral(reversed=True)

    print(zodiac_data)

    env_2 = Environment(loader=FileSystemLoader('.'))
    template = env_2.get_template('dynamic_template_horoscopo.html')

    # Render the template with the data
    html_output = template.render(zodiac_data=zodiac_data)

    # Save the generated HTML to a file
    with open('./templates/index_horoscopo.html', 'w') as f:
        f.write(html_output)

    # Pass the reversed data to the template
    return render_template('index_horoscopo.html')

if __name__ == '__main__':
    app.run(debug=True)
