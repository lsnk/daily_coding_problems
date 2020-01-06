def test_function(test_data, func):
    for args, result in test_data:
        assert func(*args) == result
