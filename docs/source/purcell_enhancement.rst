Postprocessing - Purcell Enhancement
====================================

::


    from scipy import constants as sp
    import os
    import numpy as np
    from process_data import ReadComsol,PostProcData

    # Read data from downloads
    file_dbx = os.getcwd() + '/data_postprocess/downloads/exports/Bx_fullData.csv'
    file_dby = os.getcwd() + '/data_postprocess/downloads/exports/By_fullData.csv'

    rdx = ReadComsol.ReadComsol(file_dbx)
    rdy = ReadComsol.ReadComsol(file_dby)

    # Read csv file, and get x,y annd dbx/dby data for each
    # blocked point in space
    bx_x,bx_y,bx_z = rdx.read_full_data()
    by_x,by_y,by_z = rdy.read_full_data()

    dbx = np.asarray(bx_z).astype(np.float)
    dby = np.asarray(by_z).astype(np.float)

    # Postprocess data
    post = PostProcData.PostProcData()

    # Calculate Purcell enhancement at each grid point
    Q = 10000 # Q factor - for now typed in, but will be found from CST calcs ultimately
    purcell = post.purcell_rate(g,Q)
    pdens, pedge = post.purcell_density(bx_x,bx_y,purcell) # density
