import streamlit as st

mu = st.slider('$\mu$', 0.0, 5.0, 2.5, step=0.1)
if 'var' in st.session_state:
    st.session_state.var = min(mu, st.session_state.var)
var = st.slider('$\sigma^2$', 0.0, mu, 1.0, step=0.1, key='var')

# var = st.slider('$\sigma^2$', 0.0, mu, min(mu, st.session_state.var) if 'var' in st.session_state else 1.0, step=0.1, key='var')

st.write('$\mu$:', mu, '$\sigma^2$:', var)
