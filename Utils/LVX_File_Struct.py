
import struct
kMaxPointSize = 1500

"""
 LVX file :

     # LvxFilePublicHeader:

         typedef struct {
          uint8_t signature[16];
          uint8_t version[4];
          uint32_t magic_code;
        } LvxFilePublicHeader;
"""
class LvxFilePublicHeader:

    def __init__(self):
        self.signature =[]
        self .version = []
        self.magic_code  = 0
        self.s = struct.Struct('16B 4B I')

    def __len__(self):
        return self.s.size

    def unpack(self, raw):
        v = self.s.unpack(raw)
        self.signature = v[:16]
        self.version = v[16:20]
        self.magic_code = v[20]

"""     
    # LvxFilePrivateHeader

        typedef struct {
          uint32_t frame_duration;
          uint8_t device_count;
        } LvxFilePrivateHeader;
        """

class LvxFilePrivateHeader:

    def __init__(self):
        self.frame_duration  = 0
        self.device_count  = 0
        self.s = struct.Struct('I B')

    def __len__(self):
        return self.s.size

    def unpack(self, raw):
        v = self.s.unpack(raw)
        self.frame_duration = v[0]
        self.device_count = v[1]


"""
    #  LvxDeviceInfo                for each device
        typedef struct {
          uint8_t lidar_broadcast_code[16];
          uint8_t hub_broadcast_code[16];
          uint8_t device_index;
          uint8_t device_type;
          uint8_t extrinsic_enable;
          float roll;
          float pitch;
          float yaw;
          float x;
          float y;
          float z;
        } LvxDeviceInfo;
"""
class LvxDeviceInfo:

    def __init__(self):
        self.lidar_broadcast_code  = []
        self.hub_broadcast_code  = []
        self.device_index = 0
        self.device_type = 0
        self.extrinsic_enable = 0
        self.roll = 0
        self.pitch = 0
        self.yaw = 0
        self.x = 0
        self.y = 0
        self.z = 0

        self.s = struct.Struct('16B 16B 3B 6f')

    def __len__(self):
        return self.s.size

    def unpack(self, raw):
        v = self.s.unpack(raw)
        self.lidar_broadcast_code = v[0:16]
        self.hub_broadcast_code = v[16:32]
        self.device_index = v[32]
        self.device_type = v[33]
        self.extrinsic_enable = v[34]
        self.roll = v[35]
        self.pitch = v[36]
        self.yaw = v[37]
        self.x = v[38]
        self.y = v[39]
        self.z = v[40]


"""



typedef struct {
  uint64_t current_offset;
  uint64_t next_offset;
  uint64_t frame_index;
} FrameHeader;



  """
class FrameHeader:

    def __init__(self):
        self.current_offset  = 0
        self.next_offset  = 0
        self.frame_index  = 0
        self.s = struct.Struct('3Q')

    def __len__(self):
        return self.s.size

    def unpack(self, raw):
        v = self.s.unpack(raw)
        self.current_offset  = v[0]
        self.next_offset  = v[1]
        self.frame_index  = v[2]

"""
#define kMaxPointSize 1500

typedef struct {
  uint8_t device_index;
  uint8_t version;
  uint8_t port_id;
  uint8_t lidar_index;
  uint8_t rsvd;
  uint32_t error_code;
  uint8_t timestamp_type;
  uint8_t data_type;
  uint8_t timestamp[8];
  uint8_t raw_point[kMaxPointSize];
  uint32_t pack_size;
} LvxBasePackDetail;
"""

class BasePackDetail:

    def __init__(self):
        self.device_index  = 0
        self.version = 0
        self.port_id = 0
        self.lidar_index = 0
        self.rsvd = 0
        self.error_code = 0
        self.timestamp_type = 0
        self.data_type = 0
        self.timestamp = []
        self.raw_point = []
        self.pack_size = 0
        self.s = struct.Struct(f'5B I 2B 8B {kMaxPointSize}B I')

    def __len__(self):
        return self.s.size

    def unpack(self, raw):
        v = self.s.unpack(raw)
        self.device_index  = v[0]
        self.version = v[1]
        self.port_id = v[2]
        self.lidar_index = v[3]
        self.rsvd = v[4]
        self.error_code = v[5]
        self.timestamp_type = v[6]
        self.data_type = v[7]
        self.timestamp = v[8:16]
        self.raw_point = v[16:(16+kMaxPointSize)]
        self.pack_size = v[16+kMaxPointSize]


