# GeoRidge Website

Welcome to the official website repository for **GeoRidge** - a leading geospatial technology company specializing in innovative mapping solutions, geographic data analysis, and spatial intelligence tools.

## About This Site

This is a Jekyll-based website built with the [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes) theme, deployed via GitHub Pages at [https://geo-ridge.github.io/GeoR-Website/](https://geo-ridge.github.io/GeoR-Website/).

## Site Structure

- **`index.html`** - Splash page with company overview and feature highlights
- **`_pages/about.md`** - About GeoRidge, our mission, and services
- **`_pages/projects.md`** - Featured projects and solutions
- **`_config.yml`** - Site configuration and metadata
- **`assets/images/`** - Images and visual assets

## Getting Started

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/Geo-Ridge/GeoR-Website.git
cd GeoR-Website
```

2. Install dependencies:
```bash
bundle install
```

3. Serve locally (splash page at root):

**Option A - Using the provided script:**
- **Windows**: Run `serve-local.bat`
- **macOS/Linux**: Run `bash serve-local.sh`

**Option B - Manual command:**
```bash
bundle exec jekyll serve --config _config.yml,_config_local.yml
```

The site will be available at `http://127.0.0.1:4000/`

**Note:** The `_config_local.yml` file overrides the `baseurl` setting for local development, allowing you to access the site at the root URL instead of `/GeoR-Website/`.

### Making Changes

- Update content in `_pages/` for existing pages
- Create new blog posts in `_posts/` with the format: `YYYY-MM-DD-title.md`
- Update site-wide configuration in `_config.yml`
- Add images to `assets/images/`

## Deploying

Changes pushed to the `main` or `master` branch will automatically deploy via GitHub Pages.

## Customization

To customize the site further:
1. Refer to the [Minimal Mistakes documentation](https://mmistakes.github.io/minimal-mistakes/docs/configuration/)
2. Update `_config.yml` with your preferences
3. Add custom CSS to `assets/css/`
4. Add custom JavaScript to `assets/js/`

## Contact

For questions about the website or GeoRidge:
- **Email**: contact@geo-ridge.com
- **GitHub**: [Geo-Ridge](https://github.com/Geo-Ridge/)

---

**Built with** [Jekyll](https://jekyllrb.com/) and [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes)
