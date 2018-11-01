#!/usr/bin/env python
from subprocess import call
import os

class SSHCommand:
    def __init__(self):
        return

    def upload_data(self):
        print("Uploading data to remote machine")
        rc = call("ssh_command/upload_data")

    def run_comsol(self):
        print("Running COMSOL on remote machine...")
        rc = call("ssh_command/run_comsol")

    def set_comsol_parameters(self):
        print("Uploading comsol parameter files...")
        rc = call("ssh_command/set_comsol_data")

    def get_comsol_data(self):
        print("Retrieving comsol datafiles...")
        rc = call("ssh_command/get_comsol_data")

    def scp_params(self):
        print('scp data to remote machine...')
        rc = call("ssh_command/set_comsol_data")
