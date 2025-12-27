# Quick Reference Guide for Content Management

## Quick Commands

### Create New Content

```bash
# Activate virtual environment
source env/bin/activate

# Create a new project
python manage.py create_content project "My Awesome Project" --category="Web Development"

# Create a new experience
python manage.py create_content experience "Senior Developer" --company="Tech Corp" --location="San Francisco"

# List all content
python manage.py list_content

# List only projects
python manage.py list_content --type=projects

# List only experiences
python manage.py list_content --type=experiences
```

## File Locations

- **Projects**: `content/projects/your-project-name.md`
- **Experiences**: `content/experiences/your-experience-name.md`
- **Templates**: `content/templates/`

## Common Icons (Font Awesome)

### Programming Languages
```
Python:      fab fa-python       #3776AB
JavaScript:  fab fa-js-square    #F7DF1E
TypeScript:  fab fa-js-square    #3178C6
C++:         fas fa-code         #00599C
Java:        fab fa-java         #007396
Go:          fab fa-golang       #00ADD8
Rust:        fab fa-rust         #000000
```

### Frameworks & Libraries
```
Django:      fab fa-python       #092E20
React:       fab fa-react        #61DAFB
Node.js:     fab fa-node-js      #339933
Vue.js:      fab fa-vuejs        #4FC08D
Angular:     fab fa-angular      #DD0031
Laravel:     fab fa-laravel      #FF2D20
```

### Databases
```
PostgreSQL:  fas fa-database     #336791
MongoDB:     fas fa-database     #47A248
MySQL:       fas fa-database     #4479A1
Redis:       fas fa-database     #DC382D
```

### Tools & Platforms
```
Docker:      fab fa-docker       #2496ED
Git:         fab fa-git-alt      #F05032
AWS:         fab fa-aws          #FF9900
Linux:       fab fa-linux        #FCC624
GitHub:      fab fa-github       #181717
```

### Hardware & Embedded
```
Microchip:   fas fa-microchip    #E7352C
Circuit:     fas fa-circle-nodes #00599C
PCB:         fas fa-chess-board  #009688
```

## Workflow

1. **Create**: `python manage.py create_content project "Name"`
2. **Edit**: Open the `.md` file in your editor
3. **Preview**: Reload Django server (`python manage.py runserver`)
4. **Commit**: `git add content/ && git commit -m "Add new project"`

## Tips

- Use descriptive filenames (e.g., `iot-device-manager.md`)
- Keep project descriptions concise but informative
- Include quantifiable results when possible
- Update tech stack proficiency levels honestly
- Use proper markdown formatting for readability
- Add links to live demos and GitHub repos

## Markdown Formatting

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*

- Bullet point
1. Numbered list

[Link text](https://url.com)

`inline code`

\`\`\`python
# Code block
def hello():
    print("Hello")
\`\`\`
```

## Troubleshooting

**Q: Changes not appearing on website?**
- Restart Django server
- Clear browser cache
- Check file is in correct directory

**Q: JSON not parsing?**
- Validate JSON syntax at jsonlint.com
- Ensure proper escaping of quotes
- Check closing braces

**Q: Images not showing?**
- Ensure images are in `static/images/` directory
- Use correct path: `{% static 'images/filename.png' %}`
- Run `python manage.py collectstatic`
