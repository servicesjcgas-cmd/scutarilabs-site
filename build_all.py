# Master Site Generator for ScutariLabs (Apple 2030 Design System)
import os
import subprocess

def main():
    print("ScutariLabs master build script executing...")
    subprocess.run(["python", "build.py"], check=True)
    print("All blog publications built successfully.")

if __name__ == "__main__":
    main()
