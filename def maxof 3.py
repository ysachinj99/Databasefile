def max_two(x,y):
      if x > y:
            return x
      else:
            return y
def max_Three(x,y,z):
      return max_two(x,max_two(y,z))
print(max_Three(4,5,6))
