# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: geo/USState.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='geo/USState.proto',
  package='opencannabis.geo.usa',
  syntax='proto3',
  serialized_pb=_b('\n\x11geo/USState.proto\x12\x14opencannabis.geo.usa*\xa1\t\n\x07USState\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x06\n\x02\x41L\x10\x01\x12\x0b\n\x07\x41LABAMA\x10\x01\x12\x06\n\x02\x41K\x10\x02\x12\n\n\x06\x41LASKA\x10\x02\x12\x06\n\x02\x41Z\x10\x03\x12\x0b\n\x07\x41RIZONA\x10\x03\x12\x06\n\x02\x41R\x10\x04\x12\x0c\n\x08\x41RKANSAS\x10\x04\x12\x06\n\x02\x43\x41\x10\x05\x12\x0e\n\nCALIFORNIA\x10\x05\x12\x06\n\x02\x43O\x10\x06\x12\x0c\n\x08\x43OLORADO\x10\x06\x12\x06\n\x02\x43T\x10\x07\x12\x0f\n\x0b\x43ONNECTICUT\x10\x07\x12\x06\n\x02\x44\x45\x10\x08\x12\x0c\n\x08\x44\x65laware\x10\x08\x12\x06\n\x02\x44\x43\x10\t\x12\x18\n\x14\x44ISTRICT_OF_COLUMBIA\x10\t\x12\x06\n\x02\x46L\x10\n\x12\x0b\n\x07\x46LORIDA\x10\n\x12\x06\n\x02GA\x10\x0b\x12\x0b\n\x07GEORGIA\x10\x0b\x12\x06\n\x02HI\x10\x0c\x12\n\n\x06HAWAII\x10\x0c\x12\x06\n\x02ID\x10\r\x12\t\n\x05IDAHO\x10\r\x12\x06\n\x02IL\x10\x0e\x12\x0c\n\x08ILLINOIS\x10\x0e\x12\x06\n\x02IN\x10\x0f\x12\x0b\n\x07INDIANA\x10\x0f\x12\x06\n\x02IA\x10\x10\x12\x08\n\x04IOWA\x10\x10\x12\x06\n\x02KS\x10\x11\x12\n\n\x06KANSAS\x10\x11\x12\x06\n\x02KY\x10\x12\x12\x0c\n\x08KENTUCKY\x10\x12\x12\x06\n\x02LA\x10\x13\x12\x0c\n\x08LOISIANA\x10\x13\x12\x06\n\x02ME\x10\x14\x12\t\n\x05MAINE\x10\x14\x12\x06\n\x02MD\x10\x15\x12\x0c\n\x08MARYLAND\x10\x15\x12\x06\n\x02MA\x10\x16\x12\x11\n\rMASSACHUSETTS\x10\x16\x12\x06\n\x02MI\x10\x17\x12\x0c\n\x08MICHIGAN\x10\x17\x12\x06\n\x02MN\x10\x18\x12\r\n\tMINNESOTA\x10\x18\x12\x06\n\x02MS\x10\x19\x12\x0f\n\x0bMISSISSIPPI\x10\x19\x12\x06\n\x02MO\x10\x1a\x12\x0c\n\x08MISSOURI\x10\x1a\x12\x06\n\x02MT\x10\x1b\x12\x0b\n\x07MONTANA\x10\x1b\x12\x06\n\x02NE\x10\x1c\x12\x0c\n\x08NEBRASKA\x10\x1c\x12\x06\n\x02NV\x10\x1d\x12\n\n\x06NEVADA\x10\x1d\x12\x06\n\x02NH\x10\x1e\x12\x11\n\rNEW_HAMPSHIRE\x10\x1e\x12\x06\n\x02NJ\x10\x1f\x12\x0e\n\nNEW_JERSEY\x10\x1f\x12\x06\n\x02NM\x10 \x12\x0e\n\nNEW_MEXICO\x10 \x12\x06\n\x02NY\x10!\x12\x0c\n\x08NEW_YORK\x10!\x12\x06\n\x02NC\x10\"\x12\x12\n\x0eNORTH_CAROLINA\x10\"\x12\x06\n\x02ND\x10#\x12\x10\n\x0cNORTH_DAKOTA\x10#\x12\x06\n\x02OH\x10$\x12\x08\n\x04OHIO\x10$\x12\x06\n\x02OK\x10%\x12\x0c\n\x08OKLAHOMA\x10%\x12\x06\n\x02OR\x10&\x12\n\n\x06OREGON\x10&\x12\x06\n\x02PA\x10\'\x12\x10\n\x0cPENNSYLVANIA\x10\'\x12\x06\n\x02RI\x10(\x12\x10\n\x0cRHODE_ISLAND\x10(\x12\x06\n\x02SC\x10)\x12\x12\n\x0eSOUTH_CAROLINA\x10)\x12\x06\n\x02SD\x10*\x12\x10\n\x0cSOUTH_DAKOTA\x10*\x12\x06\n\x02TN\x10+\x12\r\n\tTENNESSEE\x10+\x12\x06\n\x02TX\x10,\x12\t\n\x05TEXAS\x10,\x12\x06\n\x02UT\x10-\x12\x08\n\x04UTAH\x10-\x12\x06\n\x02VT\x10.\x12\x0b\n\x07VERMONT\x10.\x12\x06\n\x02VA\x10/\x12\x0c\n\x08VIRGINIA\x10/\x12\x06\n\x02WA\x10\x30\x12\x0e\n\nWASHINGTON\x10\x30\x12\x06\n\x02WV\x10\x31\x12\x11\n\rWEST_VIRGINIA\x10\x31\x12\x06\n\x02WI\x10\x32\x12\r\n\tWISCONSIN\x10\x32\x12\x0b\n\x07WYOMING\x10\x33\x12\x06\n\x02WY\x10\x33\x1a\x02\x10\x01\x42*\n\x1eio.opencannabis.schema.geo.usaH\x01P\x01\xa2\x02\x03OCSb\x06proto3')
)

