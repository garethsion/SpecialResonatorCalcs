python setup.py install

cd .ssh
vim config
Host galaxy
	User gjones
	HostName galaxy.lcn.ucl.ac.uk
	IdentityFile ~/.ssh/id_rsa

cd .ssh/
ssh-keygen -t rsa

scp id_rsa.pub galaxy:.ssh/authorized_keys# SpecialResonatorCalcs
# SpecialResonatorCalcs
