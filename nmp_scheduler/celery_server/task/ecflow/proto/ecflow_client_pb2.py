# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ecflow_client.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ecflow_client.proto',
  package='ecflow_client',
  syntax='proto3',
  serialized_options=_b('Z\014ecflowclient'),
  serialized_pb=_b('\n\x13\x65\x63\x66low_client.proto\x12\recflow_client\"9\n\x0eResponseStatus\x12\x11\n\thas_error\x18\x01 \x01(\x08\x12\x14\n\x0c\x65rror_string\x18\x02 \x01(\t\"H\n\rStatusRequest\x12\r\n\x05owner\x18\x01 \x01(\t\x12\x0c\n\x04repo\x18\x02 \x01(\t\x12\x0c\n\x04host\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\t\"\x84\x02\n\x15StatusRecordsResponse\x12\r\n\x05owner\x18\x01 \x01(\t\x12\x0c\n\x04repo\x18\x02 \x01(\t\x12\x1b\n\x13\x63ollected_timestamp\x18\x03 \x01(\x03\x12G\n\nstatus_map\x18\x04 \x03(\x0b\x32\x33.ecflow_client.StatusRecordsResponse.StatusMapEntry\x12\x36\n\x0fresponse_status\x18\x05 \x01(\x0b\x32\x1d.ecflow_client.ResponseStatus\x1a\x30\n\x0eStatusMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x92\x01\n\x0eStatusResponse\x12\r\n\x05owner\x18\x01 \x01(\t\x12\x0c\n\x04repo\x18\x02 \x01(\t\x12\x1b\n\x13\x63ollected_timestamp\x18\x03 \x01(\x03\x12\x0e\n\x06status\x18\x04 \x01(\t\x12\x36\n\x0fresponse_status\x18\x05 \x01(\x0b\x32\x1d.ecflow_client.ResponseStatus\"T\n\x0bNodeRequest\x12\r\n\x05owner\x18\x01 \x01(\t\x12\x0c\n\x04repo\x18\x02 \x01(\t\x12\x0c\n\x04host\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\t\x12\x0c\n\x04path\x18\x05 \x01(\t\"\x7f\n\x0cNodeResponse\x12\r\n\x05owner\x18\x01 \x01(\t\x12\x0c\n\x04repo\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x0c\n\x04node\x18\x04 \x01(\t\x12\x36\n\x0fresponse_status\x18\x05 \x01(\x0b\x32\x1d.ecflow_client.ResponseStatus2\x8d\x02\n\x13\x45\x63\x66lowClientService\x12\\\n\x14\x43ollectStatusRecords\x12\x1c.ecflow_client.StatusRequest\x1a$.ecflow_client.StatusRecordsResponse\"\x00\x12N\n\rCollectStatus\x12\x1c.ecflow_client.StatusRequest\x1a\x1d.ecflow_client.StatusResponse\"\x00\x12H\n\x0b\x43ollectNode\x12\x1a.ecflow_client.NodeRequest\x1a\x1b.ecflow_client.NodeResponse\"\x00\x42\x0eZ\x0c\x65\x63\x66lowclientb\x06proto3')
)




_RESPONSESTATUS = _descriptor.Descriptor(
  name='ResponseStatus',
  full_name='ecflow_client.ResponseStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='has_error', full_name='ecflow_client.ResponseStatus.has_error', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_string', full_name='ecflow_client.ResponseStatus.error_string', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=95,
)


_STATUSREQUEST = _descriptor.Descriptor(
  name='StatusRequest',
  full_name='ecflow_client.StatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='ecflow_client.StatusRequest.owner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo', full_name='ecflow_client.StatusRequest.repo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='ecflow_client.StatusRequest.host', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='ecflow_client.StatusRequest.port', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=169,
)


_STATUSRECORDSRESPONSE_STATUSMAPENTRY = _descriptor.Descriptor(
  name='StatusMapEntry',
  full_name='ecflow_client.StatusRecordsResponse.StatusMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ecflow_client.StatusRecordsResponse.StatusMapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ecflow_client.StatusRecordsResponse.StatusMapEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=384,
  serialized_end=432,
)

_STATUSRECORDSRESPONSE = _descriptor.Descriptor(
  name='StatusRecordsResponse',
  full_name='ecflow_client.StatusRecordsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='ecflow_client.StatusRecordsResponse.owner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo', full_name='ecflow_client.StatusRecordsResponse.repo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collected_timestamp', full_name='ecflow_client.StatusRecordsResponse.collected_timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status_map', full_name='ecflow_client.StatusRecordsResponse.status_map', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response_status', full_name='ecflow_client.StatusRecordsResponse.response_status', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STATUSRECORDSRESPONSE_STATUSMAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=432,
)


_STATUSRESPONSE = _descriptor.Descriptor(
  name='StatusResponse',
  full_name='ecflow_client.StatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='ecflow_client.StatusResponse.owner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo', full_name='ecflow_client.StatusResponse.repo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collected_timestamp', full_name='ecflow_client.StatusResponse.collected_timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='ecflow_client.StatusResponse.status', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response_status', full_name='ecflow_client.StatusResponse.response_status', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=435,
  serialized_end=581,
)


_NODEREQUEST = _descriptor.Descriptor(
  name='NodeRequest',
  full_name='ecflow_client.NodeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='ecflow_client.NodeRequest.owner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo', full_name='ecflow_client.NodeRequest.repo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='ecflow_client.NodeRequest.host', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='ecflow_client.NodeRequest.port', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='ecflow_client.NodeRequest.path', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=583,
  serialized_end=667,
)


