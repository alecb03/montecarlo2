       
import numpy as np
class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        self.N = N
        self.config = np.zeros(N, dtype=int) 
        

    def __str__(self):
        return str(self.config)

    def __repr__(self):
        return f"Bitstring((self.config.tolist))"

    def __eq__(self, other):        
        return np.array_equal(self.config, other.config)

    
    def __len__(self):
        return len(self.config)


    def on(self):
        count = 0
        for i in range(len(self.config)):
            if self.config[i] == 1:
                count += 1
        return count
    
    def off(self):
        count = 0
        for i in range(len(self.config)):
            if self.config[i] == 0:
                count += 1
        return count
    
    def flip_site(self,i):
        self.config[i] = 1 - self.config[i]
        
    
    def int(self):
        dec = 0
        power = len(self.config) - 1  
        for i in self.config:
            dec = dec + i *(2**power) 
            power = power - 1
        return dec

 

    def set_config(self, s:list[int]):
        self.config = list(s)
        
    def set_int_config(self, dec: int):
        for i in range(-1, -self.N - 1, -1):
            curr_bit = dec % 2
            self.config[i] = curr_bit
            dec = dec // 2
        return self
