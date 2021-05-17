import matplotlib.pyplot as plt
import numpy as np
import os

#file = open("data_thickness.txt")
#lines = file.readlines()
#lines[0] = []


def interpolate(x,y,a):
    os.chdir('C:/Users/JaianthV/Documents/Globus/XLD_data/XMLD/')
    with open("P_1processed.txt") as f:
             lines = f.readlines()
             Energy_new =[]
         
             del(lines[0])
         
             for line in lines:
                 split = line.split(",");
             
                 Energy_new.append(float(split[0]))
             
    
    from scipy import interpolate

    #f = interpolate.interp1d(Energy, XAS)
    f = interpolate.interp1d(x, y)
    
    if a == 0:
        xnew = Energy_new
    if a != 0:
        xnew = Energy_new[1:len(Energy_new)-9]
                        
    ynew = f(xnew)   # use interpolation function returned by `interp1d`
    #plt.plot(Energy, XAS, 'o',xnew, ynew, '-')
    #plt.plot(xnew, ynew, '-')
    #plt.show()
    return xnew, ynew


os.chdir('C:/Users/JaianthV/Documents/Globus/Digi/')

Files = "Co_XMLD_interp.txt"     
Energy_Co = []
XAS_Co = []

with open(Files) as f:
     lines = f.readlines()
         
             
     for line in lines:
         split = line.split(",");
             
         Energy_Co.append(float(split[0]))
         XAS_Co.append(float(split[1].replace("\n"," ")));
         

Files = "CoO_XMLD_interp.txt"      
Energy_CoO = []
XAS_CoO = []
with open(Files) as f:
     lines = f.readlines()
         
             
     for line in lines:
         split = line.split(",");
             
         Energy_CoO.append(float(split[0]))
         XAS_CoO.append(float(split[1].replace("\n"," ")));





Files = "CoO_exp_XMLD_interp.txt"       
Energy_CoO_exp = []
XAS_CoO_exp = []
with open(Files) as f:
     lines = f.readlines()
         
             
     for line in lines:
         split = line.split(",");
             
         Energy_CoO_exp.append(float(split[0]))
         XAS_CoO_exp.append(float(split[1].replace("\n"," ")));

###XAS



Files = "XAS.csv"       
Energy_Co_xa = []
XAS_Co_xa = []
with open(Files) as f:
     lines = f.readlines()
         
             
     for line in lines:
         split = line.split(",");
             
         Energy_Co_xa.append(float(split[0]))
         XAS_Co_xa.append(float(split[1].replace("\n"," ")));
     Energy_Co_xa_interp, XAS_Co_xa_interp = interpolate(Energy_Co_xa,XAS_Co_xa,0)
     XAS_Co_xa_interp = (XAS_Co_xa_interp - min(XAS_Co_xa_interp))/(max(XAS_Co_xa_interp)-min(XAS_Co_xa_interp))
     
     os.chdir('C:/Users/JaianthV/Documents/Globus/Digi/')
     '''
     filename_area = open("Co_XAS_lit_interp.txt","a")
     for i in range(0,len(Energy_Co_xa_interp)):
         filename_area.write("%f,%f\n"%(Energy_Co_xa_interp[i],XAS_Co_xa_interp[i]))
     filename_area.close()
     '''


os.chdir('C:/Users/JaianthV/Documents/Globus/Digi/')

Files = "XAS_CoO.csv"       
Energy_CoO_xa = []
XAS_CoO_xa = []
with open(Files) as f:
     lines = f.readlines()
         
             
     for line in lines:
         split = line.split(",");
             
         Energy_CoO_xa.append(float(split[0]))
         XAS_CoO_xa.append(float(split[1].replace("\n"," ")));
     Energy_CoO_xa_interp, XAS_CoO_xa_interp = interpolate(Energy_CoO_xa,XAS_CoO_xa,1)
     XAS_CoO_xa_interp = (XAS_CoO_xa_interp - min(XAS_CoO_xa_interp))/(max(XAS_CoO_xa_interp)-min(XAS_CoO_xa_interp))
     os.chdir('C:/Users/JaianthV/Documents/Globus/Digi/')
     '''
     filename_area = open("CoO_XAS_lit_interp.txt","a")
     for i in range(0,len(Energy_CoO_xa_interp)):
         filename_area.write("%f,%f\n"%(Energy_CoO_xa_interp[i],XAS_CoO_xa_interp[i]))
     filename_area.close()
     '''


os.chdir('C:/Users/JaianthV/Documents/Globus/Digi/')

