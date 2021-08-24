import result

def resulted(f) -> result.Result:
    """ Decorator to convert return to results
    raise exception/asserts for invalid returns
    """
    def result_check(*args, **kwargs):
        try:
            resp = f(*args, **kwargs)
            return result.Ok(resp)
        except Exception as e:
            return result.Err(str(e))
        
    return result_check

def unwrap_result(res: result.Result, msg: str):
    return res.expect(f'{msg}: \n{res.value}')

# Example
if __name__ == '__main__':
    @resulted
    def to_int(x):
        return int(x)

    try:
        print(unwrap_result(to_int('a5'), 'invalid int'))
        print(unwrap_result(to_int('12'), 'invalid int'))
    except Exception as e:
        print(f'err: {e}')

