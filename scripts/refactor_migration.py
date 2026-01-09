import os
import re
import shutil
import glob

# Configuration
SOURCE_DIR = os.path.abspath("d:/cp-algorithms/src")
ASSETS_DIR = os.path.join(SOURCE_DIR, "assets", "images")
MD_EXTENSIONS = {".md"}
IMG_EXTENSIONS = {".png", ".jpg", ".jpeg", ".svg", ".gif"}

def to_kebab_case(name):
    """Converts a filename to kebab-case."""
    # Remove extension first
    base, ext = os.path.splitext(name)
    # Replace special chars and underscores with hyphens
    s = re.sub(r'[_\s]+', '-', base)
    # Insert hyphen between camelCase (e.g., SegmentTree -> Segment-Tree)
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', s)
    # Lowercase everything
    s = s.lower()
    # Remove repetitive hyphens
    s = re.sub(r'-+', '-', s)
    # Remove leading/trailing hyphens
    s = s.strip('-')
    return s + ext

def scan_files(root_dir):
    """Scans all files and builds a map of old_abs_path -> new_abs_path."""
    file_map = {}
    
    # First, handle Images (they move to ASSETS_DIR)
    if not os.path.exists(ASSETS_DIR):
        os.makedirs(ASSETS_DIR)

    # Walk for all files
    for root, dirs, files in os.walk(root_dir):
        # Skip .git and assets dir itself if we are walking recursively
        if ".git" in root or "assets" in root:
            continue
            
        for file in files:
            old_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()
            
            if ext in IMG_EXTENSIONS:
                # Images go to assets/images, keeping their name (but maybe sanitized?)
                # Let's sanitize image names too for consistency
                new_name = to_kebab_case(file)
                new_path = os.path.join(ASSETS_DIR, new_name)
                # Handle potential duplicate names by appending a counter if needed (simple check)
                if new_path in file_map.values(): 
                    base, ext = os.path.splitext(new_name)
                    counter = 1
                    while new_path in file_map.values() or os.path.exists(new_path):
                        new_path = os.path.join(ASSETS_DIR, f"{base}-{counter}{ext}")
                        counter += 1
                
                file_map[old_path] = new_path

            elif ext in MD_EXTENSIONS:
                # Markdown files get renamed in place (kebab-case)
                new_name = to_kebab_case(file)
                new_path = os.path.join(root, new_name)
                file_map[old_path] = new_path
            
            else:
                # Other files (like js/css) - let's verify if we need to rename them
                # For now, let's just stick to renaming what we know
                pass
                
    return file_map

