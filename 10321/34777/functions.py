#  IN THE NAME OF ALLAH

import numpy as np

class Linear_Regression:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.alpha0 = 0
        self.alpha1 = 0
        self.coefficients = [self.alpha0, self.alpha1]
    
    def fit(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)
        
        x_mean = self.x.mean()
        y_mean = self.y.mean()
        
        s=0
        m=0
        #TODO
        for i in range(len(self.x)):
            s +=(self.x[i]-x_mean)*(self.y[i]-y_mean)
            m += (self.x[i]-x_mean)**2
        self.alpha1 = s/m
        self.alpha0 = y_mean - self.alpha1*x_mean
        
        self.coefficients = [self.alpha0, self.alpha1]
        return self
    
    def predict(self, x):
        #TODO
        n=len(x)
        y=[]
        for i in range(n):
            y.append(self.alpha0 + self.alpha1*x[i])
        return y
    
    def mean_squared_error(self, y_test, y_pred):
        #TODO
        e=0
        n= len(y_pred)
        for i in range(n):
            e += (y_test[i] - y_pred[i])**2
        return e/n