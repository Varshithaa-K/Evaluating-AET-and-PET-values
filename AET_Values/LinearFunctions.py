#Linear Function 1

def linear(AET,PET):
  mean_aet=np.mean(AET)
  mean_pet=np.mean(PET)
  a5=mean_aet/mean_pet
  return a5*PET


df['AET_lf_P']=linear(AET,df['PET_P'])
df['AET_lf_PM']=linear(AET,df['PET_PM'])
df['AET_lf_PT']=linear(AET,df['PET_PT'])
df['AET_lf_HS']=linear(AET,df['PET_HS'])
df['AET_lf_OD']=linear(AET,df['PET_OD'])
df['AET_lf_Ham']=linear(AET,df['PET_Ham'])
df['AET_lf_TH']=linear(AET,df['PET_TH'])
df['AET_lf_BR']=linear(AET,df['PET_BR'])

#Linear Function 2

def lf_2(pet,a,b):
  return a*np.power(pet,b)

p0=[0.01,0.1]
lower_bound=0.001
upper_bound=1
popt,pcov=curve_fit(lf_2,PET,AET,p0,bounds=[lower_bound,upper_bound])
a=popt[0]
b=popt[1]

print('a :',a)
print('b :',b)

df['AET_PF_P']=a*np.power(df['PET_P'],b)
df['AET_PF_PM']=a*np.power(df['PET_PM'],b)
df['AET_PF_PT']=a*np.power(df['PET_PT'],b)
df['AET_PF_HS']=a*np.power(df['PET_HS'],b)
df['AET_PF_OD']=a*np.power(df['PET_OD'],b)
df['AET_PF_Ham']=a*np.power(df['PET_Ham'],b)
df['AET_PF_TH']=a*np.power(df['PET_TH'],b)
df['AET_PF_BR']=a*np.power(df['PET_BR'],b)

