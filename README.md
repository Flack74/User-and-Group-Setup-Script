# 🔐 Linux User & Group Setup Script

A Python script to automate the creation of users, manage group membership, and configure a shared directory on most Linux systems.

---

## 🚀 Features

- ✅ Creates a list of users if they don't already exist
- 👥 Ensures a system group (default: `science`) exists
- ➕ Adds users to the specified group (without overwriting other group memberships)
- 📁 Creates a shared directory (default: `/opt/science_dir`) with correct group ownership and permissions
- 🛡️ Uses `subprocess` for secure command execution and better error handling
- 🔁 Idempotent — safe to run multiple times

---

## 🛠️ Requirements

- Python 3.6+
- Root privileges (required to modify users, groups, and system directories)

---

## 📦 Compatible Linux Distributions

This script works on **most Linux distributions**, including:

- Debian-based (Ubuntu, Debian, Linux Mint)
- Red Hat-based (RHEL, CentOS, Fedora)
- Arch-based (Arch Linux, Manjaro)

---

## ⚙️ Configuration

You can modify these variables at the top of the script:

```python
userlist = ["alpha", "beta", "gamma"]       # List of usernames to create
groupname = "science"                       # Name of the group
