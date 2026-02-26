#!/bin/bash

# GeoRidge Documentation Aggregator (Bash version)
# Pulls documentation from source repositories

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMP_DIR=".temp_docs"
TEMP_PATH="$SCRIPT_DIR/$TEMP_DIR"

# Project configurations (format: "key:repo:source_dir:target_dir:name")
declare -a PROJECTS=(
	"traverse:https://github.com/Geo-Ridge/geor_traverse.git:docs:_traverse_docs:GeoR Traverse"
	"mission_planner:https://github.com/Geo-Ridge/geor_mission_planner.git:docs:_mission_planner_docs:GeoR Mission Planner"
	"odm_frontend:https://github.com/Geo-Ridge/geor_odm_frontend.git:docs:_odm_docs:GeoR ODM Frontend"
	"qgis_plugins:https://github.com/Geo-Ridge/qgis-plugins.git:docs:_qgis_docs:QGIS Plugins"
)

echo ""
echo "============================================================"
echo "GeoRidge Documentation Aggregator"
echo "============================================================"

# Create temp directory
rm -rf "$TEMP_PATH" 2>/dev/null
mkdir -p "$TEMP_PATH"

success_count=0
total_count=${#PROJECTS[@]}

# Process each project
for project in "${PROJECTS[@]}"; do
	IFS=':' read -r key repo source target name <<<"$project"

	echo ""
	echo "📦 Processing: $name"
	echo "----------------------------------------------------"

	temp_repo="$TEMP_PATH/$key"
	target_docs="$SCRIPT_DIR/$target"

	# Clean old docs
	if [ -d "$target_docs" ]; then
		echo "Cleaning old documentation..."
		rm -rf "$target_docs"
	fi

	# Clone repository
	echo "Cloning $repo..."
	if ! git clone --depth 1 "$repo" "$temp_repo" 2>/dev/null; then
		echo "✗ Error cloning repository"
		continue
	fi

	# Copy documentation
	source_docs="$temp_repo/$source"
	if [ ! -d "$source_docs" ]; then
		echo "⚠️  Source directory not found: $source_docs"
		rm -rf "$temp_repo"
		continue
	fi

	mkdir -p "$target_docs"

	# Copy markdown files
	copy_count=0
	for md_file in "$source_docs"/*.md; do
		if [ -f "$md_file" ]; then
			cp "$md_file" "$target_docs/"
			echo "  ✓ Copied $(basename "$md_file")"
			((copy_count++))
		fi
	done

	# Copy subdirectories
	for item in "$source_docs"/*; do
		if [ -d "$item" ]; then
			item_name=$(basename "$item")
			if [[ "$item_name" != ".git" && "$item_name" != "__pycache__" ]]; then
				cp -r "$item" "$target_docs/"
				echo "  ✓ Copied directory $item_name/"
			fi
		fi
	done

	echo "✓ $name processed successfully!"
	((success_count++))

	# Clean up
	rm -rf "$temp_repo"
done

# Summary
echo ""
echo "============================================================"
echo "Summary"
echo "============================================================"
echo "Completed: $success_count/$total_count projects"

# Clean up temp directory
rm -rf "$TEMP_PATH"

exit $([[ $success_count -eq $total_count ]] && echo 0 || echo 1)