Files = "CoO_exp_XAS_interp.txt"       
Energy_CoO_exp_xa = []
XAS_CoO_exp_xa = []
with open(Files) as f:
     lines = f.readlines()
         
             
     for line in lines:
         split = line.split(",");
             
         Energy_CoO_exp_xa.append(float(split[0]))
         XAS_CoO_exp_xa.append(float(split[1].replace("\n"," ")));
     
   

'''         
Files = ["XMLD.csv"]
for i in range (len(Files)):
    
    with open(Files[i]) as f:
         lines = f.readlines()
         
         del(lines[0])
         
         for line in lines:
             split = line.split(",");
             
             Energy.append(float(split[0]))
             XAS.append(float(split[1].replace("\n"," ")));
             Length_array.append(len(XAS))
'''


'''     
filename_area = open("Co_XAS_lit_interp.txt","a")
for i in range(0,len(xnew)):
    filename_area.write("%f,%f\n"%(xnew[i],ynew[i]))
filename_area.close()
'''
Energy_CoO_exp = list(np.array(Energy_CoO_exp)-1.6)
Energy_CoO= list(np.array(Energy_CoO)+0.5)
XAS_Co = list((np.array(XAS_Co))*0.09)
XAS_CoO = list((np.array(XAS_CoO))*1.6)
XAS_CoO_exp = list((np.array(XAS_CoO_exp)))


XAS_Co = list((np.array(XAS_Co))/0.85)
XAS_CoO = list(((np.array(XAS_CoO))/6))
XAS_CoO_exp = list(((np.array(XAS_CoO_exp))/0.55))




Energy_Co_xa_interp = list(np.array(Energy_Co_xa_interp)-0)
XAS_Co_xa_interp = list(np.array(XAS_Co_xa_interp))

Energy_CoO_xa_interp = list(np.array(Energy_CoO_xa_interp)+0.5)
XAS_CoO_xa_interp = list(np.array(XAS_CoO_xa_interp))

Energy_CoO_exp_xa = list(np.array(Energy_CoO_exp_xa)-1.6)
XAS_CoO_exp_xa = list(np.array(XAS_CoO_exp_xa))

#plt.plot(Energy_Co_xa_interp,XAS_Co_xa_interp,Energy_CoO_xa_interp,XAS_CoO_xa_interp,Energy_CoO_exp_xa,XAS_CoO_exp_xa, linewidth='4')

#plt.plot(Energy_Co_xa_interp,XAS_Co_xa_interp,Energy_CoO_xa_interp,XAS_CoO_xa_interp, linewidth='4')

#XAS_Co = (XAS_Co - min(XAS_Co))/(max(XAS_Co)-min(XAS_Co))

#XAS_CoO = (XAS_CoO - min(XAS_CoO))/(max(XAS_CoO)-min(XAS_CoO))
#XAS_CoO = (XAS_CoO*1/6)

#XAS_CoO_exp = (XAS_CoO_exp - min(XAS_CoO_exp))/(max(XAS_CoO_exp)-min(XAS_CoO_exp))
          
plt.plot(Energy_Co,XAS_Co,Energy_CoO,XAS_CoO,Energy_CoO_exp,XAS_CoO_exp, linewidth='4')
print (len(Energy_CoO))
#plt.plot(Energy_Co[3:60],XAS_Co[3:60],Energy_CoO,XAS_CoO)

plt.axvline(x = 779, color = 'r', linestyle = '-')
plt.axvline(x = 780, color = 'r', linestyle = '-')


'''
plt.axvline(x = 777.4, color = 'r', linestyle = '-')
plt.axvline(x = 777.8, color = 'r', linestyle = '-')


plt.axvline(x = 778.4, color = 'b', linestyle = '-')
plt.axvline(x = 778.8, color = 'b', linestyle = '-')
'''
'''


plt.axvline(x = 777.4, color = 'r', linestyle = '-')
plt.axvline(x = 777.8, color = 'r', linestyle = '-')


plt.axvline(x = 778.6, color = 'b', linestyle = '-')
plt.axvline(x = 779.8, color = 'b', linestyle = '-')
'''


plt.xlabel("Energy (e.V)", fontsize = 15)
plt.ylabel("XMLD (a.u.)", fontsize = 15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(["Co","CoO","CoO_exp"], loc='top right')
#plt.ylim(0,1.09)
plt.xlim(770,790)
#text = 'Average ='+str(round(average,1)) + ' $\pm$ 0.9 ($\mu$m) '
plt.text(774.3, 1.2, "E1(779 eV)" , fontsize=15)
plt.text(780, 1.2, "E2(780 eV)" , fontsize=15)
#plt.yscale("linear")
#plt.xscale("log")
#plt.title("Co", fontsize = 15)
plt.show()
