import os
import re

# Directory containing templates
templates_dir = r'c:\Users\user\Documents\Amira\transport\templates'

# Mapping of old URLs to Django template tags
url_mappings = {
    'index.html': "{% url 'index' %}",
    'dashboard.html': "{% url 'dashboard' %}",
    'tables.html': "{% url 'tables' %}",
    'shipments.html': "{% url 'shipments' %}",
    'tours.html': "{% url 'tours' %}",
    'billing.html': "{% url 'billing' %}",
    'incidents.html': "{% url 'incidents' %}",
    'complaints.html': "{% url 'complaints' %}",
    'analytics.html': "{% url 'analytics' %}"
}

def update_template_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace href="filename.html" with Django URL tags
    for old_url, new_url in url_mappings.items():
        # Handle href="filename.html"
        content = re.sub(f'href="{old_url}"', f'href="{new_url}"', content)
        # Handle href='filename.html'
        content = re.sub(f"href='{old_url}'", f"href='{new_url}'", content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated: {os.path.basename(file_path)}")

# Process all HTML files except index.html (already handled) and shipments.html (already handled)
for filename in os.listdir(templates_dir):
    if filename.endswith('.html') and filename not in ['index.html', 'shipments.html', 'dashboard.html']:
        file_path = os.path.join(templates_dir, filename)
        update_template_file(file_path)

print("All templates updated!")
