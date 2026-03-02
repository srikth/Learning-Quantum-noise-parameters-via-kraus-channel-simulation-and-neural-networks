import torch
import torch.optim as optim
import torch.nn as nn
import matplotlib.pyplot as plt
from dataset_generator import generate_dataset
from model import NoiseRegressor
from sklearn.model_selection import train_test_split

# Generate data
X, y = generate_dataset(samples=3000)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)

X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32).view(-1, 1)

model = NoiseRegressor()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

epochs = 100
losses = []

for epoch in range(epochs):
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()

    losses.append(loss.item())

    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.6f}")

# Evaluate
with torch.no_grad():
    predictions = model(X_test)
    test_loss = criterion(predictions, y_test)
    print("\nTest MSE:", test_loss.item())

# Plot loss
plt.plot(losses)
plt.xlabel("Epoch")
plt.ylabel("Training Loss")
plt.title("Training Loss Curve")
plt.show()
