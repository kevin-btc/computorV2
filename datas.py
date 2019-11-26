class Rational:
    def __init__(self, c_name, c_value):
        pass

    def add_val(c_name, c_value):
        self.name = c_name
        self.value = c_value


class Matrices:
    pass


class Function:
    pass


class complexe:
    pass


class Datas:
    datas = {
        "rational": Rational(),
        "matrices": Matrices(),
        "function": Function(),
        "complexe": complexe(),
    }

    def __init__(self):
        pass

    def add_var():
        pass

    def del_var():
        browse_datas()

    def browse_datas_type(type_name, vars, assign_type, var_name):
        for name, var_value in list(vars.items()):
            if name.lower() == var_name.lower() and assign_type != type_name:
                del datas[type_name][var_name]

    def browse_datas(assign_type, var_name):
        for type_name, vars in datas.items():
            browse_datas_type(type_name, vars, assign_type, var_name)
