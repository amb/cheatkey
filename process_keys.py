import bpy


def cas_string(c, a, s):
    rst = "CTRL" if c else None
    ast = "ALT" if a else None
    sst = "SHIFT" if s else None
    return "-".join([i for i in [rst, ast, sst] if i])


def load_names(group=[''], search_term="", search_bind=""):
    bind_count = 0
    found_items = []

    keys = bpy.context.window_manager.keyconfigs.active.keymaps
    # print(search_term, ",", search_bind)

    # if group == [''] and search_term == "" and search_bind == "":
    #     return 0, []

    for k in keys.keys():
        if len(group) > 0 and group[0] != '':
            match = False
            for g in group:
                if g.upper() in k.upper() and len(g) > 0:
                    match = True
            if not match:
                continue
        m = keys[k]

        for n, v in m.keymap_items.items():
            if len(search_term) > 0 and search_term.upper() not in v.name.upper():
                continue

            if len(search_bind) > 0 and search_bind.upper() not in v.type.upper():
                continue

            it = [k, v.name, v.ctrl, v.alt, v.shift, v.type, v]
            found_items.append(it)

            bind_count += 1

    return bind_count, found_items