_USSTATE = _descriptor.EnumDescriptor(
  name='USState',
  full_name='opencannabis.geo.usa.USState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALABAMA', index=2, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AK', index=3, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALASKA', index=4, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AZ', index=5, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARIZONA', index=6, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AR', index=7, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARKANSAS', index=8, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CA', index=9, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIFORNIA', index=10, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CO', index=11, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLORADO', index=12, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT', index=13, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECTICUT', index=14, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DE', index=15, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Delaware', index=16, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DC', index=17, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISTRICT_OF_COLUMBIA', index=18, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FL', index=19, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLORIDA', index=20, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GA', index=21, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GEORGIA', index=22, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HI', index=23, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HAWAII', index=24, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID', index=25, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IDAHO', index=26, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IL', index=27, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ILLINOIS', index=28, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IN', index=29, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDIANA', index=30, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IA', index=31, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IOWA', index=32, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KS', index=33, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KANSAS', index=34, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KY', index=35, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KENTUCKY', index=36, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LA', index=37, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOISIANA', index=38, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ME', index=39, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAINE', index=40, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MD', index=41, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MARYLAND', index=42, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MA', index=43, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MASSACHUSETTS', index=44, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MI', index=45, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MICHIGAN', index=46, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MN', index=47, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MINNESOTA', index=48, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MS', index=49, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSISSIPPI', index=50, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MO', index=51, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSOURI', index=52, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MT', index=53, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONTANA', index=54, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NE', index=55, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEBRASKA', index=56, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NV', index=57, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEVADA', index=58, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NH', index=59, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW_HAMPSHIRE', index=60, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NJ', index=61, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW_JERSEY', index=62, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NM', index=63, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW_MEXICO', index=64, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NY', index=65, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW_YORK', index=66, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NC', index=67, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NORTH_CAROLINA', index=68, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ND', index=69, number=35,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NORTH_DAKOTA', index=70, number=35,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OH', index=71, number=36,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OHIO', index=72, number=36,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=73, number=37,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OKLAHOMA', index=74, number=37,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OR', index=75, number=38,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OREGON', index=76, number=38,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PA', index=77, number=39,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENNSYLVANIA', index=78, number=39,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RI', index=79, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RHODE_ISLAND', index=80, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SC', index=81, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOUTH_CAROLINA', index=82, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SD', index=83, number=42,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOUTH_DAKOTA', index=84, number=42,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TN', index=85, number=43,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TENNESSEE', index=86, number=43,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TX', index=87, number=44,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXAS', index=88, number=44,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UT', index=89, number=45,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UTAH', index=90, number=45,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VT', index=91, number=46,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERMONT', index=92, number=46,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VA', index=93, number=47,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIRGINIA', index=94, number=47,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WA', index=95, number=48,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WASHINGTON', index=96, number=48,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WV', index=97, number=49,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEST_VIRGINIA', index=98, number=49,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WI', index=99, number=50,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WISCONSIN', index=100, number=50,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WYOMING', index=101, number=51,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WY', index=102, number=51,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=_descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\020\001')),
  serialized_start=44,
  serialized_end=1229,
)
_sym_db.RegisterEnumDescriptor(_USSTATE)

