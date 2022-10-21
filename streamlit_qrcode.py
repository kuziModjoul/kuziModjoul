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
    
    with st.form("my_form"):
       st.write("Please enter your details in the form")
       name_and_lastName = st.text_input("Name and LasName: ")
       email = st.text_input("Email: ")
       phone_number = st.text_input("Phone number : ")


       # Every form must have a submit button.
       submitted = st.form_submit_button("Submit")
       if submitted:
           st.write(f"""Name and Last Name: {name_and_lastName} \nEmail : {email} \nPhone Number : {phone_number} """)

with col3:
    st.write("")
