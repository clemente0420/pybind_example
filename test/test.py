import py_example  # Assuming you named your Pybind11 module 'py_example'

# Test the add function
result = py_example.add(3, 4)
print(f"Result of add function: {result}")

# Test the Hello class
hello_instance = py_example.Hello()
hello_instance.say("Hello from Python!")

# Test the World class
world_instance = py_example.World()
world_instance.say("World from Python!")

# Test the Test class
test_instance = py_example.Test(10, 20)
test_instance.print()
