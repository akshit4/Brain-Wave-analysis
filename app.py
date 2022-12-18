# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 11:56:33 2022

@author: LENOVO
"""

import gradio as gr
import pickle

def make_prediction(AF3,F7,F3,FC5,T7,P7,O1,O2,P8,T8,FC6,F4,F8,AF4):
    with open("RandomForest.pkl", "rb") as f:
        clf = pickle.load(f)
        preds = clf.predict([[AF3,F7,F3,FC5,T7,P7,O1,O2,P8,T8,FC6,F4,F8,AF4]])
    if preds == 1:
        return "You to understand topic study hard."        
    return "You unable to understand topic study hard."

#Create the input component for Gradio since we are expecting 4 inputs

AF3 = gr.Number(label = "Enter the AF3")
F7 = gr.Number(label = "Enter the F7")
F3 = gr.Number(label = "Enter the F3")
FC5 = gr.Number(label = "Enter the FC5")
T7 = gr.Number(label = "Enter the T7")
P7 = gr.Number(label = "Enter the P7")
O1 = gr.Number(label = "Enter the O1")
O2 = gr.Number(label = "Enter the O2")
P8 = gr.Number(label = "Enter the P8")
T8 = gr.Number(label = "Enter the T8")
FC6 = gr.Number(label = "Enter the FC6")
F4 = gr.Number(label = "Enter the F4")
F8 = gr.Number(label = "Enter the F8")
AF4 = gr.Number(label = "Enter the AF4")


# We create the output
output = gr.Textbox()


app = gr.Interface(fn = make_prediction, 
                   inputs=[AF3,F7,F3,FC5,T7,P7,O1,O2,P8,T8,FC6,F4,F8,AF4], 
                   outputs=output)
app.launch(share=True)