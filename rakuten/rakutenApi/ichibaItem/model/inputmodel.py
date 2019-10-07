class SearchConditionModel:
    """
    検索条件モデルクラス
    """

    def __init__(
            self, arg_format=None, application_id=None, affiliate_id=None,
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
        self.format = arg_format
        self.application_id = application_id
        self.affiliate_id = affiliate_id
        self.keyword = keyword
        self.shop_code = shop_code
        self.item_code = item_code
        self.genre_id = genre_id
        self.tag_id = tag_id
        self.hits = hits
        self.page = page
        self.sort = sort
        self.min_price = min_price
        self.max_price = max_price
        self.avalilability = avalilability
        self.field = field
        self.carrier = carrier
        self.image_flag = image_flag
        self.or_flag = or_flag
        self.ng_keyword = ng_keyword
        self.purchase_type = purchase_type
        self.ship_overseas_flag = ship_overseas_flag
        self.ship_overseas_area = ship_overseas_area
        self.asuraku_flag = asuraku_flag
        self.asuraku_area = asuraku_area
        self.point_rate_flag = point_rate_flag
        self.point_rate = point_rate
        self.postage_flag = postage_flag
        self.credit_card_flag = credit_card_flag
        self.gift_flag = gift_flag
        self.has_review_flag = has_review_flag
        self.max_affiliate_rate = max_affiliate_rate
        self.min_affiliate_rate = min_affiliate_rate
        self.has_movie_flag = has_movie_flag
        self.pamphlet_flag = pamphlet_flag
        self.appoint_delivery_date_flag = appoint_delivery_date_flag
        self.genre_infomation_flag = genre_infomation_flag
        self.tag_information_flag = tag_information_flag
