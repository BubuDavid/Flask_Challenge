from flask import Flask 
from flask import render_template
from flask import request
from sklearn import datasets
from sklearn import svm
import pandas as pd
from sklearn.datasets import load_iris
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn import svm
import graphviz

import forms


iris = load_iris()
data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
le = LabelEncoder()
data['class'] = le.fit_transform(data['class'])
X = np.array(data.drop(['class'], axis=1))
y = np.array(data['class'])
clf = svm.SVC(gamma='scale')
nombres= ['setosa','versicolor','virginica']
características= ['ancho del pétalo (cm)', 'ancho del sepalo (cm)', 'longitud del petalo (cm)', 'ancho del pétalo (cm)']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
	title = "Curso Flask"
	comment_form = forms.CommentForm(request.form)
	if request.method == 'POST' and comment_form.validate():
		parametro1 = comment_form.parametros1.data
		parametro2 = comment_form.parametros2.data
		parametro3 = comment_form.parametros3.data
		parametro4 = comment_form.parametros4.data
		predecir(long_sep, ancho_sep, long_pet, ancho_pet)
	return render_template('index.html', title=title, form=comment_form)

if __name__ == '__main__':
	app.run(debug=True, port=5000)