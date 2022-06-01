import matplotlib.pyplot as plt
import os
import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
            'figure.figsize': (16,9),
            'axes.labelsize': 'xx-large',
            'axes.titlesize': 'xx-large',
            'xtick.labelsize': 'xx-large',
            'ytick.labelsize': 'xx-large'}
pylab.rcParams.update(params)

path = "C:\\Users\\Fernando\\Desktop\\RMN\\"
dirdest = path+'Ficheros\\'
if not os.path.exists(dirdest):
            os.makedirs(dirdest)
else:
    raise('Ya existe una carpeta que se llama así.')
for files in os.listdir(path):
    if files.endswith('.eRP'):
        print(files)
        #df = pd.read_csv(path+files,sep='\t') 
        #df = np.loadtxt(path+files)
        f     = open(path+files,'r',encoding='cp1252')
        #df_list.append(df)
        f.seek(0)
        count = 0
        time  = []
        sp    = []
        for line in f.readlines():
            count+=1
            if count>217:
                try: 
                    l = line.split(',')
                    timefloat=float(l[0])
                    time.append(timefloat)

                    spfloat=float(l[2])
                    sp.append(spfloat)
                except ValueError:
                    continue
        g = open(dirdest+files[:-4]+'.txt', "w")
        for i in range(len(time)):
            data = [str(time[i])+','+str(sp[i])+'\n']
            g.writelines(data)
        g.close()
        plt.plot(time,sp,label=files)
        print('Done!')
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.legend()
plt.xlabel('Tiempo (min)')
plt.ylabel('Sp (dN m)')
plt.savefig(dirdest+'Figura.png')