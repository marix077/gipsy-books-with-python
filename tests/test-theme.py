import sys
sys.path.append("../types")
import theme

myStyle = {
    "one" : 1,
    "tow" : 2,
    "three" : 3
}

style = theme.theme()

style.SetButtonStyle(myStyle)

print(style.GetButtonStyle())
