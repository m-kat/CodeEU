#!/usr/bin/env python3
# -*- coding: utf-8 -*-

    import pandas as pd
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
    from matplotlib import cm
    from mpl_toolkits.mplot3d import Axes3D
    
    dt=pd.read_csv("./flight1_mod.csv")
    
    
    
    
    
    time=np.array(dt["offsetTime"])
    speed=np.array( dt["Vel:Composite"])
    p3dA=np.array([dt["Accel:X"],dt["Accel:Y"], dt["Accel:Z"]])
    p3dG=np.array([dt["Gyro:X"],dt["Gyro:Y"], dt["Gyro:Z"]])
    p3dM=np.array([dt["Mag:X"],dt["Mag:Y"], dt["Mag:Z"]])
    
    p3dEuler=np.array([dt["Roll"],dt["Pitch"], dt["Yaw"], dt["offsetTime"]])

    
    fig=plt.figure(figsize=(5,5) , dpi=100)
    ax=fig.add_subplot(111)
    plt.xlabel("Time offset [s]")
    plt.ylabel("Velocity [m/s]")
    ax.scatter(time[0:6228],speed[0:6228], color="blue")
    ax.scatter(time[6228:6232],speed[6228:6232], color="red")
    ax.scatter(time[6233:20000],speed[6233:20000], color="blue")
    ax.annotate( "Error value ", xy=(time[6228],195), xytext = (time[6228], 210),
    arrowprops=dict(arrowstyle="-"))
    ax.set_ylim(0, 220)
    plt.show()
    
    speed[6229:6233] = np.linspace(speed[6227],speed[6233], num=4)

    fig=plt.figure(figsize=(5,5) , dpi=100)
    ax=fig.add_subplot(111)
    plt.xlabel("Time offset [s]")
    plt.ylabel("Velocity [m/s]")
    ax.plot(time,speed, color="blue")
    plt.savefig("./velocity_corr.png")
    plt.show()

    fig=plt.figure(figsize=(12,8) , dpi=100)
    ax=fig.add_subplot(221)
    plt.xlabel("Time offset [s]")
    plt.ylabel("Magnetometer : X")
    ax.plot(time,p3dM[0], color="blue")
    
    ax=fig.add_subplot(222)
    plt.xlabel("Time offset [s]")
    plt.ylabel("Magnetometer : Y")
    ax.plot(time,p3dM[1], color="blue")

    ax=fig.add_subplot(223)
    plt.xlabel("Time offset [s]")
    plt.ylabel("Magnetometer : Z")
    ax.plot(time,p3dM[2], color="blue")

    plt.show()

    fig=plt.figure(figsize=(12,10), dpi=100, frameon=False)    
    ax=fig.add_subplot(111, projection="3d")
    ax.set_title("Magnetometer")    
    ax.set_xlabel("Magnetometer:X")
    ax.set_ylabel("Magnetometer:Y")
    ax.set_zlabel("Magnetometer:Z")
    surf=ax.scatter(p3dM[0],p3dM[1],p3dM[2],color="green")
    plt.show()

    p3dM[0][6229:6233] = np.linspace(p3dM[0][6227], p3dM[0][6233], num=4)
    p3dM[1][6229:6233] = np.linspace(p3dM[1][6227], p3dM[1][6233], num=4)
    p3dM[2][6229:6233] = np.linspace(p3dM[2][6227], p3dM[2][6233], num=4)

    fig=plt.figure(figsize=(12,8) , dpi=100)
    ax=fig.add_subplot(221)
    plt.xlabel("Time offset [s]")
    plt.ylabel("Magnetometer : X")
    ax.plot(w[0],p3dM[0], color="blue")
    
    ax=fig.add_subplot(222)
    plt.xlabel("Time offset [s]")
    plt.ylabel("Magnetometer : Y")
    ax.plot(w[0],p3dM[1], color="blue")

    ax=fig.add_subplot(223)
    plt.xlabel("Time offset [s]")
    plt.ylabel("Magnetometer : Z")
    ax.plot(w[0],p3dM[2], color="blue")
    plt.show()

    fig=plt.figure(figsize=(12,10), dpi=100, frameon=False)    
    ax=fig.add_subplot(111, projection="3d")
    ax.set_title("Magnetometer")    
    ax.set_xlabel("Magnetometer:X")
    ax.set_ylabel("Magnetometer:Y")
    ax.set_zlabel("Magnetometer:Z")
    surf=ax.scatter(p3dM[0],p3dM[1],p3dM[2],color="green")
    plt.show()