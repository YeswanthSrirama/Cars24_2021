import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
import warnings
warnings.filterwarnings(action = 'ignore')
from sklearn.metrics import r2_score, accuracy_score
from xgboost import XGBRegressor


class Code:
    def __init__(self):
        self.data = pd.read_csv(r'Cars24.csv')


    def brand():
        return(tuple(data['Car Brand'].unique()))

    def model(item):
        return(data[data['Car Brand']==item]['Model'].unique())

    def location():
        return(tuple(data['Location'].unique()))

    def gear():
        return(tuple(data['Gear'].unique()))

    def fuel():
        return(tuple(data['Fuel'].unique()))

    def predict(input):
        df=data
        df = df.drop(['Unnamed: 0','EMI (monthly)'],axis=1)
        df.drop(df[df.Price>1500000].index, axis=0, inplace=True)

        df = df.dropna(axis=0)
        df = pd.concat([df,input], ignore_index=True)
        output = df.tail(1)
        print(input)

        df=pd.get_dummies(df, columns=["Location",'Fuel','Car Brand'],drop_first=True)

        encoder = LabelEncoder()
        objects = []
        for i in df.columns:
            if df[i].dtype == 'object':
                objects.append(i)
        encoder = LabelEncoder()
        encoder_list = []
        for i in objects:
            print(i)
            encoder.fit(df[i])
            encoder_list.append(encoder.classes_)
            df[i] = encoder.transform(df[i])
        df['Model Year'] = 2021 - df['Model Year']
        print('encoded the labels')
        x=df.drop(['Price'],axis=1)
        y=df['Price']
        x_testing = x.iloc[-1:]

        x.drop(x.tail(1).index, inplace=True)
        y.drop(x.tail(1).index,inplace=True)

        x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)
        print('train_test split done')
        model = XGBRegressor(max_depth=5,max_leaves=2,n_estimators=800, learning_rate=0.2)
        print('fitting the model')
        model.fit(x_train,y_train)
        print('model_fit completed')
        output['Price'] = model.predict(x_testing).astype('float')
        return output['Price']


data = pd.read_csv(r'Cars24.csv')

