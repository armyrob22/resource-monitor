import streamlit as st
import psutil
import time
import plotly.graph_objects as go

st.title("My Server Resource Monitor!")
col1, col2, col3 = st.columns(3)

cpu_usage = psutil.cpu_percent()

with col1:
    fig_cpu = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = cpu_usage,
    title = {'text': "Cpu Usage"},
    gauge = {
        'axis': {'range': [None, 100]},
        'bar': {'color': "darkblue"},
        'steps':[
            {'range': [0, 50], 'color': "lightgreen"},
            {'range': [50, 75], 'color': "yellow"},
            {'range': [75, 100], 'color': "red"}
        ],
        'threshold': {
            'line': {'color': "red", "width": 4},
            'thickness': 0.75,
            'value': 90
        }
    }
))
    st.plotly_chart(fig_cpu, use_container_width=True)

memory_usage = psutil.virtual_memory().percent

with col2:
    fig_memory = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = memory_usage,
    title = {'text': "Memory Usage"},
    gauge = {
        'axis': {'range': [None, 100]},
        'bar': {'color': "darkblue"},
        'steps':[
            {'range': [0, 50], 'color': "lightgreen"},
            {'range': [50, 75], 'color': "yellow"},
            {'range': [75, 100], 'color': "red"}
        ],
        'threshold': {
            'line': {'color': "red", "width": 4},
            'thickness': 0.75,
            'value': 90
        }
    }
))
    st.plotly_chart(fig_memory, use_container_width=True)

disk_usage = psutil.disk_usage('C:').percent

with col3:
    fig_disk = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = disk_usage,
    title = {'text': "Disk Usage"},
    gauge = {
        'axis': {'range': [None, 100]},
        'bar': {'color': "darkblue"},
        'steps':[
            {'range': [0, 50], 'color': "lightgreen"},
            {'range': [50, 75], 'color': "yellow"},
            {'range': [75, 100], 'color': "red"}
        ],
        'threshold': {
            'line': {'color': "red", "width": 4},
            'thickness': 0.75,
            'value': 90
        }
    }
))
    st.plotly_chart(fig_disk, use_container_width=True)

time.sleep(1)
st.rerun()