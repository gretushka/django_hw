from django import template

register = template.Library()

@register.filter

def cellcl(s):
    if(s):
        infl = float(s)
        if infl < 0:
            cellcl = "green"
        else:
            if infl > 5:
                cellcl = "darkred"
            else:
                if infl > 2:
                    cellcl = "red"
                else:
                    if infl >1:
                        cellcl = "pink"
                    else:
                        cellcl = "white"
    else:
        cellcl = "white"
    return cellcl