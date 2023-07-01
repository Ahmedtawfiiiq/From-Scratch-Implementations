import matplotlib.pyplot as plt
import pandas as pd
import torch
import numpy as np
import seaborn as sns
from torch.utils.data import Dataset, DataLoader
from torch import nn
from torch import optim
import itertools
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    accuracy_score,
)
from sklearn.preprocessing import LabelEncoder

if torch.cuda.is_available():
    dev = "cuda:0"
else:
    dev = "cpu"
device = torch.device(dev)
print(device)

input_dim = 10
output_dim = 1
num_epochs = 15
batch_size = 128
learn_rate = 0.0001


class Data(Dataset):
    def __init__(self, X, y):
        self.X = torch.from_numpy(X.astype(np.float32)).float().to(device)
        self.y = torch.from_numpy(y.astype(np.float32)).float().to(device)
        self.len = self.X.shape[0]

    def __getitem__(self, index):
        return self.X[index], self.y[index]

    def __len__(self):
        return self.len


class NeuralNetwork(nn.Module):
    def __init__(self, input_dim, hidden_dim1, hidden_dim2, output_dim):
        super(NeuralNetwork, self).__init__()
        self.layer_1 = nn.Linear(input_dim, hidden_dim1)
        self.layer_2 = nn.Linear(hidden_dim1, hidden_dim2)
        self.layer_3 = nn.Linear(hidden_dim2, output_dim)

    def forward(self, x):
        x = torch.relu(self.layer_1(x))
        x = torch.relu(self.layer_2(x))
        x = torch.sigmoid(self.layer_3(x))

        return x


df = pd.read_csv("dataset/telescope_data.csv", index_col=0)
g_count = df["class"].value_counts()["g"]
h_count = df["class"].value_counts()["h"]
g_df = df[df["class"] == "g"].sample(h_count)
h_df = df[df["class"] == "h"]
balanced_df = pd.concat([g_df, h_df])
# apply label encoder to balanced dataframe
label_encoder = LabelEncoder()
balanced_df["class"] = label_encoder.fit_transform(balanced_df["class"])

train_df, test_df = balanced_df.sample(frac=0.7), balanced_df.drop(
    balanced_df.sample(frac=0.7).index
)

g70, h70 = train_df[train_df["class"] == 0], train_df[train_df["class"] == 1]

# convert dataframe values to list
g70 = g70.values.tolist()
h70 = h70.values.tolist()

# split data into 10 folds
k_fold = []

for i in range(0, 4):
    k_fold.append(g70[i * 936 : i * 936 + 936] + h70[i * 936 : i * 936 + 936])

k_fold.append(g70[3744:4682] + h70[3744:4682])

print(len(k_fold[0]))
print(len(k_fold[1]))
print(len(k_fold[2]))
print(len(k_fold[3]))
print(len(k_fold[4]))


def getTrain(k_fold, k):
    train = []
    for i in range(0, 5):
        if k == i:
            continue
        train = train + k_fold[i]

    return train


def calculate_accuracy(y_true, y_pred):
    predicted = y_pred.ge(0.5).view(-1)
    return (y_true == predicted).sum().float() / len(y_true)


def round_tensor(t, decimal_places=5):
    return round(t.item(), decimal_places)


# start cross validation

ans = []
loss_fn = nn.BCELoss()
for i in range(1, 100, 10):
    tempRow = []
    for j in range(1, 100, 10):
        acc = 0
        if (j - i <= 30 and j >= i) or (j - i >= -30 and j <= i):
            for k in range(0, 5):
                vld = pd.DataFrame(k_fold[k])
                trn = pd.DataFrame(getTrain(k_fold, k))
                X_vld = vld.iloc[:, :-1].values
                y_vld = vld.iloc[:, -1].values

                X_trn = trn.iloc[:, :-1].values
                y_trn = trn.iloc[:, -1].values

                scaler = StandardScaler()
                scaler.fit(X_trn)
                X_trn = scaler.transform(X_trn)
                X_vld = scaler.transform(X_vld)

                train_data = Data(X_trn, y_trn)
                train_dataloader = DataLoader(
                    dataset=train_data, batch_size=batch_size, shuffle=False
                )

                test_data = Data(X_vld, y_vld)
                test_dataloader = DataLoader(
                    dataset=test_data, batch_size=batch_size, shuffle=False
                )

                tempModel = NeuralNetwork(10, i, j, 1)
                tempModel = tempModel.to(device)
                optimizer = torch.optim.Adam(tempModel.parameters())

                tempModel.train()
                for epoch in range(50):
                    for X, y in train_dataloader:
                        optimizer.zero_grad()
                        X = X.to(device)
                        y = y.to(device)
                        pred = tempModel(X)
                        loss = loss_fn(pred, y.unsqueeze(-1))
                        loss.backward()
                        optimizer.step()

                accTemp = 0
                for X, y in test_dataloader:
                    X = X.to(device)
                    y = y.to(device)
                    pred = tempModel(X)
                    pred = torch.squeeze(pred)
                    accTemp += round_tensor(calculate_accuracy(y, pred))

                accTemp = accTemp / 15
                acc = acc + accTemp

            acc = acc / 5
        else:
            acc = 0

        tempRow.append(acc)
        print("i = ", i, "j = ", j, acc, tempRow)

    ans.append(tempRow)

