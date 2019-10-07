from os import environ, path

import requests
import yaml

from constants import commonConstants as cc
from constants.utility import isEmpty
from ichibaItem.constants.parameter import InputParameter as ip
from ichibaItem.constants.parameter import OutputParameter as op
from model.inputmodel import SearchConditionModel
from model.outputmodel import EntireInfoModel, ItemInfoModel

CONFIG_DIR = environ["CONFIG_DIR"]
CONFIG_FILE = environ["CONFIG_FILE"]
APPLICATION_ID = environ["APPLICATION_ID"]
AFFILIATE_ID = environ["AFFILIATE_ID"]


class SourceManager():
    def __init__(self):
        config_file = path.join(CONFIG_DIR, CONFIG_FILE)
        with open(config_file, "r") as f:
            data = yaml.safe_load(f)
            self.application_id = APPLICATION_ID
            self.affiliate_id = AFFILIATE_ID
            self.format = data["rakuten_api"]["format"]
            self.base_url = data["rakuten_api"]["ichiba_item"]["base_url"]

    def fetch_search_info(
            self, input_model: SearchConditionModel) -> EntireInfoModel:
        """
        SearchConditionModelに検索条件を入れてください。
        """
        url = self.__generate_url(input_model)
        response = requests.get(url)
        response.raise_for_status()
        output_model = self.__convert_output_model(response)
        return output_model

    def __convert_output_model(
            self, response: requests.Response) -> EntireInfoModel:
        """
        requests.ResponseをEntireIndoModelに変換します。
        """

        output_model = EntireInfoModel()

        # 全体情報
        entire_data = response.json()
        output_model.count = entire_data[op.STR_COUNT]
        output_model.page = entire_data[op.STR_PAGE]
        output_model.first = entire_data[op.STR_FIRST]
        output_model.last = entire_data[op.STR_LAST]
        output_model.hits = entire_data[op.STR_HITS]
        output_model.carrir = entire_data[op.STR_CARRIER]
        output_model.page_count = entire_data[op.STR_PAGE_COUNT]
        output_model.item_info_model_list = []
        output_model.genre_info_model_list = []
        output_model.tag_info_model_list = []

        # 商品情報
        for item_data in entire_data[op.STR_ITEMS]:
            item_data = item_data[op.STR_ITEM]

            item_info_model = ItemInfoModel()
            item_info_model.item_name = item_data[op.STR_ITEM_NAME]
            item_info_model.catchcopy = item_data[op.STR_CATCHCOPY]
            item_info_model.item_code = item_data[op.STR_ITEM_CODE]
            item_info_model.item_price = item_data[op.STR_ITEM_PRICE]
            item_info_model.item_caption = item_data[op.STR_ITEM_CAPTION]
            item_info_model.item_url = item_data[op.STR_ITEM_URL]
            item_info_model.affiliate_url = item_data[op.STR_AFFILIATE_URL]
            item_info_model.image_flag = item_data[op.STR_IMAGE_FLAG]

            # 画像url
            item_info_model.small_image_urls = \
                [image[op.STR_IMAGE_URL]
                 for image in item_data[op.STR_SMALL_IMAGE_URLS]]
            item_info_model.medium_image_urls = \
                [image[op.STR_IMAGE_URL]
                 for image in item_data[op.STR_MEDIUM_IMAGE_URLS]]

            item_info_model.availability = item_data[op.STR_AVAILABILITY]
            item_info_model.tax_flag = item_data[op.STR_TAX_FLAG]
            item_info_model.postage_flag = item_data[op.STR_POSTAGE_FLAG]
            item_info_model.credit_card_flag = \
                item_data[op.STR_CREDIT_CARD_FLAG]
            item_info_model.shop_of_the_year_flag = \
                item_data[op.STR_SHOP_OF_THE_YEAR_FLAG]
            item_info_model.ship_over_seas_flag = \
                item_data[op.STR_SHIP_OVER_SEAS_FLAG]
            item_info_model.asuraku_flag = item_data[op.STR_ASURAKU_FLAG]
            item_info_model.asuraku_closing_time = \
                item_data[op.STR_ASURAKU_CLOSING_TIME]
            item_info_model.asuraku_area = item_data[op.STR_ASURAKU_AREA]
            item_info_model.affiliate_rate = item_data[op.STR_AFFILIATE_RATE]
            item_info_model.start_time = item_data[op.STR_START_TIME]
            item_info_model.end_time = item_data[op.STR_END_TIME]
            item_info_model.review_count = item_data[op.STR_REVIEW_COUNT]
            item_info_model.review_average = item_data[op.STR_REVIEW_AVERAGE]
            item_info_model.point_rate = item_data[op.STR_POINT_RATE]
            item_info_model.point_rate_start_time = \
                item_data[op.STR_POINT_RATE_START_TIME]
            item_info_model.point_rate_end_time = \
                item_data[op.STR_POINT_RATE_END_TIME]
            item_info_model.gift_flag = item_data[op.STR_GIFT_FLAG]
            item_info_model.shop_name = item_data[op.STR_SHOP_NAME]
            item_info_model.shop_url = item_data[op.STR_SHOP_URL]
            item_info_model.shop_affiliate_url = \
                item_data[op.STR_SHOP_AFFILIATE_URL]
            # ジャンル情報
            item_info_model.genre_id = item_data[op.STR_GENRE_ID]
            # タグ情報
            item_info_model.tag_id_list = item_data[op.STR_TAG_IDS]

            output_model.item_info_model_list.append(item_info_model)

        # 下記情報は使用されていない?
        # ジャンルごとの商品数
        # タグごとの商品数

        return output_model

    def __generate_url(self, input_model: SearchConditionModel):
        if isEmpty(input_model.format):
            input_model.format = self.format
        if isEmpty(input_model.application_id):
            input_model.application_id = self.application_id
        if isEmpty(input_model.affiliate_id):
            input_model.affiliate_id = self.affiliate_id

        generated_url_list = []
        generated_url_list.append(
            ip.STR_FORMAT +
            cc.STR_EQUALS +
            input_model.format
        )
        generated_url_list.append(
            ip.STR_APPLICATION_ID +
            cc.STR_EQUALS +
            input_model.application_id
        )
        if not isEmpty(input_model.affiliate_id):
            generated_url_list.append(
                ip.STR_AFFILIATE_ID +
                cc.STR_EQUALS +
                input_model.affiliate_id)
        if not isEmpty(input_model.keyword):
            generated_url_list.append(
                ip.STR_KEYWORD +
                cc.STR_EQUALS +
                input_model.keyword)
        if not isEmpty(input_model.shop_code):
            generated_url_list.append(
                ip.STR_SHOP_CODE +
                cc.STR_EQUALS +
                input_model.shop_code)
        if not isEmpty(input_model.item_code):
            generated_url_list.append(
                ip.STR_ITEM_CODE +
                cc.STR_EQUALS +
                input_model.item_code)
        if not isEmpty(input_model.genre_id):
            generated_url_list.append(
                ip.STR_GENRE_ID +
                cc.STR_EQUALS +
                input_model.genre_id)
        if not isEmpty(input_model.tag_id):
            generated_url_list.append(
                ip.STR_TAG_ID +
                cc.STR_EQUALS +
                input_model.tag_id)
        if not isEmpty(input_model.hits):
            generated_url_list.append(
                ip.STR_HITS +
                cc.STR_EQUALS +
                input_model.hits)
        if not isEmpty(input_model.page):
            generated_url_list.append(
                ip.STR_PAGE +
                cc.STR_EQUALS +
                input_model.page)
        if not isEmpty(input_model.sort):
            generated_url_list.append(
                ip.STR_SORT +
                cc.STR_EQUALS +
                input_model.sort)
        if not isEmpty(input_model.min_price):
            generated_url_list.append(
                ip.STR_MIN_PRICE +
                cc.STR_EQUALS +
                input_model.min_price)
        if not isEmpty(input_model.max_price):
            generated_url_list.append(
                ip.STR_MAX_PRICE +
                cc.STR_EQUALS +
                input_model.max_price)
        if not isEmpty(input_model.avalilability):
            generated_url_list.append(
                ip.STR_AVAILABILITY +
                cc.STR_EQUALS +
                input_model.avalilability)
        if not isEmpty(input_model.field):
            generated_url_list.append(
                ip.STR_FIELD +
                cc.STR_EQUALS +
                input_model.field)
        if not isEmpty(input_model.carrier):
            generated_url_list.append(
                ip.STR_CARRIER +
                cc.STR_EQUALS +
                input_model.carrier)
        if not isEmpty(input_model.image_flag):
            generated_url_list.append(
                ip.STR_IMAGE_FLAG +
                cc.STR_EQUALS +
                input_model.image_flag)
        if not isEmpty(input_model.or_flag):
            generated_url_list.append(
                ip.STR_OR_FLAG +
                cc.STR_EQUALS +
                input_model.or_flag)
        if not isEmpty(input_model.ng_keyword):
            generated_url_list.append(
                ip.STR_NG_KEYWORD +
                cc.STR_EQUALS +
                input_model.ng_keyword)
        if not isEmpty(input_model.purchase_type):
            generated_url_list.append(
                ip.STR_PURCHASE_TYPE +
                cc.STR_EQUALS +
                input_model.purchase_type)
        if not isEmpty(input_model.ship_overseas_flag):
            generated_url_list.append(
                ip.STR_SHIP_OVERSEAS_FLAG +
                cc.STR_EQUALS +
                input_model.ship_overseas_flag)
        if not isEmpty(input_model.ship_overseas_area):
            generated_url_list.append(
                ip.STR_SHIP_OVERSEAS_AREA +
                cc.STR_EQUALS +
                input_model.ship_overseas_area)
        if not isEmpty(input_model.asuraku_flag):
            generated_url_list.append(
                ip.STR_ASURAKU_FLAG +
                cc.STR_EQUALS +
                input_model.asuraku_flag)
        if not isEmpty(input_model.asuraku_area):
            generated_url_list.append(
                ip.STR_ASURAKU_AREA +
                cc.STR_EQUALS +
                input_model.asuraku_area)
        if not isEmpty(input_model.point_rate_flag):
            generated_url_list.append(
                ip.STR_POINT_RATE_FLAG +
                cc.STR_EQUALS +
                input_model.point_rate_flag)
        if not isEmpty(input_model.point_rate):
            generated_url_list.append(
                ip.STR_POINT_RATE +
                cc.STR_EQUALS +
                input_model.point_rate)
        if not isEmpty(input_model.postage_flag):
            generated_url_list.append(
                ip.STR_POSTAGE_FLAG +
                cc.STR_EQUALS +
                input_model.postage_flag)
        if not isEmpty(input_model.credit_card_flag):
            generated_url_list.append(
                ip.STR_CREDIT_CARD_FLAG +
                cc.STR_EQUALS +
                input_model.credit_card_flag)
        if not isEmpty(input_model.gift_flag):
            generated_url_list.append(
                ip.STR_GIFT_FLAG +
                cc.STR_EQUALS +
                input_model.gift_flag)
        if not isEmpty(input_model.has_review_flag):
            generated_url_list.append(
                ip.STR_HAS_REVIEW_FLAG +
                cc.STR_EQUALS +
                input_model.has_review_flag)
        if not isEmpty(input_model.max_affiliate_rate):
            generated_url_list.append(
                ip.STR_MAX_AFFILIATE_RATE +
                cc.STR_EQUALS +
                input_model.max_affiliate_rate)
        if not isEmpty(input_model.min_affiliate_rate):
            generated_url_list.append(
                ip.STR_MIN_AFFILIATE_RATE +
                cc.STR_EQUALS +
                input_model.min_affiliate_rate)
        if not isEmpty(input_model.has_movie_flag):
            generated_url_list.append(
                ip.STR_HAS_MOVIE_FLAG +
                cc.STR_EQUALS +
                input_model.has_movie_flag)
        if not isEmpty(input_model.pamphlet_flag):
            generated_url_list.append(
                ip.STR_PAMPHLET_FLAG +
                cc.STR_EQUALS +
                input_model.pamphlet_flag)
        if not isEmpty(input_model.appoint_delivery_date_flag):
            generated_url_list.append(
                ip.STR_APPOINT_DELIVERY_DATE_FLAG +
                cc.STR_EQUALS +
                input_model.appoint_delivery_date_flag)
        if not isEmpty(input_model.genre_infomation_flag):
            generated_url_list.append(
                ip.STR_GENRE_INFOMATION_FLAG +
                cc.STR_EQUALS +
                input_model.genre_infomation_flag)
        if not isEmpty(input_model.tag_information_flag):
            generated_url_list.append(
                ip.STR_TAG_INFORMATION_FLAG +
                cc.STR_EQUALS +
                input_model.tag_information_flag)

        parameter = cc.STR_QUESTION + cc.STR_AND.join(generated_url_list)
        url = self.base_url + parameter
        return url
