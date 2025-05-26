# Report with styling but without refresh button

from Home import st
from Home import face_rec
import pandas as pd
from datetime import datetime  # For timestamp formatting

st.set_page_config(page_title="Attendance Report", layout="wide")
st.subheader("📋 Attendance Report")

# Function to load logs from Redis
db_name = 'logs'
def load_logs(name, end=-1):
    logs_list = face_rec.r.lrange(name, start=0, end=end)
    return logs_list


# Fetch logs
logs_data = load_logs(name=db_name)

if logs_data:
    # Process logs
    data = []
    for log in logs_data:
        decoded_log = log.decode('utf-8')  # Decode binary string
        name, role, timestamp = decoded_log.split('@')
        
         # Format timestamp into readable format
        formatted_time = datetime.strptime(timestamp.split('.')[0], "%Y-%m-%d %H:%M:%S").strftime("%B %d, %Y, %I:%M %p")
        
        data.append({'Name': name, 'Role': role, 'Timestamp': formatted_time})

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Add styled table
    st.markdown(
        """
        <style>
        .styled-table {
            font-family: Arial, sans-serif;
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 18px;
            width: 100%;
            border-radius: 12px 12px 0 0;
            overflow: hidden;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
        }
        .styled-table thead tr {
            background-color: #009879;
            color: #ffffff;
            text-align: left;
            font-weight: bold;
        }
        .styled-table tbody tr {
            border-bottom: 1px solid #dddddd;
        }
        .styled-table tbody tr:nth-of-type(even) {
            background-color: #0ec777;
        }
        .styled-table tbody tr:last-of-type {
            border-bottom: 2px solid #009879;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )
    
    # Display table using custom HTML
    st.markdown(
        df.to_html(index=False, classes='styled-table', escape=False), 
        unsafe_allow_html=True
    )

else:
    st.warning("⚠️ No logs found in the database!")

# Footer with branding
st.markdown(
    """
    <hr style='border: 1px solid #ddd; margin: 30px 0px'>
    <div style='text-align: center; font-size: 0.9rem; color: #888;'>
        Powered by <strong>DLBAFRAS</strong> | Transforming Attendance Systems with AI
    </div>
    """,
    unsafe_allow_html=True
)
