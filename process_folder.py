import argparse
import os
import multiprocessing
from functools import partial

import cv2

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--i", type=str, default='./', help='Directory with the .svs files')
    parser.add_argument("--o", type=str, default='./', help='Directory to store the .jpg outputs')
    parser.add_argument("--num_procs", type=int, default=1, help='Number of processes')
    #other arguments you may have

    return parser.parse_args()

def pipeline_single_image(fn, args):
    img = cv2.imread(os.path.join(args.i, fn))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #do the processing of a single image
    return fn

def main(args):
    os.makedirs(args.o, exist_ok = True)
    pool = multiprocessing.Pool(args.num_procs)
    files = [f for f in os.listdir(args.i)]
    files = pool.map(partial(pipeline_single_image, args=args), files)
    pool.close()
    pool.join()

if __name__ == '__main__':
    args = get_args()
    main(args)
