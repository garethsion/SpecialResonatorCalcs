# Resonator QED calculations

This package contains a complete workflow for determining Quantum Electrodynamic properties of a given resonator structure. At this stage, only a few calculations are performed, including

* Single/collective spin coupling
* Purcell factor
* Pi pulse fidelity

More calculations can be added by a user in the postprocessing stage.

This package follows a complete workflow, generating the required data using several different academic software packages. The complete workflow is as follows:

1. The user generates the resonator/cross-section geometric parameters in a parameter file
2. The resonator geometry is simulated in CST Microwave Studio, and the impedance for the sytructure is calculated. This can be done in single or batch mode.
3. With this impedance calculated, the spatial dependance of the cacuum current fluctuations (J(x)) is found analytically.
4. J(x) is imported as a funnction into COMSOL, and the cross section of the resonator is simulated. Ampere's law is solved to determine the vacuum field fluctuations $\delta B(x)$ and \delta B(y)$.
5. The field fluctuations are downloaded, and postprocessing can occur with Python.

## Installation

At the moment, the package can be downloaded directly from github 

python setup.py install

In order to completer the full workflow, it is necessary to allow ssh access to the required machines. I hope ultimately to change this so that I can do it automatically (i.e. the user does not have to enter the command - I will have a script which will do it for them)

cd .ssh
vim config
Host galaxy
	User gjones
	HostName galaxy.lcn.ucl.ac.uk
	IdentityFile ~/.ssh/id_rsa

cd .ssh/
ssh-keygen -t rsa

scp id_rsa.pub galaxy:.ssh/authorized_keys# SpecialResonatorCalcs

