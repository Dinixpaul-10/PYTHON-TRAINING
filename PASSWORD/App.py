import streamlit as st

st.title("Password Analyser")
password=st.text_input("ENTER THE PASSWORD",type="password")
#st.button("validate")
if st.button("Validate"):
    upper=lower=digit=special=False

    for ch in password:
        if ch.isupper():
            upper=True
        elif ch.islower():
            lower=True
        elif ch.isdigit():
            digit=True
        else:
            special=True

    if len(password)>=8 and upper and lower and digit and special:
         st.success("Strong Password....Thank you")
    else:
         st.error("Invalid Password")    
                    
         if len(password)<8:
            st.write("Password must contain atleast 8 Chars")
         if not upper:
             st.write("Must contain upper case")
         if not lower:
             st.write("Must containn a lower case")
         if not digit:
             st.write("Must contain digit")
         if not special:
             st.write("Must contain special")               