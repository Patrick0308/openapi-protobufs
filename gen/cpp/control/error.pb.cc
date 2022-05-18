// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: control/error.proto

#include "control/error.pb.h"

#include <algorithm>

#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/wire_format_lite.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>

PROTOBUF_PRAGMA_INIT_SEG
namespace longbridgeapp {
namespace control {
namespace v1 {
constexpr Error::Error(
  ::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized)
  : msg_(&::PROTOBUF_NAMESPACE_ID::internal::fixed_address_empty_string)
  , code_(uint64_t{0u}){}
struct ErrorDefaultTypeInternal {
  constexpr ErrorDefaultTypeInternal()
    : _instance(::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized{}) {}
  ~ErrorDefaultTypeInternal() {}
  union {
    Error _instance;
  };
};
PROTOBUF_ATTRIBUTE_NO_DESTROY PROTOBUF_CONSTINIT ErrorDefaultTypeInternal _Error_default_instance_;
}  // namespace v1
}  // namespace control
}  // namespace longbridgeapp
static ::PROTOBUF_NAMESPACE_ID::Metadata file_level_metadata_control_2ferror_2eproto[1];
static constexpr ::PROTOBUF_NAMESPACE_ID::EnumDescriptor const** file_level_enum_descriptors_control_2ferror_2eproto = nullptr;
static constexpr ::PROTOBUF_NAMESPACE_ID::ServiceDescriptor const** file_level_service_descriptors_control_2ferror_2eproto = nullptr;

const uint32_t TableStruct_control_2ferror_2eproto::offsets[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::longbridgeapp::control::v1::Error, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  ~0u,  // no _inlined_string_donated_
  PROTOBUF_FIELD_OFFSET(::longbridgeapp::control::v1::Error, code_),
  PROTOBUF_FIELD_OFFSET(::longbridgeapp::control::v1::Error, msg_),
};
static const ::PROTOBUF_NAMESPACE_ID::internal::MigrationSchema schemas[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  { 0, -1, -1, sizeof(::longbridgeapp::control::v1::Error)},
};

static ::PROTOBUF_NAMESPACE_ID::Message const * const file_default_instances[] = {
  reinterpret_cast<const ::PROTOBUF_NAMESPACE_ID::Message*>(&::longbridgeapp::control::v1::_Error_default_instance_),
};

const char descriptor_table_protodef_control_2ferror_2eproto[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) =
  "\n\023control/error.proto\022\030longbridgeapp.con"
  "trol.v1\"-\n\005Error\022\022\n\004code\030\001 \001(\004R\004code\022\020\n\003"
  "msg\030\002 \001(\tR\003msgB\361\001\n\034com.longbridgeapp.con"
  "trol.v1B\nErrorProtoP\001ZCgithub.com/longbr"
  "idgeapp/openapi-protobufs/gen/go/control"
  ";controlv1\242\002\003LCX\252\002\030Longbridgeapp.Control"
  ".V1\312\002\030Longbridgeapp\\Control\\V1\342\002$Longbri"
  "dgeapp\\Control\\V1\\GPBMetadata\352\002\032Longbrid"
  "geapp::Control::V1b\006proto3"
  ;
static ::PROTOBUF_NAMESPACE_ID::internal::once_flag descriptor_table_control_2ferror_2eproto_once;
const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_control_2ferror_2eproto = {
  false, false, 346, descriptor_table_protodef_control_2ferror_2eproto, "control/error.proto", 
  &descriptor_table_control_2ferror_2eproto_once, nullptr, 0, 1,
  schemas, file_default_instances, TableStruct_control_2ferror_2eproto::offsets,
  file_level_metadata_control_2ferror_2eproto, file_level_enum_descriptors_control_2ferror_2eproto, file_level_service_descriptors_control_2ferror_2eproto,
};
PROTOBUF_ATTRIBUTE_WEAK const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable* descriptor_table_control_2ferror_2eproto_getter() {
  return &descriptor_table_control_2ferror_2eproto;
}

