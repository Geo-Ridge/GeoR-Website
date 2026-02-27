---
title: "Usage Guide"
---

This guide explains how to use the Traverse plugin inside QGIS.

---

## Launching the Plugin

1. Open QGIS.
2. Click the **Traverse** icon in the toolbar.
3. The Traverse dock panel will open.

---

## Creating a New Traverse

1. Click **New Traverse**.
2. Select or create a line layer.
3. Ensure the layer is in edit mode.
4. Begin entering traverse points.

---

## Adding Traverse Points

You can add points by:

- Clicking directly on the map canvas
- Entering coordinate values manually
- Entering bearing and distance (if supported)

Each new point automatically connects to the previous point, forming a continuous line.

---

## Editing Points

- Select a vertex to move it.
- Delete selected points using the delete option.
- Modify coordinates in the panel.
- Changes update the traverse geometry immediately.

---

## Saving Your Work

Traverse geometries are stored in the active line layer.

To save permanently:

1. Toggle editing off.
2. Click **Save** when prompted.

---

## Exporting the Traverse

To export your traverse:

1. Right-click the layer.
2. Select:

```
Export → Save Features As
```

3. Choose format:
   - Shapefile (.shp)
   - GeoPackage (.gpkg)
   - GeoJSON (.geojson)
   - CSV (if attribute-based)

---

## Best Practices

- Confirm your project CRS before starting.
- Use snapping for accurate point placement.
- Save edits frequently.
- Work in projected coordinate systems for accurate distance calculations.

---

## Common Issues

**Nothing happens when clicking**
- Ensure the layer is in edit mode.

**Geometry not saving**
- Confirm editing is enabled.

**Plugin not visible**
- Enable it in Plugin Manager.