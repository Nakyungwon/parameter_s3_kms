## awsparameter
~~~python
import awsparameter
import boto3

# encrypt
config_dict = {
    'config_key name' : {
        'key1': 'value1',
        'key2': 'value2'
    }
}
ssm_key_alias = 'kms_key_alias'
kms_client = boto3.client('kms')
awsparameter.encrypt(config_dict, ssm_key_alias, kms_client)

# upload
key_bucket = 'bucket_name'
ssm_key_alias = 'kms_key_alias'
key_name = 'key_name'
encoded_ciphertext = awsparameter.encrypt(config_dict, ssm_key_alias, kms_client) 
s3_client = boto3.client('boto3')
awsparameter.upload(key_bucket, ssm_key_alias, key_name, encoded_ciphertext, s3_client)

# download and decrypt
key_bucket = 'bucket_name'
saved_bucket_key = 'key_name'
kms_client = boto3.client('kms')
k3_client = boto3.client('s3_client')
awsparameter.decrypt(key_bucket, saved_bucket_key, kms_client, s3_client)
~~~