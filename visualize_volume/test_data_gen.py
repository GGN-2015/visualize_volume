import numpy as np

def create_centered_cube_3d(array_shape: tuple, cube_size: int) -> np.ndarray:
    """
    创建一个3D NumPy数组，在正中间生成值为-1的立方体，其余区域为0
    
    参数：
        array_shape: 3D数组的形状，格式为 (depth, height, width)
        cube_size: 立方体的边长（需小于等于数组各维度的大小）
    
    返回：
        3D ndarray，中间立方体值为-1，其余为0
    """
    # 校验输入合法性
    if len(array_shape) != 3:
        raise ValueError("array_shape 必须是3维元组 (depth, height, width)")
    if cube_size <= 0 or any(cube_size > dim for dim in array_shape):
        raise ValueError(f"立方体边长 {cube_size} 必须大于0且小于等于数组各维度大小 {array_shape}")
    
    # 1. 创建全0的3D数组
    volume = np.zeros(array_shape, dtype=np.int8)
    
    # 2. 计算数组中心点坐标（每个维度的中心索引）
    center_depth, center_height, center_width = (dim // 2 for dim in array_shape)
    
    # 3. 计算立方体在各维度的起止索引（保证立方体居中）
    # 起始索引 = 中心点 - 立方体边长//2
    # 结束索引 = 起始索引 + 立方体边长
    start_d = center_depth - cube_size // 2
    end_d = start_d + cube_size
    start_h = center_height - cube_size // 2
    end_h = start_h + cube_size
    start_w = center_width - cube_size // 2
    end_w = start_w + cube_size
    
    # 4. 给立方体区域赋值为-1
    volume[start_d:end_d, start_h:end_h, start_w:end_w] = -1
    
    return volume
