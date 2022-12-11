import streamlit as st
import pickle
import pandas as pd
import time
import os
import random
l=[]
for i in os.listdir():
    if ".pkl" in i: 
        a=i.split(".")
        l.append(a[0])
        x="""{}=pickle.load(open("{}.pkl","rb"))""".format(a[0],a[0])
        exec(x)

#['addr_state', 'columns', 'emp_length', 'emp_title', 'logistic', 'ordinal', 'purpose', 'zip_code']
st.header("P2P Loans")
#st.header(columns)
#st.header(addr_state[0])
col1, col2 = st.columns([5,5])
with col1:
    st.text_input("First Name")
with col2:
    st.text_input("Last Name")

with col1:
    addr=st.selectbox("State",addr_state[0])
with col2:
    zipp=st.selectbox("Zip Code",zip_code[0])
st.text_input('Address')
jtitle=st.selectbox('Job Title',emp_title[0][:100])
length=st.select_slider("Length of job",emp_length)
purpose=st.selectbox('Job Title',purpose[0])
loan=st.number_input('Loan Amount')
period=st.selectbox('Term (in months)',['36 months','60 months'])
int_rate=0.13
mor=st.selectbox('House Owner ship',['ANY', 'MORTGAGE', 'NONE', 'OTHER', 'OWN', 'RENT'])
verify=st.selectbox('Information is true',['Not_Verified','SVerified','Verified'])
app=st.selectbox("Application type",['Individual', 'Joint'])
method=st.selectbox("Disburement Method",['Cash', 'DirectPay'])



if st.button("predict"):

    if period == '36 months':
        p1=1
        p2=0
        p=36
    else:
        p2=1
        p1=0
        p=60

    if mor=='ANY':
        a=1
        m=0
        n=0
        o=0
        ow=0
        r=0
    elif mor=='MORTGAGE':
        a=0
        m=1
        n=0
        o=0
        ow=0
        r=0
    elif mor=='NONE':
        a=0
        m=0
        n=1
        o=0
        ow=0
        r=0
    elif mor=='OTHER':
        a=0
        m=0
        n=0
        o=1
        ow=0
        r=0
    elif mor=='OWN':
        a=0
        m=0
        n=0
        o=0
        ow=1
        r=0
    elif mor=='RENT':
        a=0
        m=0
        n=0
        o=0
        ow=0
        r=1

    if verify=='Not_Verified':
        NV=1
        SV=0
        V=0
    elif verify=='SVerified':
        NV=0
        SV=1
        V=0
    elif verify=='Verified':
        NV=0
        SV=0
        V=1
    
    import random
    w= random.randint(0,1)
    if w == 1:
        f=0
    else:
        f=1

    if app=='Joint':
        jo=1
        ind=0
    else:
        jo=0
        ind=1

    if method=='Cash':
        ca=1
        dp=0
    else:
        ca=0
        dp=1

    inst=(loan*int_rate*(1-int_rate)**p)/((1+int_rate)**(p-1))
    input_df=pd.DataFrame([{'loan_amnt':loan,'int_rate':int_rate,'installment':inst, 'emp_title':jtitle, 'emp_length':length, 'purpose':purpose, 'zip_code':zipp, 'addr_state':addr, 'term_ 36 months':p1, 'term_ 60 months':p2, 'home_ownership_ANY':a, 'home_ownership_MORTGAGE':m, 'home_ownership_NONE':n, 'home_ownership_OTHER':o, 'home_ownership_OWN':ow, 'home_ownership_RENT':r, 'verification_status_Not Verified':NV, 'verification_status_Source Verified':SV, 'verification_status_Verified':V, 'initial_list_status_f':f, 'initial_list_status_w':w, 'application_type_Individual':ind, 'application_type_Joint App':jo, 'disbursement_method_Cash':ca, 'disbursement_method_DirectPay':dp}])
    input_df[['emp_title','emp_length','purpose','zip_code','addr_state']]=ordinal.transform(input_df[['emp_title','emp_length','purpose','zip_code','addr_state']])
    result=logistic.predict(input_df)
    #st.header(result[0])

    if result[0] == 1:
        a=1
        st.header('Congratulations, you are eligible for loan.')
    else:
        a=1
        st.header("Unfortunately, you aren't eligible for loan")
