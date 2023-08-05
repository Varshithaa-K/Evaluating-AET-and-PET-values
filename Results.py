import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

df=pd.read_csv("AET_Values_DataSet.csv")
d1=pd.read_csv("Evaluation.csv")

df.dtypes

#Nash and Sutcliffe Efficieny Co-efficient
#NSE For NLF1

ET_obs = df['AET_MS']         # observed evapotranspiration
ET_pred_NLF1_PM = df['AET_NLF1_PM'] # predicted evapotranspiration
ET_pred_NLF1_PT = df['AET_NLF1_PT']
ET_pred_NLF1_P = df['AET_NLF1_P']
ET_pred_NLF1_HS = df['AET_NLF1_HS']
ET_pred_NLF1_OD = df['AET_NLF1_OD']
ET_pred_NLF1_Ham = df['AET_NLF1_Ham']

# Calculate the mean of the observed evapotranspiration values
ET_obs_mean = np.mean(ET_obs)

# Calculate the numerator and denominator of the NSE equation
numerator_NLF1_PM = np.sum((ET_obs - ET_pred_NLF1_PM)**2)
numerator_NLF1_PT = np.sum((ET_obs - ET_pred_NLF1_PT)**2)
numerator_NLF1_P = np.sum((ET_obs - ET_pred_NLF1_P)**2)
numerator_NLF1_HS = np.sum((ET_obs - ET_pred_NLF1_HS)**2)
numerator_NLF1_OD = np.sum((ET_obs - ET_pred_NLF1_OD)**2)
numerator_NLF1_Ham = np.sum((ET_obs - ET_pred_NLF1_Ham)**2)

denominator=np.sum((ET_obs-ET_obs_mean)**2)

# Calculate the NSE value
NSE_NLF1_PM = 1 - numerator_NLF1_PM / denominator
NSE_NLF1_PT = 1 - numerator_NLF1_PT / denominator
NSE_NLF1_P = 1 - numerator_NLF1_P / denominator
NSE_NLF1_HS = 1 - numerator_NLF1_HS / denominator
NSE_NLF1_OD = 1 - numerator_NLF1_OD / denominator
NSE_NLF1_Ham= 1 - numerator_NLF1_Ham / denominator

d1['NLF1']=[NSE_NLF1_PM,NSE_NLF1_PT,NSE_NLF1_P,NSE_NLF1_HS,NSE_NLF1_OD,NSE_NLF1_Ham]

# Print the NSE value
print("NSE_NLF1_PM : ",NSE_NLF1_PM)
print("NSE_NLF1_PT : ",NSE_NLF1_PT)
print("NSE_NLF1_P : ",NSE_NLF1_P)
print("NSE_NLF1_HS : ",NSE_NLF1_HS)
print("NSE_NLF1_OD : ",NSE_NLF1_OD)
print("NSE_NLF1_Ham : ",NSE_NLF1_Ham)

#Nash and Sutcliffe Efficieny Co-efficient
#NSE For NLF2

ET_obs = df['AET_MS']         # observed evapotranspiration
ET_pred_NLF2_PM = df['AET_NLF2_PM'] # predicted evapotranspiration
ET_pred_NLF2_PT = df['AET_NLF2_PT']
ET_pred_NLF2_P = df['AET_NLF2_P']
ET_pred_NLF2_HS = df['AET_NLF2_HS']
ET_pred_NLF2_OD = df['AET_NLF2_OD']
ET_pred_NLF2_Ham = df['AET_NLF2_Ham']

# Calculate the mean of the observed evapotranspiration values
ET_obs_mean = np.mean(ET_obs)

# Calculate the numerator and denominator of the NSE equation
numerator_NLF2_PM = np.sum((ET_obs - ET_pred_NLF2_PM)**2)
numerator_NLF2_PT = np.sum((ET_obs - ET_pred_NLF2_PT)**2)
numerator_NLF2_P = np.sum((ET_obs - ET_pred_NLF2_P)**2)
numerator_NLF2_HS = np.sum((ET_obs - ET_pred_NLF2_HS)**2)
numerator_NLF2_OD = np.sum((ET_obs - ET_pred_NLF2_OD)**2)
numerator_NLF2_Ham = np.sum((ET_obs - ET_pred_NLF2_Ham)**2)

