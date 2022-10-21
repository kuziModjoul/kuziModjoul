import streamlit as st

st.set_page_config( page_title="congratulations",
#                     page_icon= "random",
                    layout="wide"
 )

col1, col2, col3 = st.columns((.1,1,.1))

with col1:
    st.write("")

with col2:

    st.markdown("<center><img src='https://github.com/kuziModjoul/streamlit-webpage-example/blob/main/modjoul_logo.jpg?raw=1' width=100/></center>", unsafe_allow_html=True)
    st.markdown(" <h1 style='text-align: center;'>Congratulations you Won!!!!!!!!!</h1>", unsafe_allow_html=True)
    st.balloons()

with col3:
    st.write("")
