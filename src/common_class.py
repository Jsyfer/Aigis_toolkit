from dataclasses import dataclass

@dataclass
class AigisUnit:
    id: int
    icon: str
    unit_name: str
    info_url: str
    rare: str
    base_class: str
    property_belong: str
    property_race: str
    property_speciality: str
    property_season: str
    property_qualification: str
    property_collaboration: str
    property_distance: str
    property_sex: str
    has_extra_story: bool
    obtain_method: str
    awakening_material: str
    owned: bool
    is_awakening: bool
    complete_extra_story: bool
    all_complete: bool
