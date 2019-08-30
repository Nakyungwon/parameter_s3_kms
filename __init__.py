from aws_s3_kms_parameter import Parameters


def setup_default_session(**kwargs):
    object = Parameters(**kwargs)
    return object


def upload_s3(*args, **kwargs):
    """
    :param args:
    :param kwargs:
    :return:
    """
    return setup_default_session().upload_s3(*args, **kwargs)


def encrypt_text_with_kms(*args, **kwargs):
    """
    :param args:
    :param kwargs:
    :return:
    """
    return setup_default_session().encrypt_text_with_kms(*args, **kwargs)


def get_aws_config_from_bucket(*args, **kwargs):
    """
    :param args:
    :param kwargs:
    :return:
    """
    return setup_default_session().get_aws_config_from_bucket(*args, **kwargs)


def decrypt_text_with_kms(*args, **kwargs):
    """
    :param args:
    :param kwargs:
    :return:
    """
    return setup_default_session().decrypt_text_with_kms(*args, **kwargs)

