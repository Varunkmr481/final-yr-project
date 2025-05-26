# Basic report

from Home import st
from Home import face_rec

st.set_page_config(page_title="report", layout="wide")
st.subheader("REPORT")

# Retrieve logs data and show in file
# etract data from redis list
db_name = 'logs'
def load_logs(name, end=-1):
    # extract all data
    logs_list = face_rec.r.lrange(name, start=0, end=end)
    return logs_list

if st.button('Refresh Report'):
    st.write(load_logs(name=db_name))
    

