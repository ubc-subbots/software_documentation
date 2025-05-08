import os
import yaml

# Root directory where Triton files are located
root_dir = 'D:/repository/triton/src'  # Path to your Triton directories

# Function to create a markdown file from a given file path
def create_markdown_file(file_path, output_dir):
    file_name = os.path.basename(file_path).replace('.py', '.md').replace('.yaml', '.md').replace('.cpp', '.md')
    markdown_content = f"# {file_name}\n\n"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
        # Simple markdown formatting (You can customize it based on your needs)
        markdown_content += f"```python\n{file_content}\n```\n"
    
    # Save the markdown file in the specified output directory
    markdown_file_path = os.path.join(output_dir, file_name)
    with open(markdown_file_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    return markdown_file_path

# Function to recursively generate markdown sections for all files in directories
def generate_sections(base_path, output_dir):
    sections = []
    
    for dirpath, dirnames, filenames in os.walk(base_path):
        if not dirnames:  # If the directory has no subdirectories
            for filename in filenames:
                # Process files based on their extension
                file_path = os.path.join(dirpath, filename)
                if filename.endswith(('.py', '.yaml', '.cpp', '.xml', '.md')):  # You can add other file types if needed
                    markdown_file = create_markdown_file(file_path, output_dir)
                    relative_path = os.path.relpath(markdown_file, output_dir)
                    section = {
                        'file': f'chapter_list/{relative_path.replace(os.sep, "/")}',
                        'title': filename[:-3].replace('_', ' ').title()
                    }
                    sections.append(section)
    
    return sections

# Function to generate the overall structure
def generate_structure():
    structure = {
        'jb-book': {
            'root': 'intro',
            'chapters': []
        }
    }

    # Add sections for 'intro' and 'markdown_guide'
    structure['jb-book']['chapters'].append({
        'file': 'chapter_list/intro',
        'title': 'Intro',
        'sections': [{'file': 'chapter_list/markdown_guide', 'title': 'Misc'}]
    })

    # Output directory for markdown files
    output_dir = 'D:/repository/software_documentation/subbots_docs/chapter_list'
    
    # Add chapters and their sections by scanning directories
    for chapter_dir in ['triton_bringup', 'triton_controls', 'triton_example', 'triton_gate', 'triton_gazebo', 'triton_interfaces', 'triton_object_recognition', 'triton_pid_controller', 'triton_pipeline', 'triton_teleop', 'triton_vision_utils']:
        chapter_path = os.path.join(root_dir, chapter_dir)
        if os.path.exists(chapter_path):
            chapter = {
                'file': f'chapter_list/{chapter_dir.replace(os.sep, "/")}',
                'title': chapter_dir.replace('_', ' ').title(),
                'sections': generate_sections(chapter_path, output_dir)
            }
            structure['jb-book']['chapters'].append(chapter)
    
    return structure

# Save the generated structure to a YAML file
def save_to_yaml():
    structure = generate_structure()
    with open('book_structure.yaml', 'w', encoding='utf-8') as file:
        yaml.dump(structure, file, default_flow_style=False, sort_keys=False)
    print("book_structure.yaml has been generated.")

# Run the script
save_to_yaml()
