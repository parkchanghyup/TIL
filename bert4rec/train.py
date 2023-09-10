def train(model, criterion, optimizer, data_loader, device):
    """
    모델을 학습하는 함수

    Args:
        model : 학습할 모델
        criterion
        optimizer
        data_loader
        device

    Returns:
        loss_val : 현재 loss
        model : 학습 된 모델
    """

    model.train()
    loss_val = 0
    for idx, (seq, labels) in enumerate(data_loader):
        logits = model(seq)

        logits = logits.view(-1, logits.size(-1))
        labels = labels.view(-1).to(device)

        optimizer.zero_grad()
        loss = criterion(logits, labels)

        loss_val += loss.item()

        loss.backward()
        optimizer.step()

    loss_val /= len(data_loader)

    return loss_val, model
