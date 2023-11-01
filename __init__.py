
from IPython.core.magic import register_cell_magic
from config import USER_CODE_PATH

@register_cell_magic
def save_for_remote(line, cell):
    with open(USER_CODE_PATH, 'w') as f:
        f.write(cell)
