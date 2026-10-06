## How to

1. `bundle install --path vendor/bundle` (may need to update ruby with `brew upgrade ruby`)
2. `bundle exec jekyll serve`

More at https://jekyllrb.com.

## Structure

- Home page: `index.html` → `_layouts/home.html` + `_includes/bento/*`, styled by `assets/css/site.css`.
- Resume content: `_data/resume.yml` (keep in sync with `resources/resume/VitorCesco-ENG.pdf`).
- `helvault/` pages still render through the `BDHU/minimalist` remote theme. Don't edit them as part of site redesigns.
