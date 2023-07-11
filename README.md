# AutomationPlatform_Credential_Export

## Usage 
(Example)
clone this repo to one of your automation platform controllers 
```
cd AutomationPlatform_Credential_Export
ansible-playbook simple.yml \
 -e 'aap_hostname=192.168.56.50' -e 'aap_username=admin' -e 'aap_password=redhat' \
 -e 'target_aap_host=192.168.56.50' -e 'target_aap_user=admin' -e 'target_aap_pass=redhat' \
 -e 'controller_configuration_secure_logging=False' -e 'controller_configuration_credentials_secure_logging=False' \
 -e 'controller_validate_certs=False' -e 'controller_configuration_async_retries=6000' \
 -e 'controller_configuration_async_delay=3' -e 'controller_configuration_credentials_async_delay=3' -vv
```
