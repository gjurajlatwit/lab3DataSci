from sklearn import linear_model
import pandas as pd
from joblib import dump, load 

X = pd.read_csv('pong_data.csv')
y = X['paddle_direction']
X = X[['ball_x','ball_y','ball_vx','ball_vy']]

model = linear_model.LinearRegression()
model.fit(X,y)
print(model.coef_)
dump(model, 'mymodel.joblib')