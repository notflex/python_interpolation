import numpy as np
import matplotlib.pyplot as plt

def initial_cond(x):
    f = (10 - np.cos(2 * x) + np.log(1 + x)) / (10 + x)
    return f

if __name__=='__main__':
    xmin = 0
    xmax = 10
    h = 0.5
    N = int((xmax-xmin)//h)
    x = np.arange(xmin,xmax, h)
    f = [initial_cond(x[i]) for i in range(len(x)) ]
    def polinom(xx):
        res = 0
        for i in range(len(x)):
            mult = 1
            for j in range(len(x)):
                if (j != i):
                    mult*= (xx - x[j]) / (x[i] - x[j])
            res += f[i] * mult
        return res

    g = [polinom(x[i]) for i in range(len(x))]
    print(x)
    print(f)
    print(g)
    
    plt.plot(x,f,color='b', label='function')
    plt.plot(x,g,color='r', linestyle = '--', linewidth=1.4, label='polinom')
    plt.legend()
    plt.show()

#if __name__ == '__main__':
#    xmin = 0
#    xmax = 10
 #   N = 40
 #   x = [(xmax + xmin)/2 + (xmax - xmin) * np.cos(np.pi * (2 * m - 1) / (2 * N)) /2 for m in range (N)]
  #  f = [initial_cond(x[i]) for i in range(len(x))]


 #   def polinom(xx):
  #      res = 0
  #      for i in range(1, len(x) - 1):
  #          mult = 1
   #         for j in range(1, len(x) - 1):
   #             if (x[j] != x[i]):
   #                 mult *= (xx - x[j]) / (x[i] - x[j])
   #         res += f[i] * mult
   #     return res


  #  g = [polinom(x[i]) for i in range(len(x))]
  #  print(x)
  #  print(f)
  #  print(g)

  #  plt.plot(x, f, color='b', label='function')
   # plt.plot(x, g, linestyle = '--', linewidth=1.4, color='r', label='polinom')
    #plt.legend()
   # plt.show()