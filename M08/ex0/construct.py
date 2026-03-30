import sys
import os
import site


def main() -> None:
    try:
        base_prefix = (
                getattr(sys, "base_prefix", None) or
                getattr(sys, "real_prefix", None) or 
                sys.prefix
        )
        running = sys.prefix != base_prefix
        version = sys.executable

        if running:
            print("MATRIX STATUS: Welcome to the construct\n")
            print(f"Current Python: {version}")
            print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
            print(f"Environment Path: {sys.prefix}\n")
            print("SUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting")
            print("the global system.\n")
            print(f"Package installation path: {site.getsitepackages()[0]}")
        else:
            print("MATRIX STATUS: You're still plugged in\n")
            print(f"Current Python: {version}")
            print("Virtual Environment: None detected")
            print("WARNING: You're in the global environment")
            print("The machines can see everything you install.\n")
            print("To enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate # on Unix")
            print("matrix_env")
            print("Scripts")
            print("activate $ On Windows\n")
            print("Then run this program again.")
    
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
