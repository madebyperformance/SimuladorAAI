import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#Importar logo
im = Image.open(r'logo.png')

# Define as cores da página
st.set_page_config(
    page_title='Simulador Partnership AAI',
    page_icon=im,
    layout='wide')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown('<div style="position: fixed; bottom: 0; right: 100px;"><p style="color: white;"><span style="color:black;font-size: 20px;font-family: Barlow Semibold;">MADE BY </span><span style="color:#9966FF;font-size: 20px; font-family: Barlow Semibold, sans-serif;">PERFORMANCE</span></p></div>', unsafe_allow_html=True)

def link():
    st.sidebar.markdown("<a href='https://madebyperformance-simulador-top-50-simulador50-tww9qe.streamlit.app/' target='_blank' style='text-decoration: none; font-family: Barlow; font-weight: bold; font-size: 22px; color: white;'>SIMULADOR TOP50</a>", unsafe_allow_html=True)
    st.sidebar.markdown("<span style='font-family: Barlow; color: white; font-size: 14px;'>Clique acima para ser redirecionado ao Simulador do TOP50 2023.</span>", unsafe_allow_html=True)

link()

st.title('Simulador Partnership AAI - 2024')
st.caption("Use este simulador para calcular quanto de premiação você poderá receber ao final do ano. Importante frisar que a premiação é calculada em cima de valores preenchidos por você e a premição é uma aproximação.")

input_FatXP=st.number_input("Faturamento total do ano",format="%.0f")
fxp="{:,.0f}".format(input_FatXP) 
fxp = fxp.replace(",",".")
st.caption(f"Receita Selecionada: R$ {fxp}")
input_Incremento=st.number_input("Captação Líquida + Transferência total do ano",format="%.0f")
inc="{:,.0f}".format(input_Incremento) 
inc = inc.replace(",",".")
st.caption(f"Incremento Selecionado: R$ {inc}")
input_ROA = st.number_input("ROAt do mês")
input_C = st.number_input("Quantidade de clientes Ativos atual",format="%.0f")

if st.button("Calcular Premiação"):
    
        #Calculando premiação
        
        #FAT
        if input_FatXP >= 50000:
            pcf = ((input_FatXP/1000000)*20000)
        elif input_FatXP >= 35000:
            pcf = ((input_FatXP/1000000)*15000)
        elif input_FatXP >= 25000:
            pcf = ((input_FatXP/1000000)*10000)
        elif input_FatXP >= 15000:
            pcf = ((input_FatXP/1000000)*5000)
        elif input_FatXP < 15000:
            pcf = 0

        #INC
        if input_Incremento >= 5000000:
            pcinc = (input_Incremento/1000000) * 400
        elif input_Incremento >= 3000000:
            pcinc = (input_Incremento/1000000) * 400
        elif input_Incremento >= 2000000:
            pcinc = (input_Incremento/1000000) * 400
        elif input_Incremento >= 1000000:
            pcinc = (input_Incremento/1000000) * 400
        elif input_Incremento < 1000000:
            pcinc = 0

        #BONUS CONTA
        if input_C >= 120:
            bonus_con = 1
        elif input_C < 120:
            bonus_con = 2

        #VALIDADOR ROA
        if input_ROA >= 0.5:
            bonus_roa = 1
        elif input_ROA < 0.5:
            bonus_roa = 0

        #premiação fat
        pcf = pcf * bonus_roa
        prem_f = (pcf + pcinc)*bonus_con
        p_b_con = prem_f - (pcf + pcinc)

        #FORMATAÇÃO
        #fat
        pcf="{:,.0f}".format(pcf) 
        pcf = pcf.replace(",",".")
        #bonus conta
        p_b_con="{:,.0f}".format(p_b_con) 
        p_b_con = p_b_con.replace(",",".")
        #prem inc
        pcinc="{:,.0f}".format(pcinc) 
        pcinc = pcinc.replace(",",".")
        #prem TOTAL
        prem_f="{:,.0f}".format(prem_f) 
        prem_f = prem_f.replace(",",".")
    

        valores = [["Premiação Faturamento",pcf],["Premiação Incremento",pcinc],["Bônus contas ativas",p_b_con],["Premiação Total",prem_f]]
        df = pd.DataFrame(valores,columns=['KPI','Premiação'])
        
        st.caption(f"Premiações mostradas abaixo estão em Reais por ações da Companhia.")
        st.dataframe(df) 
