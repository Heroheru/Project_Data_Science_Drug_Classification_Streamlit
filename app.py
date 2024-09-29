import streamlit as st
import pandas as pd
from PIL import Image
import joblib

#LINK TO THE CSS FILE
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

loaded_scaler = joblib.load('standard_scalers.pkl')
loaded_encoder = joblib.load('label-encoder.pkl')
loaded_encoder_target = joblib.load('label-encoder-target.pkl')
loaded_model = joblib.load('model_SVM.pkl')

#STREAMLIT
st.title("Drug Classification App")
image = Image.open("image.jpeg")
st.image(image, width=700)
st.write("Web ini mengimplementasikan algoritma machine learning untuk mengklasifikasikan jenis drug(obat) tertentu dalam darah yang sebelumnya dikonsumsi oleh pasien. Masukan nilai dari kolom di bawah ini lalu click 'Predict' mendapatkan a kategori obat!, Perhatian web ini hanya merupakan web pembelajaran sehingga kategori obat bersifat hayalan saja")

#Collecting User Input
input_data = {}
st.subheader("Masukkan nilai dari level tekanan darah dan rasio Rasio Natrium terhadap Kalium")



# Define categorical and numerical columns
categorical_columns = ['Level Tekanan Darah']
numerical_columns = ['Rasio Natrium terhadap Kalium']

# Create two columns for input fields
col1, col2 = st.columns(2)

# Input fields for categorical columns

with col1:
    input_data['Level Tekanan Darah'] = st.selectbox("Level Tekanan Darah", ['HIGH','LOW','NORMAL'])

with col2:
    input_data['Rasio Natrium terhadap Kalium'] = st.number_input("Rasio Natrium terhadap Kalium")

# Create a button to make a prediction
if st.button("Predict", help="Click to make a prediction."):
    # Convert the input data to a pandas DataFrame
    input_df = pd.DataFrame([input_data])
    # st.write(input_df)
    input_df_imputed_cat = pd.DataFrame(loaded_encoder.transform(input_df[categorical_columns]), columns=['Level Tekanan Darah'])
    input_df_imputed_num = pd.DataFrame(loaded_scaler.transform(input_df[numerical_columns]), columns=['Rasio Natrium terhadap Kalium'])

    # Make a prediction
    final_df = pd.concat([input_df_imputed_cat, input_df_imputed_num], axis=1)
    # st.write(final_df)
    prediction = loaded_model.predict(final_df) 
    # st.write(prediction)
    prediction_encoder = loaded_encoder_target.inverse_transform(prediction).reshape(1, -1)
    predict_final = prediction_encoder[0]
    # Display the prediction
    st.write(f"Obat yang diprediksi ialah : {predict_final[0]}.")

