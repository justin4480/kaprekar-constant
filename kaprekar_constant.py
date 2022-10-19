import numpy as np
import pandas as pd

def kaprekar_constant():
    results = {}
    for i in np.arange(1_000, 10_000, 1):
        start_num = i
        iterations = 0
        while True:
            a = int(''.join(np.sort([j for j in str(i)])[::-1]))
            b = int(''.join(np.sort([j for j in str(i)])))
            if i == a - b:
                results[start_num] = {
                    'answer': a - b,
                    'iterations': iterations,
                    'unique': len(np.unique([i for i in str(start_num)])),
                }
                break
            else:
                i = a - b
                i = i if i >= 1000 else i * 10
                iterations += 1

    df = pd.DataFrame.from_dict(results, orient='index')
    unique, count = np.unique(ar=df.answer, return_counts=True)
    print(f'n={len(results)}')
    print(f'{count[1]} x {unique[1]} {df.loc[df.answer == 6174].index.values}')
    print(f'{count[0]} x {unique[0]} {df.loc[df.answer == 0].index.values}')
    (
        df
        .loc[df.answer == 6174, 'iterations']
        .value_counts()
        .sort_index()
        .plot(kind='bar')
        .set_title('Iterations to convergence')
    );

if __name__ == '__main__':
    kaprekar_constant()