



class ApiParamException(Exception):
    """
    参数验证异常类
    """
    message = None

    def __init__(self, message, *args, **kwargs):
        self.message = message

    def __str__(self):
        return self.message
