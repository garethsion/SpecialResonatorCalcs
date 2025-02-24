Using the Package
=================

There is a specific workflow which must be adhered to in order to use the package.

1. First, you must specify the cpw geometry parameters. I have specified a text file called cpw_parameters.txt where I update the values, and in a preprocessing script I simply read the parameters in from that file. The text file which specifies the parameters looks something like
   
   ::

      w = 10e-06
      t = 50e-09
      l = 8.194e-03
      pen = 200e-09
      omega = 7.3e09
      Z = 50

2. Next, you must define a preprocessing script which sets the cpw geometry parameters, and determines the current density of the structure based on those parameters. See the example current_density.py to get a better idea on how to achieve this.

3. With the current density calculated and stored in a parameter file, you can now remoteley connect to a host computer and run COMSOL. One way to achieve this is to define a python script such as the example remote_interface.py, and run that script from the terminal window with the command python remote_interface.py

4. The remote_interface script will copy the parameter list to the remote machine, update a predefined COMSOL script with the new parameters, remotely run COMSOL, and retrieve the data back to your computer.

5. With the data now retrieved, you can post-process the data to determine certain figuyres of merit. See the post-processing examples.

