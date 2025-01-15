
import pandas as pd
import pickle
import streamlit as st

with open("breast_cancer.pkl", "rb") as file:
       model = pickle.load(file)

parameters = ['clump_thickness', 'uniformity_of_cell_size',
       'uniformity_of_cell_shape', 'marginal_adhesion',
       'single_epithelial_cell_size', 'bare_nuclei', 'bland_chromatin',
       'normal_nucleoli', 'mitoses']

st.title("Breast Cancer Prediction App..")
st.info("WITH THE APPROPRIATE PARAMETER THE MODEL PREDICTS IF A PERSON IS PRONE TO BREAST CANCER OR NOT")
st.write(""" ## The parameters to be inputed are
        Clump_Thickness:
         Uniformity of cell size:
         Uniformity of cell shape:
         Marginal Adhesion:
         Single epithelial cell size:
         Bare nuclei:
         Bland Chromatin:
         Normal Nucleoi:
         Mitoses: """)
st.sidebar.subheader("USER INPUT PARAMETER FOR A SPECIFIC PATIENT")

def user_input():
       clump_thickness = st.sidebar.slider("clump_thickness", 1,10,4)
       uniformity_of_cell_size = st.sidebar.slider("uniformity_of_cell_sizie", 1, 10, 5)
       uniformity_of_cell_shape = st.sidebar.slider("uniformity_of_cell_shape", 1, 10,3)
       marginal_adhesion = st.sidebar.slider('marginal_adhesion', 1,10,5)
       single_epithelial_cell_size = st.sidebar.slider('single_epithelial_cell_size', 1, 10, 3)
       bare_nuclei = st.sidebar.slider('bare_nuclei', 1,10, 5)
       bland_chromatin = st.sidebar.slider("bland_chromatin", 1, 10, 4)
       normal_nucleoli = st.sidebar.slider("normal_nucleoli", 1, 10, 6)
       mitoses = st.sidebar.slider("mitoses", 1, 10, 4)
       features = {'clump_thickness':clump_thickness, 'uniformity_of_cell_size':uniformity_of_cell_size,
       'uniformity_of_cell_shape': uniformity_of_cell_shape, 'marginal_adhesion':marginal_adhesion,
       'single_epithelial_cell_size':single_epithelial_cell_size, 'bare_nuclei':bare_nuclei, 'bland_chromatin':bland_chromatin,
       'normal_nucleoli':normal_nucleoli, 'mitoses':mitoses}
       data = pd.DataFrame(features, index=[0])
       return data

st.subheader("User input Parameter for a patient")

df = user_input()

st.write(df)

st.markdown("## Prediction")
pred = model.predict(df)

if pred == 1:
       st.write(pred)
       st.info("The patient is cancerous")

else:
       st.write(pred)
=======
import pandas as pd
import pickle
import streamlit as st

with open("breast_cancer.pkl", "rb") as file:
       model = pickle.load(file)

parameters = ['clump_thickness', 'uniformity_of_cell_size',
       'uniformity_of_cell_shape', 'marginal_adhesion',
       'single_epithelial_cell_size', 'bare_nuclei', 'bland_chromatin',
       'normal_nucleoli', 'mitoses']

st.title("Breast Cancer Prediction App..")
st.info("WITH THE APPROPRIATE PARAMETER THE MODEL PREDICTS IF A PERSON IS PRONE TO BREAST CANCER OR NOT")
st.write(""" ## The parameters to be inputed are
        Clump_Thickness:
         Uniformity of cell size:
         Uniformity of cell shape:
         Marginal Adhesion:
         Single epithelial cell size:
         Bare nuclei:
         Bland Chromatin:
         Normal Nucleoi:
         Mitoses: """)
st.sidebar.subheader("USER INPUT PARAMETER FOR A SPECIFIC PATIENT")

def user_input():
       clump_thickness = st.sidebar.slider("clump_thickness", 1,10,4)
       uniformity_of_cell_size = st.sidebar.slider("uniformity_of_cell_sizie", 1, 10, 5)
       uniformity_of_cell_shape = st.sidebar.slider("uniformity_of_cell_shape", 1, 10,3)
       marginal_adhesion = st.sidebar.slider('marginal_adhesion', 1,10,5)
       single_epithelial_cell_size = st.sidebar.slider('single_epithelial_cell_size', 1, 10, 3)
       bare_nuclei = st.sidebar.slider('bare_nuclei', 1,10, 5)
       bland_chromatin = st.sidebar.slider("bland_chromatin", 1, 10, 4)
       normal_nucleoli = st.sidebar.slider("normal_nucleoli", 1, 10, 6)
       mitoses = st.sidebar.slider("mitoses", 1, 10, 4)
       features = {'clump_thickness':clump_thickness, 'uniformity_of_cell_size':uniformity_of_cell_size,
       'uniformity_of_cell_shape': uniformity_of_cell_shape, 'marginal_adhesion':marginal_adhesion,
       'single_epithelial_cell_size':single_epithelial_cell_size, 'bare_nuclei':bare_nuclei, 'bland_chromatin':bland_chromatin,
       'normal_nucleoli':normal_nucleoli, 'mitoses':mitoses}
       data = pd.DataFrame(features, index=[0])
       return data

st.subheader("User input Parameter for a patient")

df = user_input()

st.write(df)

st.markdown("## Prediction")
pred = model.predict(df)

if pred == 1:
       st.write(pred)
       st.info("The patient is cancerous")

else:
       st.write(pred)
       st.info("The patient is non cancerous")
