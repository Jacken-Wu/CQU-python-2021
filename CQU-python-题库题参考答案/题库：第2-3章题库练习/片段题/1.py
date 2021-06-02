consumption=eval(input())
tip = consumption / 10

tax = consumption * 7 / 100

total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

