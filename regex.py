class reg:
    # Regex for valid input

    POLYNOME    = r"(-?\b\d+)x\^(-?\d+\b)"
    MATRICES    = r"((?:^\[|\;)((?<!\])\[{1}([-+]?[0-9]*\.?[0-9]+([-+]?[0-9]+)?\,?)+(?<!\,)\])+)*\]$"
    RATIONAL    = r"([\*\-\+\%]?\(?((?:[\-\+]|(?<=\d)[\+\-\*\%]){,1}?([0-9]+[\,\.]?[0-9]*(?:[\/][1-9]+[\,\.]?[0-9]*|[\/]0+(?:[\.\,]?0*)?(?:[1-9]))*[\+\-\*\%]*?(?:\d)?)+|((?<!\d)[a-z](?!\d)+))\)?)+"
    # RATIONAL    = r"[0-9A-Za-a]*( ){0,}([+-/*]( ){0,}[0-9A-Za-a]*( ){0,})*"
    COMPLEXE    = r"(^|-|\+)(\d+)(\*?i?)"
    IS_NUMBER   = r"^[-+]?[0-9]+[,.]?[0-9]*"
    IS_FUNCTION = r"^[a-zA-Z]+\(([a-zA-Z]|[0-9]{1,65000})\)"
    ASSIGNATION = r"^([a-zA-Z]+|[a-zA-Z]+\([a-zA-Z]{1}\))\={1}"
    CALCULATION = r"[a-zA-Z\+\-\*\/\^0-9]+=\?{1}"


    # Regex for parse input

    PARSE_RATIONAL = r""

    # Regex for handler input

    STRIP_SPACE = r"[\s]{1,}"
