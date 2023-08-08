def prepary_filter(params):
    params_filter = {key: value for key, value in params if value is not None}

    return params_filter
