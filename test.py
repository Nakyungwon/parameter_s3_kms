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
encrypted_config = awsparameter.encrypt_text_with_kms(config, 'mycelebs-config')
awsparameter.upload_s3('mycelebs-config', 'mycelebs-config', 'sosos_ss', encrypted_config)