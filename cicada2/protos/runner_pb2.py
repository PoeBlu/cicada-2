# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cicada2/protos/runner.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="cicada2/protos/runner.proto",
    package="cicada_2",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=_b(
        '\n\x1b\x63icada2/protos/runner.proto\x12\x08\x63icada_2\x1a\x1bgoogle/protobuf/empty.proto"-\n\rActionRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06params\x18\x02 \x01(\x0c"\x1e\n\x0b\x41\x63tionReply\x12\x0f\n\x07outputs\x18\x01 \x01(\x0c"-\n\rAssertRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06params\x18\x02 \x01(\x0c"T\n\x0b\x41ssertReply\x12\x0e\n\x06passed\x18\x01 \x01(\x08\x12\x0e\n\x06\x61\x63tual\x18\x02 \x01(\t\x12\x10\n\x08\x65xpected\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t"!\n\x10HealthcheckReply\x12\r\n\x05ready\x18\x01 \x01(\x08\x32\xbf\x01\n\x06Runner\x12\x38\n\x06\x41\x63tion\x12\x17.cicada_2.ActionRequest\x1a\x15.cicada_2.ActionReply\x12\x38\n\x06\x41ssert\x12\x17.cicada_2.AssertRequest\x1a\x15.cicada_2.AssertReply\x12\x41\n\x0bHealthcheck\x12\x16.google.protobuf.Empty\x1a\x1a.cicada_2.HealthcheckReplyb\x06proto3'
    ),
    dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,],
)


_ACTIONREQUEST = _descriptor.Descriptor(
    name="ActionRequest",
    full_name="cicada_2.ActionRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="cicada_2.ActionRequest.type",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="params",
            full_name="cicada_2.ActionRequest.params",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=70,
    serialized_end=115,
)


_ACTIONREPLY = _descriptor.Descriptor(
    name="ActionReply",
    full_name="cicada_2.ActionReply",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="outputs",
            full_name="cicada_2.ActionReply.outputs",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=117,
    serialized_end=147,
)


_ASSERTREQUEST = _descriptor.Descriptor(
    name="AssertRequest",
    full_name="cicada_2.AssertRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="cicada_2.AssertRequest.type",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="params",
            full_name="cicada_2.AssertRequest.params",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=149,
    serialized_end=194,
)


_ASSERTREPLY = _descriptor.Descriptor(
    name="AssertReply",
    full_name="cicada_2.AssertReply",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="passed",
            full_name="cicada_2.AssertReply.passed",
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="actual",
            full_name="cicada_2.AssertReply.actual",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="expected",
            full_name="cicada_2.AssertReply.expected",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="cicada_2.AssertReply.description",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=196,
    serialized_end=280,
)


_HEALTHCHECKREPLY = _descriptor.Descriptor(
    name="HealthcheckReply",
    full_name="cicada_2.HealthcheckReply",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="ready",
            full_name="cicada_2.HealthcheckReply.ready",
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=282,
    serialized_end=315,
)

DESCRIPTOR.message_types_by_name["ActionRequest"] = _ACTIONREQUEST
DESCRIPTOR.message_types_by_name["ActionReply"] = _ACTIONREPLY
DESCRIPTOR.message_types_by_name["AssertRequest"] = _ASSERTREQUEST
DESCRIPTOR.message_types_by_name["AssertReply"] = _ASSERTREPLY
DESCRIPTOR.message_types_by_name["HealthcheckReply"] = _HEALTHCHECKREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActionRequest = _reflection.GeneratedProtocolMessageType(
    "ActionRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _ACTIONREQUEST,
        "__module__": "cicada2.protos.runner_pb2"
        # @@protoc_insertion_point(class_scope:cicada_2.ActionRequest)
    },
)
_sym_db.RegisterMessage(ActionRequest)

ActionReply = _reflection.GeneratedProtocolMessageType(
    "ActionReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _ACTIONREPLY,
        "__module__": "cicada2.protos.runner_pb2"
        # @@protoc_insertion_point(class_scope:cicada_2.ActionReply)
    },
)
_sym_db.RegisterMessage(ActionReply)

AssertRequest = _reflection.GeneratedProtocolMessageType(
    "AssertRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _ASSERTREQUEST,
        "__module__": "cicada2.protos.runner_pb2"
        # @@protoc_insertion_point(class_scope:cicada_2.AssertRequest)
    },
)
_sym_db.RegisterMessage(AssertRequest)

AssertReply = _reflection.GeneratedProtocolMessageType(
    "AssertReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _ASSERTREPLY,
        "__module__": "cicada2.protos.runner_pb2"
        # @@protoc_insertion_point(class_scope:cicada_2.AssertReply)
    },
)
_sym_db.RegisterMessage(AssertReply)

HealthcheckReply = _reflection.GeneratedProtocolMessageType(
    "HealthcheckReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _HEALTHCHECKREPLY,
        "__module__": "cicada2.protos.runner_pb2"
        # @@protoc_insertion_point(class_scope:cicada_2.HealthcheckReply)
    },
)
_sym_db.RegisterMessage(HealthcheckReply)


_RUNNER = _descriptor.ServiceDescriptor(
    name="Runner",
    full_name="cicada_2.Runner",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=318,
    serialized_end=509,
    methods=[
        _descriptor.MethodDescriptor(
            name="Action",
            full_name="cicada_2.Runner.Action",
            index=0,
            containing_service=None,
            input_type=_ACTIONREQUEST,
            output_type=_ACTIONREPLY,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name="Assert",
            full_name="cicada_2.Runner.Assert",
            index=1,
            containing_service=None,
            input_type=_ASSERTREQUEST,
            output_type=_ASSERTREPLY,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name="Healthcheck",
            full_name="cicada_2.Runner.Healthcheck",
            index=2,
            containing_service=None,
            input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            output_type=_HEALTHCHECKREPLY,
            serialized_options=None,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_RUNNER)

DESCRIPTOR.services_by_name["Runner"] = _RUNNER

# @@protoc_insertion_point(module_scope)
