def create_unique_params_list(params: str, params_to_strip: list) -> list:
    # Check if the params_to_strip list is empty
    # Check if the params list is empty

    # TODO: complete this function that takes in a string, converts to list, removes duplicates, and returns a list
    # TODO: make sure the list is unique and refers to the params_to_strip list
    # NOTE: the params_to_strip list is a list of characters that should be checked for
    pass
    
def strip_url_params(url: str, params_to_strip: list) -> str:
    url_strip, params = url.split("?")[0], url.split("?")[1]
    params_lst = create_unique_params_list(params, params_to_strip)


if __name__ == '__main__':
    url = "www.codewars.com/kata?a=1&b=2&a=2"
    print(strip_url_params(url, params_to_strip=["a", "b"]))