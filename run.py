

import argparse
import subprocess


ckp = 'pretrained/mobilenetv2_1.0-0c6065bc.pth'
name = 'rldr-md'

for i in range(9):
    p = subprocess.Popen(' '.join(['python',
                                   'imagenet.py',
                                   '-a mobilenetv2',
                                   '-d /home/dl/DATA/ImageNet/ILSVRC/Data/CLS-LOC',
                                   '--weight '+ckp,
                                   '--width-mult 1.0',
                                   '--input-size 224',
                                   '--status prune',
                                   '--method rldr',
                                   '--ckp_out ./checkpoints/'+name+'-'+str(i)+'.pth']), shell=True)
    p.wait()
    ckp = './checkpoints/'+name+'-'+str(i)+'.pth'
    p = subprocess.Popen(' '.join(['python',
                                   'imagenet.py',
                                   '-a mobilenetv2',
                                   '-d /home/dl/DATA/ImageNet/ILSVRC/Data/CLS-LOC',
                                   '--weight ' + ckp,
                                   '--width-mult 1.0',
                                   '--input-size 224',
                                   '--status train',
                                   '--ckp_out ' + ckp]), shell=True)
    p.wait()
