# Author: Prakash Sukhwal
# Aug 2021

import streamlit as st
# other libs
import numpy as np
import pandas as pd
import pickle

from sklearn.preprocessing import StandardScaler

# import pyautogui # for reset button: pip install pyautogui

# load the model.pkl
# path = r'C:\temp\model.pkl'
with open('model.pkl', "rb") as f:
	model = pickle.load(f)

# Streamlit provides a caching mechanism that allows your app to stay performant 
# even when loading data from the web, manipulating large datasets, 
# or performing expensive computations. This is done with the @st.cache decorator.
@st.cache()

def prediction(age, salary):
	# Making predictions
	prediction = model.predict([[age,salary]])
	if prediction == 0:
		pred = 'Not Buy'
	else:
		pred = 'Buy'
	return pred


# putting the app related codes in main()
def main():
	# -- Set page config
	apptitle = 'DSSI Test Logistic App'
	st.set_page_config(page_title=apptitle, page_icon='random', 
		layout= 'wide', initial_sidebar_state="expanded")
	# random icons in the browser tab

	# give a title to your app
	st.title('Solution Implementation')
	#front end elements of the web page 
	# pick colors from: https://www.w3schools.com/tags/ref_colornames.asp
	html_temp = """ <div style ="background-color:AntiqueWhite;padding:15px"> 
       <h1 style ="color:black;text-align:center;">Buy Car Assessment App</h1> 
       </div> <br/>"""

    #display the front end aspect
	st.markdown(html_temp, unsafe_allow_html = True)
	# let us make infrastructure to provide inputs
	# we will add the inputs to side bar
	st.sidebar.info('Provide input using the panel')
	st.info('Click Assess button below')

	age = st.sidebar.slider('age', 16, 100, 20)
	st.write('input age', age)
	salary = st.sidebar.slider('salary in 1000s', 10, 100, 60)
	st.write('input salary', salary*1000)
	    
	result =""
	# assessment button
	if st.button("Predict"):
		assessment = prediction(age, salary)
		st.success('**System assessment says:** {}'.format(assessment))

	# if st.button("Reset"):
	# 	pyautogui.hotkey("ctrl","F5")

	# st.balloons()
	st.success("App is working!!") # other tags include st.error, st.warning, st.help etc.

if __name__ == '__main__':
	main()