denominator=np.sum((ET_obs-ET_obs_mean)**2)

# Calculate the NSE value
NSE_NLF2_PM = 1 - numerator_NLF2_PM / denominator
NSE_NLF2_PT = 1 - numerator_NLF2_PT / denominator
NSE_NLF2_P = 1 - numerator_NLF2_P / denominator
NSE_NLF2_HS = 1 - numerator_NLF2_HS / denominator
NSE_NLF2_OD = 1 - numerator_NLF2_OD / denominator
NSE_NLF2_Ham= 1 - numerator_NLF2_Ham / denominator

d1['NLF2']=[NSE_NLF2_PM,NSE_NLF2_PT,NSE_NLF2_P,NSE_NLF2_HS,NSE_NLF2_OD,NSE_NLF2_Ham]

# Print the NSE value
print("NSE_NLF2_PM : ",NSE_NLF2_PM)
print("NSE_NLF2_PT : ",NSE_NLF2_PT)
print("NSE_NLF2_P : ",NSE_NLF2_P)
print("NSE_NLF2_HS : ",NSE_NLF2_HS)
print("NSE_NLF2_OD : ",NSE_NLF2_OD)
print("NSE_NLF2_Ham : ",NSE_NLF2_Ham)

#Nash and Sutcliffe Efficieny Co-efficient
#NSE For NLF3

ET_obs = df['AET_MS']         # observed evapotranspiration
ET_pred_NLF3_PM = df['AET_NLF3_PM'] # predicted evapotranspiration
ET_pred_NLF3_PT = df['AET_NLF3_PT']
ET_pred_NLF3_P = df['AET_NLF3_P']
ET_pred_NLF3_HS = df['AET_NLF3_HS']
ET_pred_NLF3_OD = df['AET_NLF3_OD']
ET_pred_NLF3_Ham = df['AET_NLF3_Ham']

# Calculate the mean of the observed evapotranspiration values
ET_obs_mean = np.mean(ET_obs)

# Calculate the numerator and denominator of the NSE equation
numerator_NLF3_PM = np.sum((ET_obs - ET_pred_NLF3_PM)**2)
numerator_NLF3_PT = np.sum((ET_obs - ET_pred_NLF3_PT)**2)
numerator_NLF3_P = np.sum((ET_obs - ET_pred_NLF3_P)**2)
numerator_NLF3_HS = np.sum((ET_obs - ET_pred_NLF3_HS)**2)
numerator_NLF3_OD = np.sum((ET_obs - ET_pred_NLF3_OD)**2)
numerator_NLF3_Ham = np.sum((ET_obs - ET_pred_NLF3_Ham)**2)

denominator=np.sum((ET_obs-ET_obs_mean)**2)

# Calculate the NSE value
NSE_NLF3_PM = 1 - numerator_NLF3_PM / denominator
NSE_NLF3_PT = 1 - numerator_NLF3_PT / denominator
NSE_NLF3_P = 1 - numerator_NLF3_P / denominator
NSE_NLF3_HS = 1 - numerator_NLF3_HS / denominator
NSE_NLF3_OD = 1 - numerator_NLF3_OD / denominator
NSE_NLF3_Ham= 1 - numerator_NLF3_Ham / denominator

d1['NLF3']=[NSE_NLF3_PM,NSE_NLF3_PT,NSE_NLF3_P,NSE_NLF3_HS,NSE_NLF3_OD,NSE_NLF3_Ham]

# Print the NSE value
print("NSE_NLF3_PM : ",NSE_NLF3_PM)
print("NSE_NLF3_PT : ",NSE_NLF3_PT)
print("NSE_NLF3_P : ",NSE_NLF3_P)
print("NSE_NLF3_HS : ",NSE_NLF3_HS)
print("NSE_NLF3_OD : ",NSE_NLF3_OD)
print("NSE_NLF3_Ham : ",NSE_NLF3_Ham)

#Nash and Sutcliffe Efficieny Co-efficient
#NSE For NLF4

