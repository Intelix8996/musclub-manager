from pydantic import BaseModel


class SpecialisationFull(BaseModel):
    title: str


class InstrumentFull(BaseModel):
    title: str


class MemberBrief(BaseModel):
    full_name: str
    status: str
    specialisations: dict[int, SpecialisationFull]
    instruments: dict[int, InstrumentFull]


class MembersResponse(BaseModel):
    members: dict[int, MemberBrief]


class MemberFull(BaseModel):
    full_name: str
    photo_url: str | None
    telegram: str | None
    socials: dict[str, str]
    status: str
    specialisations: dict[int, SpecialisationFull]
    instruments: dict[int, InstrumentFull]
    repertoire: str
    band_structure: str
    notes: str


class MemberResponse(BaseModel):
    member: MemberFull
