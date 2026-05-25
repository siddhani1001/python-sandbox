def to_upper_case(input_string: str) -> str:
    """Return the input string converted to upper-case."""
    if input_string is None:
        raise ValueError("input_string must not be None")
    return input_string.upper()

print(to_upper_case("hello world"))
