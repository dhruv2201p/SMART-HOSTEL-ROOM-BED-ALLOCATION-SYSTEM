"""
Backward compatibility forwarder to frontend.py
"""
import runpy

if __name__ == "__main__":
    runpy.run_path("frontend.py", run_name="__main__")
