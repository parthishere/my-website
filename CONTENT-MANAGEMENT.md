# Content Management System for Portfolio

Your portfolio now supports **markdown-based content management** for projects and experiences!

## 🎯 Quick Start

### 1. Add a New Project

```bash
source env/bin/activate
python manage.py create_content project "My Awesome Project" --category="Web Development"
```

This creates a markdown file at `content/projects/my-awesome-project.md`

### 2. Edit the Project

Open `content/projects/my-awesome-project.md` in your favorite editor and fill in:
- Project description
- Technologies used (with icons and colors)
- Links to GitHub/demo
- Key achievements

### 3. View Your Changes

Restart the Django server and your project will appear on the website automatically!

## 📝 Management Commands

### Create Content
```bash
# Create a project
python manage.py create_content project "Project Name" --category="Category"

# Create an experience
python manage.py create_content experience "Job Title" --company="Company" --location="City"
```

### List Content
```bash
# List all content
python manage.py list_content

# List only projects
python manage.py list_content --type=projects

# List only experiences
python manage.py list_content --type=experiences
```

## 📁 Directory Structure

```
content/
├── projects/           # Your project markdown files
│   ├── iot-ecosystem.md
│   └── web-app.md
├── experiences/        # Your experience markdown files
│   ├── senior-dev.md
│   └── intern.md
├── templates/          # Templates for new content
│   ├── project-template.md
│   └── experience-template.md
├── README.md           # Full documentation
└── QUICK-REFERENCE.md  # Quick reference guide
```

## ✨ Features

### Automatic Title Extraction
- Uses the `Title:` metadata from your markdown file
- Falls back to filename if no title specified

### Smart Sorting
- Projects: Featured projects appear first, then sorted by date
- Experiences: Automatically sorted by date (newest first)
- Mark projects as featured with `Featured: true` in metadata

### Tech Stack with Icons
Add a JSON block in your markdown:

```json
{
  "primary_language": "Python",
  "technologies": [
    {
      "name": "Django",
      "icon": "fab fa-python",
      "color": "#092E20",
      "proficiency": 90
    }
  ]
}
```

### Markdown Support
- Full markdown rendering
- Code syntax highlighting
- Tables
- Lists and formatting

## 📚 Documentation

- **Full Guide**: `content/README.md`
- **Quick Reference**: `content/QUICK-REFERENCE.md`
- **Templates**: `content/templates/`

## 🔧 Workflow

1. **Create**: `python manage.py create_content project "Name"`
2. **Edit**: Open the `.md` file and customize
3. **Preview**: Reload Django server
4. **Commit**: `git add content/ && git commit -m "Add project"`

## 💡 Tips

- Use descriptive filenames (e.g., `iot-device-manager.md`)
- Include quantifiable results (e.g., "Improved performance by 50%")
- Add links to GitHub repos and live demos
- Update proficiency levels honestly
- Mark your best projects as `Featured: true`

## 🎨 Common Technology Icons

```
Python:    fab fa-python       #3776AB
React:     fab fa-react        #61DAFB
Node.js:   fab fa-node-js      #339933
Docker:    fab fa-docker       #2496ED
AWS:       fab fa-aws          #FF9900
```

See `content/QUICK-REFERENCE.md` for complete list!

## 🚀 Benefits

- ✅ **No Database Changes**: Just edit markdown files
- ✅ **Version Control**: Track changes with Git
- ✅ **Easy Editing**: Use any text editor
- ✅ **Fast Updates**: No admin panel needed
- ✅ **Portable**: Move your content anywhere

## 📖 Example

Check out the example files:
- `content/projects/example-iot-project.md`
- `content/experiences/example-developer-role.md`

---

**Need help?** Check `content/README.md` for detailed documentation!