USState = enum_type_wrapper.EnumTypeWrapper(_USSTATE)
UNSPECIFIED = 0
AL = 1
ALABAMA = 1
AK = 2
ALASKA = 2
AZ = 3
ARIZONA = 3
AR = 4
ARKANSAS = 4
CA = 5
CALIFORNIA = 5
CO = 6
COLORADO = 6
CT = 7
CONNECTICUT = 7
DE = 8
Delaware = 8
DC = 9
DISTRICT_OF_COLUMBIA = 9
FL = 10
FLORIDA = 10
GA = 11
GEORGIA = 11
HI = 12
HAWAII = 12
ID = 13
IDAHO = 13
IL = 14
ILLINOIS = 14
IN = 15
INDIANA = 15
IA = 16
IOWA = 16
KS = 17
KANSAS = 17
KY = 18
KENTUCKY = 18
LA = 19
LOISIANA = 19
ME = 20
MAINE = 20
MD = 21
MARYLAND = 21
MA = 22
MASSACHUSETTS = 22
MI = 23
MICHIGAN = 23
MN = 24
MINNESOTA = 24
MS = 25
MISSISSIPPI = 25
MO = 26
MISSOURI = 26
MT = 27
MONTANA = 27
NE = 28
NEBRASKA = 28
NV = 29
NEVADA = 29
NH = 30
NEW_HAMPSHIRE = 30
NJ = 31
NEW_JERSEY = 31
NM = 32
NEW_MEXICO = 32
NY = 33
NEW_YORK = 33
NC = 34
NORTH_CAROLINA = 34
ND = 35
NORTH_DAKOTA = 35
OH = 36
OHIO = 36
OK = 37
OKLAHOMA = 37
OR = 38
OREGON = 38
PA = 39
PENNSYLVANIA = 39
RI = 40
RHODE_ISLAND = 40
SC = 41
SOUTH_CAROLINA = 41
SD = 42
SOUTH_DAKOTA = 42
TN = 43
TENNESSEE = 43
TX = 44
TEXAS = 44
UT = 45
UTAH = 45
VT = 46
VERMONT = 46
VA = 47
VIRGINIA = 47
WA = 48
WASHINGTON = 48
WV = 49
WEST_VIRGINIA = 49
WI = 50
WISCONSIN = 50
WYOMING = 51
WY = 51


DESCRIPTOR.enum_types_by_name['USState'] = _USSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036io.opencannabis.schema.geo.usaH\001P\001\242\002\003OCS'))
_USSTATE.has_options = True
_USSTATE._options = _descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
