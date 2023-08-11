import chardet


def decode_values(input_value):
    """Specifies the encoding"""
    encoding = chardet.detect(input_value)['encoding']
    try:
        output_value = input_value.decode(encoding)
        return output_value
    except (UnicodeDecodeError, TypeError):
        return ""
