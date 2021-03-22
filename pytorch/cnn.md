<table class="tfo-notebook-buttons" align="left">
  <td>
    <a target="_blank" href="https://colab.research.google.com/github/sjchoi86/upstage-basic-deeplearning/blob/main/notebook/cnn.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />Colab</a>
  </td>
  <td>
    <a target="_blank" href="https://github.com/sjchoi86/upstage-basic-deeplearning/blob/main/notebook/cnn.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />View Source</a>
  </td>
</table>

# Convolutional Neural Network (CNN)


```python
import torch
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import torch.nn.init
```

    PyTorch version:[1.8.0+cu101].
    device:[cuda:0].
    


```python
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# 랜덤 시드 고정
torch.manual_seed(0)

# GPU 사용시 랜덤 시드 고정
if device =='cuda':
    torch.cuda.manual_seed_all(0)
```

## 파라미터 설정


```python
learning_rate = 0.001
training_epochs = 15
batch_size = 100
```

### Dataset


```python
!wget www.di.ens.fr/~lelarge/MNIST.tar.gz
!tar -zxvf MNIST.tar.gz
```

    --2021-03-22 05:30:24--  http://www.di.ens.fr/~lelarge/MNIST.tar.gz
    Resolving www.di.ens.fr (www.di.ens.fr)... 129.199.99.14
    Connecting to www.di.ens.fr (www.di.ens.fr)|129.199.99.14|:80... connected.
    HTTP request sent, awaiting response... 302 Found
    Location: https://www.di.ens.fr/~lelarge/MNIST.tar.gz [following]
    --2021-03-22 05:30:24--  https://www.di.ens.fr/~lelarge/MNIST.tar.gz
    Connecting to www.di.ens.fr (www.di.ens.fr)|129.199.99.14|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: unspecified [application/x-gzip]
    Saving to: ‘MNIST.tar.gz.1’
    
    MNIST.tar.gz.1          [         <=>        ]  33.20M  5.90MB/s    in 16s     
    
    2021-03-22 05:30:41 (2.08 MB/s) - ‘MNIST.tar.gz.1’ saved [34813078]
    
    MNIST/
    MNIST/raw/
    MNIST/raw/train-labels-idx1-ubyte
    MNIST/raw/t10k-labels-idx1-ubyte.gz
    MNIST/raw/t10k-labels-idx1-ubyte
    MNIST/raw/t10k-images-idx3-ubyte.gz
    MNIST/raw/train-images-idx3-ubyte
    MNIST/raw/train-labels-idx1-ubyte.gz
    MNIST/raw/t10k-images-idx3-ubyte
    MNIST/raw/train-images-idx3-ubyte.gz
    MNIST/processed/
    MNIST/processed/training.pt
    MNIST/processed/test.pt
    


```python
from torchvision import datasets,transforms
from torchvision.datasets import MNIST
mnist_train =  MNIST(root = './', train=True, download=True, transform=transforms.ToTensor())
mnist_test =  MNIST(root = './', train=False, download=True, transform=transforms.ToTensor())
print ("mnist_train:\n",mnist_train,"\n")
print ("mnist_test:\n",mnist_test,"\n")
print ("Done.")
```

    mnist_train:
     Dataset MNIST
        Number of datapoints: 60000
        Root location: ./
        Split: Train
        StandardTransform
    Transform: ToTensor() 
    
    mnist_test:
     Dataset MNIST
        Number of datapoints: 10000
        Root location: ./
        Split: Test
        StandardTransform
    Transform: ToTensor() 
    
    Done.
    

### Data Iterator


```python
data_loader = torch.utils.data.DataLoader(dataset=mnist_train,
                                          batch_size=batch_size,
                                          shuffle=True,
                                          drop_last=True)
```

### Define Model


```python
class CNN(torch.nn.Module):

    def __init__(self):
        super(CNN, self).__init__()
        self.keep_prob = 0.5

        self.layer1 = torch.nn.Sequential(
            torch.nn.Conv2d(1, 32 ,kernel_size = 3, stride = 1, padding = 1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size = 2, stride = 2)
        )

        self.layer2 = torch.nn.Sequential(
            torch.nn.Conv2d(32, 64, kernel_size = 3, stride = 1, padding = 1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size = 2, stride = 2)
        )


        self.layer3 = torch.nn.Sequential(
            torch.nn.Conv2d(64, 128, kernel_size = 3, stride = 1, padding = 1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size = 2, stride = 2,padding = 1)
        )

        self.fc1 = torch.nn.Linear(4*4*128, 625, bias = True)
        torch.nn.init.xavier_uniform_(self.fc1.weight)
        self.layer4 = torch.nn.Sequential(
            self.fc1,
            torch.nn.ReLU(),
            torch.nn.Dropout(p=1 - self.keep_prob)
        )

        self.fc2 = torch.nn.Linear(625,10, bias= True)
        torch.nn.init.xavier_uniform_(self.fc2.weight)

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = self.layer3(out)
        out = out.view(out.size(0), -1)   # Flatten them for FC
        out = self.layer4(out)
        out = self.fc2(out)
        return out
```


```python
model = CNN().to(device)
```

### cost, optimizer define


```python
criterion = torch.nn.CrossEntropyLoss().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)
```

### train


```python
for epoch in range(15):
    avg_cost = 0

    for x,y in data_loader :
        x = x.to(device)
        y = y.to(device)

        optimizer.zero_grad()
        pred_y = model(x)
        cost = criterion(pred_y , y)
        cost.backward()
        optimizer.step()

        avg_cost += cost / len(data_loader)
    print('[Epoch: {:>4}] cost = {:>.9}'.format(epoch + 1, avg_cost))
```

    [Epoch:    1] cost = 0.186150238
    [Epoch:    2] cost = 0.0508896224
    [Epoch:    3] cost = 0.0365535654
    [Epoch:    4] cost = 0.0293492377
    [Epoch:    5] cost = 0.022197146
    [Epoch:    6] cost = 0.018347105
    [Epoch:    7] cost = 0.0163456015
    [Epoch:    8] cost = 0.0124335764
    [Epoch:    9] cost = 0.0120307775
    [Epoch:   10] cost = 0.0106590837
    [Epoch:   11] cost = 0.0114629343
    [Epoch:   12] cost = 0.00945488177
    [Epoch:   13] cost = 0.00725473929
    [Epoch:   14] cost = 0.00894559547
    [Epoch:   15] cost = 0.00592194265
    

## test


```python
with torch.no_grad():
    X_test = mnist_test.test_data.view(len(mnist_test),1,28,28).float().to(device)
    Y_test = mnist_test.test_labels.to(device)

    prediction = model(X_test)
    correct_prediction = torch.argmax(prediction, 1) == Y_test
    accuracy = correct_prediction.float().mean()
    print('정확도 : ', accuracy.item())
```

    정확도 :  0.983299970626831
    

    /usr/local/lib/python3.7/dist-packages/torchvision/datasets/mnist.py:63: UserWarning: test_data has been renamed data
      warnings.warn("test_data has been renamed data")
    /usr/local/lib/python3.7/dist-packages/torchvision/datasets/mnist.py:53: UserWarning: test_labels has been renamed targets
      warnings.warn("test_labels has been renamed targets")
    
