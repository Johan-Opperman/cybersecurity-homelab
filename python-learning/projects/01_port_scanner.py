#!/usr/bin/env python3
"""
Simple Port Scanner
Author: Oppie
Date: 2025-11-16
Purpose: Learn network programming by scanning open ports
"""

import socket
import sys
from datetime import datetime

def scan_port(target, port):
    """
    Scan a single port on target host
    Returns True if port is open, False otherwise
    """
    try:
        # Create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        # Attempt connection
        result = sock.connect_ex((target, port))
        sock.close()
        
        return result == 0  # 0 means port is open
    except:
        return False

def main():
    """Main function to run port scanner"""
    
    # Banner
    print("-" * 50)
    print("🔍 Simple Port Scanner")
    print("-" * 50)
    
    # Get target
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        target = input("Enter target IP/hostname: ")
    
    # Resolve hostname to IP
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"\n❌ Error: Could not resolve hostname {target}")
        sys.exit()
    
    print(f"\n🎯 Target: {target} ({target_ip})")
    print(f"⏰ Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    # Scan common ports
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389, 8080, 8443]
    open_ports = []
    
    try:
        for port in common_ports:
            if scan_port(target_ip, port):
                print(f"✅ Port {port:5d} - OPEN")
                open_ports.append(port)
            else:
                print(f"❌ Port {port:5d} - CLOSED")
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Scan interrupted by user")
        sys.exit()
    
    # Summary
    print("-" * 50)
    print(f"\n📊 Summary:")
    print(f"   Total ports scanned: {len(common_ports)}")
    print(f"   Open ports found: {len(open_ports)}")
    if open_ports:
        print(f"   Open ports: {', '.join(map(str, open_ports))}")
    print(f"\n⏰ Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

if __name__ == "__main__":
    main()