from awx.main.utils import decrypt_field
import os
cred = Credential.objects.get(pk=os.environ['CRED_ID'])
for key in cred.inputs:
  if cred.inputs[key].startswith('$encrypted$'):
    print ("{}: {}".format(key, decrypt_field(cred, key)))
