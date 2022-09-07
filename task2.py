"""
NOTE: You are only allowed to edit this file between the lines that say:
    # START EDITING HERE
    # END EDITING HERE

You need to complete the following methods:
    - give_pull(self): This method is called when the algorithm needs to
        select the arms to pull for the next round. The method should return
        two arrays: the first array should contain the indices of the arms
        that need to be pulled, and the second array should contain how many
        times each arm needs to be pulled. For example, if the method returns
        ([0, 1], [2, 3]), then the first arm should be pulled 2 times, and the
        second arm should be pulled 3 times. Note that the sum of values in
        the second array should be equal to the batch size of the bandit.
    
    - get_reward(self, arm_rewards): This method is called just after the
        give_pull method. The method should update the algorithm's internal
        state based on the rewards that were received. arm_rewards is a dictionary
        from arm_indices to a list of rewards received. For example, if the
        give_pull method returned ([0, 1], [2, 3]), then arm_rewards will be
        {0: [r1, r2], 1: [r3, r4, r5]}. (r1 to r5 are each either 0 or 1.)
"""

from calendar import c
import numpy as np
import math

# START EDITING HERE
# You can use this space to define any helper functions that you need.
# END EDITING HERE

class AlgorithmBatched:
    def __init__(self, num_arms, horizon, batch_size):
        self.num_arms = num_arms
        self.horizon = horizon
        self.batch_size = batch_size
        assert self.horizon % self.batch_size == 0, "Horizon must be a multiple of batch size"
        # START EDITING HERE
        # Add any other variables you need here
        # END EDITING HERE
        self.success = np.zeros(num_arms)
        self.counts = np.zeros(num_arms)
    
    def give_pull(self):
        # START EDITING HERE
        #print(self.batch_size)


        # arm_to_pull = np.array([])
        # arm_count = np.array([])

        ls = []
        for _ in range(self.batch_size):
            failure = self.counts-self.success 
            sample=np.random.beta(self.success+1,failure+1)
            #print(sample)
            ls.append(np.argmax(sample))
            # if index in arm_to_pull:
            #     index2 = np.where(arm_count==index)
            #     arm_count[index2]+=1
            #     print(arm_count[index2])
            #     #arm_count[index2]+=1
            # else:
            #     arm_to_pull = np.append(arm_to_pull,index)
            #     arm_count = np.append(arm_count,1)
                #print(arm_count)


        #arm_to_pull , arm_count = np.unique(ls, return_counts = True)

        #print(arm_to_pull,arm_count)
        

    
        # ls = []
        # batch = self.batch_size
        # while(batch != 1):
        #     next = int(batch*0.5)
        #     ls.append(next)
        #     batch-=next
        # ls.append(1)

        # a = math.ceil(self.batch_size*3/4)
        # b = math.ceil((self.batch_size-a)*3/4)
        # #c = math.ceil((self.batch_size-b-a)*3/5)
        # c = self.batch_size - a  - b
        # #print(a,b,c)


        # #print(ls)
        # ls = np.array(ls)
        # lenls = len(ls)
        # max_k = sample.argsort()[-lenls:][::-1]
        # #print(max_k)

        # max_k = sample.argsort()[-3:][::-1]
        #return arm_to_pull,arm_count
        
        return np.unique(ls, return_counts = True)
        # END EDITING HERE
    
    def get_reward(self, arm_rewards):
        # START EDITING HERE
        for i in arm_rewards:
            self.counts[i]+=len(arm_rewards[i])
            self.success[i]+=sum(arm_rewards[i])

        #print(arm_rewards)
        #print(self.counts)
        #print(self.success)

        
        # END EDITING HERE