import streamlit as st
import pandas as pd
import numpy as np

st.title('Simulador do Partnership 2023')
st.caption("Use este simulador para calcular quanto de premiação você poderá receber ao final do ano. Importante frisar que a premiação é calculada em cima de valores preenchidos por você e a premição é uma aproximação.")

opcao = st.radio( "Selecione seu grupo:",("Crescimento","Resultado"))

if opcao == "Crescimento":
    input_FatXP=st.number_input("Faturamento total do ano",format="%.0f")
    fxp="{:,.0f}".format(input_FatXP) 
    fxp = fxp.replace(",",".")
    st.caption(f"Receita Selecionada: R$ {fxp}")
    input_Incremento=st.number_input("Captação Líquida + Transferência total do ano",format="%.0f")
    inc="{:,.0f}".format(input_Incremento) 
    inc = inc.replace(",",".")
    st.caption(f"Incremento Selecionado: R$ {inc}")
    input_Contas=st.number_input("Total de contas Ativadas no ano",format="%.0f")
    input_ROA=st.number_input("ROA médio do ano")
elif opcao == "Resultado":
    input_FatXP=st.number_input("Faturamento total do ano",format="%.0f")
    fxp="{:,.0f}".format(input_FatXP) 
    fxp = fxp.replace(",",".")
    st.caption(f"Receita Selecionada: R$ {fxp}")
    input_Incremento=st.number_input("Captação Líquida + Transferência total do ano",format="%.0f")
    inc="{:,.0f}".format(input_Incremento) 
    inc = inc.replace(",",".")
    st.caption(f"Incremento Selecionado: R$ {inc}")
    input_ROA=st.number_input("ROA médio do ano")

