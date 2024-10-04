import numpy as np
import matplotlib.pyplot as plt
plt.style.use('./deeplearning.mplstyle')


def compute_model_output(x, w, b):
    """
    Computes the prediction of a linear model
    Args:
      x (ndarray (m,)): Data, m examples
      w,b (scalar)    : model parameters
    Returns
      f_wb (ndarray (m,)): model prediction
    """
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b

    return f_wb

x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])

# guess the model's w and b parameters to still give you a straight line. The automated way is to use gradient function
w = 200
b = 100
print(f"w: {w}")
print(f"b: {b}")
tmp_f_wb = compute_model_output(x_train, w, b,)

w = 200                         
b = 100
x_i = 1.2
cost_1200sqft = w * x_i + b

print(f"${cost_1200sqft:.0f} thousand dollars")