#!/usr/bin/env python3
"""
My First Python Script
Date: 2025-11-16
Purpose: Hello World and basic Python concepts
"""

def main():
    # Basic print statement
    print("🐍 Hello from Oppie's Cybersecurity Lab!")
    
    # Variables
    name = "Oppie"
    lab_services = 24
    
    print(f"\nLearner: {name}")
    print(f"Homelab Services: {lab_services}")
    
    # Simple calculation
    challenges_completed = 1
    total_challenges = 100
    progress = (challenges_completed / total_challenges) * 100
    
    print(f"\nProgress: {progress:.1f}% complete")
    print("🎯 Goal: Master cybersecurity fundamentals!\n")

if __name__ == "__main__":
    main()