if st.button("Calcular Premiação"):

    if opcao == "Crescimento":

        #Calculando premiação
        if input_FatXP >= 100000:
            pcf = ((input_FatXP/1000000)*5000)
        if input_FatXP < 100000:
            pcf = 0
        if input_Incremento >= 6000000:
            pcinc = ((input_Incremento/1000000)*400)
        if input_Incremento < 6000000:
            pcinc = 0
        if input_Contas >= 48:
            pccon = (input_Contas*100)
        if input_Contas < 48:
            pccon = 0
        
        prem = (pcinc + pccon + pcf)
        #Variante do ROA
        if input_ROA >= 0.75:
            pcroa = (prem*1)
        elif input_ROA >= 0.60 and input_ROA < 0.75:
            pcroa = (prem*0.75)
        elif input_ROA >= 0.30 and input_ROA < 0.60:
            pcroa = (prem*0.25)
        elif input_ROA < 0.30:
            pcroa = (prem*0)
        
        premt = (pcinc + pccon + pcf + pcroa)

        pcf="{:,.0f}".format(pcf) 
        pcf = pcf.replace(",",".")
        pccon="{:,.0f}".format(pccon) 
        pccon = pccon.replace(",",".")
        pcinc="{:,.0f}".format(pcinc) 
        pcinc = pcinc.replace(",",".")
        pcroa="{:,.0f}".format(pcroa) 
        pcroa = pcroa.replace(",",".")

        kpi1 = 0
        kpi2 = (prem*0.25)
        kpi3 = (prem*0.75)
        kpi4 = (prem*1)

        premt1 = premt
        premt2 = (premt+kpi2)
        premt3 = (premt+kpi3)
        premt4 = (premt+kpi4)

        kpi1="{:,.0f}".format(kpi1) 
        kpi1 = kpi1.replace(",",".")
        kpi2="{:,.0f}".format(kpi2) 
        kpi2 = kpi2.replace(",",".")
        kpi3="{:,.0f}".format(kpi3) 
        kpi3 = kpi3.replace(",",".")
        kpi4="{:,.0f}".format(kpi4) 
        kpi4 = kpi4.replace(",",".")
        
        premt1="{:,.0f}".format(premt1) 
        premt1 = premt1.replace(",",".")
        premt2="{:,.0f}".format(premt2) 
        premt2 = premt2.replace(",",".")
        premt3="{:,.0f}".format(premt3) 
        premt3 = premt3.replace(",",".")
        premt4="{:,.0f}".format(premt4) 
        premt4 = premt4.replace(",",".")

        valores = [["Faturamento XP",pcf,pcf,pcf,pcf],["Captação Líquida + Transferências",pcinc,pcinc,pcinc,pcinc],["Ativação de contas",pccon,pccon,pccon,pccon],["Adicional ROA",pcroa,pcroa,pcroa,pcroa],["Adicional KPI Global",kpi1,kpi2,kpi3,kpi4],["Premiação Total",premt1,premt2,premt3,premt4]]
        df = pd.DataFrame(valores,columns=['KPI','Meta Global <80%','Meta Global >80%','Meta Global >90%','Meta Global >100%'])

        valores2 = [["Faturamento XP",pcf],["Incremento",pcinc],["Ativação de contas",pccon],["Adicional ROA",pcroa]]
        df2 = pd.DataFrame(valores2,columns=['KPI','Premiação'])
        
        st.caption(f"Premiações mostradas abaixo estão em Reais por ações da Companhia.")
        st.dataframe(df) 

        
    if opcao == "Resultado":

        #Calculando premiação
        if input_FatXP >= 200000:
            pcf = ((input_FatXP/1000000)*10000)
        if input_FatXP < 200000:
            pcf = 0
        if input_Incremento >= 20000000:
            pcinc = ((input_Incremento/1000000)*800)
        if input_Incremento < 20000000:
            pcinc = 0
        
        prem = (pcinc + pcf)
        #Variante do ROA
        if input_ROA >= 0.75:
            pcroa = (prem*1)
        elif input_ROA >= 0.60 and input_ROA < 0.75:
            pcroa = (prem*0.75)
        elif input_ROA >= 0.30 and input_ROA < 0.60:
            pcroa = (prem*0.25)
        elif input_ROA < 0.30:
            pcroa = (prem*0)
        
        premt = (pcinc + pcf + pcroa)

        pcf="{:,.0f}".format(pcf) 
        pcf = pcf.replace(",",".")
        pcinc="{:,.0f}".format(pcinc) 
        pcinc = pcinc.replace(",",".")
        pcroa="{:,.0f}".format(pcroa) 
        pcroa = pcroa.replace(",",".")

        kpi1 = 0
        kpi2 = (prem*0.25)
        kpi3 = (prem*0.75)
        kpi4 = (prem*1)

        premt1 = premt
        premt2 = (premt+kpi2)
        premt3 = (premt+kpi3)
        premt4 = (premt+kpi4)

        kpi1="{:,.0f}".format(kpi1) 
        kpi1 = kpi1.replace(",",".")
        kpi2="{:,.0f}".format(kpi2) 
        kpi2 = kpi2.replace(",",".")
        kpi3="{:,.0f}".format(kpi3) 
        kpi3 = kpi3.replace(",",".")
        kpi4="{:,.0f}".format(kpi4) 
        kpi4 = kpi4.replace(",",".")
        
        premt1="{:,.0f}".format(premt1) 
        premt1 = premt1.replace(",",".")
        premt2="{:,.0f}".format(premt2) 
        premt2 = premt2.replace(",",".")
        premt3="{:,.0f}".format(premt3) 
        premt3 = premt3.replace(",",".")
        premt4="{:,.0f}".format(premt4) 
        premt4 = premt4.replace(",",".")
        
        valores = [["Faturamento XP",pcf,pcf,pcf,pcf],["Captação Líquida + Transferências",pcinc,pcinc,pcinc,pcinc],["Adicional ROA",pcroa,pcroa,pcroa,pcroa],["Adicional KPI Global",kpi1,kpi2,kpi3,kpi4],["Premiação Total",premt1,premt2,premt3,premt4]]
        df = pd.DataFrame(valores,columns=['KPI','Meta Global <80%','Meta Global >80%','Meta Global >90%','Meta Global >100%'])
        
        st.caption(f"Premiações mostradas abaixo estão em Reais por ações da Companhia.")
        st.dataframe(df) 