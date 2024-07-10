import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
 
# load model
model = load_model('model.h5')

length=20
features=1

#getting the training data
df=pd.read_csv('ASIANPAINT.csv')
HDFC_close=df['Close']
HDFC_close=pd.DataFrame(HDFC_close)
train_length=int(0.8*len(HDFC_close))
HDFC_train=HDFC_close.iloc[:train_length]
scaler = MinMaxScaler()
scaler.fit(HDFC_train)
scaled_train=scaler.transform(HDFC_train)
scaled_train=scaled_train.reshape(len(scaled_train),1)

def show_predict_page():
    st.title("Stock Price Prediction")
    st.write("")
    st.subheader("Stock Data from 2018 to 2022")
    st.dataframe(df[:50])
    st.write("")
    st.subheader("Future Predictions for How Many Days?")
    days=st.slider("",0,90,10)

    clicked=st.button("Predict Stock Price")

    if (clicked):
        forecast=[]
        current_batch=scaled_train[-length:]
        current_batch=current_batch.reshape((1,length,features))
        for i in range(days):
            current_pred=model.predict(current_batch)[0]
            forecast.append(current_pred)
            current_batch=np.append(current_batch[:,1:,:],[[current_pred]],axis=1)
        forecast=scaler.inverse_transform(forecast)
        df_array=np.array(HDFC_close)
        full_data=pd.DataFrame(np.concatenate((df_array.flatten(),forecast.flatten())))

        output_string="Graph showing Stock price for next "+str(days) +" days"
        st.header(output_string)
        st.line_chart(full_data)


