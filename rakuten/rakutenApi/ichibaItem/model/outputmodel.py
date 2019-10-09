from typing import List


class EntireInfoModel():
    def __init__(self):
        self.count: int = None
        self.page: int = None
        self.first: int = None
        self.last: int = None
        self.hits: int = None
        self.carrier: int = None
        self.page_count: int = None
        self.item_info_model_list: List[ItemInfoModel] = []
        self.genre_info_model_list: List[GenreInfoModel] = []
        self.tag_info_model_list: List[TagInfoModel] = []


class ItemInfoModel():
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
        self.ship_over_seas_flag: int = None
        self.ship_over_seas_area: str = None
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


class GenreInfoModel():
    def __init__(self):
        self.genre_id = None
        self.genre_name = None
        self.item_count = None
        self.genre_level = None


class TagInfoModel():
    def __init__(self):
        self.tag_id = None
        self.tag_name = None
        self.parent_tag_id = None
        self.item_count = None
