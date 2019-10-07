class EntireInfoModel():
    def __init__(self):
        self.count = None
        self.page = None
        self.first = None
        self.last = None
        self.hits = None
        self.carrir = None
        self.page_count = None
        self.item_info_model_list = [ItemInfoModel]
        self.genre_info_model_list = [GenreInfoModel]
        self.tag_info_model_list = [TagInfoModel]


class ItemInfoModel():
    def __init__(self):
        self.item_name = None
        self.catchcopy = None
        self.item_code = None
        self.item_price = None
        self.item_caption = None
        self.item_url = None
        self.affiliate_url = None
        self.image_flag = None
        self.small_image_urls = None
        self.medium_image_urls = None
        self.image_url = None
        self.availability = None
        self.tax_flag = None
        self.postage_flag = None
        self.credit_card_flag = None
        self.shop_of_the_year_flag = None
        self.ship_over_seas_flag = None
        self.ship_over_seas_aera = None
        self.asuraku_flag = None
        self.asuraku_closing_time = None
        self.asuraku_area = None
        self.affiliate_rate = None
        self.start_time = None
        self.end_time = None
        self.review_count = None
        self.review_average = None
        self.point_rate = None
        self.point_rate_start_time = None
        self.point_rate_end_time = None
        self.gift_flag = None
        self.shop_name = None
        self.shop_code = None
        self.shop_url = None
        self.shop_affiliate_url = None
        self.genre_id = None
        self.tag_id_list = None


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
