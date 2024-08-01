import nbformat as nbf

def text_to_notebook_cells(text):
    lines = text.split('\n')
    cells = []
    cell_type = 'markdown'
    cell_content = []
    
    for line in lines:
        if line.startswith('```'):
            if cell_type == 'markdown':
                if cell_content:
                    cells.append(nbf.v4.new_markdown_cell('\n'.join(cell_content)))
                cell_type = 'code'
            else:
                if cell_content:
                    cells.append(nbf.v4.new_code_cell('\n'.join(cell_content)))
                cell_type = 'markdown'
            cell_content = []
        else:
            cell_content.append(line)
    
    if cell_content:
        if cell_type == 'markdown':
            cells.append(nbf.v4.new_markdown_cell('\n'.join(cell_content)))
        else:
            cells.append(nbf.v4.new_code_cell('\n'.join(cell_content)))
    
    return cells

def read_file_as_string(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

input_text = read_file_as_string('original')
cells = text_to_notebook_cells(input_text)
nb = nbf.v4.new_notebook()
nb['cells'] = cells
output_file = '[7조]조치추천_시계열유사성.ipynb'
with open(output_file, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

