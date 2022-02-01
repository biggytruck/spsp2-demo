from shutil import copyfile
import os

pre = '/home/biggytruck/Github/vc_workspace/SpeechSplit/result/'
result_dirs = ['spsp1/R_8_1/', 'spsp1/R_1_32/', 'spsp2/R_8_1/', 'spsp2/R_1_32/']
models = ['spsp1-s', 'spsp1-l', 'spsp2-s', 'spsp2-l']

with open('./demo.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line_s = line.strip()
        if line_s in ['F', 'R', 'U']:
            key = line_s
        elif line_s != '':
            a, b, c = line_s.split('_')
            fname = '_'.join([a, c, b, c])
            copyfile(os.path.join(pre, 'spsp1/R_8_1/', key, fname+'_s.wav'), os.path.join('./assets/audios', key, fname+'_s.wav'))
            copyfile(os.path.join(pre, 'spsp1/R_8_1/', key, fname+'_t.wav'), os.path.join('./assets/audios', key, fname+'_t.wav'))
            for result_dir, model in zip(result_dirs, models):
                src = os.path.join(pre, result_dir, key, fname+'_c.wav')
                tgt = os.path.join('./assets/audios', key, fname+f'_{model}.wav')
                copyfile(src, tgt)