ET_obs = df['AET_MS']         # observed evapotranspiration
ET_pred_NLF4_PM = df['AET_NLF4_PM'] # predicted evapotranspiration
ET_pred_NLF4_PT = df['AET_NLF4_PT']
ET_pred_NLF4_P = df['AET_NLF4_P']
ET_pred_NLF4_HS = df['AET_NLF4_HS']
ET_pred_NLF4_OD = df['AET_NLF4_OD']
ET_pred_NLF4_Ham = df['AET_NLF4_Ham']

# Calculate the mean of the observed evapotranspiration values
ET_obs_mean = np.mean(ET_obs)

# Calculate the numerator and denominator of the NSE equation
numerator_NLF4_PM = np.sum((ET_obs - ET_pred_NLF4_PM)**2)
numerator_NLF4_PT = np.sum((ET_obs - ET_pred_NLF4_PT)**2)
numerator_NLF4_P = np.sum((ET_obs - ET_pred_NLF4_P)**2)
numerator_NLF4_HS = np.sum((ET_obs - ET_pred_NLF4_HS)**2)
numerator_NLF4_OD = np.sum((ET_obs - ET_pred_NLF4_OD)**2)
numerator_NLF4_Ham = np.sum((ET_obs - ET_pred_NLF4_Ham)**2)

denominator=np.sum((ET_obs-ET_obs_mean)**2)

# Calculate the NSE value
NSE_NLF4_PM = 1 - numerator_NLF4_PM / denominator
NSE_NLF4_PT = 1 - numerator_NLF4_PT / denominator
NSE_NLF4_P = 1 - numerator_NLF4_P / denominator
NSE_NLF4_HS = 1 - numerator_NLF4_HS / denominator
NSE_NLF4_OD = 1 - numerator_NLF4_OD / denominator
NSE_NLF4_Ham= 1 - numerator_NLF4_Ham / denominator

d1['NLF4']=[NSE_NLF4_PM,NSE_NLF4_PT,NSE_NLF4_P,NSE_NLF4_HS,NSE_NLF4_OD,NSE_NLF4_Ham]

# Print the NSE value
print("NSE_NLF4_PM : ",NSE_NLF4_PM)
print("NSE_NLF4_PT : ",NSE_NLF4_PT)
print("NSE_NLF4_P : ",NSE_NLF4_P)
print("NSE_NLF4_HS : ",NSE_NLF4_HS)
print("NSE_NLF4_OD : ",NSE_NLF4_OD)
print("NSE_NLF4_Ham : ",NSE_NLF4_Ham)

#Nash and Sutcliffe Efficieny Co-efficient
#NSE For LF1

ET_obs = df['AET_MS']         # observed evapotranspiration
ET_pred_LF1_PM = df['AET_lf_PM'] # predicted evapotranspiration
ET_pred_LF1_PT = df['AET_lf_PT']
ET_pred_LF1_P = df['AET_lf_P']
ET_pred_LF1_HS = df['AET_lf_HS']
ET_pred_LF1_OD = df['AET_lf_OD']
ET_pred_LF1_Ham = df['AET_lf_Ham']

# Calculate the mean of the observed evapotranspiration values
ET_obs_mean = np.mean(ET_obs)

# Calculate the numerator and denominator of the NSE equation
numerator_LF1_PM = np.sum((ET_obs - ET_pred_LF1_PM)**2)
numerator_LF1_PT = np.sum((ET_obs - ET_pred_LF1_PT)**2)
numerator_LF1_P = np.sum((ET_obs - ET_pred_LF1_P)**2)
numerator_LF1_HS = np.sum((ET_obs - ET_pred_LF1_HS)**2)
numerator_LF1_OD = np.sum((ET_obs - ET_pred_LF1_OD)**2)
numerator_LF1_Ham = np.sum((ET_obs - ET_pred_LF1_Ham)**2)

denominator=np.sum((ET_obs-ET_obs_mean)**2)

# Calculate the NSE value
NSE_LF1_PM = 1 - numerator_LF1_PM / denominator
NSE_LF1_PT = 1 - numerator_LF1_PT / denominator
NSE_LF1_P = 1 - numerator_LF1_P / denominator
NSE_LF1_HS = 1 - numerator_LF1_HS / denominator
NSE_LF1_OD = 1 - numerator_LF1_OD / denominator
NSE_LF1_Ham= 1 - numerator_LF1_Ham / denominator

