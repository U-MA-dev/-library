from os import path

import requests
import yaml
from constants import commonConstants as cc
from constants.utility import isEmpty
from ichibaItem.constants.parameter import InputParameter as ip
from ichibaItem.constants.parameter import OutputParameter as op
from ichibaItem.model.inputmodel import SearchConditionModel
from ichibaItem.model.outputmodel import \
    EntireModel, ItemModel, GenreModel, TagGroupModel, \
    TagModel, ParentGenreModel, CurrentGenreModel, ChildGenreModel


CONFIG_DIR = path.abspath(path.join(path.dirname(__file__), "..", "config"))
CONFIG_FILE = "rakutenApi.yaml"


class SourceManager():
    def __init__(self, APPLICATION_ID, AFFILIATE_ID):
        config_file = path.join(CONFIG_DIR, CONFIG_FILE)
        with open(config_file, "r") as f:
            data = yaml.safe_load(f)
            self.application_id = APPLICATION_ID
            self.affiliate_id = AFFILIATE_ID
            self.format = data["rakuten_api"]["format"]
            self.base_url = data["rakuten_api"]["ichiba_item"]["base_url"]

    def fetch_search_info(
            self, input_model: SearchConditionModel) -> EntireModel:
        """
        SearchConditionModelに検索条件を入れてください。
        """
        url = self.__generate_url(input_model)
        response = requests.get(url)
        response.raise_for_status()
        output_model = self.__convert_output_model(response)
        return output_model

    def __convert_output_model(
            self, response: requests.Response) -> EntireModel:
        """
        requests.ResponseをEntireIndoModelに変換します。
        """

        output_model = EntireModel()

        # 全体情報
        entire_data = response.json()
        output_model.count = entire_data[op.STR_COUNT]
        output_model.page = entire_data[op.STR_PAGE]
        output_model.first = entire_data[op.STR_FIRST]
        output_model.last = entire_data[op.STR_LAST]
        output_model.hits = entire_data[op.STR_HITS]
        output_model.carrier = entire_data[op.STR_CARRIER]
        output_model.page_count = entire_data[op.STR_PAGE_COUNT]
        output_model.item_model_list = []
        output_model.genre_model_list = []
        output_model.tag_model_list = []

        # 商品情報
        for item_data in entire_data[op.STR_ITEMS]:
            item_data = item_data[op.STR_ITEM]

            item_model = ItemModel()
            item_model.item_name = item_data[op.STR_ITEM_NAME]
            item_model.catchcopy = item_data[op.STR_CATCHCOPY]
            item_model.item_code = item_data[op.STR_ITEM_CODE]
            item_model.item_price = item_data[op.STR_ITEM_PRICE]
            item_model.item_caption = item_data[op.STR_ITEM_CAPTION]
            item_model.item_url = item_data[op.STR_ITEM_URL]
            item_model.affiliate_url = item_data[op.STR_AFFILIATE_URL]
            item_model.image_flag = item_data[op.STR_IMAGE_FLAG]

            # 画像url
            item_model.small_image_urls = \
                [image[op.STR_IMAGE_URL]
                 for image in item_data[op.STR_SMALL_IMAGE_URLS]]
            item_model.medium_image_urls = \
                [image[op.STR_IMAGE_URL]
                 for image in item_data[op.STR_MEDIUM_IMAGE_URLS]]

            item_model.availability = item_data[op.STR_AVAILABILITY]
            item_model.tax_flag = item_data[op.STR_TAX_FLAG]
            item_model.postage_flag = item_data[op.STR_POSTAGE_FLAG]
            item_model.credit_card_flag = \
                item_data[op.STR_CREDIT_CARD_FLAG]
            item_model.shop_of_the_year_flag = \
                item_data[op.STR_SHOP_OF_THE_YEAR_FLAG]
            item_model.ship_over_seas_flag = \
                item_data[op.STR_SHIP_OVER_SEAS_FLAG]
            item_model.ship_over_seas_area = \
                item_data[op.STR_SHIP_OVER_SEAS_AREA]
            item_model.asuraku_flag = item_data[op.STR_ASURAKU_FLAG]
            item_model.asuraku_closing_time = \
                item_data[op.STR_ASURAKU_CLOSING_TIME]
            item_model.asuraku_area = item_data[op.STR_ASURAKU_AREA]
            item_model.affiliate_rate = item_data[op.STR_AFFILIATE_RATE]
            item_model.start_time = item_data[op.STR_START_TIME]
            item_model.end_time = item_data[op.STR_END_TIME]
            item_model.review_count = item_data[op.STR_REVIEW_COUNT]
            item_model.review_average = item_data[op.STR_REVIEW_AVERAGE]
            item_model.point_rate = item_data[op.STR_POINT_RATE]
            item_model.point_rate_start_time = \
                item_data[op.STR_POINT_RATE_START_TIME]
            item_model.point_rate_end_time = \
                item_data[op.STR_POINT_RATE_END_TIME]
            item_model.gift_flag = item_data[op.STR_GIFT_FLAG]
            item_model.shop_name = item_data[op.STR_SHOP_NAME]
            item_model.shop_code = item_data[op.STR_SHOP_CODE]
            item_model.shop_url = item_data[op.STR_SHOP_URL]
            item_model.shop_affiliate_url = \
                item_data[op.STR_SHOP_AFFILIATE_URL]
            # ジャンル情報
            item_model.genre_id = item_data[op.STR_GENRE_ID]
            # タグ情報
            item_model.tag_id_list = item_data[op.STR_TAG_IDS]

            output_model.item_model_list.append(item_model)

        # ジャンルごとの商品数
        for genre_info in entire_data[op.STR_GENRE_INFORMATION]:
            genre_model = GenreModel()

            output_model.genre_model_list.append(genre_model)

            # 個別ジャンル
            # 親ジャンル
            parent_genre_data = genre_info[op.STR_PARENT][0]
            parent_genre_model = ParentGenreModel()
            parent_genre_model.genre_id = \
                parent_genre_data[op.STR_GENRE_ID]
            parent_genre_model.genre_name = \
                parent_genre_data[op.STR_GENRE_NAME]
            parent_genre_model.genre_level = \
                parent_genre_data[op.STR_GENRE_LEVEL]
            genre_model.parent_genre_model = parent_genre_model

            # 自ジャンル
            current_genre_data = genre_info[op.STR_CURRENT][0]
            current_genre_model = CurrentGenreModel()
            current_genre_model.genre_id = \
                current_genre_data[op.STR_GENRE_ID]
            current_genre_model.genre_name = \
                current_genre_data[op.STR_GENRE_NAME]
            current_genre_model.genre_level = \
                current_genre_data[op.STR_GENRE_LEVEL]
            current_genre_model.item_count = \
                current_genre_data[op.STR_ITEM_COUNT]

            genre_model.current_genre_model = current_genre_model

            # 子ジャンル
            for child_genre_data in genre_info[op.STR_CHILDREN]:
                child_genre_data = child_genre_data[op.STR_CHILD]

                child_genre_model = ChildGenreModel()
                child_genre_model.genre_id = \
                    child_genre_data[op.STR_GENRE_ID]
                child_genre_model.genre_name = \
                    child_genre_data[op.STR_GENRE_NAME]
                child_genre_model.genre_level = \
                    child_genre_data[op.STR_GENRE_LEVEL]
                child_genre_model.item_count = \
                    child_genre_data[op.STR_ITEM_COUNT]

                genre_model \
                    .child_genre_model_list.append(child_genre_model)

        # タグごとの商品数
        for tag_info in entire_data[op.STR_TAG_INFORMATION]:
            tag_group_data = tag_info[op.STR_TAG_GROUP]

            # タググループ情報
            tag_group_model = TagGroupModel()
            tag_group_model.tag_group_id = \
                tag_group_data[op.STR_TAG_GROUP_ID]
            tag_group_model.tag_group_name = \
                tag_group_data[op.STR_TAG_GROUP_NAME]
            output_model.tag_group_model_list.append(tag_group_model)

            for tag_data in tag_group_data[op.STR_TAGS]:
                tag_data = tag_data[op.STR_TAG]

                # タグ情報
                tag_model = TagModel()
                tag_model.tag_id = tag_data[op.STR_TAG_ID]
                tag_model.tag_name = tag_data[op.STR_TAG_NAME]
                tag_model.parent_tag_id = tag_data[op.STR_PARENT_TAG_ID]
                tag_model.item_count = tag_data[op.STR_ITEM_COUNT]

                tag_group_model.tag_model_list.append(tag_model)

        return output_model

    def __generate_url(self, input_model: SearchConditionModel):
        if input_model is None:
            input_model = SearchConditionModel()
        if isEmpty(input_model.format):
            input_model.format = self.format
        if isEmpty(input_model.application_id):
            input_model.application_id = self.application_id
        if isEmpty(input_model.affiliate_id):
            input_model.affiliate_id = self.affiliate_id

        generated_url_list = []
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
        if not isEmpty(input_model.format):
            generated_url_list.append(
                ip.STR_FORMAT +
                cc.STR_EQUALS +
                input_model.format)
        if not isEmpty(input_model.callback):
            generated_url_list.append(
                ip.STR_CALLBACK +
                cc.STR_EQUALS +
                input_model.callback)
        if not isEmpty(input_model.elements):
            generated_url_list.append(
                ip.STR_ELEMENTS +
                cc.STR_EQUALS +
                input_model.elements)
        if not isEmpty(input_model.format_version):
            generated_url_list.append(
                ip.STR_FORMAT_VERSION +
                cc.STR_EQUALS +
                str(input_model.format_version))
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
                str(input_model.genre_id))
        if not isEmpty(input_model.tag_id):
            generated_url_list.append(
                ip.STR_TAG_ID +
                cc.STR_EQUALS +
                str(input_model.tag_id))
        if not isEmpty(input_model.hits):
            generated_url_list.append(
                ip.STR_HITS +
                cc.STR_EQUALS +
                str(input_model.hits))
        if not isEmpty(input_model.page):
            generated_url_list.append(
                ip.STR_PAGE +
                cc.STR_EQUALS +
                str(input_model.page))
        if not isEmpty(input_model.sort):
            generated_url_list.append(
                ip.STR_SORT +
                cc.STR_EQUALS +
                input_model.sort)
        if not isEmpty(input_model.min_price):
            generated_url_list.append(
                ip.STR_MIN_PRICE +
                cc.STR_EQUALS +
                str(input_model.min_price))
        if not isEmpty(input_model.max_price):
            generated_url_list.append(
                ip.STR_MAX_PRICE +
                cc.STR_EQUALS +
                str(input_model.max_price))
        if not isEmpty(input_model.avalilability):
            generated_url_list.append(
                ip.STR_AVAILABILITY +
                cc.STR_EQUALS +
                str(input_model.avalilability))
        if not isEmpty(input_model.field):
            generated_url_list.append(
                ip.STR_FIELD +
                cc.STR_EQUALS +
                str(input_model.field))
        if not isEmpty(input_model.carrier):
            generated_url_list.append(
                ip.STR_CARRIER +
                cc.STR_EQUALS +
                str(input_model.carrier))
        if not isEmpty(input_model.image_flag):
            generated_url_list.append(
                ip.STR_IMAGE_FLAG +
                cc.STR_EQUALS +
                str(input_model.image_flag))
        if not isEmpty(input_model.or_flag):
            generated_url_list.append(
                ip.STR_OR_FLAG +
                cc.STR_EQUALS +
                str(input_model.or_flag))
        if not isEmpty(input_model.ng_keyword):
            generated_url_list.append(
                ip.STR_NG_KEYWORD +
                cc.STR_EQUALS +
                input_model.ng_keyword)
        if not isEmpty(input_model.purchase_type):
            generated_url_list.append(
                ip.STR_PURCHASE_TYPE +
                cc.STR_EQUALS +
                str(input_model.purchase_type))
        if not isEmpty(input_model.ship_overseas_flag):
            generated_url_list.append(
                ip.STR_SHIP_OVERSEAS_FLAG +
                cc.STR_EQUALS +
                str(input_model.ship_overseas_flag))
        if not isEmpty(input_model.ship_overseas_area):
            generated_url_list.append(
                ip.STR_SHIP_OVERSEAS_AREA +
                cc.STR_EQUALS +
                input_model.ship_overseas_area)
        if not isEmpty(input_model.asuraku_flag):
            generated_url_list.append(
                ip.STR_ASURAKU_FLAG +
                cc.STR_EQUALS +
                str(input_model.asuraku_flag))
        if not isEmpty(input_model.asuraku_area):
            generated_url_list.append(
                ip.STR_ASURAKU_AREA +
                cc.STR_EQUALS +
                str(input_model.asuraku_area))
        if not isEmpty(input_model.point_rate_flag):
            generated_url_list.append(
                ip.STR_POINT_RATE_FLAG +
                cc.STR_EQUALS +
                str(input_model.point_rate_flag))
        if not isEmpty(input_model.point_rate):
            generated_url_list.append(
                ip.STR_POINT_RATE +
                cc.STR_EQUALS +
                str(input_model.point_rate))
        if not isEmpty(input_model.postage_flag):
            generated_url_list.append(
                ip.STR_POSTAGE_FLAG +
                cc.STR_EQUALS +
                str(input_model.postage_flag))
        if not isEmpty(input_model.credit_card_flag):
            generated_url_list.append(
                ip.STR_CREDIT_CARD_FLAG +
                cc.STR_EQUALS +
                str(input_model.credit_card_flag))
        if not isEmpty(input_model.gift_flag):
            generated_url_list.append(
                ip.STR_GIFT_FLAG +
                cc.STR_EQUALS +
                str(input_model.gift_flag))
        if not isEmpty(input_model.has_review_flag):
            generated_url_list.append(
                ip.STR_HAS_REVIEW_FLAG +
                cc.STR_EQUALS +
                str(input_model.has_review_flag))
        if not isEmpty(input_model.max_affiliate_rate):
            generated_url_list.append(
                ip.STR_MAX_AFFILIATE_RATE +
                cc.STR_EQUALS +
                str(input_model.max_affiliate_rate))
        if not isEmpty(input_model.min_affiliate_rate):
            generated_url_list.append(
                ip.STR_MIN_AFFILIATE_RATE +
                cc.STR_EQUALS +
                str(input_model.min_affiliate_rate))
        if not isEmpty(input_model.has_movie_flag):
            generated_url_list.append(
                ip.STR_HAS_MOVIE_FLAG +
                cc.STR_EQUALS +
                str(input_model.has_movie_flag))
        if not isEmpty(input_model.pamphlet_flag):
            generated_url_list.append(
                ip.STR_PAMPHLET_FLAG +
                cc.STR_EQUALS +
                str(input_model.pamphlet_flag))
        if not isEmpty(input_model.appoint_delivery_date_flag):
            generated_url_list.append(
                ip.STR_APPOINT_DELIVERY_DATE_FLAG +
                cc.STR_EQUALS +
                str(input_model.appoint_delivery_date_flag))
        if not isEmpty(input_model.genre_infomation_flag):
            generated_url_list.append(
                ip.STR_GENRE_INFOMATION_FLAG +
                cc.STR_EQUALS +
                str(input_model.genre_infomation_flag))
        if not isEmpty(input_model.tag_information_flag):
            generated_url_list.append(
                ip.STR_TAG_INFORMATION_FLAG +
                cc.STR_EQUALS +
                str(input_model.tag_information_flag))

        parameter = cc.STR_QUESTION + cc.STR_AND.join(generated_url_list)
        url = self.base_url + parameter
        return url
