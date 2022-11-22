import streamlit as st




st.write("""
# Приложение по диагностике АГ


""")

st.sidebar.header('Введите показания пациента')




def diagnosis():
    risk_count=0
    pom_count=0
    ssz_count=0
    db=0
    
    #GROUP1
    gender=st.sidebar.selectbox('Полл',('Мужчина','Женщина'))
    #возраст
    age=st.sidebar.slider('Возраст', 0,110,43)
    smoking=st.sidebar.selectbox('Курение',('Да','Нет'))
     
    hyperchol=st.sidebar.selectbox('Дислипидемия',('Да','Нет'))
    #глюкоза плазмы и нарушение толерантности да или нет
    prediabet=st.sidebar.selectbox('Предиабет', ('Да','Нет'))
    hyperur=st.sidebar.selectbox('Гиперурекемия',('Да','Нет'))
    # избыточная масса тела и ожирение, два фактора
    height=st.sidebar.slider('Рост(см)', 0,250,170)
    weight=st.sidebar.slider('Вес(кг)', 0,250,60)
    bmi=weight/((0.01*height)**2)
    #окружность талии
    abdominal=st.sidebar.slider('Окружность талии(см)', 0,150,70)
    chss=st.sidebar.slider('Частота сердечных сокращений в минуту', 0,150,70)
    #да или нет
    semeyniy=st.sidebar.selectbox('Семеный анамнез ранних ССЗ', ('Да','Нет'))
    menopause=st.sidebar.selectbox('Ранняя менопауза', ('Да','Нет'))
    psycho_social=st.sidebar.selectbox('Психосоциальные и экономические факторы', ('Да','Нет'))
   
    #GROUP2
    sys=st.sidebar.slider('Систолическое АД(мм.рт.ст.)', 0,240,130)
    diasst=st.sidebar.slider('Диастолическое АД(мм.рт.ст.)', 0,160,87)
    pulse_press=sys-diasst
    
    ekg=st.sidebar.selectbox('Признаки ГЛЖ на ЭКГ', ('Да','Нет'))
    echoekg=st.sidebar.selectbox('Признаки ГЛЖ на ЭХОКГ ', ('Да','Нет'))
    
    sys_leg_cond=st.sidebar.selectbox('Оценивался ли Лодыжечно-плечевой индекс', ('Да','Нет'))
    
    if sys_leg_cond=='Да':
        sys_leg=st.sidebar.slider('Систолическое АД на лодыжке(мм.рт.ст.)',0,240,120)
        shoulder_index=sys_leg/sys
        if shoulder_index < 0.9:
            pom_count+=1
    
   
    hbp=st.sidebar.slider('Скорость клубочковой фильтрации(мл/мин/173м\u00b2)', 0,150,61)
    
    mau=st.sidebar.slider('Уровень Микроальбуминурии(мг в сутки)', 0,400,301)
    
    albu_kreat=st.sidebar.slider('Соотношение альбумина к креатинину в разовой моче(мг/ммоль)', 0,400,302)
    
    #GROUP3
    
    sahar=st.sidebar.selectbox('Наличие сахарного диабета',('Да','Нет'))
    
    
    #GROUP 4
    cerebro_vasc=st.sidebar.selectbox('Наличие Цереброваскулярных болезней', ('Да','Нет'))
    ibs=st.sidebar.selectbox('Наличие Ишемической Болезни Сердца', ('Да','Нет'))
    sn=st.sidebar.selectbox('Наличие Сердечной Недостаточности', ('Да','Нет'))
    fibrilationechoekg=st.sidebar.selectbox('Наличие Фибрилляции предсердий', ('Да','Нет'))
    peripher=st.sidebar.selectbox('Наличие клинических манифестных поражений периферических артерий', ('Да','Нет'))

    diag=''
    
    if age >65 and gender == 'Женщина':
        risk_count+=1
    elif age >55 and gender == 'Мужчина':
        risk_count+=1
    if smoking=='Да':
        risk_count+=1
    if hyperchol=='Да':
        risk_count+=1
    if prediabet=='Да':
        risk_count+=1
    if hyperur=='Да':
        risk_count+=1
    if bmi>=25:
        risk_count+=1
    if abdominal>=102 and gender=='Мужчина':
        risk_count+=1
    elif abdominal>=88 and gender=='Женщина':
        risk_count+=1    
    if chss>=80:
        risk_count+=1   
    if semeyniy =='Да':
        risk_count+=1
    if menopause=='Да':
        risk_count+=1
    if psycho_social=='Да':
        risk_count+=1
        
    if sahar=='Да':
        db+=1
        
        
    
    if pulse_press>=60:
        pom_count+=1
    if ekg=='Да':
        pom_count+=1
    if echoekg=='Да':
        pom_count+=1
    
    if (hbp<=60) & (hbp>=30):
        pom_count+=1
    elif hbp<30:
        ssz_count+=1
    if (mau<=300) & (mau>=30):    
        pom_count+=1
    elif mau>300: 
        ssz_count+=1
    if (albu_kreat<=300) & (albu_kreat>=30):  
        pom_count+=1
    elif albu_kreat>300: 
        ssz_count+=1    
        
    
    if cerebro_vasc=='Да':
        ssz_count+=1
    if ibs=='Да':
        ssz_count+=1
    if sn=='Да':
        ssz_count+=1
    if fibrilationechoekg=='Да':
        ssz_count+=1
    if peripher=='Да':
        ssz_count+=1
        

        
    #stage 1, 0 factors
    if (risk_count==0)&(pom_count==0)&(ssz_count==0)&(db==0)&((sys<=139)&(diasst<=89)):
        diag= 'Высоконормальное АД, Стадия 1, Низкий риск'
    elif (risk_count==0)&(pom_count==0)&(ssz_count==0)&(db==0)&(((sys<=159)&(diasst<=99)&(diasst>=90))|((diasst<=89)&(sys<=159)&(sys>=140))):
        diag= 'Гипертоническая болезнь, Стадия 1, 1 степень, Низкий риск'    
    elif (risk_count==0)&(pom_count==0)&(ssz_count==0)&(db==0)&(((sys<=179)&(diasst<=109)&(diasst>=100))|((diasst<=99)&(sys<=179)&(sys>=160))):
        diag= 'Гипертоническая болезнь, Стадия 1, 2 степень, Умеренный риск'
    
    elif (risk_count==0)&(pom_count==0)&(ssz_count==0)&(db==0)&((sys>=180)|(diasst>=110)):
        diag= 'Гипертоническая болезнь, Стадия 1, 3 степень, Высокий риск'  
    
    
    #stage 1, 1-2 factors
    elif (risk_count<=2)&(risk_count>=1)&(pom_count==0)&(ssz_count==0)&(db==0)&((sys<=139)&(diasst<=89)):
        diag= 'Высоконормальное АД, Стадия 1, Низкий риск'
    elif (risk_count<=2)&(risk_count>=1)&(pom_count==0)&(ssz_count==0)&(db==0)&(((sys<=159)&(diasst<=99)&(diasst>=90))|((diasst<=89)&(sys<=159)&(sys>=140))):
        diag= 'Гипертоническая болезнь, Стадия 1, 1 степень, Умеренный риск'
    elif (risk_count<=2)&(risk_count>=1)&(pom_count==0)&(ssz_count==0)&(db==0)&(((sys<=179)&(diasst<=109)&(diasst>=100))|((diasst<=99)&(sys<=179)&(sys>=160))):
        diag= 'Гипертоническая болезнь, Стадия 1, 2 степень, Умеренный-высокий риск'  
       
    elif (risk_count<=2)&(risk_count>=1)&(pom_count==0)&(ssz_count==0)&(db==0)&((sys>=180)|(diasst>=110)):
        diag= 'Гипертоническая болезнь, Стадия 1, 3 степень, Высокий риск'    
        
      #stage 1, 3+ factors  
    elif (risk_count>=3)&(pom_count==0)&(ssz_count==0)&(db==0)&((sys<=139)&(diasst<=89)):
        diag= 'Высоконормальное АД, Стадия 1, Низкий-умеренный риск'    
    elif (risk_count>=3)&(pom_count==0)&(ssz_count==0)&(db==0)&(((sys<=159)&(diasst<=99)&(diasst>=90))|((diasst<=89)&(sys<=159)&(sys>=140))):
        diag='Гипертоническая болезнь, Стадия 1, 1 степень, Умеренный-высокий риск'     
   
    elif (risk_count>=3)&(pom_count==0)&(ssz_count==0)&(db==0)&(((sys<=179)&(diasst<=109)&(diasst>=100))|((diasst<=99)&(sys<=179)&(sys>=160))):
        diag='Гипертоническая болезнь, Стадия 1, 2 степень, Высокий риск'
    elif (risk_count>=3)&(pom_count==0)&(ssz_count==0)&(db==0)&((sys>=180)|(diasst>=110)):
        diag= 'Гипертоническая болезнь, Стадия 1, 3 степень, Высокий риск'    
   
        
        
  #stage 2, 3
    elif (ssz_count==0):
        if ((pom_count>0)&(db>0)):
            if ((sys<=139)&(diasst<=89))&((risk_count==0)|(risk_count>0)):
                diag= 'Высоконормальное АД, Стадия 3, Очень высокий риск'  
            elif ((risk_count==0)|(risk_count>0))&(((sys<=159)&(diasst<=99)&(diasst>=90))|((diasst<=89)&(sys<=159)&(sys>=140))):
                diag= 'Гипертоническая болезнь, Стадия 3, 1 степень, Очень высокий риск' 
            elif ((risk_count==0)|(risk_count>0))&(((sys<=179)&(diasst<=109)&(diasst>=100))|((diasst<=99)&(sys<=179)&(sys>=160))):
                diag= 'Гипертоническая болезнь, Стадия 3, 2 степень, Очень высокий риск'
            elif ((risk_count==0)|(risk_count>0))&((sys>=180)|(diasst>=110)):
                diag= 'Гипертоническая болезнь, Стадия 3, 3 степень, Очень высокий риск' 
                #STAGE 2
        elif ((pom_count>0)|(db>0)):
            if ((sys<=139)&(diasst<=89))&((risk_count==0)|(risk_count>0)):
                diag= 'Высоконормальное АД, Стадия 2, Умеренный-высокий риск'
            elif ((risk_count==0)|(risk_count>0))&(((sys<=159)&(diasst<=99)&(diasst>=90))|((diasst<=89)&(sys<=159)&(sys>=140))):   
                diag= 'Гипертоническая болезнь, Стадия 2, 1 степень, Высокий риск'
            elif ((risk_count==0)|(risk_count>0))&(((sys<=179)&(diasst<=109)&(diasst>=100))|((diasst<=99)&(sys<=179)&(sys>=160))):
                diag= 'Гипертоническая болезнь, Стадия 2, 2 степень, Высокий риск'
            elif ((risk_count==0)|(risk_count>0))&((sys>=180)|(diasst>=110)):  
                diag= 'Гипертоническая болезнь, Стадия 2, 3 степень, Очень высокий риск'
                #STAGE 3
    elif (ssz_count>0):
        if ((pom_count>0)&(db>0)):
            if ((sys<=139)&(diasst<=89))&((risk_count==0)|(risk_count>0)):
                diag= 'Высоконормальное АД, Стадия 3, Очень высокий риск'  
            elif ((risk_count==0)|(risk_count>0))&(((sys<=159)&(diasst<=99)&(diasst>=90))|((diasst<=89)&(sys<=159)&(sys>=140))):
                diag= 'Гипертоническая болезнь, Стадия 3, 1 степень, Очень высокий риск' 
            elif ((risk_count==0)|(risk_count>0))&(((sys<=179)&(diasst<=109)&(diasst>=100))|((diasst<=99)&(sys<=179)&(sys>=160))):
                diag= 'Гипертоническая болезнь, Стадия 3, 2 степень, Очень высокий риск'
            elif ((risk_count==0)|(risk_count>0))&((sys>=180)|(diasst>=110)):
                diag= 'Гипертоническая болезнь, Стадия 3, 3 степень, Очень высокий риск' 
        elif ((pom_count>0)|(db>0)):
            if ((sys<=139)&(diasst<=89))&((risk_count==0)|(risk_count>0)):
                diag= ' Высоконормальное АД, Стадия 3, Очень высокий риск'  
            elif ((risk_count==0)|(risk_count>0))&(((sys<=159)&(diasst<=99)&(diasst>=90))|((diasst<=89)&(sys<=159)&(sys>=140))):
                diag= 'Гипертоническая болезнь, Стадия 3, 1 степень, Очень высокий риск' 
            elif ((risk_count==0)|(risk_count>0))&(((sys<=179)&(diasst<=109)&(diasst>=100))|((diasst<=99)&(sys<=179)&(sys>=160))):
                diag= 'Гипертоническая болезнь, Стадия 3, 2 степень, Очень высокий риск'
            elif ((risk_count==0)|(risk_count>0))&((sys>=180)|(diasst>=110)):
                diag= 'Гипертоническая болезнь, Стадия 3, 3 степень, Очень высокий риск' 
        elif ((pom_count==0)&(db==0)):
            if ((sys<=139)&(diasst<=89))&((risk_count==0)|(risk_count>0)):
                diag= 'Высоконормальное АД, Стадия 3, Очень высокий риск'  
            elif ((risk_count==0)|(risk_count>0))&(((sys<=159)&(diasst<=99)&(diasst>=90))|((diasst<=89)&(sys<=159)&(sys>=140))):
                diag= 'Гипертоническая болезнь,Стадия 3, 1 степень, Очень высокий риск' 
            elif ((risk_count==0)|(risk_count>0))&(((sys<=179)&(diasst<=109)&(diasst>=100))|((diasst<=99)&(sys<=179)&(sys>=160))):
                diag= 'Гипертоническая болезнь, Стадия 3, 2 степень, Очень высокий риск'
            elif ((risk_count==0)|(risk_count>0))&((sys>=180)|(diasst>=110)):
                diag= 'Гипертоническая болезнь, Стадия 3, 3 степень, Очень высокий риск'        
            
              
            
        
        
        
        
        
          
  
    return diag  


result=diagnosis()




st.subheader('Диагноз')
if st.button('Посмотреть диагноз'):
    st.write(result)


