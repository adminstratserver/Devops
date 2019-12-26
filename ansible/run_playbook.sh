ansible-playbook A_createnewuser.yaml -i inventry.txt -u root
ansible-playbook B_serversecurity.yaml -i inventry.txt -u root
ansible-playbook C_softwareupdate.yaml -i inventry.txt -u djangoadmin16
ansible-playbook D_createdatabase.yaml -i inventry.txt -u djangoadmin16
ansible-playbook E_pullfilesfromserver.yaml -i inventry.txt -u djangoadmin16
ansible-playbook F_installpackages.yaml -i inventry.txt -u djangoadmin16
ansible-playbook G_djangomigrate.yaml -i inventry.txt -u djangoadmin16
ansible-playbook H_gunicornngix.yaml -i inventry.txt -u djangoadmin16
