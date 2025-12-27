# Content Management Guide

This directory contains markdown files for managing your portfolio projects and experiences.

## Directory Structure

```
content/
├── projects/           # Project markdown files
├── experiences/        # Experience markdown files
├── README.md          # This file
└── templates/         # Templates for new content
```

## Quick Start

### Adding a New Project

1. Create a new `.md` file in `content/projects/`
2. Use the filename as the project slug (e.g., `my-awesome-project.md`)
3. Follow the template format (see `templates/project-template.md`)
4. Reload your Django server to see changes

### Adding a New Experience

1. Create a new `.md` file in `content/experiences/`
2. Use the filename as the experience slug (e.g., `software-engineer-company.md`)
3. Follow the template format (see `templates/experience-template.md`)
4. Reload your Django server to see changes

## Markdown Format

### Metadata (Optional)
Add metadata at the top of your file using the format:
```
Title: My Project Name
Date: 2024-01-15
Category: Web Development
```

### Tech Stack (Optional)
Add a JSON code block with your tech stack:

```json
{
  "primary_language": "Python",
  "technologies": [
    {
      "name": "Django",
      "icon": "fab fa-python",
      "color": "#092E20",
      "proficiency": 90
    },
    {
      "name": "PostgreSQL",
      "icon": "fas fa-database",
      "color": "#336791",
      "proficiency": 85
    }
  ]
}
```

### Content
Write your project/experience description in markdown:
- Use `##` for headings
- Use `-` or `*` for bullet points
- Use `**text**` for bold
- Use `[link](url)` for links
- Use `` `code` `` for inline code
- Use triple backticks for code blocks

## Helper Script

Use the helper script to quickly create new content:

```bash
# Create a new project
python manage.py create_content project "My Awesome Project"

# Create a new experience
python manage.py create_content experience "Senior Developer at XYZ"
```

## Tips

1. **File naming**: Use lowercase with hyphens (e.g., `web-scraper-tool.md`)
2. **Keep it organized**: One file per project/experience
3. **Use markdown**: It's rendered to HTML automatically
4. **Preview**: Changes appear immediately after server reload
5. **Version control**: Commit your markdown files to Git

## Icon Classes (Font Awesome)

Common icon classes for technologies:
- Python: `fab fa-python`
- JavaScript: `fab fa-js-square`
- React: `fab fa-react`
- Node.js: `fab fa-node-js`
- Database: `fas fa-database`
- Docker: `fab fa-docker`
- Git: `fab fa-git-alt`
- AWS: `fab fa-aws`
- Linux: `fab fa-linux`

## Color Codes

Common brand colors for technologies:
- Python: `#3776AB`
- JavaScript: `#F7DF1E`
- React: `#61DAFB`
- Node.js: `#339933`
- PostgreSQL: `#336791`
- MongoDB: `#47A248`
- Docker: `#2496ED`
- Git: `#F05032`