_NODERESPONSE = _descriptor.Descriptor(
  name='NodeResponse',
  full_name='ecflow_client.NodeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='ecflow_client.NodeResponse.owner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo', full_name='ecflow_client.NodeResponse.repo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='ecflow_client.NodeResponse.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node', full_name='ecflow_client.NodeResponse.node', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response_status', full_name='ecflow_client.NodeResponse.response_status', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=669,
  serialized_end=796,
)

_STATUSRECORDSRESPONSE_STATUSMAPENTRY.containing_type = _STATUSRECORDSRESPONSE
_STATUSRECORDSRESPONSE.fields_by_name['status_map'].message_type = _STATUSRECORDSRESPONSE_STATUSMAPENTRY
_STATUSRECORDSRESPONSE.fields_by_name['response_status'].message_type = _RESPONSESTATUS
_STATUSRESPONSE.fields_by_name['response_status'].message_type = _RESPONSESTATUS
_NODERESPONSE.fields_by_name['response_status'].message_type = _RESPONSESTATUS
DESCRIPTOR.message_types_by_name['ResponseStatus'] = _RESPONSESTATUS
DESCRIPTOR.message_types_by_name['StatusRequest'] = _STATUSREQUEST
DESCRIPTOR.message_types_by_name['StatusRecordsResponse'] = _STATUSRECORDSRESPONSE
DESCRIPTOR.message_types_by_name['StatusResponse'] = _STATUSRESPONSE
DESCRIPTOR.message_types_by_name['NodeRequest'] = _NODEREQUEST
DESCRIPTOR.message_types_by_name['NodeResponse'] = _NODERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResponseStatus = _reflection.GeneratedProtocolMessageType('ResponseStatus', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSESTATUS,
  __module__ = 'ecflow_client_pb2'
  # @@protoc_insertion_point(class_scope:ecflow_client.ResponseStatus)
  ))
_sym_db.RegisterMessage(ResponseStatus)

StatusRequest = _reflection.GeneratedProtocolMessageType('StatusRequest', (_message.Message,), dict(
  DESCRIPTOR = _STATUSREQUEST,
  __module__ = 'ecflow_client_pb2'
  # @@protoc_insertion_point(class_scope:ecflow_client.StatusRequest)
  ))
_sym_db.RegisterMessage(StatusRequest)

StatusRecordsResponse = _reflection.GeneratedProtocolMessageType('StatusRecordsResponse', (_message.Message,), dict(

  StatusMapEntry = _reflection.GeneratedProtocolMessageType('StatusMapEntry', (_message.Message,), dict(
    DESCRIPTOR = _STATUSRECORDSRESPONSE_STATUSMAPENTRY,
    __module__ = 'ecflow_client_pb2'
    # @@protoc_insertion_point(class_scope:ecflow_client.StatusRecordsResponse.StatusMapEntry)
    ))
  ,
  DESCRIPTOR = _STATUSRECORDSRESPONSE,
  __module__ = 'ecflow_client_pb2'
  # @@protoc_insertion_point(class_scope:ecflow_client.StatusRecordsResponse)
  ))
_sym_db.RegisterMessage(StatusRecordsResponse)
_sym_db.RegisterMessage(StatusRecordsResponse.StatusMapEntry)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), dict(
  DESCRIPTOR = _STATUSRESPONSE,
  __module__ = 'ecflow_client_pb2'
  # @@protoc_insertion_point(class_scope:ecflow_client.StatusResponse)
  ))
_sym_db.RegisterMessage(StatusResponse)

NodeRequest = _reflection.GeneratedProtocolMessageType('NodeRequest', (_message.Message,), dict(
  DESCRIPTOR = _NODEREQUEST,
  __module__ = 'ecflow_client_pb2'
  # @@protoc_insertion_point(class_scope:ecflow_client.NodeRequest)
  ))
_sym_db.RegisterMessage(NodeRequest)

NodeResponse = _reflection.GeneratedProtocolMessageType('NodeResponse', (_message.Message,), dict(
  DESCRIPTOR = _NODERESPONSE,
  __module__ = 'ecflow_client_pb2'
  # @@protoc_insertion_point(class_scope:ecflow_client.NodeResponse)
  ))
_sym_db.RegisterMessage(NodeResponse)


DESCRIPTOR._options = None
_STATUSRECORDSRESPONSE_STATUSMAPENTRY._options = None

_ECFLOWCLIENTSERVICE = _descriptor.ServiceDescriptor(
  name='EcflowClientService',
  full_name='ecflow_client.EcflowClientService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=799,
  serialized_end=1068,
  methods=[
  _descriptor.MethodDescriptor(
    name='CollectStatusRecords',
    full_name='ecflow_client.EcflowClientService.CollectStatusRecords',
    index=0,
    containing_service=None,
    input_type=_STATUSREQUEST,
    output_type=_STATUSRECORDSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CollectStatus',
    full_name='ecflow_client.EcflowClientService.CollectStatus',
    index=1,
    containing_service=None,
    input_type=_STATUSREQUEST,
    output_type=_STATUSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CollectNode',
    full_name='ecflow_client.EcflowClientService.CollectNode',
    index=2,
    containing_service=None,
    input_type=_NODEREQUEST,
    output_type=_NODERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ECFLOWCLIENTSERVICE)

DESCRIPTOR.services_by_name['EcflowClientService'] = _ECFLOWCLIENTSERVICE

# @@protoc_insertion_point(module_scope)