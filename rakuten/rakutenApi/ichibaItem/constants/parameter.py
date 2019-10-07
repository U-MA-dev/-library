class InputParameter:
    STR_FORMAT = "format"
    STR_APPLICATION_ID = "applicationId"
    STR_AFFILIATE_ID = "affiliateId"
    STR_KEYWORD = "keyword"
    STR_SHOP_CODE = "shopCode"
    STR_ITEM_CODE = "itemCode"
    STR_GENRE_ID = "genreId"
    STR_TAG_ID = "tagId"
    STR_HITS = "hits"
    STR_PAGE = "page"
    STR_SORT = "sort"
    STR_MIN_PRICE = "minPrice"
    STR_MAX_PRICE = "maxPrice"
    STR_AVAILABILITY = "availability"
    STR_FIELD = "field"
    STR_CARRIER = "carrier"
    STR_IMAGE_FLAG = "imageFlag"
    STR_OR_FLAG = "orFlag"
    STR_NG_KEYWORD = "NGKeyword"
    STR_PURCHASE_TYPE = "purchaseType"
    STR_SHIP_OVERSEAS_FLAG = "shipOverseasFlag"
    STR_SHIP_OVERSEAS_AREA = "shipOverseasArea"
    STR_ASURAKU_FLAG = "asurakuFlag"
    STR_ASURAKU_AREA = "asurakuArea"
    STR_POINT_RATE_FLAG = "pointRateFlag"
    STR_POINT_RATE = "pointRate"
    STR_POSTAGE_FLAG = "postageFlag"
    STR_CREDIT_CARD_FLAG = "creditCardFlag"
    STR_GIFT_FLAG = "giftFlag"
    STR_HAS_REVIEW_FLAG = "hasReviewFlag"
    STR_MAX_AFFILIATE_RATE = "maxAffiliateRate"
    STR_MIN_AFFILIATE_RATE = "minAffiliateRate"
    STR_HAS_MOVIE_FLAG = "hasMovieFlag"
    STR_PAMPHLET_FLAG = "pamphletFlag"
    STR_APPOINT_DELIVERY_DATE_FLAG = "appointDeliveryDateFlag"
    STR_GENRE_INFOMATION_FLAG = "genreInformationFlag"
    STR_TAG_INFORMATION_FLAG = "tagInformationFlag"


class OutputParameter:
    # 全体情報
    STR_COUNT = "count"
    STR_PAGE = "page"
    STR_FIRST = "first"
    STR_LAST = "last"
    STR_HITS = "hits"
    STR_CARRIER = "carrier"
    STR_PAGE_COUNT = "pageCount"

    # 商品情報
    STR_ITEMS = "Items"  # 全体
    STR_ITEM = "Item"  # 個別商品

    STR_ITEM_NAME = "itemName"
    STR_CATCHCOPY = "catchcopy"
    STR_ITEM_CODE = "itemCode"
    STR_ITEM_PRICE = "itemPrice"
    STR_ITEM_CAPTION = "itemCaption"
    STR_ITEM_URL = "itemUrl"
    STR_AFFILIATE_URL = "affiliateUrl"
    STR_IMAGE_FLAG = "imageFlag"
    STR_SMALL_IMAGE_URLS = "smallImageUrls"
    STR_MEDIUM_IMAGE_URLS = "mediumImageUrls"
    STR_IMAGE_URL = "imageUrl"
    STR_AVAILABILITY = "availability"
    STR_TAX_FLAG = "taxFlag"
    STR_POSTAGE_FLAG = "postageFlag"
    STR_CREDIT_CARD_FLAG = "creditCardFlag"
    STR_SHOP_OF_THE_YEAR_FLAG = "shopOfTheYearFlag"
    STR_SHIP_OVER_SEAS_FLAG = "shipOverseasFlag"
    STR_SHIP_OVER_SEAS_AERA = "shipOverseasArea"
    STR_ASURAKU_FLAG = "asurakuFlag"
    STR_ASURAKU_CLOSING_TIME = "asurakuClosingTime"
    STR_ASURAKU_AREA = "asurakuArea"
    STR_AFFILIATE_RATE = "affiliateRate"
    STR_START_TIME = "startTime"
    STR_END_TIME = "endTime"
    STR_REVIEW_COUNT = "reviewCount"
    STR_REVIEW_AVERAGE = "reviewAverage"
    STR_POINT_RATE = "pointRate"
    STR_POINT_RATE_START_TIME = "pointRateStartTime"
    STR_POINT_RATE_END_TIME = "pointRateEndTime"
    STR_GIFT_FLAG = "giftFlag"
    STR_SHOP_NAME = "shopName"
    STR_SHOP_CODE = "shopCode"
    STR_SHOP_URL = "shopUrl"
    STR_SHOP_AFFILIATE_URL = "shopAffiliateUrl"

    # ジャンル情報
    STR_GENRE_ID = "genreId"

    # タグ情報
    STR_TAG_IDS = "tagIds"

    # ジャンルごとの商品数
    STR_GENRE_INFOMATION = "GenreInformation"  # 全体
    STR_PARENT = "parent"  # 入力されたジャンルの親ジャンル
    STR_CURRENT = "current"  # ユーザの入力したジャンルID
    STR_CHILD = "child"  # ユーザの入力したジャンルIDの子ジャンル
    STR_CHILDREN = "children"  # 複数の子ジャンルがある場合
    STR_GENRE_ID = "genreId"
    STR_GENRE_NAME = "genreName"
    STR_ITEM_COUNT = "itemCount"
    STR_GENRE_LEVEL = "genreLevel"

    # タグごとの商品数
    STR_TAG_INFORMATION = "TagInformation"
    STR_TAG_GROUP = "tagGroup"  # ユーザの入力したジャンルIDに紐づくタググループの情報
    STR_TAG_GROUP_NAME = "tagGroupName"
    STR_TAG_GROUP_ID = "tagGroupId"
    STR_TAGS = "tags"  # <tags>～</tags>の中に複数の<tag>～</tag>
    STR_TAG = "tag"
    STR_TAG_ID = "tagId"
    STR_TAG_NAME = "tagName"
    STR_PARENT_TAG_ID = "parentTagId"
    STR_ITEM_COUNT = "itemCount"
