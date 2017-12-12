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
    speed=np.array( dt["Vel:Composite"]])
    p3dA=np.array([dt["Accel:X"],dt["Accel:Y"], dt["Accel:Z"]])
    p3dG=np.array([dt["Gyro:X"],dt["Gyro:Y"], dt["Gyro:Z"]])
    p3dM=np.array([dt["Mag:X"],dt["Mag:Y"], dt["Mag:Z"]])
    
    p3dEuler=np.array([dt["Roll"],dt["Pitch"], dt["Yaw"], dt["offsetTime"]])

