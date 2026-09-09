# LAU Start Code

A simple terminal-based project starter tool for quickly creating programming projects.

**LAU Start Code** allows you to create a new project directly from the terminal without manually creating folders and source files.

## Features

* Terminal-based project creation
* Simple interactive interface
* Multiple programming languages
* Built-in Web Development template
* Automatic project directory creation
* Automatic duplicate-name handling
* Projects are created inside `~/Projects`
* Can be executed from any directory after installation

## Supported Languages

Currently supported:

* Python
* TypeScript
* Java
* PHP
* JavaScript
* C
* C++
* C#
* Web Development

### Web Development

Selecting **Web Development** automatically creates:

```text
project-name/
├── index.html
├── style.css
└── script.js
```

No programming language selection is required for Web Development.

# Installation

LAU Start Code can be installed on **Windows** and **Linux**.

Choose the instructions for your operating system below.

---

## Windows

### Requirements

Before installing LAU Start Code, make sure you have:

* Windows 10 or later
* Python 3.9 or later
* Git

### 1. Install Python

Download and install Python from the official Python website.

During installation, make sure to enable:

```text
Add Python to PATH
```

After installation, open **PowerShell** or **Command Prompt** and check:

```powershell
python --version
```

If `python` is not recognized, try:

```powershell
py --version
```

### 2. Install Git

Install **Git for Windows**.

Check if Git is installed:

```powershell
git --version
```

### 3. Clone the Repository

Open **PowerShell** or **Command Prompt** and run:

```powershell
git clone https://github.com/ryuuyfynn/LAU-Start-Code---open-source.git
```

Then enter the repository:

```powershell
cd LAU-Start-Code---open-source
```

### 4. Install LAU Start Code

Install the package using pip:

```powershell
python -m pip install .
```

### 5. Run LAU Start Code

After installation, run:

```powershell
lau stcode
```

You can use `lau stcode` from any directory. You do not need to stay inside the cloned repository.

For example:

```powershell
cd Documents
lau stcode
```

---

## Linux

LAU Start Code can be installed on most Linux distributions with Python and pip.

### Arch Linux / Arch-based Distributions

#### 1. Install Requirements

Install Git, Python, and pip:

```bash
sudo pacman -S git python python-pip
```

Check Python:

```bash
python --version
```

Check pip:

```bash
python -m pip --version
```

#### 2. Clone the Repository

```bash
git clone https://github.com/ryuuyfynn/LAU-Start-Code---open-source.git
```

Enter the repository:

```bash
cd LAU-Start-Code---open-source
```

#### 3. Install LAU Start Code

```bash
python -m pip install .
```

#### 4. Run LAU Start Code

```bash
lau stcode
```

You can now use `lau stcode` from any directory.

---

### Debian / Ubuntu

#### 1. Install Requirements

Update the package list:

```bash
sudo apt update
```

Install Git, Python, and pip:

```bash
sudo apt install git python3 python3-pip
```

Check Python:

```bash
python3 --version
```

Check pip:

```bash
python3 -m pip --version
```

#### 2. Clone the Repository

```bash
git clone https://github.com/ryuuyfynn/LAU-Start-Code---open-source.git
```

Enter the repository:

```bash
cd LAU-Start-Code---open-source
```

#### 3. Install LAU Start Code

```bash
python3 -m pip install .
```

#### 4. Run LAU Start Code

```bash
lau stcode
```

You can now use `lau stcode` from any directory.

---

### Fedora

#### 1. Install Requirements

Install Git, Python, and pip:

```bash
sudo dnf install git python3 python3-pip
```

Check Python:

```bash
python3 --version
```

Check pip:

```bash
python3 -m pip --version
```

#### 2. Clone the Repository

```bash
git clone https://github.com/ryuuyfynn/LAU-Start-Code---open-source.git
```

Enter the repository:

```bash
cd LAU-Start-Code---open-source
```

#### 3. Install LAU Start Code

```bash
python3 -m pip install .
```

#### 4. Run LAU Start Code

```bash
lau stcode
```

You can now use `lau stcode` from any directory.

---

# Usage

After installation, simply run:

```bash
lau stcode
```

You do **not** need to run:

```bash
python main.py
```

You also do **not** need to be inside the LAU Start Code repository.

Projects created by LAU Start Code are stored in:

```text
~/Projects
```

## Example

Running:

```bash
lau stcode
```

can create a project like:

```text
~/Projects/
└── my-project/
    └── main.py
```

For Web Development:

```text
~/Projects/
└── my-website/
    ├── index.html
    ├── style.css
    └── script.js
```

# Duplicate Project Names

LAU Start Code automatically handles duplicate project names.

If:

```text
~/Projects/example/
```

already exists, creating another project named `example` will result in:

```text
~/Projects/example2/
```

If `example2` also exists:

```text
~/Projects/example3/
```

The number continues increasing until an available project name is found.

# Project Location

All projects created by LAU Start Code are stored inside:

```text
~/Projects
```

The `~` represents the user's home directory.

For example:

**Windows:**

```text
C:\Users\YourUsername\Projects
```

**Linux:**

```text
/home/YourUsername/Projects
```

# Command

The main command for LAU Start Code is:

```bash
lau stcode
```

This command can be executed from any directory after installation.

# License

This project is open source.
