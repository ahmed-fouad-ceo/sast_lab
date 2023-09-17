import subprocess

def unsafe_function(data):
    # Use subprocess to execute a command safely
    result = subprocess.run(["echo", data], capture_output=True, text=True)
    return "Data processed: " + result.stdout

if __name__ == "__main__":
    user_input = input("Enter some data: ")
    result = unsafe_function(user_input)
    print(result)