d1['LF']=[NSE_LF1_PM,NSE_LF1_PT,NSE_LF1_P,NSE_LF1_HS,NSE_LF1_OD,NSE_LF1_Ham]

# Print the NSE value
print("NSE_LF1_PM : ",NSE_LF1_PM)
print("NSE_LF1_PT : ",NSE_LF1_PT)
print("NSE_LF1_P : ",NSE_LF1_P)
print("NSE_LF1_HS : ",NSE_LF1_HS)
print("NSE_LF1_OD : ",NSE_LF1_OD)
print("NSE_LF1_Ham : ",NSE_LF1_Ham)

#Nash and Sutcliffe Efficieny Co-efficient
#NSE For LF2 OR POWER FUNCTION

ET_obs = df['AET_MS']         # observed evapotranspiration
ET_pred_LF2_PM = df['AET_PF_PM'] # predicted evapotranspiration
ET_pred_LF2_PT = df['AET_PF_PT']
ET_pred_LF2_P = df['AET_PF_P']
ET_pred_LF2_HS = df['AET_PF_HS']
ET_pred_LF2_OD = df['AET_PF_OD']
ET_pred_LF2_Ham = df['AET_PF_Ham']

# Calculate the mean of the observed evapotranspiration values
ET_obs_mean = np.mean(ET_obs)

# Calculate the numerator and denominator of the NSE equation
numerator_LF2_PM = np.sum((ET_obs - ET_pred_LF2_PM)**2)
numerator_LF2_PT = np.sum((ET_obs - ET_pred_LF2_PT)**2)
numerator_LF2_P = np.sum((ET_obs - ET_pred_LF2_P)**2)
numerator_LF2_HS = np.sum((ET_obs - ET_pred_LF2_HS)**2)
numerator_LF2_OD = np.sum((ET_obs - ET_pred_LF2_OD)**2)
numerator_LF2_Ham = np.sum((ET_obs - ET_pred_LF2_Ham)**2)

denominator=np.sum((ET_obs-ET_obs_mean)**2)

# Calculate the NSE value
NSE_LF2_PM = 1 - numerator_LF2_PM / denominator
NSE_LF2_PT = 1 - numerator_LF2_PT / denominator
NSE_LF2_P = 1 - numerator_LF2_P / denominator
NSE_LF2_HS = 1 - numerator_LF2_HS / denominator
NSE_LF2_OD = 1 - numerator_LF2_OD / denominator
NSE_LF2_Ham= 1 - numerator_LF2_Ham / denominator

d1['PF']=[NSE_LF2_PM,NSE_LF2_PT,NSE_LF2_P,NSE_LF2_HS,NSE_LF2_OD,NSE_LF2_Ham]

# Print the NSE value
print("NSE_LF2_PM : ",NSE_LF2_PM)
print("NSE_LF2_PT : ",NSE_LF2_PT)
print("NSE_LF2_P : ",NSE_LF2_P)
print("NSE_LF2_HS : ",NSE_LF2_HS)
print("NSE_LF2_OD : ",NSE_LF2_OD)
print("NSE_LF2_Ham : ",NSE_LF2_Ham)

#Nash and Sutcliffe Efficieny Co-efficient
#NSE For Complementary relationship Function B1963

ET_obs = df['AET_MS']         # observed evapotranspiration
ET_pred_b1963_PM = df['AET_B1963_PM'] # predicted evapotranspiration
ET_pred_b1963_PT = df['AET_B1963_PT']
ET_pred_b1963_P = df['AET_B1963_P']
ET_pred_b1963_HS = df['AET_B1963_HS']
ET_pred_b1963_OD = df['AET_B1963_OD']
ET_pred_b1963_Ham = df['AET_B1963_Ham']

# Calculate the mean of the observed evapotranspiration values
ET_obs_mean = np.mean(ET_obs)

# Calculate the numerator and denominator of the NSE equation
numerator_b1963_PM = np.sum((ET_obs - ET_pred_b1963_PM)**2)
numerator_b1963_PT = np.sum((ET_obs - ET_pred_b1963_PT)**2)
numerator_b1963_P = np.sum((ET_obs - ET_pred_b1963_P)**2)
numerator_b1963_HS = np.sum((ET_obs - ET_pred_b1963_HS)**2)
numerator_b1963_OD = np.sum((ET_obs - ET_pred_b1963_OD)**2)
numerator_b1963_Ham = np.sum((ET_obs - ET_pred_b1963_Ham)**2)

