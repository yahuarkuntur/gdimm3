

def get_active_text(combobox):
    iter = combobox.get_active_iter()
    model = combobox.get_model()
    if iter is None:
        return None
    return str(model.get_value(iter, 1))
