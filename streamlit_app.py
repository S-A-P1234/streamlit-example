from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st




with st.echo(code_location='above'):
    n1 = st.text_input('First Number', '1')
    n2 = st.text_input('First Number', '2')
    n3 = st.text_input('First Number','3')
    num1 = int(n1)
    num2 = int(n2)
    num3 = int(n3)
    l = [num1,num2,num3]
    maxn = max(l)
    
    st.write('Max Number is: ', maxn)
  
