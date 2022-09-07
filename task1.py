"""
NOTE: You are only allowed to edit this file between the lines that say:
    # START EDITING HERE
    # END EDITING HERE

This file contains the base Algorithm class that all algorithms should inherit
from. Here are the method details:
    - __init__(self, num_arms, horizon): This method is called when the class
        is instantiated. Here, you can add any other member variables that you
        need in your algorithm.
    
    - give_pull(self): This method is called when the algorithm needs to
        select an arm to pull. The method should return the index of the arm
        that it wants to pull (0-indexed).
    
    - get_reward(self, arm_index, reward): This method is called just after the 
        give_pull method. The method should update the algorithm's internal
        state based on the arm that was pulled and the reward that was received.
        (The value of arm_index is the same as the one returned by give_pull.)

We have implemented the epsilon-greedy algorithm for you. You can use it as a
reference for implementing your own algorithms.
"""

import numpy as np
import math
# Hint: math.log is much faster than np.log for scalars

class Algorithm:
    def __init__(self, num_arms, horizon):
        self.num_arms = num_arms
        self.horizon = horizon
    
    def give_pull(self):
        raise NotImplementedError
    
    def get_reward(self, arm_index, reward):
        raise NotImplementedError

# Example implementation of Epsilon Greedy algorithm
class Eps_Greedy(Algorithm):
    def __init__(self, num_arms, horizon):
        super().__init__(num_arms, horizon)
        # Extra member variables to keep track of the state
        self.eps = 0.1
        self.counts = np.zeros(num_arms)
        self.values = np.zeros(num_arms)
    
    def give_pull(self):
        if np.random.random() < self.eps:
            return np.random.randint(self.num_arms)
        else:
            return np.argmax(self.values)
    
    def get_reward(self, arm_index, reward):
        self.counts[arm_index] += 1
        n = self.counts[arm_index]
        value = self.values[arm_index]
        new_value = ((n - 1) / n) * value + (1 / n) * reward
        self.values[arm_index] = new_value


# START EDITING HERE
# You can use this space to define any helper functions that you need
# END EDITING HERE

class UCB(Algorithm):
    def __init__(self, num_arms, horizon):
        super().__init__(num_arms, horizon)
        # You can add any other variables you need here
        # START EDITING HERE

        #num_arms no. of arms
        # ucb : ucb values of each arm
        self.ucb = np.zeros(num_arms)
        #counts : no. of pull of each arm
        self.counts = np.zeros(num_arms)
        # mean : empirical mean
        self.mean = np.zeros(num_arms)
        self.h = 0
        # END EDITING HERE
        # END EDITING HERE
    
    def give_pull(self):
        # START EDITING HERE
        #print(self.h)
        #Pulling arm serial wise for first n pull
        if (self.h < self.num_arms):
            return self.h
        return np.argmax(self.ucb)
        # END EDITING HERE
    
    def get_reward(self, arm_index, reward):
        # START EDITING HERE

        # empirical means of arm_index    
        p_ = self.mean[arm_index]
        u = self.counts[arm_index]
        self.mean[arm_index]= (p_ * u + reward ) / (u+1) 

        #print(self.mean)

        self.counts[arm_index]+=1
        self.h+=1

        # mistake 1 >=  instead of >
        if (self.h > self.num_arms):
            ln = math.log(self.h)
            for arm in range(self.num_arms):
                add_to_mean = math.sqrt((2*ln)/self.counts[arm])
                self.ucb[arm]= self.mean[arm] + add_to_mean
                # second mistake self.mean[arm_index] instead of self.mean[arm]
        # END EDITING HERE


def kl(x,y):
    if x==0:
        kl_value = -math.log((1-y))
        return kl_value
    if x==1:
        kl_value = -math.log(y)
        return kl_value
    else:
        ln1 = math.log(x/y)
        ln2 = math.log((1-x)/(1-y))
        kl_value = x * ln1 + (1-x) * ln2 
        return kl_value

def bs(p_,start,end,kl_p_q):
    # middle = (start + end)/2
    # #print(middle)
    # kl_p_m = kl(p_,middle)
    # #print(kl_p_m , kl_p_q)
    # #return 0.5
    # if abs(start-end) < 0.001 or abs(kl_p_m-kl_p_q) < 0.001:
    #     return middle
    # elif(kl_p_m > kl_p_q ):
    #     return bs(p_,start,middle,kl_p_q) # return not written very big mistake
    # else:
    #     return bs(p_,middle,end,kl_p_q)

    middle = (start + end)/2
    kl_p_m = kl(p_,middle)
    while(abs(start-end) > 0.001 and abs(kl_p_m-kl_p_q) > 0.001):
        if(kl_p_m > kl_p_q ):
            end = middle
        else:
            start = middle
        middle = (start + end)/2
        kl_p_m = kl(p_,middle)
    return middle



class KL_UCB(Algorithm):
    def __init__(self, num_arms, horizon):
        super().__init__(num_arms, horizon)
        # You can add any other variables you need here
        # START EDITING HERE
        #num_arms no. of arms

        self.counts =np.zeros(num_arms)
        self.mean = np.zeros(num_arms)
        self.h = 0
        self.klucb = np.zeros(num_arms)


        # END EDITING HERE
    
    def give_pull(self):
        # START EDITING HERE 

        if self.h < self.num_arms:
            return self.h 
        return np.argmax(self.klucb)
        # END EDITING HERE
    
    def get_reward(self, arm_index, reward):
        # START EDITING HERE
        # empirical means of arm_index 
        self.h+=1
        self.counts[arm_index]+=1  
        p_ = self.mean[arm_index] 
        u = self.counts[arm_index]
        self.mean[arm_index]= ((u-1)* p_ + reward) / u

        if self.h < self.num_arms:
            return
        ln_t = math.log(self.h)
        lnln_t = math.log(ln_t)
        c = 3
        ln_final = (ln_t + c * lnln_t)
        q = 0.999

        if (self.h > self.num_arms):
            for arm in range(self.num_arms):
                kl_p_q = ln_final / self.counts[arm]
                self.klucb[arm] = bs(self.mean[arm],self.mean[arm],q,kl_p_q)

        
        # END EDITING HERE



class Thompson_Sampling(Algorithm):
    def __init__(self, num_arms, horizon):
        super().__init__(num_arms, horizon)
        # You can add any other variables you need here
        # START EDITING HERE
        self.success = np.zeros(num_arms)
        self.counts = np.zeros(num_arms)
        #self.beta = np.random.beta(1,1,num_arms)
        # END EDITING HERE
    
    def give_pull(self):
        # START EDITING HERE
        #np.random.seed(0)
        #by using random.seed(0) regret goes negative
        #sample : array to store sample value from beta distribution
        #arm : index sarting from zero


        # for every arm a draw  sample from beta distribution
        # sample = np.zeros(self.num_arms)
        # for arm in range(self.num_arms):
        #     sample[arm]=np.random.beta(self.success[arm]+1,self.counts[arm]-self.success[arm]+1)
        # #print(sample)
        # return np.argmax(sample)
        
        

        # in one line
        return np.argmax(np.random.beta(self.success+1,self.counts-self.success+1))

        # END EDITING HERE

    def get_reward(self, arm_index, reward):
        # START EDITING HERE
        self.counts[arm_index]+=1
        if reward == 1:
            self.success[arm_index]+=1
            
        #self.beta[arm_index]=np.random.beta(self.success[arm_index]+1,self.counts[arm_index]-self.success[arm_index]+1)
        #print("arm : {} rew : {} success: {} failure {} counts : {} ".format(arm_index,reward,self.success, self.beta,self.counts))
        # END EDITING HERE