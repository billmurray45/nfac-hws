from main import hello

def test_hello():
    result = hello("Bauyrzhan")
    assert result == "Hello, Bauyrzhan!", f"Expected 'Hello, Bauyrzhan!', but got {result}"

    result = hello("Assel")
    assert result == "Hello, Assel!", f"Expected 'Hello, Assel!', but got {result}"

    result = hello("")
    assert result == "Hello, !", f"Expected 'Hello, !', but got {result}"

    result = hello(" Ruslan ")
    assert result == "Hello,  Ruslan !", f"Expected 'Hello,  Ruslan !', but got {result}"