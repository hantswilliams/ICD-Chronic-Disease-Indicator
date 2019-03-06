import pandas as pd 
import numpy as np 


cc = pd.read_csv("/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ICD10_ChronicDisease_Indicator/cci_icd10cm_2019_1 (1)/cci_icd10cm_2019_1.csv")


cc.columns=cc.columns.str.replace(" ","")
cc.columns=cc.columns.str.replace("/","")
cc.columns=cc.columns.str.replace("'","")
cc.columns=cc.columns.str.replace("-","")


cc['ICD10CMCODE'] = cc['ICD10CMCODE'].apply(lambda x: x.replace("'",''))
cc['CHRONICINDICATOR'] = cc['CHRONICINDICATOR'].apply(lambda x: x.replace("'",''))
cc['BODYSYSTEM'] = cc['BODYSYSTEM'].apply(lambda x: x.replace("'",''))

cc['CHRONICINDICATOR'] = cc['CHRONICINDICATOR'].astype(int)
cc['CHRONICINDICATOR'] = cc['CHRONICINDICATOR'].replace({0: 'Not_Chronic', 1:'Chronic'})



cc.to_pickle("/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ICD10_ChronicDisease_Indicator/output/icd_cc_indicator.pkl")
cc.to_csv("/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ICD10_ChronicDisease_Indicator/output/icd_cc_indicator.csv", index=False)
