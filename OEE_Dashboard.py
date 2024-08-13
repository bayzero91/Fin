# Visualization of the OEE
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.graph_objects as go


st.set_page_config(layout="wide")

st.title("OEE Dashboard")
# add sidebar
st.sidebar.title("OEE Dashboard")

# add imputbox for the availability
availability = st.sidebar.number_input("Enter the availability for OEE", min_value=0, max_value=100, value=79)

# add imputbox for the performance
performance = st.sidebar.number_input("Enter the performance for OEE", min_value=0, max_value=100, value=85)

# add imputbox for the quality
quality = st.sidebar.number_input("Enter the quality for OEE", min_value=0, max_value=100, value=95)

# calculate the OEE
OEE = availability * performance * quality / 10000

cols = st.columns(2)

########## Visualization of the OEE ##########'
with cols[0]:
    fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = OEE,
    mode = "gauge+number+delta",
    title = {'text': "OEE"},
    delta = {'reference': 80},
    gauge = {'axis': {'range': [None, 120], "tickwidth": 1, "tickcolor": "black"},
                'bar': {'color': "black"},
                'steps' : [
                    {'range': [0, 45], 'color': "#b02525"},
                    {'range': [45, 70], 'color': "#dae019"},
                    {'range': [60,100], 'color': "#46a340"},
                    {'range': [100, 120], 'color': "#dae019"}],
                
                'threshold' : {'line': {'color': "black", 'width': 2}, 'thickness': 0.8, 'value': 80}}))
    st.plotly_chart(fig)
########## Visualization of the OEE ##########'
   
with cols[1]:
    goal = 100
    lith_dict = {'LITH': ["Goal", "Avalability", "Performance", "Quality"],
                'PERCENTAGE': [goal, availability, performance, quality]}

    df = pd.DataFrame.from_dict(lith_dict)

    max_value_full_ring = max(df['PERCENTAGE'])

    #Is used for color signal of the ring (example red if value is under 80)
    ring_colours = ["#46a340", '#dae019', '#b02525']

    ring_labels =  [f'   {x} ({v}) ' for x, v in zip(list(df['LITH']), 
                                                    list(df['PERCENTAGE']))]
    data_len = len(df)

    fig = plt.figure(figsize=(6,6), facecolor='white')

    rect = [0.1,0.1,0.8,0.8]

    # Add axis for chart background
    ax_cart = fig.add_axes(rect, facecolor='white')
    ax_cart.spines[['right', 'top', 'left', 'bottom']].set_visible(False)
    ax_cart.tick_params(axis='both', left=False, bottom=False, 
                    labelbottom=False, labelleft=False)

    # Add axis for radial backgrounds
    ax_polar_bg = fig.add_axes(rect, polar=True, frameon=False)
    ax_polar_bg.set_theta_zero_location('N')
    ax_polar_bg.set_theta_direction(1)

    # Loop through each entry in the dataframe and plot a grey
    # ring to create the background for each one
    for i in range(data_len):
        ax_polar_bg.barh(i, max_value_full_ring*1.5*np.pi/max_value_full_ring, 
                        color='gray', 
                        alpha=0.1)
    # Hide all axis items
    ax_polar_bg.axis('off')
        
    # Add axis for radial chart for each entry in the dataframe
    ax_polar = fig.add_axes(rect, polar=True, frameon=False)
    ax_polar.set_theta_zero_location('N')
    ax_polar.set_theta_direction(1)
    ax_polar.set_rgrids([0, 1, 2, 3],
                        labels=ring_labels, 
                        angle=0, 
                        fontsize=10, #fontweight='bold',
                        color='black', verticalalignment='center')

    # Loop through each entry in the dataframe and create a coloured 
    # ring for each entry
    for i in range(data_len):
        if df['PERCENTAGE'][i] == goal:
            ax_polar.barh(i, list(df['PERCENTAGE'])[i]*1.5*np.pi/max_value_full_ring,
                    color="white")
        elif df['PERCENTAGE'][i] >= goal-10:
            ax_polar.barh(i, list(df['PERCENTAGE'])[i]*1.5*np.pi/max_value_full_ring,
                    color=ring_colours[0])
        elif df['PERCENTAGE'][i] < goal-20:
            ax_polar.barh(i, list(df['PERCENTAGE'])[i]*1.5*np.pi/max_value_full_ring,
                    color=ring_colours[2])
        else:
            ax_polar.barh(i, list(df['PERCENTAGE'])[i]*1.5*np.pi/max_value_full_ring,
                    color=ring_colours[1])
                
    # Hide all grid elements for the    
    ax_polar.grid(False)
    ax_polar.tick_params(axis='both', left=False, bottom=False, 
                    labelbottom=False, labelleft=True)


    st.pyplot(fig)
