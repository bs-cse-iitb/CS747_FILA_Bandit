from task1 import Algorithm, UCB, KL_UCB, Thompson_Sampling
from task3 import *
from task2 import *
import numpy as np
horizon = 20
num_arms = 2

prob = [0.4,0.7]

prob = np.array(range(10))/10
num_arms = len(prob)
np.random.seed(0)


# ucb = KL_UCB(num_arms,horizon)
# for i in range(horizon):
#     x  = ucb.give_pull()
#     if np.random.uniform(0,1)<prob[x]:
#         rew =1
#     else:
#         rew =0
        
#     ucb.get_reward(x,rew)

from task2 import *

a = {2: np.array([1, 1, 1, 0, 1, 1, 0, 1, 0, 1]), 4: np.array([1, 1, 0, 0]), 9: np.array([0, 1, 0, 1, 0, 0])}

# print(len(a[2]))
# print(sum(a[2]))
# print(type(a))

# for i in a:
#     print(i,a[i])

t2 = AlgorithmBatched(10,20,20)
print(t2.give_pull())
t2.get_reward(a)