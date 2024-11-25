from pydantic import BaseModel


class SpecialisationFull(BaseModel):
    id: int
    title: str


class InstrumentFull(BaseModel):
    id: int
    title: str


class MemberBrief(BaseModel):
    id: int
    full_name: str
    status: str
    specialisations: list[SpecialisationFull]
    instruments: list[InstrumentFull]


class MembersResponse(BaseModel):
    members: list[MemberBrief]


class MemberFull(BaseModel):
    id: int
    full_name: str
    photo_url: str | None
    telegram: str | None
    socials: dict[str, str]
    status: str
    specialisations: list[SpecialisationFull]
    instruments: list[InstrumentFull]
    repertoire: str
    band_structure: str
    notes: str


class MemberResponse(BaseModel):
    member: MemberFull
