import os
import json

# Configuration
ENTRY_POINT = "app.py"
OUTPUT_FILE = "pocketwise_offline.html"
REQUIREMENTS = ["streamlit", "pandas", "altair"]

def get_files(base_dir):
    file_map = {}
    for root, dirs, files in os.walk(base_dir):
        # Skip hidden/build dirs
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('dist', 'build', '__pycache__', 'apk_build')]
        
        for file in files:
            if file.endswith('.py') or file.endswith('.json') or file.endswith('.md') or file.endswith('.glif'):
                path = os.path.join(root, file)
                rel_path = os.path.relpath(path, base_dir).replace("\\", "/")
                
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        file_map[rel_path] = content
                except Exception as e:
                    print(f"Skipping binary or unreadable file: {rel_path}")
    return file_map

def generate_html(files):
    files_json = json.dumps(files, indent=2, ensure_ascii=False)
    requirements_json = json.dumps(REQUIREMENTS)
    
    html = f"""<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>PocketWise Student</title>
    <script src="https://cdn.jsdelivr.net/npm/@stlite/mountable@0.52.0/build/stlite.js"></script>
    <style>
        body, html {{ margin: 0; padding: 0; height: 100%; }}
        #root {{ height: 100%; }}
    </style>
  </head>
  <body>
    <div id="root"></div>
    <script>
      stlite.mount(
        {{
          requirements: {requirements_json},
          entrypoint: "{ENTRY_POINT}",
          files: {files_json},
          args: ["--theme.base", "light"] 
        }},
        document.getElementById("root")
      );
    </script>
  </body>
</html>
"""
    return html

if __name__ == "__main__":
    print("Scanning files...")
    files = get_files(".")
    print(f"Found {len(files)} files.")
    
    html_content = generate_html(files)
    
    with open(OUTPUT_FILE, "w", encoding='utf-8') as f:
        f.write(html_content)
        
    print(f"Successfully created {OUTPUT_FILE}!")
    print("You can open this file in Chrome/Edge to test it.")
    print("To make it an APK, use a tool like 'Website 2 APK Builder' on this file.")
