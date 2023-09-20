from os import system

namedict={'0P000102ML.L': 'Legal_\&_General_US_Index_Trust', '0P000023C7.L': 'Legal_\&_General_UK_Index_Trust', '0P000023CJ.L': 'Legal_\&_General_Japan_Index_Tr', '0P00015E7M.L': 'Virgin_Global_Share_Fund', '0P000023HM.L': 'Legal_\&_General_Pacific_Index_T', '0P000023NV.L': 'Legal_\&_General_European_Index', '0P000023C5.L': 'L\&G_MSCI_World_Socially_Respons', '0P00002059.L': 'Legal_\&_General_Active_Sterling', '0P0000HN9B.L': 'JPM_Asia_Growth_Fund_B_-_Net_Ac'}

for key in namedict.keys():
    comm='sed -i "s/%s/%s/i" GLdist'%(key,namedict[key])
    print(comm)
    system(comm)
