import streamlit as st
import requests
from datetime import date

st.title('PregWeek')
st.subheader('Calculate the number of weeks for you pregnancy')

conceive_date = st.date_input("Conceive Date", value=date.today())
last_date = st.date_input("Last Date", value=date.today())

if st.button('Calculate'):
    if conceive_date and last_date:
        data = {
            'conceiving_date': conceive_date.isoformat(),
            'last_date': last_date.isoformat()
        }

        try:
            response = requests.post('http://127.0.0.1:8000/v1/calcweeks', json=data)
            if response.status_code == 200:
                result = response.json()['response']
                st.write(f"You are in week {result['weeks']+1} of the pregnancy. How exciting!")
                
            else:
                st.write(f"Failed to send POST request. Status code: {response.status_code}")
                st.write(response.text)
        except Exception as e:
            st.write(f"An error occurred: {e}")
    else:
        st.write("Please select both dates.")
