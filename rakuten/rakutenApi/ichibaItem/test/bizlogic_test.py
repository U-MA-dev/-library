# pylint: disable=line-too-long
# flake8: noqa

import json
from os import path
import unittest
from unittest.mock import MagicMock

import yaml
from requests import Response

from ichibaItem.bizlogic import SourceManager
from ichibaItem.model.inputmodel import SearchConditionModel
from ichibaItem.model.outputmodel import \
    EntireModel, ItemModel, GenreModel, TagGroupModel, \
    TagModel, ParentGenreModel, CurrentGenreModel, ChildGenreModel


RESORCE_FOLDER = path.abspath("resorce")
APPLICATION_ID = "test_application_id"
AFFILIATE_ID = "test_affiliate_id"


class TestConvertOutputModel(unittest.TestCase):

    def test_json_data_single(self):
        response_json = None
        with open(path.join(
                RESORCE_FOLDER, "TestConvertOutputModel_single.json")) as f:
            response_json = json.loads(f.read())

        # モック設定
        response_moc = Response()
        response_moc.json = MagicMock(return_value=response_json)

        # テスト実施
        source_manager = SourceManager(APPLICATION_ID, AFFILIATE_ID)
        entire_model: EntireModel = \
            source_manager._SourceManager__convert_output_model(response_moc)

        self.assertEqual(entire_model.count, 1303)
        self.assertEqual(entire_model.page, 1)
        self.assertEqual(entire_model.first, 1)
        self.assertEqual(entire_model.last, 1)
        self.assertEqual(entire_model.hits, 1)
        self.assertEqual(entire_model.carrier, 0)
        self.assertEqual(entire_model.page_count, 100)
        self.assertEqual(len(entire_model.item_model_list), 1)
        self.assertEqual(len(entire_model.genre_model_list), 1)
        self.assertEqual(len(entire_model.tag_group_model_list), 1)

        # 商品検索結果モデル1
        item_model1: ItemModel = \
            entire_model.item_model_list[0]
        self.assertEqual(item_model1.item_name,
                         "【中古】 TOEFL\u3000TEST対策iBTスピーキング ／川端淳司【著】 【中古】afb")
        self.assertEqual(item_model1.catchcopy,
                         "")
        self.assertEqual(item_model1.item_code,
                         "bookoffonline:11274473")
        self.assertEqual(item_model1.item_price,
                         822)
        self.assertEqual(item_model1.item_caption,
                         "川端淳司【著】販売会社/発売会社：テイエス企画/テイエス企画発売年月日：2006/08/07JAN：9784887840706／／付属品〜CD3枚付")
        self.assertEqual(item_model1.item_url,
                         "https://hb.afl.rakuten.co.jp/hgc/g00rc686.s3lt7e53.g00rc686.s3lt8845/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fbookoffonline%2F0015504910%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fbookoffonline%2Fi%2F11274473%2F")
        self.assertEqual(item_model1.affiliate_url,
                         "https://hb.afl.rakuten.co.jp/hgc/g00rc686.s3lt7e53.g00rc686.s3lt8845/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fbookoffonline%2F0015504910%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fbookoffonline%2Fi%2F11274473%2F")
        self.assertEqual(item_model1.image_flag,
                         1)
        self.assertEqual(len(item_model1.small_image_urls),
                         1)
        self.assertEqual(item_model1.small_image_urls[0],
                         "https://thumbnail.image.rakuten.co.jp/@0_mall/bookoffonline/cabinet/223/0015504910l.jpg?_ex=64x64")
        self.assertEqual(len(item_model1.medium_image_urls),
                         1)
        self.assertEqual(item_model1.medium_image_urls[0],
                         "https://thumbnail.image.rakuten.co.jp/@0_mall/bookoffonline/cabinet/223/0015504910l.jpg?_ex=128x128")
        self.assertEqual(item_model1.availability,
                         1)
        self.assertEqual(item_model1.tax_flag,
                         0)
        self.assertEqual(item_model1.postage_flag,
                         1)
        self.assertEqual(item_model1.credit_card_flag,
                         1)
        self.assertEqual(item_model1.shop_of_the_year_flag,
                         0)
        self.assertEqual(item_model1.ship_over_seas_flag,
                         0)
        self.assertEqual(item_model1.ship_over_seas_area,
                         "")
        self.assertEqual(item_model1.asuraku_flag,
                         0)
        self.assertEqual(item_model1.asuraku_area,
                         "")
        self.assertEqual(item_model1.affiliate_rate,
                         3)
        self.assertEqual(item_model1.start_time,
                         "")
        self.assertEqual(item_model1.end_time,
                         "")
        self.assertEqual(item_model1.review_count,
                         0)
        self.assertEqual(item_model1.review_average,
                         0)
        self.assertEqual(item_model1.point_rate,
                         1)
        self.assertEqual(item_model1.point_rate_start_time,
                         "")
        self.assertEqual(item_model1.point_rate_end_time,
                         "")
        self.assertEqual(item_model1.gift_flag,
                         0)
        self.assertEqual(item_model1.shop_name,
                         "ブックオフオンライン楽天市場店")
        self.assertEqual(item_model1.shop_code,
                         "bookoffonline")
        self.assertEqual(item_model1.shop_url,
                         "https://hb.afl.rakuten.co.jp/hgc/g00rc686.s3lt7e53.g00rc686.s3lt8845/?pc=https%3A%2F%2Fwww.rakuten.co.jp%2Fbookoffonline%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fbookoffonline%2F")
        self.assertEqual(item_model1.shop_affiliate_url,
                         "https://hb.afl.rakuten.co.jp/hgc/g00rc686.s3lt7e53.g00rc686.s3lt8845/?pc=https%3A%2F%2Fwww.rakuten.co.jp%2Fbookoffonline%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fbookoffonline%2F")
        self.assertEqual(item_model1.genre_id,
                         "208714")
        self.assertEqual(len(item_model1.tag_id_list),
                         0)

        # ジャンル情報検索結果モデル1
        genre_model1: GenreModel = \
            entire_model.genre_model_list[0]
        self.assertEqual(len(genre_model1.child_genre_model_list), 1)

        # 親ジャンル
        parent_genre_model1: ParentGenreModel = genre_model1.parent_genre_model
        self.assertEqual(parent_genre_model1.genre_id, "208709")
        self.assertEqual(parent_genre_model1.genre_name, "語学関係資格")
        self.assertEqual(parent_genre_model1.genre_level, "3")

        # 現ジャンル
        current_genre_model1: CurrentGenreModel = genre_model1.current_genre_model
        self.assertEqual(current_genre_model1.genre_id, "208714")
        self.assertEqual(current_genre_model1.genre_name, "その他")
        self.assertEqual(current_genre_model1.genre_level, "4")
        self.assertEqual(current_genre_model1.item_count, "1303")

        # 子ジャンル
        child_genre_model1: ChildGenreModel = genre_model1.child_genre_model_list[0]
        self.assertEqual(child_genre_model1.genre_id, "566035")
        self.assertEqual(child_genre_model1.genre_name, "その他")
        self.assertEqual(child_genre_model1.genre_level, "3")
        self.assertEqual(child_genre_model1.item_count, "5160")

        # タググループ情報検索結果モデル1
        tag_group_model1: TagGroupModel = \
            entire_model.tag_group_model_list[0]
        self.assertEqual(tag_group_model1.tag_group_id, 1001050)
        self.assertEqual(tag_group_model1.tag_group_name, "限定特典")
        self.assertEqual(len(tag_group_model1.tag_model_list), 1)

        # タグ情報検索結果モデル1
        tag_model: TagModel = \
            tag_group_model1.tag_model_list[0]
        self.assertEqual(tag_model.tag_id, 1011605)
        self.assertEqual(tag_model.tag_name, "初回版・特装版")
        self.assertEqual(tag_model.parent_tag_id, 0)
        self.assertEqual(tag_model.item_count, 0)


    def test_json_data_multi(self):
        response_json = None
        with open(path.join(
                RESORCE_FOLDER, "TestConvertOutputModel_multi.json")) as f:
            response_json = json.loads(f.read())

        # モック設定
        response_moc = Response()
        response_moc.json = MagicMock(return_value=response_json)

        # テスト実施
        sourceManager = SourceManager(APPLICATION_ID, AFFILIATE_ID)
        entire_model: EntireModel = \
            sourceManager._SourceManager__convert_output_model(response_moc)

        self.assertEqual(entire_model.count, 164282)
        self.assertEqual(entire_model.page, 1)
        self.assertEqual(entire_model.first, 1)
        self.assertEqual(entire_model.last, 3)
        self.assertEqual(entire_model.hits, 3)
        self.assertEqual(entire_model.carrier, 0)
        self.assertEqual(entire_model.page_count, 100)
        self.assertEqual(len(entire_model.item_model_list), 3)
        self.assertEqual(len(entire_model.genre_model_list), 1)
        self.assertEqual(len(entire_model.tag_group_model_list), 3)

        # 商品検索結果モデル1
        item_model1: ItemModel = \
            entire_model.item_model_list[0]
        self.assertEqual(item_model1.item_name,
                         "【中古】 TOEFL\u3000TEST対策iBTスピーキング ／川端淳司【著】 【中古】afb")
        self.assertEqual(item_model1.catchcopy,
                         "")
        self.assertEqual(item_model1.item_code,
                         "bookoffonline:11274473")
        self.assertEqual(item_model1.item_price,
                         822)
        self.assertEqual(item_model1.item_caption,
                         "川端淳司【著】販売会社/発売会社：テイエス企画/テイエス企画発売年月日：2006/08/07JAN：9784887840706／／付属品〜CD3枚付")
        self.assertEqual(item_model1.item_url,
                         "https://hb.afl.rakuten.co.jp/hgc/g00rc686.s3lt7e53.g00rc686.s3lt8845/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fbookoffonline%2F0015504910%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fbookoffonline%2Fi%2F11274473%2F")
        self.assertEqual(item_model1.affiliate_url,
                         "https://hb.afl.rakuten.co.jp/hgc/g00rc686.s3lt7e53.g00rc686.s3lt8845/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fbookoffonline%2F0015504910%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fbookoffonline%2Fi%2F11274473%2F")
        self.assertEqual(item_model1.image_flag,
                         1)
        self.assertEqual(len(item_model1.small_image_urls),
                         1)
        self.assertEqual(item_model1.small_image_urls[0],
                         "https://thumbnail.image.rakuten.co.jp/@0_mall/bookoffonline/cabinet/223/0015504910l.jpg?_ex=64x64")
        self.assertEqual(len(item_model1.medium_image_urls),
                         1)
        self.assertEqual(item_model1.medium_image_urls[0],
                         "https://thumbnail.image.rakuten.co.jp/@0_mall/bookoffonline/cabinet/223/0015504910l.jpg?_ex=128x128")
        self.assertEqual(item_model1.availability,
                         1)
        self.assertEqual(item_model1.tax_flag,
                         0)
        self.assertEqual(item_model1.postage_flag,
                         1)
        self.assertEqual(item_model1.credit_card_flag,
                         1)
        self.assertEqual(item_model1.shop_of_the_year_flag,
                         0)
        self.assertEqual(item_model1.ship_over_seas_flag,
                         0)
        self.assertEqual(item_model1.ship_over_seas_area,
                         "")
        self.assertEqual(item_model1.asuraku_flag,
                         0)
        self.assertEqual(item_model1.asuraku_area,
                         "")
        self.assertEqual(item_model1.affiliate_rate,
                         3)
        self.assertEqual(item_model1.start_time,
                         "")
        self.assertEqual(item_model1.end_time,
                         "")
        self.assertEqual(item_model1.review_count,
                         0)
        self.assertEqual(item_model1.review_average,
                         0)
        self.assertEqual(item_model1.point_rate,
                         1)
        self.assertEqual(item_model1.point_rate_start_time,
                         "")
        self.assertEqual(item_model1.point_rate_end_time,
                         "")
        self.assertEqual(item_model1.gift_flag,
                         0)
        self.assertEqual(item_model1.shop_name,
                         "ブックオフオンライン楽天市場店")
        self.assertEqual(item_model1.shop_code,
                         "bookoffonline")
        self.assertEqual(item_model1.shop_url,
                         "https://hb.afl.rakuten.co.jp/hgc/g00rc686.s3lt7e53.g00rc686.s3lt8845/?pc=https%3A%2F%2Fwww.rakuten.co.jp%2Fbookoffonline%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fbookoffonline%2F")
        self.assertEqual(item_model1.shop_affiliate_url,
                         "https://hb.afl.rakuten.co.jp/hgc/g00rc686.s3lt7e53.g00rc686.s3lt8845/?pc=https%3A%2F%2Fwww.rakuten.co.jp%2Fbookoffonline%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fbookoffonline%2F")
        self.assertEqual(item_model1.genre_id,
                         "208714")
        self.assertEqual(len(item_model1.tag_id_list),
                         0)

        # 商品検索結果モデル2
        item_model2: ItemModel = \
            entire_model.item_model_list[1]
        self.assertEqual(item_model2.item_name,
                         "【バーゲン本】瞬感英単語600点突破最初の450語ーTOEIC\u3000TEST [ 栗本\u3000孝子 ]")
        self.assertEqual(item_model2.catchcopy,
                         "【楽天ブックスならいつでも送料無料】")
        self.assertEqual(item_model2.item_code,
                         "book:19012960")
        self.assertEqual(item_model2.item_price,
                         440)
        self.assertEqual(item_model2.item_caption,
                         "栗本\u3000孝子 （株）誠文堂新光社バーゲン本,バーゲンブック,送料無料,半額,50%OFF,タイムセール シュンカンエイタンゴ600テントッパサイショノ450ゴーTOEIC\u3000TEST クリモト\u3000タカコ 予約締切日：2018年02月06日 ページ数：271p サイズ：単行本 ISBN：4528189544376 本 語学・学習参考書 語学関係資格 TOEIC 資格・検定 語学関係資格 TOEIC バーゲン本 語学・学習参考書")
        self.assertEqual(item_model2.item_url,
                         "https://hb.afl.rakuten.co.jp/hgc/g00q0726.s3lt72b0.g00q0726.s3lt8afe/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fbook%2F15351909%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fbook%2Fi%2F19012960%2F")
        self.assertEqual(item_model2.affiliate_url,
                         "https://hb.afl.rakuten.co.jp/hgc/g00q0726.s3lt72b0.g00q0726.s3lt8afe/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fbook%2F15351909%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fbook%2Fi%2F19012960%2F")
        self.assertEqual(item_model2.image_flag,
                         1)
        self.assertEqual(len(item_model2.small_image_urls),
                         3)
        self.assertEqual(item_model2.small_image_urls[0],
                         "https://thumbnail.image.rakuten.co.jp/@0_mall/book/cabinet/4376/4528189544376.jpg?_ex=64x64")
        self.assertEqual(item_model2.small_image_urls[1],
                         "https://thumbnail.image.rakuten.co.jp/@0_mall/book/cabinet/4376/4528189544376_2.jpg?_ex=64x64")
        self.assertEqual(item_model2.small_image_urls[2],
                         "https://thumbnail.image.rakuten.co.jp/@0_mall/book/cabinet/4376/4528189544376_3.jpg?_ex=64x64")
        self.assertEqual(len(item_model2.medium_image_urls),
                         3)
        self.assertEqual(item_model2.medium_image_urls[0],
                         "https://thumbnail.image.rakuten.co.jp/@0_mall/book/cabinet/4376/4528189544376.jpg?_ex=128x128")
        self.assertEqual(item_model2.medium_image_urls[1],
                         "https://thumbnail.image.rakuten.co.jp/@0_mall/book/cabinet/4376/4528189544376_2.jpg?_ex=128x128")
        self.assertEqual(item_model2.medium_image_urls[2],
                         "https://thumbnail.image.rakuten.co.jp/@0_mall/book/cabinet/4376/4528189544376_3.jpg?_ex=128x128")
        self.assertEqual(item_model2.availability,
                         1)
        self.assertEqual(item_model2.tax_flag,
                         0)
        self.assertEqual(item_model2.postage_flag,
                         0)
        self.assertEqual(item_model2.credit_card_flag,
                         1)
        self.assertEqual(item_model2.shop_of_the_year_flag,
                         0)
        self.assertEqual(item_model2.ship_over_seas_flag,
                         0)
        self.assertEqual(item_model2.ship_over_seas_area,
                         "")
        self.assertEqual(item_model2.asuraku_flag,
                         0)
        self.assertEqual(item_model2.asuraku_area,
                         "")
        self.assertEqual(item_model2.affiliate_rate,
                         3)
        self.assertEqual(item_model2.start_time,
                         "2019-10-04 20:00")
        self.assertEqual(item_model2.end_time,
                         "2019-10-11 01:59")
        self.assertEqual(item_model2.review_count,
                         6)
        self.assertEqual(item_model2.review_average,
                         4.5)
        self.assertEqual(item_model2.point_rate,
                         1)
        self.assertEqual(item_model2.point_rate_start_time,
                         "")
        self.assertEqual(item_model2.point_rate_end_time,
                         "")
        self.assertEqual(item_model2.gift_flag,
                         0)
        self.assertEqual(item_model2.shop_name,
                         "楽天ブックス")
        self.assertEqual(item_model2.shop_code,
                         "book")
        self.assertEqual(item_model2.shop_url,
                         "https://hb.afl.rakuten.co.jp/hgc/g00q0726.s3lt72b0.g00q0726.s3lt8afe/?pc=https%3A%2F%2Fwww.rakuten.co.jp%2Fbook%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fbook%2F")
        self.assertEqual(item_model2.shop_affiliate_url,
                         "https://hb.afl.rakuten.co.jp/hgc/g00q0726.s3lt72b0.g00q0726.s3lt8afe/?pc=https%3A%2F%2Fwww.rakuten.co.jp%2Fbook%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fbook%2F")
        self.assertEqual(item_model2.genre_id,
                         "208883")
        self.assertEqual(len(item_model2.tag_id_list),
                         0)

        # 商品検索結果モデル3
        item_model3: ItemModel = \
            entire_model.item_model_list[2]
        self.assertEqual(item_model3.item_name,
                         "【中古】 新TOEIC\u3000TEST\u3000900点特急 パート5＆6 / 加藤 優 / 朝日新聞出版 [単行本]【メール便送料無料】【あす楽対応】")
        self.assertEqual(item_model3.catchcopy,
                         "【メール便送料無料、通常24時間以内出荷】")
        self.assertEqual(item_model3.item_code,
                         "comicset:11623705")
        self.assertEqual(item_model3.item_price,
                         323)
        self.assertEqual(item_model3.item_caption,
                         "著者：加藤 優出版社：朝日新聞出版サイズ：単行本ISBN-10：402330977xISBN-13：9784023309777■こちらの商品もオススメです ● 新TOEIC\u3000test読解特急 1駅1題 / 神崎 正哉, TEX加藤, Daniel Warriner / 朝日新聞出版 [新書] ● 新TOEIC\u3000test英文法出るとこだけ！ 直前5日間で100点差がつく27の鉄則 / 小石 裕子 / アルク [単行本] ● 新TOEIC\u3000TEST出る単特急金のフレーズ / TEX加藤 / 朝日新聞出版 [新書] ● 新TOEIC\u3000test文法特急 1駅1題 / 花田 徹也 / 朝日新聞出版 [新書] ● 新TOEIC\u3000TESTパート3・4特急実力養成ドリル / 神崎正哉, Daniel Warriner / 朝日新聞出版 [単行本] ● 新TOEIC\u3000TESTパート1・2特急2出る問難問200 / 森田鉄也 / 朝日新聞出版 [単行本] ● 中学3年間の英語でTOEICテスト630点を取る本 / 小池真由美 / フォレスト出版 [単行本（ソフトカバー）] ● 新TOEIC\u3000TEST文法特急 2（急所アタック編） / 花田徹也 / 朝日新聞出版 [単行本] ● 新TOEICテスト中学英語リスニングで600点！ / 小石 裕子 / アルク [単行本] ● 新TOEIC\u3000TEST読解特急 5（ダブルパッセージ編） / 神崎正哉, TEX加藤, Daniel Warriner / 朝日新聞出版 [単行本] ● イタリアの缶詰 おいしくて・たのしくて・にぎやか / 内田 洋子 / 大和書房 [単行本] ● 新TOEIC\u3000TEST読解特急 2（スピード強化編） / 神崎正哉, TEX加藤, ダニエル・ワーリナ / 朝日新聞出版 [新書] ■通常24時間以内に出荷可能です。■メール便は、1冊から送料無料です。※宅配便の場合、2,500円以上送料無料です。※あす楽ご希望の方は、宅配便をご選択下さい。※「代引き」ご希望の方は宅配便をご選択下さい。■ただいま、しおり、カレンダーをプレゼントしております。■お急ぎの方は「もったいない本舗\u3000お急ぎ便店」をご利用ください。最短翌日配送、手数料198円から■まとめ買いの方は「もったいない本舗\u3000おまとめ店」がお買い得です。■中古品ではございますが、良好なコンディションです。決済は、クレジットカード、代引き等、各種決済方法がご利用可能です。■万が一品質に不備が有った場合は、返金対応。■クリーニング済み。■商品画像に「帯」が付いているものがありますが、中古品のため、実際の商品には付いていない場合がございます。■”s1、s2”などの番号は、弊社管理番号です。どちらでもご購入いただけます。■商品状態の表記につきまして・非常に良い：\u3000\u3000使用されてはいますが、\u3000\u3000非常にきれいな状態です。\u3000\u3000書き込みや線引きはありません。・良い：\u3000\u3000比較的綺麗な状態の商品です。\u3000\u3000ページやカバーに欠品はありません。\u3000\u3000文章を読むのに支障はありません。・可：\u3000\u3000文章が問題なく読める状態の商品です。\u3000\u3000マーカーやペンで書込があることがあります。\u3000\u3000商品の痛みがある場合があります。")
        self.assertEqual(item_model3.item_url,
                         "https://hb.afl.rakuten.co.jp/hgc/g00qs416.s3lt71a5.g00qs416.s3lt8ec3/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fcomicset%2F402330977x%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fcomicset%2Fi%2F11623705%2F")
        self.assertEqual(item_model3.affiliate_url,
                         "https://hb.afl.rakuten.co.jp/hgc/g00qs416.s3lt71a5.g00qs416.s3lt8ec3/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fcomicset%2F402330977x%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fcomicset%2Fi%2F11623705%2F")
        self.assertEqual(item_model3.image_flag,
                         1)
        self.assertEqual(len(item_model3.small_image_urls),
                         1)
        self.assertEqual(item_model3.small_image_urls[0],
                         "https://thumbnail.image.rakuten.co.jp/@0_mall/comicset/cabinet/05052595/bkv0dnpgyajeaqqf.jpg?_ex=64x64")
        self.assertEqual(len(item_model3.medium_image_urls),
                         1)
        self.assertEqual(item_model3.medium_image_urls[0],
                         "https://thumbnail.image.rakuten.co.jp/@0_mall/comicset/cabinet/05052595/bkv0dnpgyajeaqqf.jpg?_ex=128x128")
        self.assertEqual(item_model3.availability,
                         1)
        self.assertEqual(item_model3.tax_flag,
                         0)
        self.assertEqual(item_model3.postage_flag,
                         1)
        self.assertEqual(item_model3.credit_card_flag,
                         1)
        self.assertEqual(item_model3.shop_of_the_year_flag,
                         1)
        self.assertEqual(item_model3.ship_over_seas_flag,
                         0)
        self.assertEqual(item_model3.ship_over_seas_area,
                         "")
        self.assertEqual(item_model3.asuraku_flag,
                         1)
        self.assertEqual(item_model3.asuraku_area,
                         "群馬県/埼玉県/千葉県/東京都/神奈川県/新潟県/富山県/石川県/福井県/山梨県/長野県/岐阜県/静岡県/愛知県/三重県/滋賀県/京都府/大阪府/兵庫県/奈良県/宮城県/山形県/福島県/茨城県/栃木県")
        self.assertEqual(item_model3.affiliate_rate,
                         3)
        self.assertEqual(item_model3.start_time,
                         "")
        self.assertEqual(item_model3.end_time,
                         "")
        self.assertEqual(item_model3.review_count,
                         0)
        self.assertEqual(item_model3.review_average,
                         0)
        self.assertEqual(item_model3.point_rate,
                         1)
        self.assertEqual(item_model3.point_rate_start_time,
                         "")
        self.assertEqual(item_model3.point_rate_end_time,
                         "")
        self.assertEqual(item_model3.gift_flag,
                         0)
        self.assertEqual(item_model3.shop_name,
                         "もったいない本舗\u3000楽天市場店")
        self.assertEqual(item_model3.shop_code,
                         "comicset")
        self.assertEqual(item_model3.shop_url,
                         "https://hb.afl.rakuten.co.jp/hgc/g00qs416.s3lt71a5.g00qs416.s3lt8ec3/?pc=https%3A%2F%2Fwww.rakuten.co.jp%2Fcomicset%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fcomicset%2F")
        self.assertEqual(item_model3.shop_affiliate_url,
                         "https://hb.afl.rakuten.co.jp/hgc/g00qs416.s3lt71a5.g00qs416.s3lt8ec3/?pc=https%3A%2F%2Fwww.rakuten.co.jp%2Fcomicset%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fcomicset%2F")
        self.assertEqual(item_model3.genre_id,
                         "208711")
        self.assertEqual(len(item_model3.tag_id_list),
                         0)

        # ジャンル情報検索結果モデル1
        genre_model1: GenreModel = \
            entire_model.genre_model_list[0]
        self.assertEqual(len(genre_model1.child_genre_model_list), 3)

        # 親ジャンル
        parent_genre_model1: ParentGenreModel = genre_model1.parent_genre_model
        self.assertEqual(parent_genre_model1.genre_id, "208709")
        self.assertEqual(parent_genre_model1.genre_name, "語学関係資格")
        self.assertEqual(parent_genre_model1.genre_level, "3")

        # 現ジャンル
        current_genre_model1: CurrentGenreModel = genre_model1.current_genre_model
        self.assertEqual(current_genre_model1.genre_id, "208714")
        self.assertEqual(current_genre_model1.genre_name, "その他")
        self.assertEqual(current_genre_model1.genre_level, "4")
        self.assertEqual(current_genre_model1.item_count, "1303")

        # 子ジャンル
        child_genre_model1: ChildGenreModel = genre_model1.child_genre_model_list[0]
        self.assertEqual(child_genre_model1.genre_id, "566035")
        self.assertEqual(child_genre_model1.genre_name, "その他")
        self.assertEqual(child_genre_model1.genre_level, "3")
        self.assertEqual(child_genre_model1.item_count, "5160")

        child_genre_model2: ChildGenreModel = genre_model1.child_genre_model_list[1]
        self.assertEqual(child_genre_model2.genre_id, "222")
        self.assertEqual(child_genre_model2.genre_name, "testGenreName2")
        self.assertEqual(child_genre_model2.genre_level, "2")
        self.assertEqual(child_genre_model2.item_count, "22")

        child_genre_model3: ChildGenreModel = genre_model1.child_genre_model_list[2]
        self.assertEqual(child_genre_model3.genre_id, "333")
        self.assertEqual(child_genre_model3.genre_name, "testGenreName3")
        self.assertEqual(child_genre_model3.genre_level, "3")
        self.assertEqual(child_genre_model3.item_count, "33")

        # タググループ情報検索結果モデル1
        tag_group_model1: TagGroupModel = \
            entire_model.tag_group_model_list[0]
        self.assertEqual(tag_group_model1.tag_group_id, 1001050)
        self.assertEqual(tag_group_model1.tag_group_name, "限定特典")
        self.assertEqual(len(tag_group_model1.tag_model_list), 1)

        # タグ情報検索結果モデル1
        tag_model: TagModel = \
            tag_group_model1.tag_model_list[0]
        self.assertEqual(tag_model.tag_id, 1011605)
        self.assertEqual(tag_model.tag_name, "初回版・特装版")
        self.assertEqual(tag_model.parent_tag_id, 0)
        self.assertEqual(tag_model.item_count, 0)

        # タググループ情報検索結果モデル2
        tag_group_model2: TagGroupModel = \
            entire_model.tag_group_model_list[1]
        self.assertEqual(tag_group_model2.tag_group_id, 2)
        self.assertEqual(tag_group_model2.tag_group_name, "testGroupName2")
        self.assertEqual(len(tag_group_model2.tag_model_list), 3)

        # タグ情報検索結果モデル2-1
        tag_model: TagModel = \
            tag_group_model2.tag_model_list[0]
        self.assertEqual(tag_model.tag_id, 111)
        self.assertEqual(tag_model.tag_name, "test1")
        self.assertEqual(tag_model.parent_tag_id, 1)
        self.assertEqual(tag_model.item_count, 11)

        # タグ情報検索結果モデル2-2
        tag_model: TagModel = \
            tag_group_model2.tag_model_list[1]
        self.assertEqual(tag_model.tag_id, 222)
        self.assertEqual(tag_model.tag_name, "test2")
        self.assertEqual(tag_model.parent_tag_id, 2)
        self.assertEqual(tag_model.item_count, 22)

        # タグ情報検索結果モデル2-3
        tag_model: TagModel = \
            tag_group_model2.tag_model_list[2]
        self.assertEqual(tag_model.tag_id, 333)
        self.assertEqual(tag_model.tag_name, "test3")
        self.assertEqual(tag_model.parent_tag_id, 3)
        self.assertEqual(tag_model.item_count, 33)

        # タググループ情報検索結果モデル3
        tag_group_model1: TagGroupModel = \
            entire_model.tag_group_model_list[2]
        self.assertEqual(tag_group_model1.tag_group_id, 3)
        self.assertEqual(tag_group_model1.tag_group_name, "testGroupName3")
        self.assertEqual(len(tag_group_model1.tag_model_list), 1)

        # タグ情報検索結果モデル1
        tag_model: TagModel = \
            tag_group_model1.tag_model_list[0]
        self.assertEqual(tag_model.tag_id, 3111)
        self.assertEqual(tag_model.tag_name, "test31")
        self.assertEqual(tag_model.parent_tag_id, 31)
        self.assertEqual(tag_model.item_count, 311)


