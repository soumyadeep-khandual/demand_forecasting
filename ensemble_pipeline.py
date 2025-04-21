from keras.layers import Dense, Flatten, Input, LSTM
from numpy.typing import NDArray
from sklearn.preprocessing import StandardScaler
from sktime.performance_metrics.forecasting import MeanAbsoluteScaledError


def regressive_predict(model, train_df, num_steps=12, sp=12):
    result = []
    train_df_new = train_df.copy()
    for _ in range(num_steps):
        pred = model.predict(train_df_new[-sp:].reshape(1, sp, 5))
        train_df_new = np.vstack([train_df_new, pred])
        result.append(pred)
    return np.array(result).reshape(num_steps, 5)

def ml_pipeline(df, n_test=12, sp=12, num_steps=12):
    # Train Test Split
    df_train = df[:-n_test].copy()
    df_test = df[-n_test:].copy()
    
    # Normalize
    std = StandardScaler()
    df_train = std.fit_transform(df_train)
    df_test = std.transform(df_test)

    # VAR MODEL
    model_var = VAR(df_train)
    model_var_fit = model.fit(maxlags=sp)
    # model_var_fit.summary()
    result_var = model_var_fit.forecast(
        df_train[-12:],
        steps=12,
    )

    # Neural Network model data prep
    df_train_mlp = np.array(
        [df_train[i - sp - 1 : i] for i in range(sp + 1, len(df_train))]
    )

    df_mlp_x = df_train_mlp[:, :sp, :]
    df_mlp_y = df_train_mlp[:, sp, :]

    # MLP Model
    mlp_forecaster = keras.Sequential(
        layers=[
            Input(shape=(sp, 5)),
            Flatten(),
            Dense(
                256,
                activation=keras.activations.relu,
                # kernel_regularizer=keras.regularizers.L1L2(l1=0.1, l2=0.1),
                # bias_regularizer=keras.regularizers.L1L2(l1=0.1, l2=0.1),
            ),
            Dense(
                128,
                activation=keras.activations.relu,
                # kernel_regularizer=keras.regularizers.L1L2(l1=0.1, l2=0.1),
                # bias_regularizer=keras.regularizers.L1L2(l1=0.1, l2=0.1),
            ),
            Dense(
                5,
                activation=keras.activations.linear,
                # kernel_regularizer=keras.regularizers.L1L2(l1=0.1, l2=0.1),
                # bias_regularizer=keras.regularizers.L1L2(l1=0.1, l2=0.1),
            ),
        ],
        trainable=True,
        name="mpl_forecaster",
    )
    mlp_forecaster.compile(
    optimizer=keras.optimizers.AdamW(learning_rate=3e-3),
    loss=keras.losses.mean_squared_error,
    )
    mlp_train_hist = mlp_forecaster.fit(
    df_mlp_x, df_mlp_y, epochs=100, validation_split=0.2
    )
    result_mlp = regressive_predict(
        mlp_forecaster, 
        df_train, 
        num_steps=num_steps, 
        sp=sp,
    )
    
    # LSTM Model
    lstm_forecaster = keras.Sequential(
        layers=[
            Input(shape=(LAG, 5)),
            LSTM(128),
            Dense(64, activation=keras.activations.relu),
            Dense(5, activation=keras.activations.linear),
        ],
        trainable=True,
        name="lstm_forecaster",
    )    
    lstm_forecaster.compile(
        optimizer=keras.optimizers.AdamW(learning_rate=1e-2),
        loss=keras.losses.mean_squared_error,
        metrics=[keras.metrics.RootMeanSquaredError],
    )
    lstm_forecaster_hist = lstm_forecaster.fit(
        df_mlp_x, df_mlp_y, epochs=100, validation_split=0.2
    )
    result_lstm = regressive_predict(
        lstm_forecaster, 
        df_train, 
        num_steps=12, 
        sp=12,
    )
    mase = MeanAbsoluteScaledError(sp=12)
    mase_var = mase(df_test[:,0], result_var[:,0], y_train=df_train[:,0])
    mase_mlp = mase(df_test[:,0], result_mlp[:,0], y_train=df_train[:,0])
    mase_lstm = mase(df_test[:,0], result_lstm[:,0], y_train=df_train[:,0])
    losses = np.array([mase_var, mase_mlp, mase_lstm])
    loss_inv = 1 / losses
    weight = loss_inv / sum(loss_inv)
    result_ensemble = (
        result_var*weight[0]
        +result_mlp*weight[1]
        +result_lstm*weight[2]
    )
    mase_ensemble = mase(
        df_test[:,0], 
        result_ensemble[:,0], 
        y_train=df_train[:,0]
    )

    return {
        "var":{
            "result": result_var,
            "mase": mase_var,
        },
        "mlp":{
            "result": result_mlp,
            "mase": mase_mlp,
        },
        "lstm":{
            "result": result_lstm,
            "mase": mase_lstm
        },
        "ensemble":{
            "result": result_ensemble,
            "mase": mase_ensemble
        }
    }