print(ans)
print(device)

labels = ["1", "11", "21", "31", "41", "51", "61", "71", "81", "91"]
df_cm = pd.DataFrame(ans, index=labels, columns=labels)
plt.figure(figsize=(16, 6))
hmap = sns.heatmap(df_cm, annot=True, fmt="f")
hmap.yaxis.set_ticklabels(hmap.yaxis.get_ticklabels(), rotation=0, ha="right")
hmap.xaxis.set_ticklabels(hmap.xaxis.get_ticklabels(), rotation=30, ha="right")
plt.ylabel("hidden_layer1")
plt.xlabel("hidden_layer2")

hidd1 = 0
hidd2 = 0
maxAcc = ans[0][0]
for i in range(10):
    for j in range(10):
        if ans[i][j] > maxAcc:
            maxAcc = ans[i][j]
            hidd1 = i
            hidd2 = j
hidd1 = 1 + hidd1 * 10
hidd2 = 1 + hidd2 * 10
print(hidd1, hidd2)

hidden_dim1 = hidd1
hidden_dim2 = hidd2
print(hidden_dim1)
print(hidden_dim2)

"""# **Training preparation**"""

# read data
trainingSet = pd.read_csv("../../finalData/training.csv")
testingSet = pd.read_csv("../../finalData/testing.csv")

# training data
x_train = trainingSet.iloc[:, :-1].values  # features
y_train = trainingSet.iloc[:, -1].values  # labels
x_test = testingSet.iloc[:, :-1].values  # features
y_test = testingSet.iloc[:, -1].values  # labels

scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

train_data = Data(x_train, y_train)
train_dataloader = DataLoader(dataset=train_data, batch_size=batch_size, shuffle=False)

test_data = Data(x_test, y_test)
test_dataloader = DataLoader(dataset=test_data, batch_size=batch_size, shuffle=False)

"""## Model creation"""

model = NeuralNetwork(input_dim, hidden_dim1, hidden_dim2, output_dim)
model = model.to(device)

loss_fn = nn.BCELoss()

optimizer = torch.optim.Adam(model.parameters())

"""## Start training"""

loss_values = np.array([])

for epoch in range(num_epochs):
    for X, y in train_dataloader:
        optimizer.zero_grad()
        X = X.to(device)
        y = y.to(device)
        pred = model(X)
        loss = loss_fn(pred, y.unsqueeze(-1))
        loss_values = np.append(loss_values, loss.item())
        loss.backward()
        optimizer.step()
    print(f"Epoch num {epoch}")
    print("--------------------------")

print("Training Complete")

step = np.linspace(0, num_epochs, loss_values.shape[0])

fig, ax = plt.subplots(figsize=(20, 12))
plt.plot(step, loss_values)
plt.title("Step-wise Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.show()

"""## Start testing"""

num_correct = 0
num_samples = 0
y_pred = np.array([])

model.eval()
with torch.no_grad():
    for X, y in test_dataloader:
        X = X.to(device)
        y = y.to(device)
        outputs = model(X)
        predicted = np.where(outputs.cpu().data.numpy() <= 0.5, 0, 1)
        predicted = list(itertools.chain(*predicted))
        y_pred = np.append(y_pred, predicted)
        num_correct += (predicted == y.cpu().data.numpy()).sum().item()
        num_samples += y.size(0)
print(
    f"Correct = {num_correct} and total = {num_samples} then accuracy = {100* num_correct // num_samples}%"
)

"""# Statistics"""

print(classification_report(torch.from_numpy(y_test), torch.from_numpy(y_pred)))

cm = confusion_matrix(y_test, y_pred)

labels = ["h", "g"]
columns = [f"Predicted {label}" for label in labels]
index = [f"Actual {label}" for label in labels]
table = pd.DataFrame(cm, columns=columns, index=index)
table

acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
specificity = cm[0, 0] / (cm[0, 0] + cm[0, 1])
f1 = f1_score(y_test, y_pred)

print("model_accuracy = ", acc)
print("model_precision = ", prec)
print("model_recall = ", recall)
print("model_specificity = ", specificity)
print("model_f1 = ", f1)
