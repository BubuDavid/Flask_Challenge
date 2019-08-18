# Importing important things.
from flask import Flask
from flask import request
from flask import render_template
from flowers import cards
from forms import Flower_Form
from API_reader import get_prediction
from flowers2 import flower

# Declaring my app name.
app = Flask(__name__)

# Define an index function.
@app.route('/', methods=['GET', 'POST'])
def index():

	form = Flower_Form(request.form)
	flag = False

	if request.method == 'POST':
		if form.LS.data is not None and form.AS.data is not None and form.LP.data is not None and form.AP.data is not None:
			print(f"Información capturada: {form.LS.data} {form.AS.data} {form.LP.data} {form.AP.data} ")
			
			response = get_prediction('https://bubufirstapi.glitch.me/api/v0.0/predict', 'response_prediction.json', form.LS.data, form.AS.data, form.LP.data, form.AP.data)

			print()
			print()
			print(response['response'][2]['species'].split()[1])
			flower_specie = response['response'][2]['species'].split()[1]

			print(flower[flower_specie]['photo'])

			return render_template('specie.html', flower_specie = flower_specie, flower = flower)

		else:
			flag = True

	return render_template('index.html', cards = cards, flag=flag)

# run method.
app.run(debug = True, port = 8000)
