import streamlit as st
import numpy as np
import pickle


loaded_model = pickle.load(open('classifier.pkl','rb'))

def banknote_predict(input_data):
    # changing the array as we are predicting for one instance
    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==0):
        return 'THe NOte is Authentic'
    
    else:
        return 'The Note is Fake'
st.title('Hello World')

def main():
    st.subheader('Enter your values')
    variance = st.text_input('Enter Variance')
    skewness = st.text_input('Enter skewness')
    curtosis = st.text_input('Enter Curtosis')
    entropy = st.text_input('Enter Entropy')

    prediction = ''

    if st.button('Predict the result'):
        prediction = banknote_predict([variance,skewness,curtosis,entropy])

    st.success(prediction)
         


if __name__ =='__main__':
     main()