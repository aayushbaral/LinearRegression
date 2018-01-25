import pandas as pd
import numpy as np

#Reading the data from a csv file
def read_data(filename):
    if filename:
        data = pd.read_csv(filename)
        return data


def step_gradient(data, current_theta_0, current_theta_1, learning_rate):
    theta_0 = 0
    theta_1 = 0
    N = float(len(data))

    for i in range(0, len(data)):
        
        xValues = data[i, 0]
        yValues = data[i, 1]
        theta_0 += 2/N * ((current_theta_0 + current_theta_1 * xValues) - yValues)

        theta_1 += 2/N * (((current_theta_0 + current_theta_1 * xValues) - yValues) * xValues)
        

    new_theta0 = current_theta_0 - (learning_rate * theta_0)
    new_theta1 = current_theta_1 - (learning_rate * theta_1)
    return new_theta0, new_theta1

def gradient_descent(initial_theta_0, initial_theta_1, learning_rate, num_iterations, data):
    theta_0 = initial_theta_0
    theta_1 = initial_theta_1
    for i in range(0, num_iterations):
        theta_0, theta_1 = step_gradient(data, theta_0, theta_1, learning_rate)
    return (theta_0, theta_1)


#Testing

def run():
    data = read_data("C:\\Users\\click\\Desktop\\bitcoin.csv")
    #Using only Closing Price and Volume from the data
    data = np.asarray(data[["Volume (BTC)", "Close"]])
    initial_theta0 = 0
    initial_theta1 = 0
    num_iterations = 100
    learning_rate = 0.0001
    print "After '{0}' iterations, the gradient descent is '{1}'".format(num_iterations, gradient_descent(initial_theta0, initial_theta1, learning_rate, num_iterations, data))


if __name__ == '__main__':
    run()

    
    
    



