import streamlit as st
from streamlit import fragment
import psutil
import time
import plotly.graph_objects as go
import os
import json
from datetime import datetime
import pandas as pd

# Simple log storage
LOG_DIR = "/app/logs"
os.makedirs(LOG_DIR, exist_ok=True)

def save_log_entry(service_name, level, message):
    """Save a log entry to file"""
    timestamp = datetime.now().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "service": service_name,
        "level": level,
        "message": message
    }

    # Append to service-specific log file
    log_file = os.path.join(LOG_DIR, f"{service_name}.log")
    with open(log_file, 'a') as f:
        f.write(json.dumps(log_entry) + '\n')

def read_logs(service_name=None):
    """Read logs from files"""
    logs = []

    if service_name:
        log_file = os.path.join(LOG_DIR, f"{service_name}.log")
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                for line in f:
                    logs.append(json.loads(line.strip()))
    else:
            # Read all log files
            for filename in os.listdir(LOG_DIR):
                if filename.endswith('.log'):
                    with open(os.path.join(LOG_DIR, filename), 'r') as f:
                        for line in f:
                            logs.append(json.loads(line.strip()))
    return logs
    
# Read logs
st.header("logs")
logs = read_logs()

if logs:
    #Convert to DataFrame for easy display
    df = pd.DataFrame(logs)

    #Filter by service
    services = df['service'].unique()
    selected_service = st.selectbox("Filter by service", ["ALL"] + list(services))

    if selected_service != "ALL":
        df = df[df['service'] == selected_service]

    #Display logs
    st.dataframe(df)

    #Basic stats
    st.subheader("Log statistics")
    error_count = len(df[df['level'] == 'ERROR'])
    warning_count = len(df[df['level'] == 'WARNING'])
    col4, col5 = st.columns(2)
    col4.metric("Errors", error_count)
    col5.metric("Warnings", warning_count)

else:
    st.info("No logs yet. Start generating some logs!")

st.title("My Cluster Monitor with logs!")
@fragment(run_every="1s")
def live_metrics():
    col1, col2, col3, col4 = st.columns(4)
    cpu_usage = psutil.cpu_percent(interval=1)

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

    disk_usage = psutil.disk_usage('/').percent

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
     

    #per_cpu_usage = psutil.cpu_percent(percpu=True)

    #with col4:
        
live_metrics()