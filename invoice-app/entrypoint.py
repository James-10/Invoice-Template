import os
import subprocess

host = "0.0.0.0"
port = "8080"
module = "app.main:app"

def main():
    cmd = [
        "uvicorn",
        module,
        "--host",
        host,
        "--port",
        port,
        "--reload"
    ]
    print(cmd)
    subprocess.run(cmd)


if __name__ == "__main__":
    main()
