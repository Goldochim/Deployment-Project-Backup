# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 19:36:49 2020
@author: DELL
"""

import streamlit as st
import pickle
import sklearn

clf=pickle.load(open(clf_job.pkl, 'rb'))

def welcome():
    return "Welcome All"

def job_Prediction(Gender, Course, School_Type,Qualification, Job_Search_Mode):
    prediction=clf.predict(['Gender', 'Course', 'School_Type', 'Qualification', 'Job_Search_Mode'])
    print(prediction)
    return 'The prediction value is'+ prediction

def main():
    st.title("First Job Predictor")
    html_temp="""
    <div style="background-color:tomato;padding:8px">
    <h2 style="color:white;text-align:center;"> Job via NYSC predictor</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    Gender=st.text_input("GENDER (0=Male, 1=Female)", " ")
    Course=st.text_input("COURSE (Type a number between 1-121, check list for school names)", " ")
    School_Type=st.text_input("SCHOOL_TYPE (0=state, 1=Federal , 2=Indigenous , 3=Foreign , 4=Private)", " ")
    Qualification=st.text_input("QUALIFICATION (0=Masters, 1=HND, 2=PhD, 3=OND, 4=Bachelors)", " ")
    Job_Search_Mode=st.text_input("JOB_SEARCH MODE (0=UnI/poly, 1=Personal contacts, 2=Employer's website, 3=Media, 4=Recruitment agency-online or offline,5=Social Media, 6=Internship)", " ")
    result=""
    if st.button("Predict"):
        result=job_Prediction(Gender, Course, School_Type,Qualification, Job_Search_Mode)
    st.success('The first job prediction via NYSC is {}'.format(result))
    if st.button("Prediction Note"):
        st.text("0-No, No job via NYSC, 1=Yes, job via NYSC")
        
if __name__=='__main__':
    main()
