
import LVX_File_Struct
class LVX_Reader:
    def __init__(self):
        self.public_header = LvxFilePublicHeader()
        self.private_header = LvxFilePrivateHeader()
        self.device_info_list = [] # of LvxDeviceInfo()