// Force running AddDescriptors() at dynamic initialization time.
PROTOBUF_ATTRIBUTE_INIT_PRIORITY static ::PROTOBUF_NAMESPACE_ID::internal::AddDescriptorsRunner dynamic_init_dummy_control_2ferror_2eproto(&descriptor_table_control_2ferror_2eproto);
namespace longbridgeapp {
namespace control {
namespace v1 {

// ===================================================================

class Error::_Internal {
 public:
};

Error::Error(::PROTOBUF_NAMESPACE_ID::Arena* arena,
                         bool is_message_owned)
  : ::PROTOBUF_NAMESPACE_ID::Message(arena, is_message_owned) {
  SharedCtor();
  if (!is_message_owned) {
    RegisterArenaDtor(arena);
  }
  // @@protoc_insertion_point(arena_constructor:longbridgeapp.control.v1.Error)
}
Error::Error(const Error& from)
  : ::PROTOBUF_NAMESPACE_ID::Message() {
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
  msg_.UnsafeSetDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  #ifdef PROTOBUF_FORCE_COPY_DEFAULT_STRING
    msg_.Set(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), "", GetArenaForAllocation());
  #endif // PROTOBUF_FORCE_COPY_DEFAULT_STRING
  if (!from._internal_msg().empty()) {
    msg_.Set(::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr::EmptyDefault{}, from._internal_msg(), 
      GetArenaForAllocation());
  }
  code_ = from.code_;
  // @@protoc_insertion_point(copy_constructor:longbridgeapp.control.v1.Error)
}

inline void Error::SharedCtor() {
msg_.UnsafeSetDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
#ifdef PROTOBUF_FORCE_COPY_DEFAULT_STRING
  msg_.Set(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), "", GetArenaForAllocation());
#endif // PROTOBUF_FORCE_COPY_DEFAULT_STRING
code_ = uint64_t{0u};
}

Error::~Error() {
  // @@protoc_insertion_point(destructor:longbridgeapp.control.v1.Error)
  if (GetArenaForAllocation() != nullptr) return;
  SharedDtor();
  _internal_metadata_.Delete<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

inline void Error::SharedDtor() {
  GOOGLE_DCHECK(GetArenaForAllocation() == nullptr);
  msg_.DestroyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}

void Error::ArenaDtor(void* object) {
  Error* _this = reinterpret_cast< Error* >(object);
  (void)_this;
}
void Error::RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena*) {
}
void Error::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}

void Error::Clear() {
// @@protoc_insertion_point(message_clear_start:longbridgeapp.control.v1.Error)
  uint32_t cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  msg_.ClearToEmpty();
  code_ = uint64_t{0u};
  _internal_metadata_.Clear<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

const char* Error::_InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) {
#define CHK_(x) if (PROTOBUF_PREDICT_FALSE(!(x))) goto failure
  while (!ctx->Done(&ptr)) {
    uint32_t tag;
    ptr = ::PROTOBUF_NAMESPACE_ID::internal::ReadTag(ptr, &tag);
    switch (tag >> 3) {
      // uint64 code = 1 [json_name = "code"];
      case 1:
        if (PROTOBUF_PREDICT_TRUE(static_cast<uint8_t>(tag) == 8)) {
          code_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint64(&ptr);
          CHK_(ptr);
        } else
          goto handle_unusual;
        continue;
      // string msg = 2 [json_name = "msg"];
      case 2:
        if (PROTOBUF_PREDICT_TRUE(static_cast<uint8_t>(tag) == 18)) {
          auto str = _internal_mutable_msg();
          ptr = ::PROTOBUF_NAMESPACE_ID::internal::InlineGreedyStringParser(str, ptr, ctx);
          CHK_(::PROTOBUF_NAMESPACE_ID::internal::VerifyUTF8(str, "longbridgeapp.control.v1.Error.msg"));
          CHK_(ptr);
        } else
          goto handle_unusual;
        continue;
      default:
        goto handle_unusual;
    }  // switch
  handle_unusual:
    if ((tag == 0) || ((tag & 7) == 4)) {
      CHK_(ptr);
      ctx->SetLastTag(tag);
      goto message_done;
    }
    ptr = UnknownFieldParse(
        tag,
        _internal_metadata_.mutable_unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(),
        ptr, ctx);
    CHK_(ptr != nullptr);
  }  // while
message_done:
  return ptr;
failure:
  ptr = nullptr;
  goto message_done;
#undef CHK_
}

