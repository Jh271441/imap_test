# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/map/proto/vehicle_id.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"modules/map/proto/vehicle_id.proto\x12\rapollo.common\"@\n\tVehicleID\x12\x0b\n\x03vin\x18\x01 \x01(\t\x12\r\n\x05plate\x18\x02 \x01(\t\x12\x17\n\x0fother_unique_id\x18\x03 \x01(\t')



_VEHICLEID = DESCRIPTOR.message_types_by_name['VehicleID']
VehicleID = _reflection.GeneratedProtocolMessageType('VehicleID', (_message.Message,), {
  'DESCRIPTOR' : _VEHICLEID,
  '__module__' : 'modules.map.proto.vehicle_id_pb2'
  # @@protoc_insertion_point(class_scope:apollo.common.VehicleID)
  })
_sym_db.RegisterMessage(VehicleID)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VEHICLEID._serialized_start=53
  _VEHICLEID._serialized_end=117
# @@protoc_insertion_point(module_scope)
