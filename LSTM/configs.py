import argparse


def set_args():
    # 创建ArgumentParser()对象，并为参数解析器赋予一个名字
    parser = argparse.ArgumentParser(description="model parameter")

    # 调用add_argument()方法添加参数
    # parser.add_argument('--random_seed', type=int, default=42, help="random seed")
    # parser.add_argument('--name', default="Cat2eacher", help="Coder Name")
    # 数据集相关参数
    parser.add_argument('--dataset_path',
                        default=r"../HARdataset/dataset.csv", type=str, help='file path')
    # 训练相关参数
    parser.add_argument('--device', type=str, default="cpu", help='training device')
    parser.add_argument('--batch_size', type=int, default=32, help='input batch size')
    parser.add_argument('--epochs', type=int, default=30, help='number of epochs to train')
    parser.add_argument('--lr', type=float, default=0.001, help='select the learning rate')
    parser.add_argument('--time_step', type=int, default=10, help='time step')
    parser.add_argument('--output_size', type=int, default=4, help='output size for Dense')
    parser.add_argument('--save_model', type=str, default=r"../checkpoints/", help='model save path')

    # 使用parse_args()解析参数
    args = parser.parse_args()
    return args
