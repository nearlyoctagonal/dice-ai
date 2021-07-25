# This file contains the full strategy using expectation values, as outlined in 

import numpy as np

class Microstate():
    '''This class encapsulates all information and functions regarding a microstate'''
    
    def __init__(self,dice,n_rerolls=2):
        '''
        dice: numpy array of dice results
        n_rerolls: number od rerolls remaining
        '''
        
        self.dice = dice
        self.n_rerolls = n_rerolls
        
    def decision(desired,dice=self.dice,n_rerolls=self.n_rerolls):
        '''
        IN
        desired: numpy array of desired result
        
        OUT
        keep: boolean array saying which dice to keep
        p: probability of getting the desired result when keeping these dice
        '''
        
        # determine which dice match the desired result
    
        # arrays to keep track of how often each dice result appears
        n_desired = np.array([sum(desired == i) for i in range(1,7)])
        n_found = np.zeros(6)
        
        match = np.full(5,True)
        
        for i,d in enumerate(dice):
            if d in desired and n_found[d-1] <= n_desired[d-1]:
                match[i] = True
                n_found[d-1] += 1
        
        if n_rerolls == 1:
            keep = match
            reroll = 5-sum(keep)
            p = np.math.factorial(reroll)/6**(reroll)
        
        if n_rerolls == 2:
            # find all possible combinations of dice to keep
            keep_possibilities = [np.array([a,b,c,d,e]) for a in [True,False] for b in [True,False] for c in [True,False] for d in [True,False] for e in [True,False]]
            
        return keep,p    