import streamlit as st
import pickle as pkl
from sklearn.linear_model import LinearRegression 

train=pkl.load(open('test.pkl','rb'))

st.title("Welcome to House Price Prediction System")
st.write("Enter Details of House")
area=st.text_input("Enter area")
bd=st.text_input("Enter no of bedrooms")
bt=st.text_input("Enter no of bathrooms")
so=st.text_input("Enter no of stories")
pr=st.text_input("Enter no of parkings")
choice=["Yes","No"]
choice2=["Furnished","Semi-Furnished","Not-Furnished"]
mr=st.selectbox('MainRoad:',choice)
gr=st.selectbox('Guestroom Available:',choice)
bm=st.selectbox('Basement:',choice)
hw=st.selectbox('Hotwater available:',choice)
ac=st.selectbox('AC available:',choice)
pf=st.selectbox('Prefarea:',choice)
fs=st.selectbox('furnishingstatus:',choice2)

def choicee(x):
    if x=="Yes":
        return 1
    else:
        return 0

def choicee2(x):
    if x=="Furnished":
        return 2
    elif x=="Semi-Furnished":
        return 1
    else:
        return 0

area = int(area) if area else 0
bd = int(bd) if bd else 0
bt = int(bt) if bt else 0
so = int(so) if so else 0
pr = int(pr) if pr else 0

mr=choicee(mr)
gr=choicee(gr)
bm=choicee(bm)
hw=choicee(hw)
ac=choicee(ac)
fs=choicee2(fs)
pf=choicee(pf)

x=int(train.predict([[area,bd,bt,so,mr,gr,bm,hw,ac,pr,pf,fs]])[0])
z=st.button("Predict")
if z:    
    st.write("Predicted price="+str(x))