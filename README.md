Vcenter managment/administration package.

Setup:  
python3 -m venv env  
source env/bin/activate  

env/bin/pip install setuptools==54.2.0 pip==21.0.1  
env/bin/pip install ./vc_manager  

Update vcmgmt.py with your vcenter URL and credentials.  


Examples:  
Show all VMs in my vCenter:  
    vcmgmt machines --show  
  
Show all VMs with "johnadams" in their name:  
    vcmgmt machines --show --keyword johnadams  
  
Destroy all VMs with "nickelback" in their name:  
vcmgmt machines --destroy --keyword nickelback  
