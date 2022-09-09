"""
NOTE: You are only allowed to edit this file between the lines that say:
    # START EDITING HERE
    # END EDITING HERE

This file contains the AlgorithmManyArms class. Here are the method details:
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
"""

from socket import AddressFamily
import numpy as np

# START EDITING HERE
# You can use this space to define any helper functions that you need
# END EDITING HERE

class AlgorithmManyArms:
    def __init__(self, num_arms, horizon):
        self.num_arms = num_arms
        # Horizon is same as number of arms
        #self.arms = np.array(range(self.num_arms))
        #self.success =np.zeros(self.num_arms)
        self.counts = np.zeros(self.num_arms)
        self.mean = np.zeros(self.num_arms)
        #self.h=0
        #self.counter=0
        #self.limit = 0.9
    def give_pull(self):
        # START EDITING HERE

        # for i in range(self.num_arms)
        # if np.argmax(self.mean)>0.9:
        #     return np.argmax(self.mean)

        # 

        # step = round(((self.h+1) * 0.4)/(self.num_arms-1 ),2)
        # #print(step)
        # print((0.96-step))
        # update = self.num_arms/10
        # limit = 0.96
        # if(self.h>update):
        #     limit -= 0.04
        #     update +=self.num_arms/10

        # print(limit)
        # if self.h==0:
        #     self.h+=1
        highest_mean = np.argmax(self.mean)
        if self.mean[highest_mean] > 0.96:  # 0.99  for last 300
            return highest_mean
        else:
            return np.random.randint(self.num_arms) 

    
        # sample = np.zeros(len(self.arms))
        # for arm in range(len(self.arms)):
        #     sample[arm]=np.random.beta(self.success[arm]+1,1)
        # #print(sample)
        # return self.arms[np.argmax(sample)]
        raise NotImplementedError
        # END EDITING HERE
    
    def get_reward(self, arm_index, reward):
        # START EDITING HERE
        
        #print(arm_index, reward)
        #print(self.arms)
        # self.h+=1
        p_ = self.mean[arm_index]
        u = self.counts[arm_index]
        self.mean[arm_index]= (p_ * u + reward ) / (u+1)

        self.counts[arm_index]+=1



        # index = np.where(self.arms==arm_index)
        # self.counts[index]+=1
        # if reward == 0:
        #     self.arms = np.delete(self.arms,index)
        #     self.success = np.delete(self.success, index)
        #     self.counts  = np.delete(self.counts, index)
        #     self.mean = np.delete(self.mean, index)
        # else:
        #     self.success[index]+=1
        #     p_ = self.mean[index]
        #     u = self.counts[index]
        #     self.mean[index]= (p_ * (u-1) + reward ) / u
        
        #print(self.mean)
        #print(self.counts)


        
        # self.counts[arm_index]+=1
        #raise NotImplementedError
        # END EDITING HERE
