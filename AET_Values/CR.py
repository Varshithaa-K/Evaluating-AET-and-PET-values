#Complementary Relationship function 1
#B1963

df['AET_B1963_P']=2*(df['PET_PT'])-df['PET_P'];
df['AET_B1963_PM']=2*(df['PET_PT'])-df['PET_PM'];
df['AET_B1963_PT']=2*(df['PET_PT'])-df['PET_PT'];
df['AET_B1963_HS']=2*(df['PET_PT'])-df['PET_HS'];
df['AET_B1963_OD']=2*(df['PET_PT'])-df['PET_OD'];
df['AET_B1963_Ham']=2*(df['PET_PT'])-df['PET_Ham'];
df['AET_B1963_TH']=2*(df['PET_PT'])-df['PET_TH'];
df['AET_B1963_BR']=2*(df['PET_PT'])-df['PET_BR'];

#Complementary Relationship function 2
#G1989

#calculate psychrometric constant
PSY = 0.000665*df['PA_F']

T=df['TA_F']
#calculate slope of vapor pressure curve
slope=4098*(0.6108*np.exp((17.27*T)/(T+237.3)))/((T+237.3)**2)

# CR METHODS
df['AET_G1989_P']=(((PSY + slope)/PSY)*(df['PET_PT']))-(PSY/slope)*(df['PET_P']);
df['AET_G1989_PM']=(((PSY + slope)/PSY)*(df['PET_PT']))-(PSY/slope)*(df['PET_PM']);
df['AET_G1989_PT']=(((PSY + slope)/PSY)*(df['PET_PT']))-(PSY/slope)*(df['PET_PT']);
df['AET_G1989_HS']=(((PSY + slope)/PSY)*(df['PET_PT']))-(PSY/slope)*(df['PET_HS']);
df['AET_G1989_OD']=(((PSY + slope)/PSY)*(df['PET_PT']))-(PSY/slope)*(df['PET_OD']);
df['AET_G1989_Ham']=(((PSY + slope)/PSY)*(df['PET_PT']))-(PSY/slope)*(df['PET_Ham']);
df['AET_G1989_TH']=(((PSY + slope)/PSY)*(df['PET_PT']))-(PSY/slope)*(df['PET_TH']);
df['AET_G1989_BR']=(((PSY + slope)/PSY)*(df['PET_PT']))-(PSY/slope)*(df['PET_BR']);

#Complementary Relationship function 3
#B2015

c=0.12;
df['AET_B2015_P']=(np.power(df['PET_PT']/df['PET_P'],2)*(((2-c)*df['PET_P'])-((1-2*c)*df['PET_PT'])-c*np.power(df['PET_PT'],2)/df['PET_P']));
df['AET_B2015_PM']=(np.power(df['PET_PT']/df['PET_PM'],2)*(((2-c)*df['PET_PM'])-((1-2*c)*df['PET_PT'])-c*np.power(df['PET_PT'],2)/df['PET_PM']));
df['AET_B2015_PT']=(np.power(df['PET_PT']/df['PET_PT'],2)*(((2-c)*df['PET_PT'])-((1-2*c)*df['PET_PT'])-c*np.power(df['PET_PT'],2)/df['PET_PT']));
df['AET_B2015_HS']=(np.power(df['PET_PT']/df['PET_HS'],2)*(((2-c)*df['PET_HS'])-((1-2*c)*df['PET_PT'])-c*np.power(df['PET_PT'],2)/df['PET_HS']));
df['AET_B2015_OD']=(np.power(df['PET_PT']/df['PET_OD'],2)*(((2-c)*df['PET_OD'])-((1-2*c)*df['PET_PT'])-c*np.power(df['PET_PT'],2)/df['PET_OD']));
df['AET_B2015_Ham']=(np.power(df['PET_PT']/df['PET_Ham'],2)*(((2-c)*df['PET_Ham'])-((1-2*c)*df['PET_PT'])-c*np.power(df['PET_PT'],2)/df['PET_Ham']));
df['AET_B2015_TH']=(np.power(df['PET_PT']/df['PET_TH'],2)*(((2-c)*df['PET_TH'])-((1-2*c)*df['PET_PT'])-c*np.power(df['PET_PT'],2)/df['PET_TH']));
df['AET_B2015_BR']=(np.power(df['PET_PT']/df['PET_BR'],2)*(((2-c)*df['PET_BR'])-((1-2*c)*df['PET_PT'])-c*np.power(df['PET_PT'],2)/df['PET_BR']));

#Complementary Relationship function 4
#M2015

ε=0.12
df['AET_M2015_P']=(1/ε)*(((1+ε)*df['PET_PT'])-df['PET_P']);
df['AET_M2015_PM']=(1/ε)*(((1+ε)*df['PET_PT'])-df['PET_PM']);
df['AET_M2015_PT']=(1/ε)*(((1+ε)*df['PET_PT'])-df['PET_PT']);
df['AET_M2015_HS']=(1/ε)*(((1+ε)*df['PET_PT'])-df['PET_HS']);
df['AET_M2015_OD']=(1/ε)*(((1+ε)*df['PET_PT'])-df['PET_OD']);
df['AET_M2015_Ham']=(1/ε)*(((1+ε)*df['PET_PT'])-df['PET_Ham']);
df['AET_M2015_TH']=(1/ε)*(((1+ε)*df['PET_PT'])-df['PET_TH']);
df['AET_M2015_BR']=(1/ε)*(((1+ε)*df['PET_PT'])-df['PET_BR']);

df.to_csv("AET_Values_DataSet.csv",index=False)
