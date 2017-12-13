#!/usr/bin/env python3
# -*- coding: utf-8 -*-

        import pandas as pd
        import numpy as np
        import matplotlib
        import matplotlib.pyplot as plt
        from matplotlib import cm
        from mpl_toolkits.mplot3d import Axes3D
        
        dt=pd.read_csv("./flight1.csv")
        
        
        
        
        
        time=np.array(dt["offsetTime"])
        speed=np.array( dt["Vel:Composite"])
        
        speedV=np.array([dt["Vel:N"], dt["Vel:E"], -dt["Vel:D"]])
        p3dEuler=np.array([dt["Roll"],dt["Pitch"], dt["Yaw"]])
    
        speed[6229:6233] = np.linspace(speed[6227],speed[6233], num=4)
        speedV[0][6229:6233] = np.linspace(speedV[0][6227],speedV[0][6233], num=4)
        speedV[1][6229:6233] = np.linspace(speedV[1][6227],speedV[1][6233], num=4)
        speedV[2][6229:6233] = np.linspace(speedV[2][6227],speedV[2][6233], num=4)
    
        Pitch = p3dEuler[1]*np.pi/180
        Yaw = p3dEuler[2]*np.pi/180
        Roll=p3dEuler[0]*np.pi/180
    
        rotX = [ 
                np.array( [ [1,0,0],
                           [0, np.cos(i), np.sin(i)],
                           [0, -np.sin(i), np.cos(i)]
                        ]) for i in Pitch
                ]
        rotY = [ 
                np.array( [ [np.cos(i), 0, -np.sin(i)],
                           [0, 1, 0],
                           [np.sin(i), 0, np.cos(i)]
                        ]) for i in Roll
                ]
        rotZ = [ 
                np.array( [ [np.cos(i), np.sin(i), 0],
                           [-np.sin(i), np.cos(i), 0],
                           [0,0,1]
                        ]) for i in Yaw
                ]
                
        dirM= np.matmul(rotX,rotY)             
        dirM= np.matmul(dirM, rotZ)             
        
        Vecs=[[],[],[]]
    
    
        s0 = np.matmul(dirM[0],np.array([speedV[0][0],speedV[1][0],speedV[2][0]]))
        
        Vecs[0].append(s0[0])
        Vecs[1].append(s0[1])
        Vecs[2].append(s0[2])
        
        for i in range(1,len(time)):  
            s0=np.matmul(dirM[i],np.array([speedV[0][i],speedV[1][i],speedV[2][i]]))
            Vecs[0].append(s0[0])
            Vecs[1].append(s0[1])
            Vecs[2].append(s0[2])
            
        Vecs2 = [[Vecs[0][0]],[Vecs[1][0]],[Vecs[2][0]]]
        for i in range(1,len(speed)):        
            Vecs2[0].append((Vecs[0][i]+Vecs[0][i-1])*(time[i]-time[i-1])/2)
            Vecs2[1].append((Vecs[1][i]+Vecs[1][i-1])*(time[i]-time[i-1])/2)
            Vecs2[2].append((Vecs[2][i]+Vecs[2][i-1])*(time[i]-time[i-1])/2)
            
            
            
        X0 = 0
        Y0 = 0
        Z0 = 0
        X0=Vecs2[0][0]
        Y0=Vecs2[1][0]        
        Z0=Vecs2[2][0]        
    
        V2= [ [] , [] , []]
        V2[0].append(X0) 
        V2[1].append(Y0)
        V2[2].append(Z0)
    
        for i in range(1, len(Vecs[0])):        
            X0=X0+Vecs2[0][i]
            Y0=Y0+Vecs2[1][i]        
            Z0=Z0+Vecs2[2][i]        
            V2[0].append(X0) 
            V2[1].append(Y0)
            V2[2].append(Z0)  
                  
        fig=plt.figure(figsize=(12,8))
        ax=fig.add_subplot(221)
        surf=ax.scatter(time, V2[0],color="blue")
        ax.set_ylabel("X")
        ax.set_xlabel("Time [s]")
    
        ax=fig.add_subplot(222)
        surf=ax.scatter(time, V2[1],color="blue")
        ax.set_ylabel("Y")
        ax.set_xlabel("Time [s]")
    
        ax=fig.add_subplot(223)
        surf=ax.scatter(time, V2[2],color="blue")
        ax.set_ylabel("Z")
        ax.set_xlabel("Time [s]")
        
    
        ax=fig.add_subplot(224, projection="3d")
        surf=ax.scatter(V2[0], V2[1], V2[2],color="green")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")    
        ax.set_zlabel("Z")       
        plt.show()
            