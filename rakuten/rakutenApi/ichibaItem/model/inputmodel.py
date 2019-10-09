class SearchConditionModel:
    """
    検索条件モデルクラス
    """

    def __init__(
            self, application_id=None, affiliate_id=None, arg_format=None,
            callback=None, elements=None, format_version=None,
            keyword=None, shop_code=None, item_code=None, genre_id=None,
            tag_id=None, hits=None, page=None, sort=None, min_price=None,
            max_price=None, avalilability=None, field=None, carrier=None,
            image_flag=None, or_flag=None, ng_keyword=None, purchase_type=None,
            ship_overseas_flag=None, ship_overseas_area=None,
            asuraku_flag=None, asuraku_area=None, point_rate_flag=None,
            point_rate=None, postage_flag=None, credit_card_flag=None,
            gift_flag=None, has_review_flag=None, max_affiliate_rate=None,
            min_affiliate_rate=None, has_movie_flag=None, pamphlet_flag=None,
            appoint_delivery_date_flag=None, genre_infomation_flag=None,
            tag_information_flag=None
    ):
        self.application_id: str = application_id
        self.affiliate_id: str = affiliate_id
        self.format: str = arg_format
        self.callback: str = callback
        self.elements: str = elements
        self.format_version: int = format_version
        self.keyword: str = keyword
        self.shop_code: str = shop_code
        self.item_code: str = item_code
        self.genre_id: int = genre_id
        self.tag_id: int = tag_id
        self.hits: int = hits
        self.page: int = page
        self.sort: str = sort
        self.min_price: int = min_price
        self.max_price: int = max_price
        self.avalilability: int = avalilability
        self.field: int = field
        self.carrier: int = carrier
        self.image_flag: int = image_flag
        self.or_flag: int = or_flag
        self.ng_keyword: str = ng_keyword
        self.purchase_type: int = purchase_type
        self.ship_overseas_flag: int = ship_overseas_flag
        self.ship_overseas_area: str = ship_overseas_area
        self.asuraku_flag: int = asuraku_flag
        self.asuraku_area: int = asuraku_area
        self.point_rate_flag: int = point_rate_flag
        self.point_rate: int = point_rate
        self.postage_flag: int = postage_flag
        self.credit_card_flag: int = credit_card_flag
        self.gift_flag: int = gift_flag
        self.has_review_flag: int = has_review_flag
        self.max_affiliate_rate: float = max_affiliate_rate
        self.min_affiliate_rate: float = min_affiliate_rate
        self.has_movie_flag: int = has_movie_flag
        self.pamphlet_flag: int = pamphlet_flag
        self.appoint_delivery_date_flag: int = appoint_delivery_date_flag
        self.genre_infomation_flag: int = genre_infomation_flag
        self.tag_information_flag: int = tag_information_flag
