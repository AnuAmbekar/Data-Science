import streamlit as st
import pickle

st.write('### Loan Prediction')

dependents = st.slider(label='How many dependents?', min_value=0, max_value=5)
education = st.radio(label='Tertiary education or not?', options=['Yes', 'No'])

if education == 'Yes':
    education = 0
else:
    education = 1

self_employed = st.radio(label='Self employed?', options=['Yes', 'No'])
if self_employed == 'Yes':
    self_employed = 0
else:
    self_employed = 1

income_annum = st.number_input(label='Annual income?')
loan_amount = st.number_input(label='Loan amount?')
loan_term = st.number_input(label='Loan term?')
cibil_score = st.number_input(label='Credit score?')
residential_assets_value = st.number_input(label='Residential assets value?')
commercial_assets_value = st.number_input(label='Commercial assets value?')
luxury_assets_value = st.number_input(label='Luxury assets value?')
bank_asset_value = st.number_input(label='Bank assets value?')

print(income_annum)
dbfile = open('C://Users/anurag/Documents/Python/Loan/important', 'rb')    
model = pickle.load(dbfile)

prediction = model.predict([[dependents, education, self_employed, income_annum, loan_amount, loan_term, cibil_score,
                            residential_assets_value, commercial_assets_value, luxury_assets_value, bank_asset_value]])

if prediction == 0:
    st.write('No')
else:
    st.write('Yes')