def update_content(content, file_path, file_map):
    """Updates links, image paths, and code blocks in the content."""
    
    current_dir = os.path.dirname(file_path)
    # We need the NEW path of the current file to calculate relative links correctly?
    # Actually, standard links are relative. 
    # If we rename content BEFORE moving file, relative paths are relative to OLD location.
    # If we rename content AFTER moving file, relative paths are relative to NEW location.
    # Let's assume we are updating content BEFORE renaming the file definition on disk,
    # BUT we want the links to point to the NEW locations.
    
    # 1. Update Code Blocks: `{.cpp file=foo}` -> ```cpp title="foo"
    def code_repl(match):
        lang = match.group(2) or ""
        # if lang starts with ., remove it
        if lang.startswith('.'): lang = lang[1:]
        
        props = match.group(3)
        # extract file=...
        m_file = re.search(r'file=([^\s\}]+)', props)
        title_attr = ""
        if m_file:
            title_attr = f' title="{m_file.group(1)}"'
        
        return f'```{lang}{title_attr}'

    # Regex for old style code blocks
    # Pattern: ```{.cpp file=...} OR ```cpp ... (mixed?)
    # The prompt specified: `{.cpp file=...}`
    # Commonly: ```{.cpp file=...}  ... ```
    content = re.sub(r'^(\s*)```\{\.([a-zA-Z0-9_]+)\s+(.*?)\}', code_repl, content, flags=re.MULTILINE)

    # 2. Update Links and Images
    # Pattern: [text](link) or ![alt](link)
    # We ignore external links (http/https/ftp) and anchors (#)
    
    def link_repl(match):
        full_match = match.group(0) # e.g. [text](link)
        is_image = full_match.startswith('!')
        text = match.group(1)
        link = match.group(2)
        
        # Skip external links
        if link.startswith('http') or link.startswith('//') or link.startswith('mailto:'):
            return full_match
        
        # Handle anchor only
        if link.startswith('#'):
            return full_match
            
        # Split link and anchor
        parts = link.split('#')
        path_part = parts[0]
        anchor_part = '#' + parts[1] if len(parts) > 1 else ''
        
        if not path_part:
             return full_match

        # Resolve absolute path of the target
        # Since it's a relative link, it's relative to current_dir (old location)
        try:
            target_abs = os.path.abspath(os.path.join(current_dir, path_part))
        except:
             return full_match # weird path?

        # Find this target in our map
        # Note: image paths might not be in file_map if they are not scanned (e.g. if I missed some ext)
        # But we scanned recursive.
        
        # If the file exists on disk (or is in our map), we map it
        if target_abs in file_map:
            new_target_abs = file_map[target_abs]
        else:
            # Maybe it's a file we aren't renaming, or it doesn't exist?
            # If it's an image we didn't catch?
            if os.path.splitext(target_abs)[1].lower() in IMG_EXTENSIONS:
                 # It should have been in file_map... unless regex missed it
                 # Checking case sensitivity issues? Windows is case insensitive.
                 # Let's try to match lower case
                 found = False
                 for k, v in file_map.items():
                     if k.lower() == target_abs.lower():
                         new_target_abs = v
                         found = True
                         break
                 if not found:
                     return full_match # Can't fix what we don't know
            else:
                 # Markdown file that wasn't mapped?
                 # Maybe it's a directory link?
                 if os.path.isdir(target_abs):
                     # We didn't map directories specifically, but we renamed files inside.
                     # Directory renaming is implicit if we rename all files? 
                     # Wait, if we rename 'Graph_Theory/foo.md' to 'graph-theory/foo.md', 
                     # we are effectively renaming the directory.
                     # Simplification: We only map FILES. 
                     # Links often point to files. If a link points to a dir, standard markdown usually requires index.md?
                     # MkDocs strict mode might complain.
                     # Let's skip dir links for now or assume they point to index.md
                     return full_match
                 
                 # Try case insensitive lookup for MD files too
                 found = False
                 for k,v in file_map.items():
                     if k.lower() == target_abs.lower():
                         new_target_abs = v
                         found = True
                         break
                 if not found:
                     return full_match # Target not found
        
        # Now we have new_target_abs.
        # We need to compute the relative path from the NEW location of the current file
        # to the NEW location of the target file.
        
        my_new_abs = file_map[file_path]
        my_new_dir = os.path.dirname(my_new_abs)
        
        new_rel_link = os.path.relpath(new_target_abs, my_new_dir)
        
        # Normalize slashes to /
        new_rel_link = new_rel_link.replace('\\', '/')
        
        return f"{'!' if is_image else ''}[{text}]({new_rel_link}{anchor_part})"

    # Regex for links: [text](url) or ![text](url)
    # Be careful with nested brackets. This simple regex handles standard cases.
    content = re.sub(r'(!?\[.*?\])\((.*?)\)', link_repl, content)

    return content

def main():
    print("Scanning files...")
    file_map = scan_files(SOURCE_DIR)
    
    print(f"Found {len(file_map)} files to process.")
    
    # Process contents FIRST (reading from old paths)
    # We will write to a temp dict content_map: new_path -> content
    # effectively preparing the new state of the world
    
    write_queue = {}
    
    # Filter for markdown files to process content
    md_files = [f for f in file_map.keys() if f.endswith('.md')]
    
    print("Processing content...")
    for old_path in md_files:
        try:
            with open(old_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = update_content(content, old_path, file_map)
            
            # We will write this to the NEW path
            new_path = file_map[old_path]
            write_queue[new_path] = new_content
            
        except Exception as e:
            print(f"Error reading {old_path}: {e}")

    # Now perform the actual moves and writes
    
    # 1. Move Images
    print("Moving images...")
    img_files = [f for f in file_map.keys() if os.path.splitext(f)[1].lower() in IMG_EXTENSIONS]
    for old_path in img_files:
        new_path = file_map[old_path]
        if old_path == new_path: continue
        
        # Create dir if not exists
        os.makedirs(os.path.dirname(new_path), exist_ok=True)
        
        # Move file
        print(f"Move: {os.path.basename(old_path)} -> assets/...")
        try:
            shutil.move(old_path, new_path)
        except Exception as e:
            print(f"Failed to move {old_path}: {e}")

    # 2. Write Markdown files
    # Note: Some files are just renamed, some have content changes.
    # If the file path changed, we write to new path and delete old one?
    # Risk: Overwriting if new path matches another old path (rare with kebab-case unless collision)
    
    print("Updating markdown files...")
    for new_path, content in write_queue.items():
        # Find the old path for this new path
        old_path = [k for k, v in file_map.items() if v == new_path][0]
        
        # If directory structure changes (e.g. upper/snake case dirs), ensure new dir exists
        os.makedirs(os.path.dirname(new_path), exist_ok=True)
        
        # Write content
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        # If path is different, delete old file
        # BUT be careful on case-insensitive FS (Windows). 
        # d:\Foo.md and d:\foo.md are same.
        # If we write to foo.md, Foo.md is overwritten.
        # So we don't need to delete if it's just a case change.
        if old_path.lower() != new_path.lower():
            if os.path.exists(old_path):
                os.remove(old_path)
    
    # 3. Clean up empty directories?
    # Optional cleanup step
    
    print("Refactoring complete.")

if __name__ == "__main__":
    main()
