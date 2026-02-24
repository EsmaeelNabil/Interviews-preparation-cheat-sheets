import re
import os
import glob
from pathlib import Path

def smart_break_line(content, max_length=110):
    """
    Break a long blockquote line intelligently.
    Returns a list of lines (without '> ' prefix).
    """
    if len(content) <= max_length:
        return [content]
    
    lines = []
    
    # Priority break points (in order of preference)
    # 1. After closing bracket + sentence end if **TL;DR:** or similar prefix
    match = re.match(r'^(\[![\w]+\]|\*\*[^:]+:\*\*)\s+(.*)', content)
    if match:
        prefix = match.group(1)
        rest = match.group(2)
        lines.append(prefix)  # First line has just the marker
        
        # Now break the rest
        rest_lines = smart_break_line(rest, max_length)
        lines.extend(rest_lines)
        return lines
    
    # 2. Break at logical points (in priority order)
    break_points = [
        (r'(\. )(?=[A-Z])', '. '),      # After period before capital
        (r'(\. )', '. '),                # After any period
        (r'(, )', ', '),                 # After comma
        (r'( → )', ' → '),               # Before/after arrow
        (r'( \| )', ' | '),              # Before/after pipe
        (r'(: )', ': '),                 # After colon
        (r'( )', ' '),                   # Last resort: space
    ]
    
    current_line = ""
    words = content.split()
    
    for word in words:
        test_line = (current_line + " " + word).lstrip()
        
        if len(test_line) <= max_length:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)
    
    return lines


def fix_blockquotes(filepath):
    """
    Read a markdown file, find long blockquotes (>150 chars),
    and break them intelligently across multiple lines with '> ' prefix.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False
    
    new_lines = []
    changes_made = 0
    
    for i, line in enumerate(lines):
        # Check if it's a blockquote line
        if line.startswith('>'):
            # Remove the '> ' prefix and get content
            content = line[1:].lstrip()
            content = content.rstrip('\n')
            
            # If it's longer than 150 chars, break it
            if len(content) > 150:
                broken = smart_break_line(content, max_length=110)
                for broken_line in broken:
                    new_lines.append(f"> {broken_line}\n")
                changes_made += 1
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    
    # Write back only if changes were made
    if changes_made > 0:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            return True
        except Exception as e:
            print(f"Error writing {filepath}: {e}")
            return False
    
    return False


def main():
    # Find all markdown files recursively
    md_files = glob.glob('/Users/esmaeelnabil/Pdev/android/**/*.md', recursive=True)
    
    total_files = len(md_files)
    fixed_files = 0
    
    print(f"Found {total_files} markdown files")
    print("Processing...\n")
    
    for filepath in sorted(md_files):
        if fix_blockquotes(filepath):
            fixed_files += 1
            print(f"✓ Fixed: {filepath}")
    
    print(f"\n{'='*60}")
    print(f"Summary: Fixed {fixed_files}/{total_files} files")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
