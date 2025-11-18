# 🔐 Cybersecurity Homelab

> **My journey from beginner to cybersecurity professional through hands-on practice**

[![Homelab](https://img.shields.io/badge/Homelab-24%20Services-blue)](http://192.168.110.21:3000)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker)](https://www.docker.com/)
[![Linux](https://img.shields.io/badge/Platform-Linux%20ARM64-orange)](https://www.linux.org/)

---

## 📋 Table of Contents

- [About](#about)
- [Architecture](#architecture)
- [Services](#services)
- [Learning Path](#learning-path)
- [Challenges Completed](#challenges-completed)
- [Tools & Technologies](#tools--technologies)
- [Setup Guide](#setup-guide)
- [Documentation](#documentation)

---

## 🎯 About

This is my personal cybersecurity learning environment built using Docker containers. I'm documenting my journey from complete beginner to understanding web application security, penetration testing, and defensive security practices.

**Start Date:** November 16, 2025  
**Current Focus:** Web Application Security (OWASP Top 10)

---

## 🏗️ Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                    HOMELAB INFRASTRUCTURE                    │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────────┐  ┌──────────────────┐                │
│  │  Vulnerable Apps  │  │  Security Tools  │                │
│  ├──────────────────┤  ├──────────────────┤                │
│  │ • DVWA           │  │ • Kali Linux     │                │
│  │ • WebGoat        │  │ • CyberChef      │                │
│  │ • Juice Shop     │  │ • Trivy Scanner  │                │
│  │ • VAmPI API      │  │ • ModSecurity    │                │
│  └──────────────────┘  └──────────────────┘                │
│                                                               │
│  ┌──────────────────┐  ┌──────────────────┐                │
│  │   Development    │  │   Monitoring     │                │
│  ├──────────────────┤  ├──────────────────┤                │
│  │ • VS Code        │  │ • Portainer      │                │
│  │ • Jupyter Lab    │  │ • Grafana        │                │
│  │ • Gitea          │  │ • Netdata        │                │
│  │ • Trilium Notes  │  │ • Uptime Kuma    │                │
│  └──────────────────┘  └──────────────────┘                │
│                                                               │
│  ┌─────────────────────────────────────────┐                │
│  │           Infrastructure                 │                │
│  ├─────────────────────────────────────────┤                │
│  │ MySQL • PostgreSQL • MongoDB            │                │
│  │ Nginx Proxy Manager • WireGuard VPN     │                │
│  │ Pi-hole DNS • Homepage Dashboard        │                │
│  └─────────────────────────────────────────┘                │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Services

### Vulnerable Applications (Practice Targets)
| Service | Port | Purpose | Status |
|---------|------|---------|--------|
| **DVWA** | 8080 | SQL Injection, XSS, CSRF | ✅ Running |
| **WebGoat** | 8081 | OWASP lessons & challenges | ✅ Running |
| **Juice Shop** | 3001 | Modern web vulnerabilities | ✅ Running |
| **VAmPI** | 8083 | API security testing | ✅ Running |

### Security Tools
| Service | Port | Purpose | Status |
|---------|------|---------|--------|
| **Kali Linux** | - | Penetration testing toolkit | ✅ Running |
| **CyberChef** | 8089 | Data encoding/decoding | ✅ Running |
| **Trivy** | 8088 | Container vulnerability scanner | ✅ Running |
| **ModSecurity** | 8095 | Web Application Firewall | ✅ Running |

### Development Environment
| Service | Port | Purpose | Status |
|---------|------|---------|--------|
| **VS Code** | 8443 | Browser-based IDE | ✅ Running |
| **Jupyter Lab** | 8888 | Python notebooks | ✅ Running |
| **Gitea** | 3004 | Private Git server | ✅ Running |
| **Trilium** | 8085 | Documentation & notes | ✅ Running |

---

## 📚 Learning Path

### Phase 1: Foundations (Current)
- [x] Set up homelab infrastructure
- [x] Deploy vulnerable applications
- [x] Configure monitoring tools
- [ ] Complete OWASP Top 10 basics
- [ ] Document 10 vulnerabilities

### Phase 2: Web Application Security
- [ ] SQL Injection (all types)
- [ ] Cross-Site Scripting (XSS)
- [ ] Authentication vulnerabilities
- [ ] Session management flaws
- [ ] API security testing

### Phase 3: Advanced Topics
- [ ] Exploit development
- [ ] Binary exploitation
- [ ] Network penetration testing
- [ ] Wireless security
- [ ] Red team operations

---

## 🏆 Challenges Completed

### Juice Shop
- [x] **Score Board Discovery** - Found hidden score board page
- [ ] DOM XSS
- [ ] SQL Injection
- [ ] Broken Authentication

### DVWA
- [ ] SQL Injection (Low)
- [ ] XSS Reflected
- [ ] Command Injection
- [ ] File Upload

### WebGoat
- [ ] General: HTTP Basics
- [ ] Injection Flaws
- [ ] Authentication Flaws

**Total Challenges Solved:** 1/100+

---

## 🛠️ Tools & Technologies

**Containerization:**
- Docker & Docker Compose
- 24 containers running simultaneously

**Operating Systems:**
- Linux (ARM64 architecture)
- Kali Linux (pentesting)

**Languages & Frameworks:**
- Python (scripting & analysis)
- Bash (automation)
- SQL (database exploitation)
- JavaScript (web analysis)

**Security Tools:**
- Metasploit Framework
- Burp Suite
- OWASP ZAP
- Nmap
- Wireshark

---

## 📖 Setup Guide

### Prerequisites
```bash
# Docker & Docker Compose
# Linux system (ARM64 compatible)
# 4GB+ RAM recommended
# 50GB+ storage
```

### Quick Start
```bash
# Clone repository
git clone https://github.com/oppie/cybersecurity-homelab
cd cybersecurity-homelab

# Start all services
docker compose up -d

# Access homepage
http://192.168.110.21:3000
```

### Service Access
- **Homepage Dashboard:** http://192.168.110.21:3000
- **Portainer:** https://192.168.110.21:9443
- **Trilium Notes:** http://192.168.110.21:8085

---

## 📝 Documentation

All my learning notes, vulnerability findings, and progress updates are documented in:
- **Trilium Notes** (http://192.168.110.21:8085)
- **[LEARNING_LOG.md](LEARNING_LOG.md)** (weekly updates)
- **LinkedIn** (public milestones)

---

## 🎓 Resources

**Learning Platforms:**
- [OWASP WebGoat](https://owasp.org/www-project-webgoat/)
- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)
- [HackTheBox](https://www.hackthebox.com/)
- [TryHackMe](https://tryhackme.com/)

**Documentation:**
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)

---

## 📫 Connect With Me

- **LinkedIn:** [Your LinkedIn Profile]
- **GitHub:** [Your GitHub Profile]
- **Blog:** [Optional]

---

## 📊 Stats
```
Services Running:    24/24
Uptime:              99.9%
Challenges Solved:   1
Days Learning:       3
CVEs Discovered:     0 (yet!)
```

---

## 📜 License

This project is for educational purposes only. Use responsibly and ethically.

---

**Last Updated:** November 16, 2025