denominator=np.sum((ET_obs-ET_obs_mean)**2)

# Calculate the NSE value
NSE_b1963_PM = 1 - numerator_b1963_PM / denominator
NSE_b1963_PT = 1 - numerator_b1963_PT / denominator
NSE_b1963_P = 1 - numerator_b1963_P / denominator
NSE_b1963_HS = 1 - numerator_b1963_HS / denominator
NSE_b1963_OD = 1 - numerator_b1963_OD / denominator
NSE_b1963_Ham= 1 - numerator_b1963_Ham / denominator

d1['LF']=[NSE_b1963_PM,NSE_b1963_PT,NSE_b1963_P,NSE_b1963_HS,NSE_b1963_OD,NSE_b1963_Ham]

# Print the NSE value
print("NSE_b1963_PM : ",NSE_b1963_PM)
print("NSE_b1963_PT : ",NSE_b1963_PT)
print("NSE_b1963_P : ",NSE_b1963_P)
print("NSE_b1963_HS : ",NSE_b1963_HS)
print("NSE_b1963_OD : ",NSE_b1963_OD)
print("NSE_b1963_Ham : ",NSE_b1963_Ham)

#Calculating Relative Error

# calculate mean observed value

mean_observed = np.mean(df['LE_F_MDS']/2.45)

# calculate RE for each data point
residuals_NLF1_P = (df['LE_F_MDS']/2.45) - df['AET_NLF1_P']
residuals_NLF2_P = (df['LE_F_MDS']/2.45) - df['AET_NLF2_P']
residuals_NLF3_P = (df['LE_F_MDS']/2.45) - df['AET_NLF3_P']
residuals_NLF4_P = (df['LE_F_MDS']/2.45) - df['AET_NLF4_P']
residuals_linear_P = (df['LE_F_MDS']/2.45) - df['AET_lf_P']
residuals_power_P = (df['LE_F_MDS']/2.45) - df['AET_PF_P']

relative_errors_NLF1_P = residuals_NLF1_P / mean_observed
relative_errors_NLF2_P = residuals_NLF2_P / mean_observed
relative_errors_NLF3_P = residuals_NLF3_P / mean_observed
relative_errors_NLF4_P = residuals_NLF4_P / mean_observed
relative_errors_linear_P = residuals_linear_P / mean_observed
relative_errors_power_P = residuals_power_P / mean_observed


# calculate mean RE
mean_re_NLF1 = np.mean(relative_errors_NLF1_P)
mean_re_NLF2 = np.mean(relative_errors_NLF2_P)
mean_re_NLF3 = np.mean(relative_errors_NLF3_P)
mean_re_NLF4 = np.mean(relative_errors_NLF4_P)
mean_re_linear = np.mean(relative_errors_linear_P)
mean_re_power =  np.mean(relative_errors_power_P)

#print the values
print("re_NLF1 : ",mean_re_NLF1)
print("re_NLF2 : ",mean_re_NLF2)
print("re_NLF3 : ",mean_re_NLF3)
print("re_NLF4 : ",mean_re_NLF4)
print("re_linear : ",mean_re_linear)
print("re_power : ",mean_re_power)

# Assuming you have two arrays, one with observed values and one with predicted values
observed_values = df['LE_F_MDS']/2.45
predicted_values_NLF1 = df['AET_NLF1_PM']
predicted_values_NLF2 = df['AET_NLF2_PM']
predicted_values_NLF3 = df['AET_NLF3_PM']
predicted_values_NLF4 = df['AET_NLF4']
predicted_values_linear = df['AET_linear']
predicted_values_power = df['AET_power']

# Calculate the difference between observed and predicted values
diff_NLF1 = observed_values - predicted_values_NLF1
diff_NLF2 = observed_values - predicted_values_NLF2
diff_NLF3 = observed_values - predicted_values_NLF3
diff_NLF4 = observed_values - predicted_values_NLF4
diff_linear = observed_values - predicted_values_linear
diff_power = observed_values - predicted_values_power

