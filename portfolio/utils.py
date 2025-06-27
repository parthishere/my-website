import os
import json
import re
import markdown
from django.conf import settings

def load_markdown_content(content_type, filename):
    """
    Load and parse markdown content from the content directory
    
    Args:
        content_type (str): 'projects' or 'experiences'
        filename (str): filename without .md extension
    
    Returns:
        dict: Parsed markdown content with metadata
    """
    content_path = os.path.join(settings.BASE_DIR, 'content', content_type, f'{filename}.md')
    
    if not os.path.exists(content_path):
        return None
    
    with open(content_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Parse markdown with metadata extension
    md = markdown.Markdown(extensions=['meta', 'codehilite', 'tables'])
    html_content = md.convert(content)
    
    # Extract metadata if available
    metadata = getattr(md, 'Meta', {})
    
    # Extract tech stack from JSON blocks
    tech_stack = extract_tech_stack(content)
    
    return {
        'html_content': html_content,
        'metadata': metadata,
        'raw_content': content,
        'tech_stack': tech_stack
    }

def get_all_projects():
    """Get all project markdown files"""
    projects_dir = os.path.join(settings.BASE_DIR, 'content', 'projects')
    if not os.path.exists(projects_dir):
        return []
    
    projects = []
    for filename in os.listdir(projects_dir):
        if filename.endswith('.md'):
            project_name = filename[:-3]  # Remove .md extension
            content = load_markdown_content('projects', project_name)
            if content:
                projects.append({
                    'slug': project_name,
                    'name': project_name.replace('-', ' ').title(),
                    **content
                })
    
    return projects

def get_all_experiences():
    """Get all experience markdown files"""
    experiences_dir = os.path.join(settings.BASE_DIR, 'content', 'experiences')
    if not os.path.exists(experiences_dir):
        return []
    
    experiences = []
    for filename in os.listdir(experiences_dir):
        if filename.endswith('.md'):
            experience_name = filename[:-3]  # Remove .md extension
            content = load_markdown_content('experiences', experience_name)
            if content:
                experiences.append({
                    'slug': experience_name,
                    'name': experience_name.replace('-', ' ').title(),
                    **content
                })
    
    return experiences

def extract_tech_stack(content):
    """Extract tech stack JSON from markdown content"""
    # Look for JSON blocks in the content
    json_pattern = r'```json\s*\n(.*?)\n```'
    matches = re.findall(json_pattern, content, re.DOTALL)
    
    for match in matches:
        try:
            data = json.loads(match)
            if 'technologies' in data or 'primary_language' in data:
                return data
        except json.JSONDecodeError:
            continue
    
    return None