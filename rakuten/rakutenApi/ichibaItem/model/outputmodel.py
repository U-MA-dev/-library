from typing import List


class EntireModel():
    def __init__(self):
        self.count: int = None
        self.page: int = None
        self.first: int = None
        self.last: int = None
        self.hits: int = None
        self.carrier: int = None
        self.page_count: int = None
        self.item_model_list: List[ItemModel] = []
        self.genre_model_list: List[GenreModel] = []
        self.tag_group_model_list: List[TagGroupModel] = []


class ItemModel():
    def __init__(self):
        self.item_name: str = None
        self.catchcopy: str = None
        self.item_code: str = None
        self.item_price: int = None
        self.item_caption: str = None
        self.item_url: str = None
        self.affiliate_url: str = None
        self.image_flag: int = None
        self.small_image_urls: List[str] = None
        self.medium_image_urls: List[str] = None
        self.availability: int = None
        self.tax_flag: int = None
        self.postage_flag: int = None
        self.credit_card_flag: int = None
        self.shop_of_the_year_flag: int = None
        self.ship_overseas_flag: int = None
        self.ship_overseas_area: str = None
        self.asuraku_flag: int = None
        self.asuraku_closing_time: str = None
        self.asuraku_area: str = None
        self.affiliate_rate: float = None
        self.start_time: str = None
        self.end_time: str = None
        self.review_count: int = None
        self.review_average: float = None
        self.point_rate: float = None
        self.point_rate_start_time: str = None
        self.point_rate_end_time: str = None
        self.gift_flag: int = None
        self.shop_name: str = None
        self.shop_code: str = None
        self.shop_url: str = None
        self.shop_affiliate_url: str = None
        self.genre_id: str = None
        self.tag_id_list: List[int] = None


class GenreModel():
    def __init__(self):
        self.parent_genre_model: ParentGenreModel = None
        self.current_genre_model: CurrentGenreModel = None
        self.child_genre_model_list: List[ChildGenreModel] = []


class BaseGenreModel():
    def __init__(self):
        self.genre_id: str = None
        self.genre_name: str = None
        self.genre_level: str = None


class ParentGenreModel(BaseGenreModel):
    pass


class CurrentGenreModel(BaseGenreModel):
    def __init__(self):
        super().__init__()
        self.item_count: str = None


class ChildGenreModel(BaseGenreModel):
    def __init__(self):
        super().__init__()
        self.item_count: str = None


class TagGroupModel():
    def __init__(self):
        self.tag_group_id: int = None
        self.tag_group_name: str = None
        self.tag_model_list: List[TagModel] = []


class TagModel():
    def __init__(self):
        self.tag_id: int = None
        self.tag_name: str = None
        self.parent_tag_id: int = None
        self.item_count: int = None
