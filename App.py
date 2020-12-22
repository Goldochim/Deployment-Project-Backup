# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 19:36:49 2020
@author: DELL
"""

import streamlit as st
import pickle

clf = pickle.load(open("classifier.pkl", 'rb'))

def welcome():
    return "Welcome All"

def job_Prediction(Gender, Course, School_Type,Qualification, Job_Search_Mode):
    prediction=clf.predict(['Gender', 'Course', 'School_Type', 'Qualification', 'Job_Search_Mode'])
    print(prediction)
    return 'The prediction value is'+ prediction

def main():
    st.title("First Job Predictor")
    html_temp="""
    <div style="background-color:AntiqueWhite1;padding:10px">
    <h2 style="color:white;text-align:center;"> Job via NYSC predictor</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    Gender=st.text_input("Gender", "Type here")
    Course=st.text_input("Course", "Type here")
    School_Type=st.text_input("School_Type", "Type here")
    Qualification=st.text_input("Qualification", "Type here")
    Job_Search_Mode=st.text_input("Job_Search_Mode", "Type here")
    result=""
    if st.button("Predict"):
        result=job_Prediction(Gender, Course, School_Type,Qualification, Job_Search_Mode)
    st.success('The first job prediction via NYSC is {}'.format(result))
    if st.button("Prediction Note"):
        st.text("0-No, No job via NYSC, 1=Yes, job via NYSC")
        
if __name__=='__main__':
    main()
