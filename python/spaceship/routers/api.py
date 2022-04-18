from itertools import product
import json
from fastapi import APIRouter
import numpy as np

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get('/matrix')
def randMatrix() -> dict:
    matrix1 = np.random.rand(10, 10)
    matrix2 = np.random.rand(10, 10)
    product = np.matmul(matrix1, matrix2)
    return {
        "matrix1": json.dumps(matrix1.tolist()),
        "matrix2": json.dumps(matrix2.tolist()),
        "product": json.dumps(product.tolist())
    }
