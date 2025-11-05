#!/usr/bin/env python3
import http.server
import socketserver
import os
import time

os.chdir('/Users/lsiegle/Desktop/agents/nba-gradient-agent')

# Kill any existing process on port 8080
os.system("lsof -ti:8080 | xargs kill -9 >/dev/null 2>&1")
time.sleep(1)

try:
    with socketserver.TCPServer(("", 8080), http.server.SimpleHTTPRequestHandler) as httpd:
        httpd.allow_reuse_address = True
        print("🏀 http://localhost:8080")
        httpd.serve_forever()
except OSError:
    print("❌ Port 8080 in use, trying 8081...")
    with socketserver.TCPServer(("", 8081), http.server.SimpleHTTPRequestHandler) as httpd:
        httpd.allow_reuse_address = True
        print("🏀 http://localhost:8081")
        httpd.serve_forever()