# Square the difference
sq_diff_NLF1 = diff_NLF1 ** 2
sq_diff_NLF2 = diff_NLF2 ** 2
sq_diff_NLF3 = diff_NLF3 ** 2
sq_diff_NLF4 = diff_NLF4 ** 2
sq_diff_linear = diff_linear ** 2
sq_diff_power= diff_power ** 2


# Calculate the mean of squared differences
mean_sq_diff_NLF1 = np.mean(sq_diff_NLF1)
mean_sq_diff_NLF2 = np.mean(sq_diff_NLF2)
mean_sq_diff_NLF3 = np.mean(sq_diff_NLF3)
mean_sq_diff_NLF4 = np.mean(sq_diff_NLF4)
mean_sq_diff_linear = np.mean(sq_diff_linear)
mean_sq_diff_power = np.mean(sq_diff_power)

# Take the square root of mean squared differences to get RMSE
rmse_NLF1 = np.sqrt(mean_sq_diff_NLF1)
rmse_NLF2 = np.sqrt(mean_sq_diff_NLF2)
rmse_NLF3 = np.sqrt(mean_sq_diff_NLF3)
rmse_NLF4 = np.sqrt(mean_sq_diff_NLF4)
rmse_linear = np.sqrt(mean_sq_diff_linear)
rmse_power = np.sqrt(mean_sq_diff_power)

print("RMSE_NLF1:", rmse_NLF1)
print("RMSE_NLF2:", rmse_NLF2)
print("RMSE_NLF3:", rmse_NLF3)
print("RMSE_NLF4:", rmse_NLF4)
print("RMSE_linear:", rmse_linear)
print("RMSE_power:", rmse_power)

observed_data = df['LE_F_MDS']/2.45
simulated_data_NLF1 = df['AET_NLF1']
simulated_data_NLF2 = df['AET_NLF2']
simulated_data_NLF3 = df['AET_NLF3']
simulated_data_NLF4 = df['AET_NLF4']
simulated_data_linear = df['AET_linear']
simulated_data_power = df['AET_power']


# calculate mean and standard deviation of observed and simulated data
mean_obs = np.mean(observed_data)
sd_obs = np.std(observed_data)
mean_sim_NLF1 = np.mean(simulated_data_NLF1)
mean_sim_NLF2 = np.mean(simulated_data_NLF2)
mean_sim_NLF3 = np.mean(simulated_data_NLF3)
mean_sim_NLF4 = np.mean(simulated_data_NLF4)
mean_sim_linear = np.mean(simulated_data_linear)
mean_sim_power = np.mean(simulated_data_power)

sd_sim_NLF1 = np.std(simulated_data_NLF1)
sd_sim_NLF2 = np.std(simulated_data_NLF2)
sd_sim_NLF3 = np.std(simulated_data_NLF3)
sd_sim_NLF4 = np.std(simulated_data_NLF4)
sd_sim_linear = np.std(simulated_data_linear)
sd_sim_power = np.std(simulated_data_power)

# calculate correlation coefficient (CC) between observed and simulated data
cc_NLF1 = np.corrcoef(observed_data, simulated_data_NLF1)[0,1]
cc_NLF2 = np.corrcoef(observed_data,simulated_data_NLF2)[0,1]
cc_NLF3 = np.corrcoef(observed_data,simulated_data_NLF3)[0,1]
cc_NLF4 = np.corrcoef(observed_data,simulated_data_NLF4)[0,1]
cc_linear = np.corrcoef(observed_data,simulated_data_linear)[0,1]
cc_power = np.corrcoef(observed_data,simulated_data_power)[0,1]

# calculate relative error (RE) between observed and simulated data
re_NLF1 = np.sum(np.abs(np.array(simulated_data_NLF1) - np.array(observed_data))) / np.sum(np.array(observed_data))
re_NLF2 = np.sum(np.abs(np.array(simulated_data_NLF2) - np.array(observed_data))) / np.sum(np.array(observed_data))
re_NLF3 = np.sum(np.abs(np.array(simulated_data_NLF3) - np.array(observed_data))) / np.sum(np.array(observed_data))
re_NLF4 = np.sum(np.abs(np.array(simulated_data_NLF4) - np.array(observed_data))) / np.sum(np.array(observed_data))
re_linear = np.sum(np.abs(np.array(simulated_data_linear) - np.array(observed_data))) / np.sum(np.array(observed_data))
re_power = np.sum(np.abs(np.array(simulated_data_power) - np.array(observed_data))) / np.sum(np.array(observed_data))

