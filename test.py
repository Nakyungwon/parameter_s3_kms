import awsparameter

ssm_key = 'ssgdfm_aws_config'
key_bucket = 'encrypt-keys-test'
config=awsparameter.decrypt_text_with_kms(key_bucket, ssm_key)
print(config)

key = 'mycelebs-config'
config = {
    'asdf':{
        'sdfsdf':'sdfsdfdsfsf'
    }
}
awsparameter.encrypt_text_with_kms(config, key)