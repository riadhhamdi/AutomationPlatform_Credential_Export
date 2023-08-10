from awx.main.utils import decrypt_field
import os

cred = Credential.objects.get(pk=os.environ['CRED_ID'])
for key in cred.inputs:
    if cred.inputs[key].startswith('$encrypted$'):
        decrypted_value = decrypt_field(cred, key)
        if "\n" in decrypted_value:
            # Format multi-line strings for valid YAML output
            decrypted_value = "|\n" + "\n".join(["  " + line for line in decrypted_value.splitlines()])
        print("{}: {}".format(key, decrypted_value))