# calculate KGE
kge_NLF1 = 1 - np.sqrt((cc_NLF1-1)**2 + (re_NLF1-1)**2 + (np.log(sd_sim_NLF1/sd_obs))**2)
kge_NLF2 = 1 - np.sqrt((cc_NLF2-1)**2 + (re_NLF2-1)**2 + (np.log(sd_sim_NLF2/sd_obs))**2)
kge_NLF3 = 1 - np.sqrt((cc_NLF3-1)**2 + (re_NLF3-1)**2 + (np.log(sd_sim_NLF3/sd_obs))**2)
kge_NLF4 = 1 - np.sqrt((cc_NLF4-1)**2 + (re_NLF4-1)**2 + (np.log(sd_sim_NLF4/sd_obs))**2)
kge_linear = 1 - np.sqrt((cc_linear-1)**2 + (re_linear-1)**2 + (np.log(sd_sim_linear/sd_obs))**2)
kge_power = 1 - np.sqrt((cc_power-1)**2 + (re_power-1)**2 + (np.log(sd_sim_power/sd_obs))**2)

print("KGE_NLF1:", kge_NLF1)
print("KGE_NLF2:", kge_NLF2)
print("KGE_NLF3:", kge_NLF3)
print("KGE_NLF4:", kge_NLF4)
print("KGE_linear:", kge_linear)
print("KGE_power:", kge_power)

# Load NSE data for each PET method into a pandas DataFrame


obs=df['AET_MS']
numerator_HS = np.sum((df['PET_HS'] -obs)**2)
numerator_TH = np.sum((df['PET_TH'] -obs)**2)
numerator_OD = np.sum((df['PET_OD'] -obs)**2)
numerator_Ham = np.sum((df['PET_Ham'] -obs)**2)
numerator_BR = np.sum((df['PET_BR'] -obs)**2)

obs_mean=np.mean(obs)

denominator=np.sum((obs-obs_mean)**2)

# Calculate the NSE value
NSE_HS = 1 - numerator_HS / denominator
NSE_TH = 1 - numerator_TH / denominator
NSE_OD = 1 - numerator_OD / denominator
NSE_Ham = 1 - numerator_Ham / denominator
NSE_BR = 1 - numerator_BR / denominator

print("NSE_HS : ",NSE_HS)
print("NSE_TH : ",NSE_TH)
print("NSE_OD : ",NSE_OD)
print("NSE_Ham : ",NSE_Ham)
print("NSE_BR : ",NSE_BR)

#Calculating Relative Error

# calculate mean observed value

mean_observed = np.mean(df['PET_PM']*28.9)

# calculate RE for each data point
residuals_HS = (df['AET_MS'])-df['PET_HS']
residuals_TH = (df['AET_MS'])-df['PET_TH']
residuals_OD = (df['AET_MS'])-df['PET_OD']
residuals_Ham = (df['AET_MS'])-df['PET_Ham']
residuals_BR = (df['AET_MS'])-df['PET_BR']

relative_errors_HS=residuals_HS/mean_observed
relative_errors_TH=residuals_TH/mean_observed
relative_errors_OD=residuals_OD/mean_observed
relative_errors_Ham=residuals_Ham/mean_observed
relative_errors_BR=residuals_BR/mean_observed

# calculate mean RE
mean_re_HS=np.mean(relative_errors_HS)
mean_re_TH=np.mean(relative_errors_TH)
mean_re_OD=np.mean(relative_errors_OD)
mean_re_Ham=np.mean(relative_errors_Ham)
mean_re_BR=np.mean(relative_errors_BR)

#print the values
print("RE_HS : ",mean_re_HS)
print("RE_TH : ",mean_re_TH)
print("RE_OD : ",mean_re_OD)
print("RE_Ham : ",mean_re_Ham)
print("RE_BR : ",mean_re_BR)

