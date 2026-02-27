---
title: "Traverse"
permalink: /docs/traverse/
---


Traverse is a Python-based QGIS plugin for creating and managing survey traverses.

A traverse is a connected sequence of line segments defined by coordinates, bearings, and distances. Traverse helps surveyors and GIS professionals construct, edit, and manage these line sequences directly inside QGIS.

---

## Features

- Create connected traverse line sequences
- Interactive dockable panel interface
- Add, edit, and delete traverse points
- Automatically connect line segments
- Works inside QGIS editing workflows
- Built using Python and PyQt

---

## Repository Structure

```
traverse/
│
├── traverse.py
├── traverse_dockwidget.py
├── traverse_dockwidget_base.ui
├── resources.qrc
├── resources.py
├── metadata.txt
├── icon.png
├── compile.bat
├── icons/
├── import/
```

### File Overview

- **traverse.py** – Main plugin entry point
- **traverse_dockwidget.py** – Dockable UI logic
- **traverse_dockwidget_base.ui** – Qt Designer interface layout
- **resources.qrc / resources.py** – Qt resource system
- **metadata.txt** – QGIS plugin metadata
- **icons/** – UI icon assets

---

## Requirements

- QGIS 3.x
- Python 3.x
- PyQt5 (included with QGIS)

---

## Documentation

- [Setup Guide](setup/)
- [Usage Guide](usage/)

---

## License

Refer to the repository for licensing information.