class TestGenerateUrl(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        CONFIG_DIR = path.abspath(path.join(path.dirname(__file__),"..", "..", "config"))
        CONFIG_FILE = "rakutenApi.yaml"

        config_file = path.join(CONFIG_DIR, CONFIG_FILE)
        with open(config_file, "r") as f:
            data = yaml.safe_load(f)
            cls.application_id = APPLICATION_ID
            cls.affiliate_id = AFFILIATE_ID
            cls.format = data["rakuten_api"]["format"]
            cls.base_url = data["rakuten_api"]["ichiba_item"]["base_url"]

    def test_input_model_normal(self):
        input_model = SearchConditionModel()
        input_model.application_id = "test1"
        input_model.affiliate_id = "test2"
        input_model.format = "test3"
        input_model.callback = "test4"
        input_model.elements = "test5"
        input_model.format_version = 6
        input_model.keyword = "test7"
        input_model.shop_code = "test8"
        input_model.item_code = "test9"
        input_model.genre_id = 10
        input_model.tag_id = 11
        input_model.hits = 12
        input_model.page = 13
        input_model.sort = "test14"
        input_model.min_price = 15
        input_model.max_price = 16
        input_model.avalilability = 17
        input_model.field = 18
        input_model.carrier = 19
        input_model.image_flag = 20
        input_model.or_flag = 21
        input_model.ng_keyword = "test22"
        input_model.purchase_type = 23
        input_model.ship_overseas_flag = 24
        input_model.ship_overseas_area = "test25"
        input_model.asuraku_flag = 26
        input_model.asuraku_area = 27
        input_model.point_rate_flag = 28
        input_model.point_rate = 29
        input_model.postage_flag = 30
        input_model.credit_card_flag = 31
        input_model.gift_flag = 32
        input_model.has_review_flag = 33
        input_model.max_affiliate_rate = 34
        input_model.min_affiliate_rate = 35
        input_model.has_movie_flag = 36
        input_model.pamphlet_flag = 37
        input_model.appoint_delivery_date_flag = 38
        input_model.genre_infomation_flag = 39
        input_model.tag_information_flag = 40

        expected_url = self.base_url + "?" + \
            "applicationId=" + "test1" + "&" + \
            "affiliateId=" + "test2" + "&" + \
            "format=" + "test3" + "&" + \
            "callback=" + "test4" + "&" + \
            "elements=" + "test5" + "&" + \
            "formatVersion=" + "6" + "&" + \
            "keyword=" + "test7" + "&" + \
            "shopCode=" + "test8" + "&" + \
            "itemCode=" + "test9" + "&" + \
            "genreId=" + "10" + "&" + \
            "tagId=" + "11" + "&" + \
            "hits=" + "12" + "&" + \
            "page=" + "13" + "&" + \
            "sort=" + "test14" + "&" + \
            "minPrice=" + "15" + "&" + \
            "maxPrice=" + "16" + "&" + \
            "availability=" + "17" + "&" + \
            "field=" + "18" + "&" + \
            "carrier=" + "19" + "&" + \
            "imageFlag=" + "20" + "&" + \
            "orFlag=" + "21" + "&" + \
            "NGKeyword=" + "test22" + "&" + \
            "purchaseType=" + "23" + "&" + \
            "shipOverseasFlag=" + "24" + "&" + \
            "shipOverseasArea=" + "test25" + "&" + \
            "asurakuFlag=" + "26" + "&" + \
            "asurakuArea=" + "27" + "&" + \
            "pointRateFlag=" + "28" + "&" + \
            "pointRate=" + "29" + "&" + \
            "postageFlag=" + "30" + "&" + \
            "creditCardFlag=" + "31" + "&" + \
            "giftFlag=" + "32" + "&" + \
            "hasReviewFlag=" + "33" + "&" + \
            "maxAffiliateRate=" + "34" + "&" + \
            "minAffiliateRate=" + "35" + "&" + \
            "hasMovieFlag=" + "36" + "&" + \
            "pamphletFlag=" + "37" + "&" + \
            "appointDeliveryDateFlag=" + "38" + "&" + \
            "genreInformationFlag=" + "39" + "&" + \
            "tagInformationFlag=" + "40"

        source_manager = SourceManager(APPLICATION_ID, AFFILIATE_ID)
        url = source_manager._SourceManager__generate_url(input_model)

        self.assertEqual(url, expected_url)

    def test_input_model_normal_full(self):
        input_model = SearchConditionModel()
        input_model.application_id = "テスト1"
        input_model.affiliate_id = "テスト2"
        input_model.format = "テスト3"
        input_model.callback = "テスト4"
        input_model.elements = "テスト5"
        input_model.format_version = 6
        input_model.keyword = "テスト7"
        input_model.shop_code = "テスト8"
        input_model.item_code = "テスト9"
        input_model.genre_id = 10
        input_model.tag_id = 11
        input_model.hits = 12
        input_model.page = 13
        input_model.sort = "テスト14"
        input_model.min_price = 15
        input_model.max_price = 16
        input_model.avalilability = 17
        input_model.field = 18
        input_model.carrier = 19
        input_model.image_flag = 20
        input_model.or_flag = 21
        input_model.ng_keyword = "テスト22"
        input_model.purchase_type = 23
        input_model.ship_overseas_flag = 24
        input_model.ship_overseas_area = "テスト25"
        input_model.asuraku_flag = 26
        input_model.asuraku_area = 27
        input_model.point_rate_flag = 28
        input_model.point_rate = 29
        input_model.postage_flag = 30
        input_model.credit_card_flag = 31
        input_model.gift_flag = 32
        input_model.has_review_flag = 33
        input_model.max_affiliate_rate = 34
        input_model.min_affiliate_rate = 35
        input_model.has_movie_flag = 36
        input_model.pamphlet_flag = 37
        input_model.appoint_delivery_date_flag = 38
        input_model.genre_infomation_flag = 39
        input_model.tag_information_flag = 40

        expected_url = self.base_url + "?" + \
            "applicationId=" + "テスト1" + "&" + \
            "affiliateId=" + "テスト2" + "&" + \
            "format=" + "テスト3" + "&" + \
            "callback=" + "テスト4" + "&" + \
            "elements=" + "テスト5" + "&" + \
            "formatVersion=" + "6" + "&" + \
            "keyword=" + "テスト7" + "&" + \
            "shopCode=" + "テスト8" + "&" + \
            "itemCode=" + "テスト9" + "&" + \
            "genreId=" + "10" + "&" + \
            "tagId=" + "11" + "&" + \
            "hits=" + "12" + "&" + \
            "page=" + "13" + "&" + \
            "sort=" + "テスト14" + "&" + \
            "minPrice=" + "15" + "&" + \
            "maxPrice=" + "16" + "&" + \
            "availability=" + "17" + "&" + \
            "field=" + "18" + "&" + \
            "carrier=" + "19" + "&" + \
            "imageFlag=" + "20" + "&" + \
            "orFlag=" + "21" + "&" + \
            "NGKeyword=" + "テスト22" + "&" + \
            "purchaseType=" + "23" + "&" + \
            "shipOverseasFlag=" + "24" + "&" + \
            "shipOverseasArea=" + "テスト25" + "&" + \
            "asurakuFlag=" + "26" + "&" + \
            "asurakuArea=" + "27" + "&" + \
            "pointRateFlag=" + "28" + "&" + \
            "pointRate=" + "29" + "&" + \
            "postageFlag=" + "30" + "&" + \
            "creditCardFlag=" + "31" + "&" + \
            "giftFlag=" + "32" + "&" + \
            "hasReviewFlag=" + "33" + "&" + \
            "maxAffiliateRate=" + "34" + "&" + \
            "minAffiliateRate=" + "35" + "&" + \
            "hasMovieFlag=" + "36" + "&" + \
            "pamphletFlag=" + "37" + "&" + \
            "appointDeliveryDateFlag=" + "38" + "&" + \
            "genreInformationFlag=" + "39" + "&" + \
            "tagInformationFlag=" + "40"

        source_manager = SourceManager(APPLICATION_ID, AFFILIATE_ID)
        url = source_manager._SourceManager__generate_url(input_model)

        self.assertEqual(url, expected_url)

    def test_input_model_none(self):
        input_model = None

        expected_url = self.base_url + "?" + \
            "applicationId=" + self.application_id + "&" \
            "affiliateId=" + self.affiliate_id + "&" \
            "format=" + self.format

        source_manager = SourceManager(APPLICATION_ID, AFFILIATE_ID)
        url = source_manager._SourceManager__generate_url(input_model)

        self.assertEqual(url, expected_url)
