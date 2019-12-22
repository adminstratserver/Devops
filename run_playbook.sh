ansible-playbook A_createnewuser.yaml -i inventry.txt -u root
ansible-playbook B_serversecurity.yaml -i inventry.txt -u root
ansible-playbook C_softwareupdate.yaml -i inventry.txt -u djangoadmin16
ansible-playbook D_createdatabase.yaml -i inventry.txt -u djangoadmin16
