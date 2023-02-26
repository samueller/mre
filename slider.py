import streamlit as st
from datetime import time
mu = st.slider('$\mu$', 0.0, 5.0, 1.0, step=0.1)
var = st.slider('$\sigma^2$', 0.0, mu, 1.0, step=0.1)
st.write('$\mu$:', mu, '$\sigma^2$:', var) 
