import os

# Your specific directory structure
structure = """
app/
│
├
|── orchestrator/
│   ├── planner_agent.py
│   ├── workflow_engine.py
│   ├── workflow_models.py
│   ├── execution_context.py
│   └── workflow_parser.py
│
"""

def create_project_structure(text_structure):
    # This keeps track of which folder level we are currently in
    path_stack = []
    
    for line in text_structure.strip().split('\n'):
        # 1. Clean formatting characters but keep leading spaces to determine depth
        clean_line = line.replace('├── ', '    ').replace('└── ', '    ').replace('│', ' ')
        
        # 2. Calculate depth based on 4-space indentation
        indent_count = len(clean_line) - len(clean_line.lstrip())
        depth = indent_count // 4
        
        # 3. Get the actual folder or file name
        name = clean_line.strip()
        if not name:
            continue
            
        # 4. Remove trailing slash if present for path joining
        clean_name = name.rstrip('/')
        
        # 5. Adjust the stack to the current depth
        path_stack = path_stack[:depth]
        path_stack.append(clean_name)
        
        # 6. Construct the full path
        full_path = os.path.join(*path_stack)
        
        # 7. Determine if it's a file or folder
        # If it has a dot (extension) it's a file, otherwise it's a folder
        if '.' in clean_name:
            # Ensure the directory containing the file exists
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            # Create an empty file
            with open(full_path, 'a'):
                os.utime(full_path, None)  # Update timestamp if file exists
            print(f"📄 Created file:   {full_path}")
        else:
            os.makedirs(full_path, exist_ok=True)
            print(f"📁 Created folder: {full_path}")

if __name__ == "__main__":
    print("🚀 Starting project structure creation...\n")
    create_project_structure(structure)
    print("\n✅ Structure created successfully!")
