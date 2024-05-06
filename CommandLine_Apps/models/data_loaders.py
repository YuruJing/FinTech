import torch
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split


# create train and test data loaders
def create_loaders(new_data, sequence_length=30, test_size=0.25, batch_size=32):
    tickers = new_data.columns.get_level_values(0).unique().to_list()
    # preprocess the data
    inputs = {}
    targets = {}
    for t in tickers:
        inputs[t] = []
        targets[t] = []
        for i in range(sequence_length, len(new_data)):  # stride, window size =1
            inputs[t].append(torch.tensor(new_data[t].iloc[i - sequence_length:i, :-1].values).float())
            targets[t].append(torch.tensor(new_data[t].iloc[i, -1]).float())

    # split the data into training and testing sets
    X_train, X_test, y_train, y_test = {}, {}, {}, {}
    for t in tickers:
        X_train[t], X_test[t], y_train[t], y_test[t] = train_test_split(inputs[t], targets[t], test_size=test_size,
                                                                        shuffle=False)

    # create dataloaders
    train_dataloaders = {}
    test_dataloaders = {}
    for t in tickers:
        train_dataloaders[t] = DataLoader(TensorDataset(torch.stack(X_train[t], dim=0), torch.Tensor(y_train[t])),
                                          batch_size=batch_size, shuffle=True)
        test_dataloaders[t] = DataLoader(TensorDataset(torch.stack(X_test[t], dim=0), torch.Tensor(y_test[t])),
                                         batch_size=batch_size)
