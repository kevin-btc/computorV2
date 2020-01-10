# Regex for valid input

POLYNOME = r"(-?\b\d+)x\^(-?\d+\b)"
RATIONAL = r"([\*\-\+\%\/]?\(?((?:[\-\+]|(?<=\d)[\+\-\*\%\/]){,1}?((?:[0-9]+[\.]?[0-9])*(?:[\/][1-9]+[\.]?[0-9]*|[\/]0+(?:[\.]?0*)?(?:[1-9]))*[\+\-\*\%\/]*?(?:\d)?)+)\)?)+"
MATRICES = r"((?:^\[|\;)((?<!\])\[{1}((.*)?\,?)+(?<!\,)\])+)*\]$"
COMPLEXE = r"(^|-|\+)(\d+)(\*?i?)"
FUNCTION = r"[a-zA-Z]+(?=\((?:[a-zA-Z]{1,65000})\))"

IS_NUMBER = r"^[-+]?[0-9]+[.]?[0-9]*"
IS_LETTER = r"[a-zA-Z]+"
IS_ASSIGN = r"^([a-zA-Z]+|[a-zA-Z]+\([a-zA-Z]+\))(?=\s*\=\s*){1}"
IS_CALCUL = r"[a-zA-Z\+\-\*\/\^0-9]+=\?{1}"

# Regex for handler input

STRIP_SPACE = r"[\s]{1,}"
CONTAIN_LTR = r"(\([a-zA-Z]+\))"

# Regex for Parse fronction

PARSE_FUNCT = r"(?<=(?:[a-zA-Z]\())([a-zA-Z]+)(?=\))"
PARAM_FUNCT = r"(?<=(?:[a-zA-Z]\())([0-9]+(?:\.[0-9]+)?)(?=\))"

#PARSE_PARAM = r"(?:^|(?<=[*/%+-\[\s]))[a-zA-Z]+(?=[*/%+-\]\s]|$)|[a-zA-Z]+(?=\((?:[0-9]+(?:\.[0-9]+)?)\))"
PARSE_PARAM = r"[a-zA-Z]+"
BRACKET_LEFT = "("
BRACKET_RGTH = ")"
