from seq_exp import *


if __name__ == "__main__":
        pre_load = None #Set this to path to saved dstcae_c3d model

        if pre_load == None:
                print('No model path given, please update pre_load variable in dstcae_c3d_main_test.py')

        else:
                img_width, img_height, win_len = 64,64,2
                
                dset = 'Thermal-Dummy'
                img_width, img_height = 64,64

                clstm_ae_exp = SeqExp(dset = dset, pre_load = pre_load, img_width = img_width, \
                        img_height = img_height, win_len = win_len)


                clstm_ae_exp.test(animate = True)




























































































































































