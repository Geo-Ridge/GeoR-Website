#!/usr/bin/env python3
"""
GeoRidge Documentation Aggregator
Pulls documentation from source repositories and organizes them in the website.
"""

import os
import shutil
import subprocess
from pathlib import Path
from typing import Dict, List

# Configuration for projects
PROJECTS = {
    "traverse": {
        "repo": "https://github.com/Geo-Ridge/geor_traverse.git",
        "source_dir": "docs",
        "target_dir": "_traverse_docs",
        "name": "GeoR Traverse",
    },
    "mission_planner": {
        "repo": "https://github.com/Geo-Ridge/geor_mission_planner.git",
        "source_dir": "docs",
        "target_dir": "_mission_planner_docs",
        "name": "GeoR Mission Planner",
    },
    "odm_frontend": {
        "repo": "https://github.com/Geo-Ridge/geor_odm_frontend.git",
        "source_dir": "docs",
        "target_dir": "_odm_docs",
        "name": "GeoR ODM Frontend",
    },
    "qgis_plugins": {
        "repo": "https://github.com/Geo-Ridge/qgis-plugins.git",
        "source_dir": "docs",
        "target_dir": "_qgis_docs",
        "name": "QGIS Plugins",
    },
}

TEMP_DIR = ".temp_docs"
WEBSITE_ROOT = Path(__file__).parent


def clone_repo(repo_url: str, temp_path: Path) -> bool:
    """Clone a repository to a temporary directory."""
    try:
        print(f"Cloning {repo_url}...")
        subprocess.run(
            ["git", "clone", "--depth", "1", repo_url, str(temp_path)],
            check=True,
            capture_output=True,
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error cloning {repo_url}: {e.stderr.decode()}")
        return False


def copy_docs(source: Path, target: Path) -> int:
    """Copy documentation files from source to target."""
    if not source.exists():
        print(f"  [WARNING] Source directory not found: {source}")
        return 0

    # Create target directory
    target.mkdir(parents=True, exist_ok=True)

    # Copy all markdown files
    count = 0
    for md_file in source.glob("*.md"):
        try:
            shutil.copy2(md_file, target / md_file.name)
            count += 1
            print(f"  [OK] Copied {md_file.name}")
        except Exception as e:
            print(f"  [ERROR] Error copying {md_file.name}: {e}")

    # Copy subdirectories (images, assets, etc.)
    for item in source.iterdir():
        if item.is_dir() and item.name not in [".git", "__pycache__"]:
            try:
                target_subdir = target / item.name
                if target_subdir.exists():
                    shutil.rmtree(target_subdir)
                shutil.copytree(item, target_subdir)
                print(f"  [OK] Copied directory {item.name}/")
            except Exception as e:
                print(f"  [ERROR] Error copying directory {item.name}: {e}")

    return count


def add_frontmatter(file_path: Path, title: str, project_name: str):
    """Add Jekyll frontmatter to markdown files if missing."""
    try:
        content = file_path.read_text()

        # Check if frontmatter already exists
        if content.startswith("---"):
            return

        # Create frontmatter
        frontmatter = f"""---
title: "{title}"
excerpt: "Documentation for {project_name}"
---

"""
        # Write back with frontmatter
        file_path.write_text(frontmatter + content)
        print(f"  [OK] Added frontmatter to {file_path.name}")
    except Exception as e:
        print(f"  [ERROR] Error adding frontmatter to {file_path.name}: {e}")


def process_project(project_key: str, project_config: Dict) -> bool:
    """Process a single project."""
    print(f"\n[PROJECT] Processing: {project_config['name']}")
    print("-" * 50)

    temp_repo = WEBSITE_ROOT / TEMP_DIR / project_key
    target_docs = WEBSITE_ROOT / project_config["target_dir"]

    # Clean up old docs
    if target_docs.exists():
        print(f"Cleaning old documentation...")
        shutil.rmtree(target_docs)

    # Clone repository
    if not clone_repo(project_config["repo"], temp_repo):
        return False

    # Copy documentation
    source_docs = temp_repo / project_config["source_dir"]
    count = copy_docs(source_docs, target_docs)

    # Add frontmatter to all markdown files
    print(f"Processing {count} documentation files...")
    for md_file in target_docs.glob("*.md"):
        title = md_file.stem.replace("-", " ").title()
        add_frontmatter(md_file, title, project_config["name"])

    # Clean up temp directory
    try:
        shutil.rmtree(temp_repo)
    except Exception as e:
        print(f"Warning: Could not clean up temp directory: {e}")

    print(f"[OK] {project_config['name']} processed successfully!")
    return True


def main():
    """Main function to orchestrate documentation pulling."""
    print("\n" + "=" * 60)
    print("GeoRidge Documentation Aggregator")
    print("=" * 60)

    # Create temp directory
    temp_path = WEBSITE_ROOT / TEMP_DIR
    if temp_path.exists():
        shutil.rmtree(temp_path)
    temp_path.mkdir()

    # Process each project
    results = {}
    for project_key, project_config in PROJECTS.items():
        results[project_key] = process_project(project_key, project_config)

    # Summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)

    successful = sum(1 for v in results.values() if v)
    total = len(results)

    for project_key, project_config in PROJECTS.items():
        status = "[OK]" if results[project_key] else "[FAILED]"
        print(f"{status}: {project_config['name']}")

    print(f"\nCompleted: {successful}/{total} projects")

    # Clean up temp directory
    try:
        shutil.rmtree(temp_path)
    except Exception as e:
        print(f"Warning: Could not clean up temp directory: {e}")

    return all(results.values())


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
