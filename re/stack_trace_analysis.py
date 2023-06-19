
import traceback

def analyze_stack_trace():
    try:
        raise Exception("Test exception for stack trace")
    except Exception as e:
        stack_trace = traceback.format_exc()
        print("Stack trace:")
        print(stack_trace)

if __name__ == "__main__":
    analyze_stack_trace()
