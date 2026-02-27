---
title: "Setup Guide"
---

This guide explains how to install and configure the Traverse plugin in QGIS.

---

## Requirements

Before installation, ensure:

- QGIS 3.x is installed
- Python 3.x is available
- PyQt5 is installed (bundled with QGIS)

---

## Step 1 – Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/sgraham3/traverse.git
```

Or download the repository as a ZIP file and extract it.

---

## Step 2 – Install as a QGIS Plugin

### Manual Installation

1. Locate your QGIS plugin directory.

**Windows**
```
C:\Users\<username>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\
```

**Linux**
```
~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/
```

**macOS**
```
~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/
```

2. Copy the entire `traverse` folder into the `plugins` directory.

3. Restart QGIS.

4. Open:

```
Plugins → Manage and Install Plugins
```

5. Enable **Traverse** from the installed plugins list.

---

## Step 3 – Compile Qt Resources (If Needed)

If icons do not display properly, compile the Qt resource file:

```bash
pyrcc5 resources.qrc -o resources.py
```

On Windows, you may use:

```bash
compile.bat
```

---

## Step 4 – Verify Installation

- Launch QGIS
- Enable the plugin
- Confirm the Traverse toolbar icon appears
- Open the dock panel

If errors occur, check the QGIS Python Console:

```
Plugins → Python Console
```

---

## Troubleshooting

**Plugin does not appear**
- Ensure it is placed inside the correct `plugins` directory.
- Restart QGIS after copying.

**Icons missing**
- Recompile `resources.qrc`.

**Errors during load**
- Review error messages in the Python Console.