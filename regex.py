class reg:
    # Regex for valid input

    POLYNOME = r"(-?\b\d+)x\^(-?\d+\b)"
    RATIONAL = r"([\*\-\+\%]?\(?((?:[\-\+]|(?<=\d)[\+\-\*\%]){,1}?((?:[0-9]+[\,\.]?[0-9])*(?:[\/][1-9]+[\,\.]?[0-9]*|[\/]0+(?:[\.\,]?0*)?(?:[1-9]))*[\+\-\*\%]*?(?:\d)?)+)\)?)+"
    # RATIONAL = r"([+\-*%/]?(\d+|\d*[.]?\d+))+"
    MATRICES = r"((?:^\[|\;)((?<!\])\[{1}((" + RATIONAL + ")?\,?)+(?<!\,)\])+)*\]$"
    COMPLEXE = r"(^|-|\+)(\d+)(\*?i?)"
    FUNCTION = r"[a-zA-Z]+(?=\((?:[a-zA-Z]{1,65000})\))"

    IS_NUMBER = r"^[-+]?[0-9]+[.]?[0-9]*"
    IS_ASSIGN = r"^([a-zA-Z]+|[a-zA-Z]+\([a-zA-Z]+\))(?=\s*\=\s*){1}"
    IS_CALCUL = r"[a-zA-Z\+\-\*\/\^0-9]+=\?{1}"

    # Regex for parse input

    PARSE_RATIONAL = r""

    # Regex for handler input

    STRIP_SPACE = r"[\s]{1,}"


# [a-zA-Z]+\(((?P<var>[a-zA-Z]{1,65000}))\)\s*\=\s*\(?(?:[+-]?(?:(?:(?:\d+|(?P=var)|\d+\*?(?P=var))\^\d+)|(?:\d+(?P=var))|\d+\*?(?P=var)|(?:\d+)|(?:(?P=var))))+\)?
