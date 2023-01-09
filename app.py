import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))

def predict_insuranceprices(age,smoker,bmi):
    input=np.array([[age,smoker,bmi]])
    prediction=model.predict(input)
    return(prediction[0])

def main():
    st.title("Streamlit Tutorial")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Medical Insurance Price Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)


    age = st.text_input("age","Type Here")
    smoker = st.text_input("smoker","Type Here")
    bmi = st.text_input("bmi","Type Here")
    

    if st.button("Predict"):
        output=predict_insuranceprices(age,smoker,bmi)
        st.success('The insurance price is {}'.format(output))

        

if __name__=='__main__':
    main()