import testing_library as test_lib
message = "000"
add = [-143, 2324, 676]
def test_echo():
    ser = test_lib.open_conection('/dev/ttyUSB1')
    try:
        # test_lib.echo(ser, message)
        # test_lib.echo(ser, "Hello!")
        print(hex(sum(add)))
        test_lib.add(ser, add)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        test_lib.close_conection(ser)

if __name__ == "__main__":
    test_echo()
