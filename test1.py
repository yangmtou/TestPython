def triangle():
    name = input('你的名字是什么？ ')
    width = int(input('输入三角形宽度: '))
    height = int(input('输入三角形的高度:'))
    result = width*height//2
    print(f'三角形的面积: {result}')

triangle()
