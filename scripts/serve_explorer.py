#!/usr/bin/env python3
"""
Local HTTP server to launch the interactive Dialectic Corpus Explorer.
"""
import os
import sys
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8080

def run_server():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    os.chdir(base_dir)
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    url = f"http://localhost:{PORT}/explorer/"
    print(f"\n{'='*60}")
    print(f"  🌐 El-Mehasin-vel-Ezdad Dialectic Explorer Server")
    print(f"  Serving on: {url}")
    print(f"  Press Ctrl+C to stop.")
    print(f"{'='*60}\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)

if __name__ == "__main__":
    run_server()
