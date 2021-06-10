color = {
    'red': 1,
    'blue': 2,
    'yellow': 3,
    3: 'purple',
    4: 'orange',
    5: 'green'
}
color_1 = input()
color_2 = input()
if color_1 not in color or color_2 not in color or color_1 == color_2:
    print('error')
else:
    print(color[color[color_1] + color[color_2]])


