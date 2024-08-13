import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np
import joblib  # Assuming your trained model is saved as a .pkl file

st.set_page_config(layout="wide")

# Load the trained model (adjust the filename to your actual model file)
model = joblib.load('model_xgb_quality_prediction.pkl')
X = pd.read_csv('data_X.csv')
X = X.drop('date_time', axis=1)

# Define the structure of your DataFrame
def create_template_dataframe():
    columns = ['timestamp'] + ['predicted_quality'] + [X.columns[i] for i in range(17)]
    return pd.DataFrame(columns=columns)

# Function to add new input data to the DataFrame
def add_row_to_dataframe(df,features,prediction):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_row = pd.Series([timestamp] +[prediction] + features, index=st.session_state.df.columns)
    (st.session_state.df).loc[len(df)] = new_row
    return st.session_state.df


# Function to make predictions
def predict_quality(features):
    features_array = np.array(features).reshape(1, -1)  # Reshape for a single prediction
    prediction = model.predict(features_array)
    return prediction[0]

# Streamlit app UI
st.title("Quality Prediction App")

# Create an empty DataFrame with the required columns
if 'df' not in st.session_state:
    st.session_state.df = create_template_dataframe()

# Create columns for horizontal layout
cols = st.columns(17)

# Display the median values of the features
stat_X = X.describe()

# Create input fields for the 17 features, arranged horizontally
features = []
for i, col in enumerate(cols):
    feature_input = col.number_input(f'{X.columns[i]}', value=stat_X.loc['50%', :][i], format="%.2f")
    features.append(feature_input)

# Button to submit the features and get prediction
if st.button("Submit and Predict Quality"):
    # Add a new row to the DataFrame
    predicted_quality = round(predict_quality(features),0)
    st.session_state.df = add_row_to_dataframe(st.session_state.df,features,predicted_quality)
    
    
    # Display the results
    st.subheader(f"Predicted Quality: {predicted_quality:.0f}")
    st.write("Updated DataFrame:")
    st.write(st.session_state.df)

