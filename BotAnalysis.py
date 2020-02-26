# -*- coding: utf-8 -*-

import pandas as pd
from matplotlib import pyplot as plt


#Read Data
data_in= pd.read_excel('January Chatlog SB 3 - scrubbed.xlsx')

#Plan types
plan_types = data_in['Plan Types']
#plan_types.dropna(inplace=True)
plan_type_PPO=[x for x in plan_types if (x == '[PPO]')]
plan_type_HMO=[x for x in plan_types if (x == '[HMO]')]
plan_type_others=[x for x in plan_types if ((x !='[PPO]')&(x !='[HMO]'))]

values=[len(plan_type_PPO),len(plan_type_HMO), len(plan_type_others)]
labels=['PPO','HMO','Others']

#Plot HMO vs PPO
plt.pie(values, labels=labels)
plt.show()

#Unsupported questions
unsupported_user_input= data_in.loc[data_in['Intent']=='unsupported.fallback']
unsupported_user_input.to_csv('Unsupported_questions.csv')

#Id card issues
id_card_unsupported= unsupported_user_input[unsupported_user_input['User Request'].str.contains('card')]
id_card_unsupported.to_csv('unsupported_idCard_questions.csv')

#Extracting the URLs
URL_Colmn= data_in['Quickpick URLs']
URL_Colmn.dropna(inplace=True)



  
        
    
    
    
    
    