uint8_t* Error::_InternalSerialize(
    uint8_t* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const {
  // @@protoc_insertion_point(serialize_to_array_start:longbridgeapp.control.v1.Error)
  uint32_t cached_has_bits = 0;
  (void) cached_has_bits;

  // uint64 code = 1 [json_name = "code"];
  if (this->_internal_code() != 0) {
    target = stream->EnsureSpace(target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteUInt64ToArray(1, this->_internal_code(), target);
  }

  // string msg = 2 [json_name = "msg"];
  if (!this->_internal_msg().empty()) {
    ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::VerifyUtf8String(
      this->_internal_msg().data(), static_cast<int>(this->_internal_msg().length()),
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::SERIALIZE,
      "longbridgeapp.control.v1.Error.msg");
    target = stream->WriteStringMaybeAliased(
        2, this->_internal_msg(), target);
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormat::InternalSerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(::PROTOBUF_NAMESPACE_ID::UnknownFieldSet::default_instance), target, stream);
  }
  // @@protoc_insertion_point(serialize_to_array_end:longbridgeapp.control.v1.Error)
  return target;
}

size_t Error::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:longbridgeapp.control.v1.Error)
  size_t total_size = 0;

  uint32_t cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // string msg = 2 [json_name = "msg"];
  if (!this->_internal_msg().empty()) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::StringSize(
        this->_internal_msg());
  }

  // uint64 code = 1 [json_name = "code"];
  if (this->_internal_code() != 0) {
    total_size += ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::UInt64SizePlusOne(this->_internal_code());
  }

  return MaybeComputeUnknownFieldsSize(total_size, &_cached_size_);
}

const ::PROTOBUF_NAMESPACE_ID::Message::ClassData Error::_class_data_ = {
    ::PROTOBUF_NAMESPACE_ID::Message::CopyWithSizeCheck,
    Error::MergeImpl
};
const ::PROTOBUF_NAMESPACE_ID::Message::ClassData*Error::GetClassData() const { return &_class_data_; }

void Error::MergeImpl(::PROTOBUF_NAMESPACE_ID::Message* to,
                      const ::PROTOBUF_NAMESPACE_ID::Message& from) {
  static_cast<Error *>(to)->MergeFrom(
      static_cast<const Error &>(from));
}


void Error::MergeFrom(const Error& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:longbridgeapp.control.v1.Error)
  GOOGLE_DCHECK_NE(&from, this);
  uint32_t cached_has_bits = 0;
  (void) cached_has_bits;

  if (!from._internal_msg().empty()) {
    _internal_set_msg(from._internal_msg());
  }
  if (from._internal_code() != 0) {
    _internal_set_code(from._internal_code());
  }
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
}

void Error::CopyFrom(const Error& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:longbridgeapp.control.v1.Error)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool Error::IsInitialized() const {
  return true;
}

void Error::InternalSwap(Error* other) {
  using std::swap;
  auto* lhs_arena = GetArenaForAllocation();
  auto* rhs_arena = other->GetArenaForAllocation();
  _internal_metadata_.InternalSwap(&other->_internal_metadata_);
  ::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr::InternalSwap(
      &::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(),
      &msg_, lhs_arena,
      &other->msg_, rhs_arena
  );
  swap(code_, other->code_);
}

::PROTOBUF_NAMESPACE_ID::Metadata Error::GetMetadata() const {
  return ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(
      &descriptor_table_control_2ferror_2eproto_getter, &descriptor_table_control_2ferror_2eproto_once,
      file_level_metadata_control_2ferror_2eproto[0]);
}

// @@protoc_insertion_point(namespace_scope)
}  // namespace v1
}  // namespace control
}  // namespace longbridgeapp
PROTOBUF_NAMESPACE_OPEN
template<> PROTOBUF_NOINLINE ::longbridgeapp::control::v1::Error* Arena::CreateMaybeMessage< ::longbridgeapp::control::v1::Error >(Arena* arena) {
  return Arena::CreateMessageInternal< ::longbridgeapp::control::v1::Error >(arena);
}
PROTOBUF_NAMESPACE_CLOSE

// @@protoc_insertion_point(global_scope)
#include <google/protobuf/port_undef.inc>
