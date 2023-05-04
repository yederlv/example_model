#%%
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

#%%
# Carga de datos
df = pd.read_csv("https://raw.githubusercontent.com/acosta187/datos/main/brain_stroke.csv")

#%%
# Convertir 'stroke' (target) en valores binarios
df['stroke'] = df['stroke'].replace({'No': 0, 'Yes': 1})

#%%
# Variables categóricas y numéricas
char_var = ['gender', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
num_var = ['age', 'avg_glucose_level', 'bmi']

#%%
# Preprocesamiento de datos
full_pipeline = ColumnTransformer([
    ("num", preprocessing.MinMaxScaler(), num_var),
    ("cat", OneHotEncoder(handle_unknown='ignore'), char_var)
])

#%%
X = full_pipeline.fit_transform(df)
y = df.stroke

#%%
# Separar los datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#%%
# Modelo XGBoost
#xgb_model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')

xgb_model = XGBClassifier(random_state=153468)

# Entrenar el modelo con los datos de entrenamiento
xgb_model.fit(X_train, y_train)

# Hacer predicciones con los datos de prueba
y_pred = xgb_model.predict(X_test)

# Evaluar el modelo
from sklearn.metrics import accuracy_score

print('Accuracy:', accuracy_score(y_test, y_pred))