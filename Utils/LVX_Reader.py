
from LVX_File_Struct import *

class LVX_Reader:
    def __init__(self):
        self.public_header = LvxFilePublicHeader()
        self.private_header = LvxFilePrivateHeader()
        self.device_info_list = [] # of LvxDeviceInfo()

        self.frame_header = FrameHeader()
        self.base_pack_detail = BasePackDetail()

    def ReadStruct(self, struct):
        raw = self.f.read(len(struct))
        struct.unpack(raw)


    def open(self, lvx_fn):
        self.f = open(lvx_fn,'rb')

        self.ReadStruct(self.public_header)
        self.ReadStruct(self.private_header)

        for i in range(self.private_header.device_count):
            device_info = LvxDeviceInfo()
            self.ReadStruct(device_info)
            self.device_info_list.append(device_info)

    def ReadFrame(self):
        self.ReadStruct(self.frame_header)
        self.ReadStruct(self.base_pack_detail)

    def close(self):
        self.f.close()

if __name__ == "__main__":
    lvx_file = LVX_Reader()
    lvx_file.open('../lvx/2021-02-05_11-57-52.lvx')

    while(True):
        lvx_file.ReadFrame()
        if not frm:
            break

    lvx_file.close()
    a = 4