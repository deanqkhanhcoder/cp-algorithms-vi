import os
import re

SOURCE_DIR = os.path.abspath("d:/cp-algorithms/src")

def fix_content(content):
    # Fix standard links: [[text]] -> [text]
    # Be careful not to break valid [[...]] if used for wikilinks, but we want standard md.
    # The regression created [[text]](link).
    # We want [text](link).
    
    # Regex: \[(\[.*?\])\]\((.*?)\)
    # This matches [[text]](link)
    
    def repl(m):
        inner = m.group(1) # [text]
        link = m.group(2)
        # inner is [text]. We want text.
        text = inner[1:-1]
        return f"[{text}]({link})"

    # Fix images: ![![text]](link)
    # The regression likely produced ![![text]](link)
    # Regex: !\[(!\[.*?\])\]\((.*?)\)
    
    def img_repl(m):
        inner = m.group(1) # ![text]
        link = m.group(2)
        # inner is ![text]. We want text (alt).
        text = inner[2:-1]
        return f"![{text}]({link})"

    # Apply fix for images first (more specific)
    # Pattern matching ![![...]]
    content = re.sub(r'!\[(!\[.*?\])\]\((.*?)\)', img_repl, content)
    
    # Apply fix for links
    # Pattern matching [[...]]
    # Note: This might match [[link]] independent of ()? 
    # The previous script only touched [text](link) patterns.
    # So we look for [[text]](link).
    content = re.sub(r'\[(\[.*?\])\]\((.*?)\)', repl, content)
    
    return content

def main():
    print("Fixing double brackets...")
    count = 0
    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content = fix_content(content)
                    
                    if new_content != content:
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        count += 1
                        # print(f"Fixed {file}")
                except Exception as e:
                    print(f"Error {path}: {e}")
    
    print(f"Fixed {count} files.")

if __name__ == "__main__":
    main()
