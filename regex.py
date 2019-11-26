class reg:
    # Regex for valid input

    POLYNOME = r"(-?\b\d+)x\^(-?\d+\b)"
    RATIONAL = r"([\*\-\+\%]?\(?((?:[\-\+]|(?<=\d)[\+\-\*\%]){,1}?((?:[0-9]+[\,\.]?[0-9])*(?:[\/][1-9]+[\,\.]?[0-9]*|[\/]0+(?:[\.\,]?0*)?(?:[1-9]))*[\+\-\*\%]*?(?:\d)?)+)\)?)+"
    MATRICES = r"((?:^\[|\;)((?<!\])\[{1}((" + RATIONAL + ")?\,?)+(?<!\,)\])+)*\]$"
    COMPLEXE = r"(^|-|\+)(\d+)(\*?i?)"

    IS_NUMBER = r"^[-+]?[0-9]+[,.]?[0-9]*"
    IS_ASSIGN = r"^([a-zA-Z]+|[a-zA-Z]+\([a-zA-Z]{1}\))\={1}"
    IS_CALCUL = r"[a-zA-Z\+\-\*\/\^0-9]+=\?{1}"
    IS_FUNCTION = r"^[a-zA-Z]+\(([a-zA-Z]|[0-9]{1,65000})\)"

    # Regex for parse input

    PARSE_RATIONAL = r""

    # Regex for handler input

    STRIP_SPACE = r"[\s]{1,}"
